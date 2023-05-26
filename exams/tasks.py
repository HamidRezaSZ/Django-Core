from celery import shared_task
from django.db.models import F


def calculate_score(no_correct_questions, no_wrong_questions, no_all_questions, exam) -> float:
    try:
        return (((no_correct_questions * exam.wrong_questions_weight) - (no_wrong_questions * exam.correct_questions_weight)) / (no_all_questions * exam.wrong_questions_weight)) * 100
    except Exception:
        return 0


@shared_task
def create_result(user_pk, exam_pk):

    from accounts.models import User

    from .models import Exam, Result, UserAnswer

    exam = Exam.objects.get(id=exam_pk)
    user = User.objects.get(id=user_pk)
    all_score = 0
    all_questions = 0
    result_child = []
    exam_childs = exam.child.filter()
    if exam_childs.exists():
        for child in exam_childs:
            no_all_questions = child.question_set.filter().count()
            no_correct_questions = UserAnswer.objects.filter(
                user=user, exam=child, answer=F('question__correct_answer')).count()
            no_answered_questions = UserAnswer.objects.filter(
                user=user, exam=child).count()
            no_not_answered = no_all_questions - no_answered_questions
            no_wrong_questions = no_all_questions - no_correct_questions - no_not_answered
            score = calculate_score(no_correct_questions,
                                    no_wrong_questions, no_all_questions, child)
            result_child.append(
                Result.objects.create(
                    user=user, exam=child, no_all_questions=no_all_questions, no_wrong_questions=no_wrong_questions,
                    no_correct_questions=no_correct_questions, score=score))
            all_score += score
            all_questions += no_all_questions
        childs_count = exam_childs.count()
        max_score = calculate_score(all_questions,
                                    0, all_questions, exam)
        score = all_score/childs_count
        parent = Result.objects.create(user=user, exam=exam, no_all_questions=0,
                                       no_wrong_questions=0, no_correct_questions=0, score=score, max_score=max_score)
        for child in result_child:
            child.parent = parent
            child.save()
    else:
        no_all_questions = exam.question_set.filter().count()
        no_correct_questions = UserAnswer.objects.filter(
            user=user, exam=exam, answer=F('question__correct_answer')).count()
        no_answered_questions = UserAnswer.objects.filter(
            user=user, exam=exam).count()
        no_not_answered = no_all_questions - no_answered_questions
        no_wrong_questions = no_all_questions - no_correct_questions - no_not_answered
        score = calculate_score(no_correct_questions,
                                no_wrong_questions, no_all_questions, exam)
        max_score = calculate_score(no_all_questions,
                                    0, no_all_questions, exam)
        Result.objects.create(user=user, exam=exam, no_all_questions=no_all_questions,
                              no_wrong_questions=no_wrong_questions, no_correct_questions=no_correct_questions,
                              score=score, max_score=max_score)

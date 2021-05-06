from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator


def index(request):
    """
    Pybo 질문 목록 출력
    """
    # ---------------------------------- [edit] ---------------------------------- #
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent') # 정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: # recent
        question_list = Question.objects.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw) |  # 답변 글쓴이검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(comment__content__icontains=kw)  |  # 질문 댓글 검색
            Q(answer__comment__content__icontains=kw)  # 답변 댓글 검색
        ).distinct()
    # ---------------------------------------------------------------------------- #

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # ---------------------------------- [edit] ---------------------------------- #
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # page, kw, so가 추가되었다.
    # ---------------------------------------------------------------------------- #
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    Pybo 질문 세부 사항
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

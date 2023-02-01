from django.shortcuts                   import render, get_object_or_404, redirect
from django.utils                       import timezone
from django.core.paginator              import Paginator  
from django.contrib.auth.decorators     import login_required
from django.core.exceptions             import ValidationError
from django.http                        import QueryDict

from rest_framework             import status
from rest_framework.response    import Response
from rest_framework.views       import APIView
from rest_framework.generics    import ListAPIView, RetrieveUpdateDestroyAPIView

from .models        import Question, Answer
from .forms         import QuestionForm, AnswerForm
from .serializers   import QuestionSerializer, AnswerSerializer
from .permissions   import IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly, IsStaffOrReadOnly

import logging 

logger = logging.getLogger('json_logger')


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    logger.info("GET access Board List", extra={'request': request})

    return render(request, 'board/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)

# def answer_create(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     question.answer_set.create(content = request.POST.get('content'), create_date = timezone.now())
#     return redirect('board:detail', question_id = question.id)


@login_required(login_url='accounts:login')
def answer_create(request, question_id):  # 둘 중 하나 쓰면 됨.
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "GET":
        form = AnswerForm()
        context = {'question': question, 'form': form}
        return render(request, 'board/question_detail.html', context)

    elif request.method == "POST":
        # 시리얼라이저 생성
        answer_serializer = AnswerSerializer(data=request.POST)

        if answer_serializer.is_valid():  # 내용 검사
            answer_serializer.save()  # 저장
        else:  # 내용에 문제 있을 때
            raise ValidationError(answer_serializer.errors)
        logger.info("POST access BOARD_ANSWER Creation",
                    extra={'request': request})

        return redirect('board:detail', question_id=question.id)

    """
    regacy code >>
    """
    # question = get_object_or_404(Question, pk = question_id)
    # if request.method == "POST":

    #     form = AnswerForm(request.POST)
    #     if form.is_valid():
    #         answer = form.save(commit = False)
    #         answer.author = request.user  # author 속성에 로그인 계정 저장
    #         answer.create_date = timezone.now()
    #         answer.question = question
    #         answer.save()
    #         return redirect('board:detail', question_id = question.id)
    # else:
    #     form = AnswerForm()

    # context = {'question': question, 'form': form}
    # return render(request, 'board/question_detail.html', context)


@login_required(login_url='accounts:login')
def question_create(request):

    if request.method == 'GET':
        form = QuestionForm()
        # return render(request=request, template_name='accounts/signup.html')
        context = {'form': form}
        return render(request, 'board/question_form.html', context)

    elif request.method == 'POST':
        # 시리얼라이저 생성
        question_serializer = QuestionSerializer(data=request.POST)

        if question_serializer.is_valid():  # 내용 검사
            question_serializer.save()  # 저장
            logger.info("POST access BOARD_QUESTION Creation",
                        extra={'request': request})
        else:
            raise ValidationError(question_serializer.errors)

        return redirect('index')

    return redirect('index')

    """
    regacy code >>
    """
    # if request.method == 'POST':
    #     form = QuestionForm(request.POST)

    #     if form.is_valid():
    #         question = form.save(commit = False)
    #         question.author = request.user  # author 속성에 로그인 계정 저장
    #         question.create_date = timezone.now()
    #         question.save()
    #         return redirect('board:index')
    # else:
    #     context = {'form': form}
    # return render(request, 'board/question_form.html', context)


class BoardAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # print("BoardAPIView_perform_create")  # PROCESS CHEK
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):

        # print("BoardAPIView_list")  # PROCESS CHEK
        # print("BoardAPIView_list_self.get_queryset : ", self.get_queryset())  # PROCESS CHEK
        queryset = self.filter_queryset(self.get_queryset())
        # print("BoardAPIView_list_queryset : ", queryset)  # PROCESS CHEK
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        # print("BoardAPIView_create")  # PROCESS CHEK
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.hit += 1 # 조회수 1 증가
    #     instance.save()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    def update(self, request, * args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_object_cache', None):
            instance._prefetched_object_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

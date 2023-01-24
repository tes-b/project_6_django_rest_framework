from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator  
from django.contrib.auth.decorators import login_required

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)

# def answer_create(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     question.answer_set.create(content = request.POST.get('content'), create_date = timezone.now())
#     return redirect('board:detail', question_id = question.id)

@login_required(login_url = 'accounts:login')
def answer_create(request, question_id): # 둘 중 하나 쓰면 됨.
    """
    board answer_apply
    """
    question = get_object_or_404(Question, pk = question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit = False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id = question.id)
    else:
        form = AnswerForm()
    
    context = {'question': question, 'form': form}
    return render(request, 'board/question_detail.html', context)

@login_required(login_url = 'accounts:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        
        if form.is_valid():
            question = form.save(commit = False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    
    context = {'form': form}
    return render(request, 'board/question_form.html', context)


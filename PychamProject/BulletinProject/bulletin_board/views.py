from django.shortcuts import render, get_object_or_404
from .models import Bulletin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


# Create your views here.
# 1. 함수 2. 클래스(재사용성 大)

def index(request):
    # 게시글 전체 목록조회
    bulletin_list = Bulletin.objects.all().order_by('-writeDate') # 작성일 desc로 정렬
    context = {'bulletin_list': bulletin_list}
    return render(request, 'bulletin/index.html', context)

def create_bulletin(request):
    # 새 글 작성 get
    return render(request, 'bulletin/create_bulletin.html')

def add_bulletin(request):
    # 새 글 작성 post
    bulletin = Bulletin()
    bulletin.title = request.POST['title']
    bulletin.content =  request.POST['content']
    bulletin.name =  request.POST['name']
    bulletin.password =  request.POST['pincode']
    bulletin.save()

    # redirect
    return HttpResponseRedirect(reverse('bulletin_board:index'))


def view_bulletin(request, bulletin_id):
    # 글 조회
    bulletin = get_object_or_404(Bulletin, pk=bulletin_id)
    # get_object_or_404 pk값이 없을땐 404 error 페이지 출력
    return render(request, 'bulletin/detail.html', {'bulletin': bulletin})


def update_bulletin(request, bulletin_id):
    # 글 수정
    bulletin = Bulletin.objects.get(id=bulletin_id)

    if request.method == "POST":
        bulletin.title = request.POST['title']
        bulletin.content = request.POST['content']
        bulletin.writeDate = timezone.datetime.now()
        bulletin.save()
        return HttpResponseRedirect(reverse('bulletin_board:view', args=(bulletin_id,)))

    else:
        return render(request, 'bulletin/detail.html', {'bulletin': bulletin})


def delete_bulletin(request, bulletin_id):
    bulletin = Bulletin.objects.get(id=bulletin_id)
    bulletin.delete()
    return HttpResponseRedirect(reverse('bulletin_board:index'))
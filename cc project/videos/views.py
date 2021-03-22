from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .forms import file_upload_form
from .models import videos, like
from io import StringIO, BytesIO
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile


# Create your views here.


@login_required
def uploadfiles(request):                                                                                       # File uplaod page, as soon as file is uploaded the location of the file and dir are stored to its progress model attribtes by creating an instance ,and also storing the current file details to the user instance
        if request.method == 'POST':
            form = file_upload_form(request.POST, request.FILES)
            if form.is_valid():
                form_inst = form.save(commit=False)
                form_inst.user_name = request.user
                form_inst.save()
                
                messages.success(request, f'File has been uploaded successfully')
                return redirect('profile')
            else:
                return HttpResponse("invalid, go back and try again!")
        else:
            form = file_upload_form()
            return render(request, 'videos/upload.html' , {'form':form})

@login_required
def myvideos(request):
    if request.method == 'POST':
        qset = videos.objects.filter(user_name = request.user).order_by(request.POST['sort_by'])
    else:
        qset = videos.objects.filter(user_name = request.user)
    #print(request.user.watchlist.video.all())
    return render(request, 'videos/myvideos.html', {'qset':qset, 'title':'User Files'})


def home(request):
    if request.method == 'POST':
        print(request.POST['action'])
        if request.POST['action'] == 'sort':
            qset = videos.objects.filter(private=False).order_by(request.POST['sort_by'])
        else:
            qset = videos.objects.filter(private=False).filter(name__contains = request.POST['keyword'])
            return render(request, 'videos/home.html', {'qset':qset, 'title':'Home', 'flag':'search', 'keyword':request.POST['keyword']})
    else:
        qset = videos.objects.filter(private = False)
    #if qset:
    #    print('empty')
    return render(request, 'videos/home.html', {'qset':qset, 'title':'Home'})


def add_like(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            video_id = request.POST['video_id']
            red = request.POST['page']
            video = videos.objects.get(id = video_id)

            if request.user in video.liked.all():
                video.liked.remove(request.user)
            else:
                video.liked.add(request.user)
            
            likes, created = like.objects.get_or_create(user_name = request.user, video_id = video_id)
            if not created:
                if likes.value == 'Like':
                    likes.value = 'Unlike'
                else:
                    likes.value = 'Like'
            likes.save()
    else:
        return HttpResponse("Please Login First!")
    return redirect(red)

@login_required
def add_to_watchlist(request):
    if request.method == "POST":
        redirect_page = request.POST['redirect']
        print(request.POST['id'])
        if request.POST['action'] == 'add':
            inst = request.user.watchlist
            video_inst = videos.objects.get(id = request.POST['id'])
            inst.video.add(video_inst)
            inst.save()
            messages.success(request, f'Video has been added to your watchlist')

        else:
            inst = request.user.watchlist
            video_inst = videos.objects.get(id = request.POST['id'])
            inst.video.remove(video_inst)
            inst.save()
            messages.success(request, f'Video has been removed from your watchlist')
        return redirect(redirect_page)
    else:
        return HttpResponse("No Data 404 error")

@login_required
def watchlist(request):
    if request.method == "POST":
        qset = request.user.watchlist.video.all().order_by(request.POST['sort_by'])
    else:
        qset = request.user.watchlist.video.all()
    return render(request, 'videos/watchlist.html', {'qset':qset})

@login_required
def liked_videos(request):
    qset = like.objects.filter(user_name = request.user)
    return render(request, 'videos/liked.html', {'qset':qset})
from django.shortcuts import render
from .models import Video , Book , Course , Podcast


#-----------------Videos-----------------#

def show_video(request , video_id):
    
    video = Video.objects.get(video_id = video_id)
    url = video.link

    #get the youtube video info from the url
    thumbnail_url = "https://img.youtube.com/vi/" + url.split('=')[1] + "/0.jpg"
    
    return render(request, 'video.html', {'video': video, 'thumbnail_url': thumbnail_url})

def get_videos(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        return render(request, 'videos.html', {'videos': videos})
    
#-----------------Books-----------------#
    
def get_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'books.html', {'books': books})
    
#-----------------Courses-----------------#

def get_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        return render(request, 'courses.html', {'courses': courses})
    
#-----------------Podcasts-----------------#
    
def get_podcasts(request):
    if request.method == 'GET':
        podcasts = Podcast.objects.all()
        return render(request, 'podcasts.html', {'podcasts': podcasts})
    

from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ImageUploadForm
from django.conf import settings
from .utils import opencv_dface

def first_view(request):
    return render(request, 'imageprocessingapp/first_view.html', {})


def uimage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)  # 이미지르 업로드할때 쓰는 form
        if form.is_valid():
            myfile = request.FILES['image']
            #
            fs = FileSystemStorage()  # 이미지 파일을 저장할때 쓰는 함수
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'imageprocessingapp/uimage.html', {'form': form, 'uploaded_file_url' : uploaded_file_url})
    else:
        form = UploadImageForm()
        return render(request, 'imageprocessingapp/uimage.html', {'form': form})


def dface(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            opencv_dface(imageURL)

            return render(request, 'imageprocessingapp/dface.html', {'form': form, 'post': post})
    else:
        form = ImageUploadForm()
    return render(request, 'imageprocessingapp/dface.html', {'form': form})
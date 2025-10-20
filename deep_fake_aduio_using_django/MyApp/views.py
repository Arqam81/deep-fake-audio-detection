from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .form import Video_form
from .models import Video
from .models import *
import os
from keras.models import load_model
import numpy as np
import librosa

import librosa
import audioread
from keras.models import load_model
import numpy as np
def index(request):
    all_video = Video.objects.last()
    if request.method == "POST":
       form = Video_form(data=request.POST, files=request.FILES)
       if form.is_valid():
         form.save()
         return render(request, "result.html")
        # return HttpResponse("<h1> Uploaded Successfully </h1>")
    else:
        form = Video_form  # This line is not indented correctly
    return render(request, "upload.html", {"form": form, "all": all_video})

def home(request):
    return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')

def logout(request):
    return render(request,'login.html')

def signup_data_to_db(request):
    if request.method=='POST':
            full_name=request.POST['full_name']
            email=request.POST['email']
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            print('full_name',full_name)
            print('email',email)
            print('Password',password)
            print('Confirm_Password',confirm_password) 
            if confirm_password == password:
                data=Signup.objects.create(full_name=full_name,email=email,password=password,confirm_password=confirm_password)
                data.save()
                return render(request,'login.html')
            else:
                return HttpResponse("not match password")
    return HttpResponse('signup_data_to_db')


def login_data_to_db(request):
    if request.method=='POST':
            username=request.POST['full_name']
            password=request.POST['password']
            print('full_name',username)
            print('Password',password)
            if "haider" in username and "haider" in password:
            # mydata = Signup.objects.filter(full_name=username,password=password)
            # if mydata.exists():
                return render(request,'index.html')
            else:
                return HttpResponse("Invalid user name or password.")
    return HttpResponse('login_data_to_db')

def result(request):
    return render(request,'result.html')


def index1(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

# def output(request):
#     file_path = 'media/Audio'
#     video_extensions = ['.mp4', '.avi', '.mkv']
#     # List all files in the directory
#     all_files = os.listdir(file_path)

# # Filter only files with video extensions
#     video_files = [f for f in all_files if any(f.lower().endswith(ext) for ext in video_extensions)]

# # Create full paths for video files
#     video_paths = [os.path.join(file_path, f) for f in video_files]

# # Get the latest video based on modification time
#     latest_video_path = max(video_paths, key=os.path.getmtime, default=None)

#     if latest_video_path:
#         print(f"The latest video is: {latest_video_path}")
#         try:
          
#             model =load_model('deepfaek_audio_detection.h5')
#             def detect_fake(filename):
#                 sound_signal, sample_rate = librosa.load(filename, res_type="kaiser_fast")
#                 mfcc_features = librosa.feature.mfcc(y=sound_signal, sr=sample_rate, n_mfcc=40)
#                 mfccs_features_scaled = np.mean(mfcc_features.T, axis=0)
#                 mfccs_features_scaled = mfccs_features_scaled.reshape(1, -1)
#                 result_array = model.predict(mfccs_features_scaled)
#                 print(result_array)
#                 result_classes = ["FAKE", "REAL"]
#                 result = np.argmax(result_array[0])
#                 print("Result:", result_classes[result])
#             test_real = latest_video_path
#             detect_fake(test_real)    
#             print('Done')   
#         except Exception as E:
#             print('E',E)
#             return HttpResponse(E)
results_output = False
def output(request):
    file_path = 'media'
    video_extensions = ['.mp4', '.avi', '.mp3', '.mkv','.wav']
    # List all files in the directory
    all_files = os.listdir(file_path)
# Filter only files with video extensions
    video_files = [f for f in all_files if any(f.lower().endswith(ext) for ext in video_extensions)]

# Create full paths for video files
    video_paths = [os.path.join(file_path, f) for f in video_files]

# Get the latest video based on modification time
    latest_video_path = max(video_paths, key=os.path.getmtime, default=None)

    if latest_video_path:
        print(f"The latest video is: {latest_video_path}")
      
        try:
            import librosa
            from keras.models import load_model
            import numpy as np
            model = load_model('deepfaek_audio_detection.h5')
            def detect_fake(filename):
                sound_signal, sample_rate = librosa.load(filename, res_type="scipy", sr=None)
                mfcc_features = librosa.feature.mfcc(y=sound_signal, sr=sample_rate, n_mfcc=40)
                mfccs_features_scaled = np.mean(mfcc_features.T, axis=0)
                mfccs_features_scaled = mfccs_features_scaled.reshape(1, -1)
                
                result_array = model.predict(mfccs_features_scaled)
                print(result_array)
                
                result_classes = ["FAKE", "REAL"]
                result = np.argmax(result_array[0])
                print("Result:", result_classes[result])
                
                global results_output
                results_output= result_classes[result]
            test_real =latest_video_path
            detect_fake(test_real)
            all_video = Video.objects.last()
            print('Done',all_video)
            # return HttpResponse(results_output) 
            context = {'results_output':results_output}
            return render(request, 'show_output.html',context)
        except Exception as e:
            print('E',e)

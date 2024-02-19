from django.core.files.images import ImageFile
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from pyns.models import *
import os, zipfile, shutil

from users.models import CustomUser
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
def index(request, pagename=None, id=None):
    context = {}
    
    try:
        if not request.user.id:
            return render(request, 'login.html', context=context)
        else:
            if (pagename) and (pagename != 'index') and not (str(pagename).__contains__('.html')):
                context['id'] = id
                return render(request, f'{pagename}.html', context=context)
            else:
                context['id'] = id
                return render(request, f'index.html', context=context)
    except Exception as e:
        return HttpResponse(str(e))

@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            login_url = request.POST.get('next', '/') # get next page
            return redirect("index")
        
        else:
            print('Wrong Username or Password')
            return render(request, 'login.html', context={'error_message': 'Invalid login credentials'})
    else:
        next_url = request.GET.get('next', '/') # get next page
        context = {'next_url':next_url}
        return render(request, 'login.html', context)
    

@csrf_exempt
@login_required
def logoutView(request):
    try:
        logout(request)
    except:
        pass
    return render(request, 'login.html')
@csrf_exempt
def registerView(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        userCheck = CustomUser.objects.filter(Q(username=username) | Q(email=email))
        if userCheck.exists():
            print('User Already Exists')
            return render(request, 'register.html', context={'error_message': 'User Already Exists'})
        else:
            if password1==password2:
                password = password1
                newUser = CustomUser.objects.create_user(username=username, password=password, email=email)
                newUser.save()
                login(request, newUser)
                return redirect('/')
            else: 
                print('Password Mismatch')
                return render(request, 'register.html', context={'error_message': 'Password Mismatch'})
    else:
        next_url = request.GET.get('next', '/') # get next page
        context = {'next_url':next_url}
        return render(request, 'register.html', context)
    
@csrf_exempt
def addPyn(request):
    if request.method == 'POST':
        
        title = request.POST.get('title')
        image = request.FILES.get('image')
        user = request.user
        # tags = request.POST.get('tags')
        if request.user.id:
            pyn = Pyn.objects.create(title=title, image=image, user=user)
            pyn.save()
            
            return redirect('/', context={'success_message': 'Image Added Successfully'})
        else: 
            return render(request, 'add_pyn.html', context={'error_message': 'Invalid User'})
    else:
        next_url = request.GET.get('next', '/') # get next page
        context = {'next_url':next_url}
        return render(request, 'add_pyn.html', context)
def userPyns(request, id):
    context = {}
    try:
        if not request.user.id:
            return render(request, 'login.html', context=context)
        else:
            context['user_pyns'] = Pyn.objects.filter(user_id=id)
            return render(request, f'user_pyns.html', context=context)
    except Exception as e:
        return HttpResponse(str(e))
def savePyn(request, id):
    context={}
    try:
        if not request.user.id:
            return render(request, 'login.html', context=context)
        else:
            saved = SavedPyn.objects.filter(user_id=request.user.id, pyn_id=id)
            if not saved.exists():
                saved_pyn = SavedPyn.objects.create(user_id=request.user.id, pyn_id=id)
                saved_pyn.save()
            return JsonResponse({'success_message': 'Pyn Saved'})
    except Exception as e:
        return JsonResponse({'error': str(e)})
def removePyn(request, id):
    context={}
    try:
        if not request.user.id:
            return render(request, 'login.html', context=context)
        else:
            saved = SavedPyn.objects.filter(user_id=request.user.id, pyn_id=id)
            if saved.exists():
                saved[0].delete()
                return JsonResponse({'success_message': 'Pyn Removed'})
    except Exception as e:
        return JsonResponse({'error': str(e)})
def likePyn(request, id):
    context={}
    try:
        if not request.user.id:
            return render(request, 'login.html', context=context)
        else:
            liked = Likes.objects.filter(user_id=request.user.id, pyn_id=id)
            if not liked.exists():
                liked_pyn = Likes.objects.create(user_id=request.user.id, pyn_id=id)
                liked_pyn.save()
                return JsonResponse({'success_message': 'Pyn Liked'})
            else:
                liked[0].delete()
                return JsonResponse({'success_message': 'Pyn UnLiked'})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    

def userSavedPyns(request, id):
    context = {}
    try:
        if not request.user.id:
            return render(request, 'login.html', context=context)
        else:
            context['saved_pyns'] = SavedPyn.objects.filter(user_id=id)
            return render(request, f'saved_pyns.html', context=context)
    except Exception as e:
        return HttpResponse(str(e))
def userLikedPyns(request, id):
    context = {}
    try:
        if not request.user.id:
            return render(request, 'login.html', context=context)
        else:
            context['liked_pyns'] = Likes.objects.filter(user_id=id)
            return render(request, f'liked_pyns.html', context=context)
    except Exception as e:
        return HttpResponse(str(e))
    
    
@csrf_exempt
def addPynBulk(request):
    if request.method == 'POST':
        zip_file = request.FILES.get('zip_file')
        if zip_file:
            if request.user.id:
                with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                    temp_dir = 'temp_extracted_images'
                    os.makedirs(temp_dir, exist_ok=True)
                    zip_ref.extractall(temp_dir)
                    
                    for filename in os.listdir(temp_dir):
                        title = os.path.splitext(filename)[0]
                        image_path = os.path.join(temp_dir, filename)
                        image_field_file = ImageFile(open(image_path, "rb"))
                        print(image_field_file)
                        pyn = Pyn.objects.create(title=title, image=image_field_file, user=request.user)
                        pyn.save()
                # os.rmdir(temp_dir)
                shutil.rmtree(temp_dir)
                return redirect('/', context={'success_message': 'Images Added Successfully'})
            else: 
                return render(request, 'add_pyn_bulk.html', context={'error_message': 'Invalid User'})
        else: 
            return render(request, 'add_pyn_bulk.html', context={'error_message': 'No zip file uploaded'})
    else:
        next_url = request.GET.get('next', '/') # get next page
        context = {'next_url':next_url}
        return render(request, 'add_pyn_bulk.html', context)
    
    

def pynDetails(request, id):
    context = {}
    try:
        if not request.user.id:
            return render(request, 'login.html', context=context)
        else:
            context['pyn_detail'] = Pyn.objects.filter(id=id)
            return render(request, f'pyn_details.html', context=context)
    except Exception as e:
        return HttpResponse(str(e))
    
def search(request):
    context = {}
    try:
        if request.method == 'POST':
            if not request.user.id:
                return render(request, 'login.html', context=context)
            else:
                query = request.POST.get('search_query')
                context['results'] = Pyn.objects.filter(Q(title__icontains=query)|Q(user__username__icontains=query))
                context["query"]=query
                print(context)
                return render(request, f'searched.html', context=context)
        else:
            next_url = request.GET.get('next', '/') # get next page
            context = {'next_url':next_url}
            return redirect('/')
    except Exception as e:
        return HttpResponse(str(e))
    

def deletePyn(request, id):
    context={}
    try:
        if not request.user.id:
            return render(request, 'login.html', context=context)
        else:
            pyn = Pyn.objects.filter(id=id)
            if pyn[0].user == request.user:
                pyn.delete()
                return JsonResponse({'success_message': 'Pyn Deleted'})
            else:
                return JsonResponse({'error_message': 'User unauthorized to delete Pyn'})
    except Exception as e:
        return JsonResponse({'error': str(e)})
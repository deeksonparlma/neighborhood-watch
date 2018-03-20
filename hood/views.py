from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm
from .models import MyUser,Neighborhood,Post,Business

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    test = "Working!!"
    current_user = request.user
    profile = MyUser.get_user()
    posts = Post.get_post()
    return render(request,'index.html',{"test":test,
                                        "current_user":current_user,
                                        "profile":profile,
                                        "posts":posts})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    test = "Working!!"
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = current_user
            new.save()
            return redirect(index)
    else:
        form = CreateProfileForm()
    return render(request,'profile/create.html',{"test":test,"upload_form":form})

@login_required(login_url='/accounts/login/')
def view_profile(request):
    test="Working!!"
    current_user = request.user
    profile = MyUser.get_user()
    posts = Post.get_post()
    return render(request,'profile/profile.html',{"test":test,
                                                  "profile":profile,
                                                  "current_user":current_user,
                                                  "posts":posts})

@login_required(login_url='/accounts/login/')
def neighborhood(request):
    test="Neighborhood!!"
    user = MyUser.get_user()
    count = 0
    neiba = Neighborhood.get_neighborhood()
    hood = get_object_or_404(Neighborhood)
    for me in neiba:
        for us in user:
            if us.neighborhood.id == me.id:
                count += 1
    hood.occupants_count = count
    hood.save()
    return render(request,'neighborhood.html',{"test":test,
                                                   "me":neiba,
                                                   "count":count,
                                                   "user":user,})
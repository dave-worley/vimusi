import os
from datetime import date

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from .models import TeacherProfile
from .forms import TeacherProfileForm

def list(req):
    profiles = TeacherProfile.objects.all()
    paginator = Paginator(profiles, 9)
    pg = req.GET.get("page")
    try:
        profiles = paginator.page(pg)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        profiles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        profiles = paginator.page(paginator.num_pages)
    return render(req, "teacher-list.html", {"profiles":profiles})

def handle_uploads(req, keys):
    saved = []

    upload_dir = settings.UPLOAD_PATH
    upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)

    if not os.path.exists(upload_full_path):
        os.makedirs(upload_full_path)

    for key in keys:
        if key in req.FILES:
            upload = req.FILES[key]
            while os.path.exists(os.path.join(upload_full_path, upload.name)):
                upload.name = '_' + upload.name
            dest = open(os.path.join(upload_full_path, upload.name), 'wb')
            for chunk in upload.chunks():
                dest.write(chunk)
            dest.close()
            saved.append((key, os.path.join(upload_dir, upload.name)))
    # returns [(key1, path1), (key2, path2), ...]
    return saved

def goto_profile(req):
    return HttpResponseRedirect("/member/")

@login_required
def create_profile(req):
    try:
        profile = TeacherProfile.objects.get(user = req.user)
    except TeacherProfile.DoesNotExist:
        profile = None
    if not profile:
        if req.method == "POST":
            f = TeacherProfileForm(req.POST, req.FILES)
            if f.is_valid():
                teacher_profile = TeacherProfile()
                teacher_profile.user = req.user
                teacher_profile.availability = f.cleaned_data["availability"]
                teacher_profile.about = f.cleaned_data["about"]
                saved_files = handle_uploads(req, ["audio_sample", "profile_picture", "profile_video"])
                for file in saved_files:
                    setattr(teacher_profile, file[0], file[1])
                teacher_profile.save()
                return goto_profile(req)
        else:
            f = TeacherProfileForm()
        return render(req, "teacher-profile-form.html", {"form": f})
    else:
        return goto_profile(req)

def tprof(req, teacher_profile):
    userp = False
    if req.user.is_authenticated() and teacher_profile.user == req.user:
        userp = True
    return render(req, "teacher-profile.html", {"profile": teacher_profile, "userp":userp})

def profile(req, username = None):
    if req.user.is_authenticated() and req.user.username is username or not username:
        teacher_profile = get_object_or_404(TeacherProfile, user = req.user)
    else:
        teacher_profile = get_object_or_404(TeacherProfile, user__username = username)
    return tprof(req, teacher_profile)

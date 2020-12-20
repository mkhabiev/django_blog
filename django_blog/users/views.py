from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from users.forms import ProfileForm
from users.models import Profile


@csrf_exempt
def get_profile(request):
    method_profile = request.method
    print(method_profile)
    if method_profile == 'POST':
        profile = Profile.objects.create(name='Arata', sex='male', age=23, hobby='reading books')
        return HttpResponse('Created new profile')
    if method_profile in ['PUT', 'PATCH']:
        profile = Profile.objects.create(name='Arata', sex='male', age=23, hobby='reading books')
        profile.name = "Miko"
        profile.age = 19
        profile.sex = 'female'
        profile.hobby = 'dancing'
        profile.save()
        return HttpResponse('Put the information to my profile')
    if method_profile == 'GET':
        saved_profile = Profile.objects.all()
        return HttpResponse(saved_profile)
    if method_profile == 'DELETE':
        profile = Profile.objects.get(pk=1)
        profile.delete()
        return HttpResponse('Profile deleted')
    return HttpResponse('My profile')


class ProfileView(ListView):
    model = Profile
    template_name = 'users/index_profile.html'

    def get_queryset(self):
        return Profile.objects.all()


# def get_real_profile(request):
#     context = {
#         'profile': Profile.objects.all()
#     }
#     return render(request, 'users/index_profile.html', context)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/detail_profile.html'


# def get_real_profile_detail(request, pk):
#     profile = get_object_or_404(Profile, pk=pk)
#     context = {
#         'profile': profile
#     }
#     return render(request, 'users/detail_profile.html', context)


def add_profile(request):
    method = request.method
    if method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        print(form.data)
        Profile.objects.create(name=form.data['name'],
                               sex=form.data['sex'],
                               age=form.data['age'],
                               hobby=form.data['hobby'],
                               image=form.data['image'],
                               about=form.data['about'])
        return HttpResponse('Profile Created Successfully')
    else:
        form = ProfileForm()
    return render(request, 'users/add_profile.html', {'form': form})
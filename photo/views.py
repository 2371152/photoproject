from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# p444
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# p455
from .models import PhotoPost
# p507
from django.views.generic import DetailView
from django.views.generic import DeleteView


class IndexView(ListView):
    template_name = 'index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    paginate_by = 9


@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    form_class = PhotoPostForm
    template_name = "post_photo.html"
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        postdate = form.save(commit=False)
        postdate.user = self.request.user
        postdate.save()
        return super().form_valid(form)

# p449


class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

# p476


class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = PhotoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories

# p483


class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list

# p490


class DetailView(DetailView):
    template_name = 'detail.html'
    model = PhotoPost


# p498


class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = PhotoPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

# p506


class PhotoDeleteView(DeleteView):
    model = PhotoPost
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('photo:mypage')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

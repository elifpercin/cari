from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, HttpResponse
from .models import Post, Ucret, Odeme
from .forms import PostForm, OdemeForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import math
from hesap.templatetags.hesap_tags import get_ucret


def form_ornek(request):
    gelen_mesaj = request.GET.get('mesaj', None)
    print(gelen_mesaj)
    return render(request, 'hesap/form.html', context={'gelen_mesaj': gelen_mesaj})


def index(request):
    return render(request, 'anasayfa.html')


def post_detail(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    secilen = None
    # postform=PostForm(request.POST or None, instance= instance)
    posts = Post.objects.filter(title=instance.title).exclude(pk=instance.pk)
    data = sum(posts.values_list('ders__ders__ucret', flat=True))
    ucret = 0

    return render(request, 'hesap/detail.html',
                  context={'post': instance, 'posts': posts, 'secilen': secilen, 'ucret': ucret, 'data': data})


def post_create(request):
    post_form = PostForm()
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            created_post = post_form.save(commit=True)
            return HttpResponseRedirect(reverse('hesap:post_detail', kwargs={'pk': created_post.id}))

    return render(request, 'hesap/post_create.html', context={'form': post_form})


def post_list(request):
    hesap_list = Post.objects.all()
    page=request.GET.get('page',1)
    paginator=Paginator(hesap_list,6)
    try:
        hesap_list=paginator.page(page)
    except EmptyPage :
        hesap_list=paginator.page(paginator.num_pages)
    except PageNotAnInteger :
        hesap_list=paginator.page(1)
    return render(request, 'hesap/post_list.html', context={'post_list': hesap_list})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(data=request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            ders = form.cleaned_data['ders']
            if ders.ders_adi == 'Matematik':
                ucret, created = Ucret.objects.get_or_create(ders=ders)
                if not created:
                    ucret.ders = ders
                    ucret.ucret = 50
                    ucret.save()
                else:
                    ucret.ucret = 50
                    ucret.save()
            elif ders.ders_adi == 'Fizik':
                ucret, created = Ucret.objects.get_or_create(ders=ders)
                if not created:
                    ucret.ders = ders
                    ucret.ucret = 40
                    ucret.save()
                else:
                    ucret.ucret = 40
                    ucret.save()

                ucret.save()
            form.save(commit=True)
            return HttpResponseRedirect(reverse('hesap:post_detail', kwargs={'pk': form.instance.pk}))

    return render(request, 'hesap/post_update.html', context={'form': form})


def deneme(request):
    return render(request, 'hesap/../templates/base.html')


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect(reverse('hesap:post_list'))


def odeme_al(request,pk):
    odemeforms = OdemeForm(data=request.POST or None)

    if odemeforms.is_valid():
        odeme = odemeforms.cleaned_data.get('odeme')
        print(pk)
        instance = get_object_or_404(Post, pk=pk)

        posts = Post.objects.filter(title=instance.title).exclude(pk=instance.pk)
        data = sum(posts.values_list('ders__ders__ucret', flat=True))
        islem=data-odeme



        return render(request, 'hesap/odemeislem.html', context={'odemeformu': odemeforms, 'odeme': odeme,'data':data,'islem':islem})

    return render(request, 'hesap/odeme_al.html', context={'odemeformu': odemeforms})


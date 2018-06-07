from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from .forms import ArticleForm
from .models import Article


# Create your views here.



def index(request):
    form = ArticleForm(request.POST or None)
    articles = Article.objects.all()
    context = {'articles': articles, 'form': form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'article/index.html', context)


def article(request, pk):
    data = get_object_or_404(Article, pk=pk)
    to_list = data.text.rstrip().replace('.', '').replace(',', '').replace('!', '').lower().split(' ')
    data_new = ' '.join(sorted(to_list, key=lambda x: (to_list.count(x), x)))
    return render(request, 'article/article.html', {'data_new': data_new, 'data':data})
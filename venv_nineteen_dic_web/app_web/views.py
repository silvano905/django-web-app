from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, DetailView, CreateView, UpdateView
from .forms import FirstForm, TranslateForm, CreateForm
import json
from . import models
from django.db.models import Q


class IndexHome(TemplateView):
    template_name = 'home.html'


class IndexForm(TemplateView):
    template_name = 'form.html'

    def get(self, request):
        form = FirstForm()
        formm = TranslateForm()
        return render(request, self.template_name, {'form': form, 'formm': formm})

    def post(self, request):
        form = FirstForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user.set_password(password)
            user.save()

            return render(request, 'home.html', {'name': username})


# --------------------------------

class IndexFormTranslate(TemplateView):  # you can't save this form
    template_name = 'home.html'

    def get(self, request):
        form = TranslateForm()
        return render(request, self.template_name, {'formm': form})

    def post(self, request):
        form = TranslateForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']

            word_list = open('app_web/JSON/list_of_words.txt', 'r')
            final_words_list = word_list.read()
            translate = json.loads(final_words_list)
            try:
                final_word = translate[text]
                return render(request, 'translation.html', {'insert_me': final_word})

            except:
                final_word = 'Sorry {} is not in the dictionary'.format(text)
                return render(request, 'translation.html', {'insert_me': final_word})


# --------------------------------------------------------


def listwords(request):
    query = request.GET.get('q')
    queryset = models.MakeWord.objects.all()

    if query is not None:
        queryset = queryset.filter(Q(english__icontains=query) | Q(spanish__icontains=query) | Q(sentence__icontains=query))
    context = {
        "object_list": queryset
    }
    return render(request, 'word_list.html', context)


class WordDetail(DetailView):
    context_object_name = 'word_list'
    model = models.MakeWord
    template_name = 'word_details.html'


# class WordCreate(CreateView):
#     fields = ('english', 'spanish', 'sentence', 'profile_pic')
#     model = models.MakeWord


class WordDelete(DeleteView):
    model = models.MakeWord
    success_url = reverse_lazy('translate')


class WordUpdate(UpdateView):
    fields = ('english', 'spanish', 'sentence', 'profile_pic')
    model = models.MakeWord


def createword(request):
    form = CreateForm()

    if request.method == "POST":
        form = CreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'home.html')
        else:
            print("error form invalid")

    return render(request, 'app_web/makeword_form.html', {'form': form})  # after it saves return the index page
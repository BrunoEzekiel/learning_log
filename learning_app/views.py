from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from.forms import TopicForm
from .models import Topic

def index(request):
    return render(request, 'index.html')

def topics(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_app:topics'))
    context = {'form': form}
    return render(request, 'new_topic.html', context)

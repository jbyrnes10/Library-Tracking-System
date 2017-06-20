from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from project.models import MediaItem, MediaHistory

def index(request):
    media_list = MediaItem.objects.all()

    for item in media_list:
        history_list = MediaHistory.objects.filter(media_item=item)

    context_dict = {'media': media_list, 'history': history_list}

    return render(request, 'index.html', context=context_dict)

def admin_actions(request):
    return render(request, 'admin_actions.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def search_results(request):
    if request.method == 'POST':
        search_text = request.POST.get('searchText')
        media = MediaItem.objects.filter(Q(title__icontains=search_text) | Q(isbn__icontains=search_text))
        # | Q(topic__contains=search_text)

    return render_to_response('search_results.html', {"results": media, }, context_instance=RequestContext(request))

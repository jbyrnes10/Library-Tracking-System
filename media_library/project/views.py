from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from models import MediaItem, MediaHistory
from datetime import datetime

def index(request):
    media_list = MediaItem.objects.all()
    available_list = MediaItem.objects.filter(checked_out=False)
    unavailable_list = MediaItem.objects.filter(checked_out=True)

    context_dict = {'media': media_list, 'available': available_list, 'unavailable': unavailable_list}
    return render(request, 'index.html', context=context_dict)

def admin_actions(request):
    return render(request, 'admin_actions.html', {})

def check_out(request, media_id):
    clicked_media = MediaItem.objects.get(id=media_id)
    clicked_media.checked_out = True
    clicked_media.save()
    new_check_out = MediaHistory.objects.create(media_item_id=media_id, date_out=datetime.now(), borrower_id=3)
    new_check_out.save()
    media_history = MediaHistory.objects.filter(media_item_id=media_id)


    context_dict = {'checked_out_media': clicked_media, 'checked_out_history': media_history}
    return render(request, 'cart.html', context=context_dict)

def search_results(request):
    if request.method == 'POST':
        search_text = request.POST.get('searchText')
        media = MediaItem.objects.filter(Q(title__icontains=search_text) | Q(isbn__icontains=search_text))

    return render_to_response('search_results.html', {'results': media, }, context_instance=RequestContext(request))

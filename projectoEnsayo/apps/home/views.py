from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext

from models import Articles

def home(request):
	article = Articles.objects.order_by('-pub_date')
	paginator = Paginator(article, 2) # show 2 articles per page

	# Make sure page request is an int. If not, deliver first page.
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

    # If page request (9999) is out of range, deliver last page of results.
	try:
		page_articles = paginator.page(page)
	except (EmptyPage, InvalidPage):
		page_articles = paginator.page(paginator.num_pages)

	return render_to_response('base_home.html', {'page_articles': page_articles, 
	                                            'article': article},
	                        context_instance = RequestContext(request))

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

item_list = ['Introduction', 'Search', 'Index', 'Administrator']
def index_nav(request):
	t = get_template('demo1.html')
	html = t.render(Context({'item_list': item_list}))
	return HttpResponse(html)

def sub_menu(request, nav):	
	submenu = nav
	html = "<html><body>Submenu : %s .</body></html>" % submenu
	return HttpResponse(html)	
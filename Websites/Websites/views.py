from django.http import HttpResponse

def render_page(request):
    return HttpResponse("<b>hello you are on the page where i have created </b>")

def next_page(request,nextpage):
    displayed_text= ""
    if nextpage=="hello":
        displayed_text="<b> this is hello which is been used to test dynamic routes</b>"
    elif nextpage=="2":
        displayed_text="<b>this is the 2nd dynamic routpage </b>"
    return HttpResponse(displayed_text)



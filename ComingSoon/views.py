from django.shortcuts import render
from. import utils


# Create your views here.
def home(request):
    if request.method == 'POST':
        to = request.POST['email']
        utils.send_email('subject of the message', 'email body', '<p>email body</p>', [to ])
    return render(request, 'index.html')

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from RestAPI.task import SayHelloAfter10Sec


#6379 - redis Post
# pip install celery
# pip install redis
#pip install django-celery-beat
#pip install django-celery-results

def Home(request):
    return render(request, "ApiData.html")


@api_view(["POST", "GET"])
def ListofPosts(request):
    return Response(data = [{"title":"This is Api Call"}, {"title":"this is my second dict"},{"title":"this is my second dict"},
                            {"title":"this is my second dict"}, {"title":"this is my second dict"}, {"title":"this is my second dict"},
                            {"title":"this is my second dict"}])



def Send_Mail(request):

    # from_mail = settings.EMAIL_HOST_USER
    # to_mail = ["prateek29mishra@gmail.com"]
    # html = get_template("MailTemp.html").render({"Name":"Prateek"})
    # print("Hello 2")
    # sub = "Test Mail from Pure Django..."
    # msg = EmailMultiAlternatives(sub, " ", from_mail, to_mail)
    # msg.attach_alternative(html, "text/html")
    # print("Hello 3")
    # msg.send()

    SayHelloAfter10Sec.delay()
    return HttpResponse("Mail Sent....")

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EnquirySerializer,NewsletterSerializer
from .models import NewsLetter,Enquiry
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.

@api_view(['GET'])
def apioverview(request):
    api_endpoints = {
        'All Enquireies':'/api/enquiries',
        'Inspect Enquiry':'/api/enquiries/<int:pk>/',
        'Add Enquiry':'/api/send-request/',
        'Delete':'/api/enquiries/<int:pk>/',
   }
    return Response(api_endpoints)


@api_view(['GET'])
def enquiries(request):
    tasks = Enquiry.objects.all()
    serializer=EnquirySerializer(tasks,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def inspect(request,pk):
    tasks = NewsLetter.objects.get(id=pk)
    serializer=EnquirySerializer(tasks,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def information(request):
    serializer=EnquirySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        email=request.data['email']
        send_mail(
                'You are invited!',
                 'random text here',
                'Nautilus Technologies',
                [email],
                fail_silently=False,
                html_message = render_to_string('emails/invitation.html', {'email': email, 'url': 'nautilus.tech'})
                 ## So you specify the html_message parameter here. 
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
@api_view(['DELETE'])
def delete(request,pk):
    tasks=Enquiry.objects.get(id=pk)
    tasks.delete()
    return Response('Deleted')

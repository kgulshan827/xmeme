from django.shortcuts import render,redirect
from .models import Meme
from .import forms
from .serializers import MemeSerializer,NewMemeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def meme_input(request):


    if request.method == 'POST':
        form=forms.MemeForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('list')
    else:
      form=forms.MemeForm()
    return render(request,'meme_input.html',{'form':form})

def meme_list(request):
    meme=Meme.objects.all().order_by('-date')
    return render(request,'meme_list.html',{'meme':meme,})


 
 
class MemeAPIView(APIView):
 
    def get(self, request):
        memes = Meme.objects.all()
        serializer = MemeSerializer(memes, many=True)
        return Response(serializer.data)
 
    def post(self, request):
        serializer = MemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
class MemeDetails(APIView):
 
    def get_object(self, id):
        try:
            return Meme.objects.get(id=id)
        except Meme.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
 
    def get(self, request, id):
        article = self.get_object(id)
        serializer = MemeSerializer(article)
        return Response(serializer.data)
 
 
 
    def patch(self, request,id):
        memes = self.get_object(id)
    
        serializer = NewMemeSerializer(memes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def search(request):
    if request.method=='GET':
        search=request.GET.get('search')

        meme=Meme.objects.all().filter(caption=search)
        return render(request,'search.html',{'meme':meme})
 
    



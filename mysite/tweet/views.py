from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect
# Create your views here.

def index(request):
    return render(request,'index.html')

# CRUD operrations on Tweets  
# ----------------------------
# Reading the Tweets
def tweet_list(request):
    # Get all the tweets     ---  objects.all() ----> Returns list 
    tweets = Tweet.objects.all().order_by('-created_at') 
    
    return render(request,'tweet_list.html',{'tweets':tweets})
# Creating the Tweets
def tweet_create(request):
    # If user has filled the form and sent the request
    if request.method=='POST':
        # Getting the form
        form = TweetForm(request.POST,request.FILES)
        # This condition handles most important form validations
        if form.is_valid():
            # Save the form but not in the database
            tweet = form.save(commit=False)
            # you don't get the user in the tweet but u get it in the request object
            tweet.user = request.user
            tweet.save()
            
            # After successful creation of the tweet we are redirecting the user to the tweet_list page. 
            return redirect('tweet_list')
    else:
        #  user sending the empty form
        form = TweetForm()
    
    # Finally rendering the form 
    return render(request,'tweet_form.html',{'form':form})
# Editing the Tweets

# def tweet_edit(request,pageName/pageId):  pageName/pageId/... ----> These should be same in the urls     
def tweet_edit(request,tweet_id):
    
    # If there is already a tweet get it , only if the person wanted to edit is the original user 
    tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user)
    
    if request.method=='POST':
        # Getting the form , instance ---> to know whether it is the tweet that we want to edit
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            # Save the form but not in the database
            tweet = form.save(commit=False)
            # you don't get the user in the tweet but u get it in the request object
            tweet.user = request.user
            tweet.save()
            
            # After successful creation of the tweet we are redirecting the user to the tweet_list page. 
            return redirect('tweet_list')
    else:
        
        form = TweetForm(instance=tweet)
        
    return render(request,'tweet_form.html',{'form':form})
# Deleting the Tweets
def tweet_delete(request,tweet_id):
    
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})
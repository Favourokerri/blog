from django.shortcuts import render, redirect
from .models import Category, BlogPost, NewsLetter, Comment
from blog.validate import email_validation
from django.contrib import messages

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    categories = Category.objects.all()
    blog_posts = BlogPost.objects.all().order_by('-updated_at')

    # Pagination
    paginator = Paginator(blog_posts, 15)  # Show 1 blog post per page
    page = request.GET.get('page')

    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        blog_posts = paginator.page(paginator.num_pages)

    context = {
        "categories": categories,
        "blogPosts": blog_posts,
    }

    return render(request, 'home.html', context)



def SingleBlogPost(request, id):
    """ function for single blog post"""
    try:
        blogPost = BlogPost.objects.get(id=id)
    except Exception as e:
        print("this blog post may have been deleted")
    
    related_posts = BlogPost.objects.filter(category=blogPost.category).exclude(id=blogPost.id)
    comments = Comment.objects.filter(post=blogPost).order_by('-created_at')
    comment_count = comments.count()
    
    context = {"singleblogPosts": blogPost,
               "relatedPosts": related_posts,
               "comments": comments,
               "comment_count":comment_count}
    return render(request, 'blogpost.html', context)

def comment(request, id):
    """ comment section """
    if request.method == 'POST':
        name = request.POST['c-name']
        email = request.POST['c-email']
        comment_text = request.POST['c-comment']
        
        try:
            blogPost = BlogPost.objects.get(id=id)
        except BlogPost.DoesNotExist:
            messages.error(request, "The specified blog post does not exist.")
            return redirect('home')  # Redirect to the home page or another appropriate view
        
        comment_instance = Comment.objects.create(post=blogPost, name=name, email=email, comment=comment_text)
        messages.success(request, 'Comment created successfully')
        return redirect('singleblogpost', id=blogPost.id)



def newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if not email_validation(email):
            messages.warning(request, "not a valid email")
            return redirect('home')
        else:
            try:
                if not NewsLetter.objects.filter(email=email).exists():
                    NewsLetter.objects.create(email=email)
                    messages.success(request, "thanks for subscribing")
                else:
                    messages.warning(request, "you have already subscribed")
                return redirect('home')
            except Exception as e:
                messages.error(request, 'sorry an error occured. try again later or contact us')
                print(e)
                return redirect('home')

def search(request):
    query = request.GET.get('category', '')  # Default to an empty string if 'category' is not present in the request
    search_value = request.GET.get('search', '')

    try:
        categories = Category.objects.all()

        if query:
            blog_posts = BlogPost.objects.filter(category__category=query)
        elif search_value:
            blog_posts = BlogPost.objects.filter(title__icontains=search_value)

        print("Query:", query)
        print("Search Value:", search_value)
        print("blogPosts:", blog_posts)

    except Exception as e:
        messages.error(request, "Sorry, an error occurred. Please contact the admin.")
        print(e)
        blog_posts = []  # Set blog_posts to an empty list in case of an error

    context = {
        "blogPosts": blog_posts,
        "categories": categories,
    }
    return render(request, 'home.html', context)
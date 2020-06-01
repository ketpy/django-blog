from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from slugify import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required  

def Home(request):
	all_posts = BlogPost.objects.all()
	return render(request, 'Blogs/home.html', {'all_posts' : all_posts})

def PerPost(request, id , blog_slug):
	post = get_object_or_404(BlogPost, id = id, BlogSlug = blog_slug)
	return render(request, 'Blogs/post.html', {'post' : post})

@login_required
def NewPost(request):
	form = BlogPostForm()

	if request.method == "POST":
		form = BlogPostForm(request.POST ,request.FILES)
		if form.is_valid():
			form 		  = form.save(commit = False)
			form_slug 	  = slugify(str(request.POST['Title']))[0:20]
			form.Author   = request.user
			form.BlogSlug = form_slug
			form.save()


			messages.info(request, 'Blog Created Successfully...')

			return redirect('/post/{}/{}/'.format( str(form.id) , form_slug ))
	return render(request, 'Blogs/new_blog.html', {'form' : form})

@login_required
def DeletePost(request, id , blog_slug):
	post = get_object_or_404(BlogPost, id = id, BlogSlug = blog_slug)
	if post.Author == request.user:
		post.delete()
		messages.info(request, 'Your Blog Post Has Been Deleted Successfully.')
		return redirect('/')
	else :
		messages.info(request, 'You Cannot Delete This Blog Post.')
		return redirect('/')

@login_required
def EditPost(request, id , blog_slug):

	blog_post = get_object_or_404(BlogPost, id = id, BlogSlug = blog_slug)

	if blog_post.Author == request.user:
		form = BlogPostForm(instance = blog_post)

		if request.method == "POST":
			form = BlogPostForm(request.POST or None, request.FILES or None,  instance= blog_post)
			if form.is_valid():
				form = form.save(commit = False)
				form_slug = slugify(str(request.POST['Title']))
				form.Author = request.user
				form.BlogSlug = form_slug
				form.save()

				messages.info(request, 'Your post has been updated successfully.')

				return redirect('/post/{}/{}/'.format(id , form_slug ))
		return render(request, 'Blogs/edit_blog.html', {'form' : form})
	else :
		messages.info(request, 'You cannot edit this post.')
		return redirect(request, '/')
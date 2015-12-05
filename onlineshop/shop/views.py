from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from shop.models import Item, ItemImage, Category, Comment, Featured, FeaturedMainImage
from shop.forms import CommentForm

# from django.views.decorators.clickjacking import xframe_options_exempt
# from django.views.decorators.clickjacking import xframe_options_deny
# from django.views.decorators.clickjacking import xframe_options_sameorigin


def index(request):
    item_list = Item.objects.all()
    category_list = Category.objects.all()

    featured_list = Featured.objects.all()
    featured_image = FeaturedMainImage.objects.all()

    return render(request, 'shop/main.html', {'item_list': item_list, 'category_list': category_list, 'featured_list': featured_list, 'featured_image': featured_image, })

def featured_item(request, pk):
    category_list = Category.objects.all()
    featured_item = get_object_or_404(Featured, pk=pk)
    images = FeaturedMainImage.objects.filter(featured_id=pk)

    params = {'category_list': category_list, 'featured_item': featured_item, 'images': images, }
    return render(request,'shop/featured_item.html', params)


def category(request):
    category_list = Category.objects.all()

    #item_count = Item.objects.filter(category_id=Item).count()

    return render(request, 'shop/categories.html', {'category_list': category_list, })


def each_category(request, pk):
    category_list = Category.objects.all()

    item_list = Item.objects.filter(category_id=pk)
    each_category = get_object_or_404(Category, pk=pk)
    return render(request, 'shop/each_category.html', {'category_list': category_list, 'item_list': item_list, 'each_category': each_category,})


# @xframe_options_deny
def item_info(request, pk):
    item = Item.objects.get(pk=pk)
    item_images = ItemImage.objects.filter(item_id=pk)
    comments = ContentType.objects.get_for_model(item)
    #comment = Comment.objects.filter(content_type__pk=comments.id, object_id=item.id)
    comment= item.comments.all()

    category_list = Category.objects.all()
    comment_form = CommentForm()
    params = {'item': item, 'category_list': category_list, 'item_images': item_images, 'comment_form': comment_form,
    'comment':comment, }
    response = render(request, 'shop/item_info.html', params )
    return response

#@login_required
def comment_new(request, pk):
    item = get_object_or_404(Item, pk=pk)
    author = User.objects.filter()
    #author = User.objects.get()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.item = item
            if request.user.is_authenticated():
                comments.author=request.user
            #comments.author = author
            message = form.cleaned_data['message']
            item.comments.create(author=request.user, message=message)
            comments.save()

            """if request.is_ajax():
                return render(request, 'shop/item_info.html', {'comment': comment,})
            else:"""
            return redirect('shop:item_info', pk)
    else:
        form = CommentForm()

    return render(request, 'shop/comment_form.html', {'form': form, 'author': request.user, })

def comment_edit(request, item_pk, pk):
    item = get_object_or_404(Item, pk=item_pk)
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.item = item
            comment.save()
            return redirect('shop:item_info', comment.item.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'shop/comment_form.html', {'form': form, })

def comment_delete(request, item_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
        comment.delete()
        return redirect('shop:item_info', comment.object_id)

    return render(request, 'shop/comment_delete.html')

def user_exp(request):

    category_list = Category.objects.all()
    return render(request,'shop/user_exp.html', {'category_list': category_list, })

def buy_it(request):
    category_list = Category.objects.all()
    return render(request,'shop/buy_it.html', {'category_list': category_list, })

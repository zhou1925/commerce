from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from .recomender import Recommender
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'shop/contact.html'

def contact(request):
    return render(request, 'shop/contact.html')


def home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/index.html', {'category': category,
                                               'categories': categories,
                                               'products': products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        #products = Product.objects.filter(available=True)
        #products = products.filter(category=category)
        products = Product.objects.filter(category=category)

    search_query = request.GET.get('search')
    if search_query:
        products = Product.objects.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query)
        )

    return render(request, 'shop/shop-grid.html', {'category': category,
                                                   'categories': categories,
                                                   'products': products,
                                                   'page': page})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    return render(request,
                  'shop/shop-details.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'recommended_products': recommended_products})




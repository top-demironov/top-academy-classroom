from django.shortcuts import render, redirect

from products.forms import ProductForm
from products.models import Product


def product_list(request):
	products = Product.objects.all()
	return render(request, 'products/product_list.html', {'products': products})


def add_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('product_list')
		else:
			pass
	else:
		form = ProductForm()
		return render(request, 'products/add_product.html',
								{'form': form})

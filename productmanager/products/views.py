from django.shortcuts import render, redirect

from products.forms import ProductForm
from products.models import Product


def product_list(request):
	products = Product.objects.all()
	return render(request, 'products/product_list.html', {'products': products})


def add_product(request):
	if request.method == 'POST':
		print(request.POST['completed'])

		# form = ProductForm(request.POST)
		# if form.is_valid():
		# 	form.save()

		return redirect('product_list')
	else:
		form = ProductForm()
		return render(request, 'products/add_product.html',
								{'form': form})





# +++++ 1. Повторение сложных тем
# 2. Night coding (2), заинтересованность в обучении
# +++++ 3. Кофе-машина
# +++++ 4. Сложные темы, одна домашняя работа на неделю
# +++++ 5. Работа над ошибками



# Вторник
# 1. Ретроспектива
# 2. Разбираем домашку
# 3. Свободное время для закрытия долгов

# Четверг
# 1. Теория
# 2. Практика









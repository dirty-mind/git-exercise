from django.shortcuts import render
def index(request):
	return render(request,"proApp/index.html")
	
def mobiles(request):
	mobiles={
		'pro1' : 'nokia',
		'pro2' : 'ios',
		'pro3' : 'shiao',
	}
	return render(request,"proApp/products.html",context = mobiles)
def laptops(request):
	laptops = {
	
		'pro1' : 'asus',
		'pro2' : 'dell',
		'pro3' : 'hp',
	}
	return render(request,"proApp/products.html",context = laptops)
def gadg(request):
	dadg = {
		'pro1' : 'a',
		'pro2' : 'b',
		'pro3' : 'c',
	}
	return render(request,"proApp/products.html",context = gadg)
				
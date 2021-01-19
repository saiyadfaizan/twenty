
import datetime as dt
import json
from json import loads

from django.conf import settings
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserCreationForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import (DetailView, FormView, ListView, TemplateView,
                                  View)
from django.views.generic.edit import CreateView
from .filters import CategoryFilter, OrderFilter
from .forms import EditUserProfileForm, UpdateUserForm, UserRegisterForm, ProductForm, ProductUpdateForm
from .models import *
from .tasks import send_email_task
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {}
    return render(request, 'store/index.html', context)
    
# Views for Admin side:

class AdminLoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'store/adminpages/adminlogin.html'
    success_url = reverse_lazy('adminstore')

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None and Admin.objects.filter(user=user).exists():
            login(self.request, user)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, 
            "error": "Invalid credentials"})

        return super().form_valid(form)


class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/admin-login/")
        return super().dispatch(request, *args, **kwargs)



class AdminStoreView(TemplateView, AdminRequiredMixin):
    template_name = 'store/adminpages/adminstore.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_products = Product.objects.all()
        context = {'all_products':all_products}
        return context

    
class AdminOrderView(TemplateView, AdminRequiredMixin):
    template_name = 'store/adminpages/adminorderlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allorders = Order.objects.filter(complete=True).order_by("-id")
        allstatus = ORDER_STATUS
        context = {'allorders': allorders, 'allstatus':allstatus}
        return context


class AdminOrderDetailView(AdminRequiredMixin, View):
    
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)
        shipping = ShippingAddress.objects.get(order__id=order_id)
        context = {'order': order, 'order_items': order_items, 'shipping':shipping}
        return render(request, 'store/adminpages/adminorderdetail.html', context)

class AdminProfileView(AdminRequiredMixin, TemplateView):

    def get(self, request):
        user = request.user
        form = EditUserProfileForm(request.POST, instance=request.user)
        return render(request, 'store/adminpages/adminprofile.html',
                      {'name': request.user, 'form': form})


class AdminAddProductView(FormView):
    form_class = ProductForm
    success_url = reverse_lazy('adminstore')
    template_name = 'store/adminpages/adminaddproduct.html'
    
        
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url )


class AdminOrderStatuChangeView(AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        order_id = self.kwargs['order_id']
        order = Order.objects.get(id=order_id)
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect(reverse_lazy('adminorderdetail', kwargs={'order_id': order_id}))

def admincategory(request):
	
	orders = Order.objects.all()
	adminFilter = OrderFilter(request.GET, queryset=orders)
	orders = adminFilter.qs 
	context = {'orders':orders, 'adminFilter':adminFilter}

	return render(request, 'store/adminpages/admincategory.html', context) 

class AdminAllProductView(AdminRequiredMixin, TemplateView):
    template_name = 'store/adminpages/adminallproduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allproducts = Product.objects.all()
        context = {'allproducts': allproducts}
        return context

def updateproduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductUpdateForm(instance=product)

    if request.method == 'POST':
       form = ProductUpdateForm(request.POST, instance=product)
       if form.is_valid():
           form.save()
       return redirect('adminallproduct')

    context = {'form':form}

    return render(request, 'store/adminpages/editproduct.html', context)


def deleteproduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('adminallproduct')

    context = {'product':product}

    return render(request, 'store/adminpages/deleteproduct.html', context)

# Views for User side:

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'store/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


class LoginView(generic.View):
    form_class = AuthenticationForm
    template_name = 'store/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request=request)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None and Customer.objects.filter(user=user).exists():
                login(request, user)
                return redirect('store')
            else:
                return HttpResponse("Inactive user.")
        else:
            #return HttpResponse('Wrong Password')
            return render(request, 'store/wrongpassword.html')

        return render(request, "store/store.html")

'''

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'store/login.html'
    success_url = reverse_lazy('store')

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None and Customer.objects.filter(user=user).exists():
            login(self.request, user)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)
'''

class LogoutView(generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return reverse('index')

class UpdateUserView(LoginRequiredMixin, generic.UpdateView):
    form_class = UpdateUserForm
    template_name = 'store/update_user.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial, instance=request.user)
        context = {'form': form}
        return render(request, 'store/update_user.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('profile')

        return render(request, 'store/update_user.html', context)


class UpdatePasswordView(LoginRequiredMixin, generic.FormView):
    form_class = PasswordChangeForm
    template_name = 'store/change_password.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial, user=request.user)
        context = {'form': form}
        return render(request, 'store/change_password.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, user=request.user)
        context = {'form': form}
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/')

        return render(request, 'store/change_password.html', context)

@login_required()
def store(request):
    
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    products = Product.objects.all()
    
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

@login_required()
def cart(request):

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all().order_by('product__name')
    cartItems = order.get_cart_items
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

@login_required()
def checkout(request):

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all().order_by('product__name')
    cartItems = order.get_cart_items
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

@login_required()
def profile(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditUserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
        else:
            form = EditUserProfileForm(instance=request.user)
        return render(request, 'store/profile.html',
                      {'name': request.user, 'form': form})
    else:
        return render('store/store.html')

@login_required()
def updateItem(request):

    data = json.loads(request.body.decode('utf-8'))
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

@login_required()
def processOrder(request):

    transaction_id = dt.datetime.now().timestamp()
    data = json.loads(request.body.decode('utf-8'))
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order.emailAddress = request.user.email
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
        order.status = 'Order Received'
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Order Placed', safe=False)


class OrderHistory(View, LoginRequiredMixin):

    def get(self, request):
        email = str(request.user.email)
        order_details = Order.objects.filter(emailAddress=email).exclude(
            status='Order Initiated').order_by('-date_ordered')
        context = {'order_details': order_details}
        return render(request, 'store/order_history.html', context)

class ViewOrder(View, LoginRequiredMixin):

    def get(self, request, order_id):
        email = str(request.user.email)
        order = Order.objects.get(id=order_id, emailAddress=email)
        order_items = OrderItem.objects.filter(order=order)
        shipping = ShippingAddress.objects.get(order__id=order_id)
        context = {'order': order, 'order_items': order_items, 'shipping':shipping}
        return render(request, 'store/order_detail.html', context)

@login_required()
def category(request):
	
	products = Product.objects.all()
	myFilter = CategoryFilter(request.GET, queryset=products)
	products = myFilter.qs 
	context = {'products':products, 'myFilter':myFilter}
	return render(request, 'store/category.html', context) 

@login_required()
def success(request):
    
    send_email_task(request.user.email)
    customer = request.user.customer
    context = {'customer':customer}
    return render(request, 'store/success.html', context)


class SearchView(ListView):
    model = Product
    template_name = 'store/search.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('query')
        products = Product.objects.filter(Q(name__icontains=query) | Q(
            description__icontains=query) | Q(category__name__icontains=query))
        return products

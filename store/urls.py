from os import name, path

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import (LoginView, LogoutView, OrderHistory, SearchView,
                    SignUpView, UpdatePasswordView, UpdateUserView, ViewOrder, 
                    AdminLoginView, AdminStoreView, AdminOrderDetailView, AdminOrderView,
                    AdminProfileView, AdminAddProductView, AdminOrderStatuChangeView, AdminAllProductView,
                    admincategory, updateproduct, deleteproduct, index)

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('profile/', views.profile, name="profile"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('order_history/', OrderHistory.as_view(), name='order_history'),
    path('order/<int:order_id>', ViewOrder.as_view(), name='order_detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('category/', views.category, name='category'),
    path('success/', views.success, name='success'),
   

    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update_user/', UpdateUserView.as_view(), name='update_user'),
    path('change_password/', UpdatePasswordView.as_view(), name='change_password'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='store/password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='store/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='store/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='store/password_reset_complete.html'), name='password_reset_complete'),

    path('admin-login/', AdminLoginView.as_view(), name='adminlogin'),
    path('admin-store/', AdminStoreView.as_view(), name='adminstore'),
    path('admin-order/', AdminOrderView.as_view(), name='adminorder'),
    path('admin-profile/', AdminProfileView.as_view(), name='adminprofile'),
    path('admin-addproduct/', AdminAddProductView.as_view(), name='adminaddproduct'),
    path('admin-orderdetail/<int:order_id>/', AdminOrderDetailView.as_view(), name='adminorderdetail'),
    path('admin-order-<int:order_id>-change/', AdminOrderStatuChangeView.as_view(), name="adminorderstatuschange"),
    path('admin-category/', views.admincategory, name='admincategory'),
    path('admin-allproduct/', AdminAllProductView.as_view(), name='adminallproduct'),
    path('updateproduct/<str:pk>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<str:pk>/', views.deleteproduct, name='deleteproduct'),
    #path('admin-updateproduct/<int:product_id>', AdminUpdateProductView.as_view(), name='adminupdateproduct'),


]

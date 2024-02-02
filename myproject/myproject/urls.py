from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from myapp.views import ClientList, ClientDetail, ProductList, BillList, RegisterUser, ClientCSVExport, ClientCSVImport,BillDetail, ProductDetail,ClientListView,ClientCreateView

urlpatterns = [
    path('clients/', ClientList.as_view(), name='client-list'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('bills/', BillList.as_view(), name='bill-list'),
    path('register/', RegisterUser.as_view(), name='register-user'),
    path('clients/export/', ClientCSVExport.as_view(), name='client-csv-export'),
    path('clients/import/', ClientCSVImport.as_view(), name='client-csv-import'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('clients/', ClientList.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('bills/', BillList.as_view(), name='bill-list'),
    path('bills/<int:pk>/', BillDetail.as_view(), name='bill-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('clients/list/', ClientListView.as_view(), name='client-list-view'),
    path('clients/create/', ClientCreateView.as_view(), name='client-create-view'),
]

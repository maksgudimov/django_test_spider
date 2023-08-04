from django.urls import path,include

from .views import OrganizationList,ProductsList ,SearchProductsList,InsertProducts#,ProductsList
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('api/organizations/<int:district_id>/', OrganizationList.as_view()),
    path('api/products/<int:organization_id>/', ProductsList.as_view()),
    path('api/products/search/<str:name_product>/', SearchProductsList.as_view()),
    path('api/products/insert/', InsertProducts.as_view()),
    path('api/token/', obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)

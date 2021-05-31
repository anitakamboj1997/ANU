from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('add/', views.add_stu),
    path('show', views.show),

    
    # path('update/<int:pk>', views.ContactUpdate.as_view(), name='contact_update'),
    path('delete/<int:pk>', views.delete_stu, name='contact_delete',),
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]
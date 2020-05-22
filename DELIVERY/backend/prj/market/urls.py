from django.conf.urls import url, include
from rest_framework import routers
from market.views.category import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('v1/',include(router.urls)),
    path('v1/',include([
        path('generic/',include(router.urls)),
        path('market',include('market.urls')
        
    ])),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]


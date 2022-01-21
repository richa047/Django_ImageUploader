

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),# flow url.py(mac)->  shop.url(shop)view.index->  views.py(shop)(index fun)
     path('blog/', include('blog.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
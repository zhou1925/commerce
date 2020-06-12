from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap


sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path(_('orders/'), include('orders.urls', namespace='orders')),
    path(_('cart/'), include('cart.urls', namespace='cart')),
    path(_('blog/'), include('blog.urls', namespace='blog')),
    path('', include('shop.urls', namespace='shop')),
    path(_('payment/'), include('payments.urls', namespace='payment')),
    path(_('coupons/'), include('coupons.urls', namespace='coupons')),


    path('rosetta/', include('rosetta.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


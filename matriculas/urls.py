from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^lang/$", TemplateView.as_view(template_name="language.html"), name="language"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^sermepa/", include("sermepa.urls")),
    url(r"^pasarela/", include("pasarela.urls")),
    url(r"^pagosonline/", include("pagosonline.urls")),
    url(r"^cambridge/", include("cambridge.urls")),
    url(r"^hobetuz/", include("hobetuz.urls")),
    url(r"^intensivos/", include("intensivos.urls")),
    url(r"^leveltests/", include("leveltests.urls")),
	url(r"^i18n/", include('django.conf.urls.i18n')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from fluent_pages.sitemaps import PageSitemap
from fluent_pages.views import RobotsTxtView
from fluent_blogs.sitemaps import (EntrySitemap, CategoryArchiveSitemap, 
                                   AuthorArchiveSitemap, TagArchiveSitemap)

sitemaps = {
    'pages': PageSitemap,
    'blog_entries': EntrySitemap,
    'blog_categories': CategoryArchiveSitemap,
    'blog_authors': AuthorArchiveSitemap,
    'blog_tags': TagArchiveSitemap,

}


urlpatterns = [
    path('sitemap.xml', TemplateView.as_view(template_name='django.contrib.sitemaps.views.sitemap'), {'sitemaps': sitemaps}),
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("jazmin_leon_llc.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path('pages/', include('fluent_pages.urls')),
    path('admin/util/taggit_autosuggest/', include('taggit_autosuggest.urls')),
    path('taggit/', include('taggit_selectize.urls')),
    path('blog/comments/', include('fluent_comments.urls')),   # or fluent_comments.urls
    path('filer/', include('filer.urls')),
    path('securefiler/', include('filer.server.urls')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

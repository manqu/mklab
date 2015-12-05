from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'shop.views.index', name='index'),
    url(r'^featured_item/(?P<pk>\d+)/$', 'shop.views.featured_item', name='featured_item'),
    url(r'^category/$', 'shop.views.category', name='category'),
    url(r'^category/(?P<pk>\d+)/$', 'shop.views.each_category', name='each_category'),
    url(r'^item/(?P<pk>\d+)/$', 'shop.views.item_info', name='item_info'),
    url(r'^item/(?P<pk>\d+)/comment/new/$', 'shop.views.comment_new', name='comment_new'),
    url(r'^item/(?P<item_pk>\d+)/comment/(?P<pk>\d+)/edit/$', 'shop.views.comment_edit', name='comment_edit'),
    url(r'^item/(?P<item_pk>)\d+/comment/(?P<pk>\d+)/delete/$', 'shop.views.comment_delete', name='comment_delete'),
    url(r'^user_exp/$', 'shop.views.user_exp', name='user_exp'),
    url(r'^buy_it/$', 'shop.views.buy_it', name='buy_it'),
]

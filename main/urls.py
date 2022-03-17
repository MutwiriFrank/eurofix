
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('dealers/', views.dealers_page, name = 'dealers' ),
    path('about/', views.about, name = 'about' ),
    path('gallery/', views.gallery, name = 'about' ),
    path('all-products/', views.all_products, name = 'all-products' ),
    path("", views.subscription, name="subscription"),
    
    path('<slug:slug>/', views.category_page ),  # category
    path('tile-applications/<slug:slug>/', views.product_page ),
    path('waterproofing/<slug:slug>/', views.product_page, name = 'waterproofing' ),
    path('cement/<slug:slug>/', views.product_page, name = 'cement' ),
    path('finishing-and-decorations/<slug:slug>/', views.product_page, name = 'finishin-and-decorations' ),
    path('bricks-and-cabros/<slug:slug>/', views.product_page, name = 'pavingblocks' ),
    path('blocks/<slug:slug>/', views.product_page, name = 'blocks' ),
    path('construction-chemicals/<slug:slug>/', views.product_page, name = 'construction-chemicals' ),

    
    
]

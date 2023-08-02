from django.urls import path,include
from techdoc_apis import views


urlpatterns = [    
    path('manufacture/',views.find_manufactures,name='manufacture'),
    path('model/',views.find_model,name='model'),
    path('type/',views.find_type,name='type'),
    path('sidebar/',views.find_sidebar,name='sidebar'),
    path('categories/',views.find_categories_subcategories,name='categories'),
    path('categories_subcategories/',views.find_subcategories_subcategories,name='categories_subcategory'),
    path('find_articles/',views.find_articles_from_categories,name='article'),
    path('article_info/',views.find_article_information,name='article_info'),
    path('autoCompletesuggestions/',views.AutoCompleteSuggestions,name='autoCompletesuggestions'),
    path('oempartsearch/',views.OEM_FILTER_FROM_DATABASE,name='oempartsearch'),
    

]
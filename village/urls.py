from django.contrib import admin
from django.urls import path
from emploi_village import views
from emploi_village.views import VilleAutocomplete, MetierAutocomplete
from django.conf import settings
from django.conf.urls.static import static
from emploi_village.views import inscription_custom  # Import de la vue
from emploi_village.views import afficher_personnels,supprimer_personnel,admin1
from emploi_village.views import admin_page, ajoute_village, ajoute_metier



urlpatterns = [
    path('admin1/', admin_page, name='admin1'),
    path('admin/', admin.site.urls),
    path('', views.pagea, name='pagea'),
    path('teste0/', views.teste0, name='teste0'),
    #path('inscription_custom/', inscription_custom, name='inscription_custom'),
    path('affiche_village/', views.affiche_village, name='affiche_village'),
    path('affiche_metier/', views.affiche_metier, name='affiche_metier'),
    path('list_personnel/', views.list_personnel, name='list_personnel'),
    path('inscription/', inscription_custom, name='inscription_custom'),
    path('ville-autocomplete/', VilleAutocomplete.as_view(), name='ville-autocomplete'),
    path('metier-autocomplete/', MetierAutocomplete.as_view(), name='metier-autocomplete'),
    path('ajoute_village/', ajoute_village, name='ajoute_village'),
    path('ajoute_metier/', ajoute_metier, name='ajoute_metier'),
    path('afficher_personnels/', afficher_personnels, name='afficher_personnels'),
    path('supprimer_personnel  /<int:personnel_id>/', supprimer_personnel, name='supprimer_personnel'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
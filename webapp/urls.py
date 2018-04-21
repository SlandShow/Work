from django.conf.urls import url, include
# from .views import index
#from .views import MessageViewSet

#urlpatterns = [
 #   url(r'^$', views.index, name='index'),

    # Test api 
  #  url(r'^api/test', views.test_api, name='test_api'),
#]


from rest_framework import routers
from .views import MessageViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'message', MessageViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = [
  url(r'^$', MessageViewSet, name='message'),
  # url(r'^api/test', views.test_api, name='test_api')
]
 
urlpatterns += router.urls
# = router.urls

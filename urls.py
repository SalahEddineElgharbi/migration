from django.conf.urls import url, include 


from . import views
app_name='blog'   # coome name space  blog : show wla : index
handler404='monweb.views.handler404'
urlpatterns = [
 
    url(r'^$' , views.inde, name ='index'),
    url(r'^posts/(?P<id>[0-9]+)$',views.show , name='show'),
  
]

include
from . import views

urlpatterns = [
    url(r'^input/', views.input, name='input'),
    url(r'^authenticate/', views.authenticate, name='authenticate'),
    url(r'^train/', views.train, name='train'),
    url(r'^result/', views.result, name='result')
]

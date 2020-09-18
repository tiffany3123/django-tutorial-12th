from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]



# 예를 들어
# polls 앱 -> 'polls'
# polls 앱 안에있는 index 뷰 -> 'index'

# 위에 두개를 하려면 /polls/index 이렇게 써야함



from django.urls import path
from graphene_django.views import GraphQLView

app_name = "patient"

urlpatterns = [
    path('graph-ql/', GraphQLView.as_view(graphiql=True)),
]
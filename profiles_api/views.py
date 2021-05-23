# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View"""

    def get(self, request, format=None):
        """Returns a list of APiView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch , put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is manually to URLS',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

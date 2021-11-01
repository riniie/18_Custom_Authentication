from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .authentication import CustomAuthentication
from .models import Student
from .serializers import StudentSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]

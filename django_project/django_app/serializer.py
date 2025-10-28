from rest_framework import serializers
from .models import StudentDetails

class Student_Seralizer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = "__all__"
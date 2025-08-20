from rest_framework import serializers
from .models import Course, CourseClass
from users.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "course_code", "course_name", "description"]

class CourseClassSerializer(serializers.ModelSerializer):
    teacher_detail = UserSerializer(source="teacher", read_only=True)
    course_detail = CourseSerializer(source="course", read_only=True)

    class Meta:
        model = CourseClass
        fields = [
            "id", "course", "course_detail", "code", "teacher", "teacher_detail",
            "semester", "room", "schedule_day", "start_time", "end_time",
            "created_at", "updated_at"
        ]
        read_only_fields = ["created_at", "updated_at"]


        class Meta:
            model = CourseClass
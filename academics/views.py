from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from core.permissions import AdminOrReadOnly, IsAdminOrTeacher
from .models import CourseClass
from .serializers import CourseClassSerializer
from academics.serializers import CourseClassSerializer


class CourseClassViewSet(viewsets.ModelViewSet):
    queryset = CourseClass.objects.select_related("course", "teacher", "semester").all()
    serializer_class = CourseClassSerializer
    permission_classes = [AdminOrReadOnly]
    search_fields = ["course__code", "course__name", "code", "teacher__username"]

    @action(detail=True, methods=["post"], permission_classes=[IsAdminOrTeacher])
    def assign_teacher(self, request, pk=None):
        """
        Assign a teacher to the class (Admin or Teacher only)
        payload: {"teacher_id": 5}
        """
        obj = self.get_object()
        teacher_id = request.data.get("teacher_id")
        if not teacher_id:
            return Response({"detail": "teacher_id required"}, status=status.HTTP_400_BAD_REQUEST)
        from users.models import User
        try:
            teacher = User.objects.get(pk=teacher_id, role="TEACHER")
        except User.DoesNotExist:
            return Response({"detail": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        obj.teacher = teacher
        obj.save()
        return Response(self.get_serializer(obj).data)
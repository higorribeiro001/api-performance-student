from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import StudentPerformance
from .serializers import StudentPerformanceSerializer
from rest_framework.pagination import PageNumberPagination
from network import rede_neural

class StudentPerformanceView(ModelViewSet):
    queryset = StudentPerformance.objects.all()
    serializer_class = StudentPerformanceSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        try:
            params = [
                request.data['age'],
                request.data['gender'],
                request.data['ethnicity'],
                request.data['paramental_education'],
                request.data['study_time_weekly'],
                request.data['absenses'],
                request.data['tutoring'],
                request.data['parental_suporte'],
                request.data['extracurricular'],
                request.data['sports'],
                request.data['music'],
                request.data['voluteering'],
            ]

            output = rede_neural(params)[0][0] or 0

            output_categ = (
                'A' if output > 3.5 else
                'B' if 3.0 <= output < 3.5 else
                'C' if 2.5 <= output < 3.0 else
                'D' if 2.0 <= output < 2.5 else
                'F'
            )

            request.data.update(
                {
                    'gpa': output,
                    'grade_class': output_categ
                },
            )

            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()

            return Response(
                {
                    'resultado': output,
                    'classe': output_categ
                }, 
                status=status.HTTP_201_CREATED
            )
        
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_400_BAD_REQUEST)

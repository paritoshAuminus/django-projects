from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# -------------------------------------
# CRUD operation using APIView with CBV
# -------------------------------------

class StudentAPI(APIView):
    
    # GET - Read All or Single data
    def get(self, request, pk=None):
        
        # Read single data
        if pk:
            try:
                student = Student.objects.get(id=pk)
                serailizer = StudentSerializer(student)
                return Response(serailizer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        # Read all data
        else:
            students = Student.objects.all()
            serailizer = StudentSerializer(students, many=True)
            return Response(serailizer.data, status=status.HTTP_200_OK)

    # POST - Create new student
    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # PUT - Update data (complete update)
    def put(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(instance=student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # PATCH - Updating partial data
    def patch(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'error:': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(instance=student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE - Delete data
    def delete(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
            student.delete()
            return Response({'message': 'Student deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'error: Student not found.'}, status=status.HTTP_404_NOT_FOUND)
        
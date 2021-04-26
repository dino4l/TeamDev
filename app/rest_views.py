from rest_framework import status, decorators, response, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .use_cases import *
from .serializers import *

@api_view(['GET', 'POST'])
def index_view(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)
        questions = new_questions_case(page, limit)
        serializer = QuestionSerializer(questions, many=True)
        st = status.HTTP_200_OK
    elif request.method == 'POST':
        question = create_question_case(request.POST, request.user)
        serializer = QuestionSerializer(question)
        if serializer.is_valid():
            st = status.HTTP_201_CREATED
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response('Error', status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status=st)

@api_view(['GET'])
def hot_view(request):
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    questions = hot_questions_case(page, limit)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def question_id_view(request, qid):
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    question, answers = question_by_id_case(qid, page, limit)
    print(question)
    print(answers)
    if question is None:
        return Response('Error', status=status.HTTP_400_BAD_REQUEST)
    qserializer = QuestionSerializer(question)
    aserializer = AnswerSerializer(answers, many=True)
    data = {"question": qserializer.data, "answers": aserializer.data }
    return Response(data)

from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializer import *
from core.views.query_db import conn_db


@api_view(['GET', ])
@permission_classes((AllowAny, ))
def access_valid(request):

    return Response({'API - Insight Local'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_pedido(request):
    serializer = PedidoSerializer(data=request.data)
    if serializer.is_valid():

        # Gravar pedido no banco oracle
        insert_sql = f"INSERT INTO api_pedido (column_name, column_name) VALUES ({request.cod_produto}, {request.desc_produto})"
        queryset_insert_oracle(insert_sql)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'não foi possível cadastrar pedido no db'}, status=status.HTTP_400_BAD_REQUEST)


def queryset_insert_oracle(select_oracle):
    """
    Função responsável por gravar pedido no banco oracle
    """

    cur, con = conn_db()
    cur.execute(select_oracle)

    cur.close()
    con.close()

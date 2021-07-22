from django.shortcuts import render
from core.query import query_ult_entrada, query_estoque, query_hist, query_p_compras, query_p_vendas, query_produto, query_fornecedor


def ult_entrada(request, template_name='teste.html'):
    query_ult_entrada()
    return render(request, template_name)


def estoque(request, template_name='teste.html'):
    query_estoque()
    return render(request, template_name)


def hist_estoque(request, template_name='teste.html'):
    query_hist()
    return render(request, template_name)


def p_compras(request, template_name='teste.html'):
    query_p_compras()
    return render(request, template_name)


def p_vendas(request, template_name='teste.html'):
    query_p_vendas()
    return render(request, template_name)


def produto(request, template_name='teste.html'):
    query_produto()
    return render(request, template_name)


def fornecedor(request, template_name='teste.html'):
    query_fornecedor()
    return render(request, template_name)

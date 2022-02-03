from core.tasks import *
from apscheduler.schedulers.background import BackgroundScheduler
from core.views.api_login import get_data_company


# def hello_word():
#     print("test - hello word")
#
#
# def run_tasks():
#     print("ok")
#     # task_fornecedores()
#     # task_produtos()
#     # task_historico()
#     # task_vendas()
#     # task_pedidos()
#     # task_entradas()
#     # task_estoque()


# def start():
#     company = get_data_company()
#
#     scheduler = BackgroundScheduler(timezone='America/Sao_Paulo', job_defaults={'max_instances': 2})
#     # scheduler.add_job(hello_word, 'interval', seconds=120)
#
#
#     if company.enable_tasks:
#         # scheduler.add_job(run_tasks, 'interval', seconds=900)
#         scheduler.add_job(run_tasks, 'interval', seconds=3600)
#     scheduler.start()
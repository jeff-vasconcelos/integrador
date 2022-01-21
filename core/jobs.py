from core.tasks import *
from apscheduler.schedulers.background import BackgroundScheduler
from core.views.api_login import get_data_business


def hello_word():
    print("test - hello word")


def run_tasks():

    task_fornecedores()
    task_produtos()
    task_historico()
    task_vendas()
    task_pedidos()
    task_entradas()
    task_estoque()


def start():
    business = get_data_business()

    scheduler = BackgroundScheduler(timezone='America/Sao_Paulo', job_defaults={'max_instances': 2})
    # scheduler.add_job(hello_word, 'interval', seconds=120)


    if business.enable_tasks:
        #scheduler.add_job(run_tasks, 'interval', seconds=30)
        scheduler.add_job(run_tasks, 'interval', seconds=2400)
    scheduler.start()
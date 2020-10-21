## send mail for me..... (100000)
from __future__ import absolute_import
import time
from celery.decorators import task

@task
def SayHelloAfter10Sec():
    time.sleep(10)
    print("Hello.. I am from Celery and Redis...")
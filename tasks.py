from os import path as os_path
from sys import path as sys_path
from inspect import currentframe as f
from invoke import task

APP_PATH = os_path.abspath(
    os_path.dirname(__file__)
)
LIB_PATH = os_path.join(APP_PATH, 'libtool')
sys_path.insert(
    1,
    os_path.abspath(os_path.join(LIB_PATH))
)

from benchmarks import (
    bitslicing
)

#from examples import (
#    hamming
#)

EXIST_T_MSG_TMPL = (
    'Set existing %s target name'
)

@task(optional=['target'])
def bench(c, target=None):
    t = globals().get(target, None)
    if not t:
        print(EXIST_T_MSG_TMPL % f().f_code.co_name)
        return    
    t.run()


#@task(optional=['target'])
#def example(c, target=None):
#    t = globals().get(target, None)
#    if not t:
#        print(EXIST_T_MSG_TMPL % f().f_code.co_name)
#        return    
#    t.run()

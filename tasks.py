from invoke import task
from benchmarks import (
    bitslicers
)


@task(optional=['target'])
def bench(c, target=None):
    t = globals().get(target, None)
    if not t:
        print('Set banchmark group name')
        return    
    t.bench()

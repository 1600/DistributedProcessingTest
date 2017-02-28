import gevent

def foo():
    print "running in foo"
    #gevent.sleep(0)
    print "context switch to foo again"

def bar():
    print 'switching to bar'
    gevent.sleep(0)
    print 'implicit context switch'

gevent.joinall([gevent.spawn(foo),gevent.spawn(bar)])


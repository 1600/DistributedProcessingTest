import gevent

def foo():
    print "running in foo"
    gevent.sleep(0)
    print "context switch to foo again"

def bar():
    print 'switching to bar'
    gevent.sleep(0)
    print 'back to bar....'

def koo():
    print 'switching to koo'
    gevent.sleep(0)
    print 'back to koo again!'


gevent.joinall([gevent.spawn(foo),gevent.spawn(bar),gevent.spawn(koo)])



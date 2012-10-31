import sys, gc
 
def make_cycle():
    l = { }
    l[0] = l
 
def main():
    print "Garbage collection thresholds: %r,%r,%r" % gc.get_threshold()
    collected = gc.collect()
    print "Garbage collector: collected %d objects." % (collected)
    print "Creating cycles..."
    for i in range(10000):
        make_cycle()
    collected = gc.collect()
    print "Garbage collector: collected %d objects." % (collected)
 
if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
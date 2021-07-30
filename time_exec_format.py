import time

def exec(i):
    if i <= 2:
        return 1;
    else:
        f = exec(i-1) + exec(i-2)
    return f

start = time.time()

print(exec(4))

end = time.time()
execution_time = end - start

print ('--- %0.3fms. --- ' % ( execution_time*1000.))
print("--- %s seconds ---" % (execution_time ))
print("--- %s minutes ---" % (execution_time / 60))

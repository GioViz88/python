from datetime import datetime

def exec(i):
    if i <= 2:
        return 1;
    else:
        f = exec(i-1) + exec(i-2)
    return f

start_time = datetime.now()

print(exec(4))

time_elapsed = datetime.now() - start_time
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

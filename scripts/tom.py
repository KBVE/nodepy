import time 

start_time = time.time()

for i in range (0,100000):
        print(i, end=' ');


end_time = time.time()

print(f"\nTime taken: {end_time - start_time} seconds");
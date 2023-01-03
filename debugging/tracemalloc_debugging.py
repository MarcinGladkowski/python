import tracemalloc

tracemalloc.start(10) # 10 frames of stack

time1 = tracemalloc.take_snapshot()

import waste_memory_program

x = waste_memory_program.run()

time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'lineno')

for stat in stats[:3]:
    print(stat)
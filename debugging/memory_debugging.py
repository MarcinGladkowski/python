import gc

found_objects = gc.get_objects()
print(f'{len(found_objects)} objects before')

import waste_memory_program

hold_reference = waste_memory_program.run()

found_objects = gc.get_objects()
print(f'{len(found_objects)} objects after')
for obj in found_objects[:3]:
    print(repr(obj)[:100])
def main(a: str = 'default'):
    print("Hello world >> stdout")

for n in dir(main):
    print(n)    
    
    
print(main.__code__)
print(main.__defaults__)
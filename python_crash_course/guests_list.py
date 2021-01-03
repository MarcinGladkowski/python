guests_list = ['Kubica', 'Musk', 'Gates']

print(f'Hi! {guests_list[0]}')
print(f'Hi! {guests_list[1]}')
print(f'Hi! {guests_list[2]}')

print(f'{guests_list[2]} cannot arrive')

guests_list.remove('Gates')
guests_list.insert(2, 'Verstapen')

print(f'Hi! {guests_list[0]}')
print(f'Hi! {guests_list[1]}')
print(f'Hi! {guests_list[2]}')

print('We have more space!')

guests_list.insert(0, 'Raikonnen')
guests_list.insert(1, 'Leclerc')
guests_list.append('Vettel')

print(f'Hi! {guests_list[0]}')
print(f'Hi! {guests_list[1]}')
print(f'Hi! {guests_list[2]}')
print(f'Hi! {guests_list[3]}')
print(f'Hi! {guests_list[4]}')
print(f'Hi! {guests_list[5]}')

print(f'We have only two seats!')

print(f'Really sorry! {guests_list.pop()}')
print(f'Really sorry! {guests_list.pop()}')
print(f'Really sorry! {guests_list.pop()}')
print(f'Really sorry! {guests_list.pop()}')

print(guests_list)

print(f'Welcome to our dinner {guests_list[0]}')
print(f'Welcome to our dinner {guests_list[1]}')

print(guests_list)
print(guests_list[1])
del guests_list[0]
# move element to other index
del guests_list[0]

print(guests_list)




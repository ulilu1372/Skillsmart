def Keymaker(k):
    door_array = []
    for x in range(k):
        door_array.append('0')
    step = 1
    for i in range(k):
        j = step - 1
        while j < k:
            if door_array[j] == '1':
                door_array[j] = '0'
            else:
                door_array[j] = '1'
            j += step
        step = step + 1
    door_array = ''.join(door_array)
    return door_array

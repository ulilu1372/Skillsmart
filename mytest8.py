def SumOfThe(N, data):
           
    for i in range(1):
            sum = 0
            new_data = []
            new_data = data[1:len(data)]
            for j in range(len(new_data)):
                sum += new_data[j]
            if data[i] == sum:
                return data[i]
                
    for i in range(1, len(data) - 1):
            sum = 0
            new_data = []
            new_data = data[:i] + data[i + 1:]
            for j in range(len(new_data)):
                sum += new_data[j]
            if data[i] == sum:
                return data[i]           
                
        
    for i in range(len(data) - 1, len(data)):
            sum = 0 
            new_data = []
            new_data = data[0:len(data) - 1]
            for j in range(len(new_data)):
                sum += new_data[j]
            if data[i] == sum:
                return data[i]

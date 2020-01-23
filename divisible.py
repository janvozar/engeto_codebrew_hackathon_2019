start = int(input("Enter starting number: "))
stop = int(input("Enter stopping number: "))
divisor = int(input("Enter divisor: "))
results = []

def divisible(start,stop,divisor):
    if(divisor==0):
        print('Cannot divide by Zero!')
    else:
        for i in range(start,stop+1):
            if i%divisor==0:
                results.append(i)
        print('Numbers in range ' + str(start) + ', ' + str(stop) + ' divisible by ' + str(divisor) + ':')
        print(results)

divisible(start, stop, divisor)
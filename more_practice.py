 #x = int(input("Please enter an integer: ")
#if x < 0:
 #   x = 0
  #  print("Negative changed to zero")
#elif x == 0:
 #   print("Zero")
#elif x == 1:
  #  print("Single")
#else:
   # print("More")

#measure some strings
#words = ['cat','window','defenstrate']
#for w in words:
 #   print(w, len(w))

def is_prime(num):
    """
    Naive method for checking primes.
    """
    for n in range(2,num):
        if num % n == 0:
            print("Not prime")
            break
    else:
        if num % n != 0:
            print('prime')
    
is_prime(25)




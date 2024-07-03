def PrintFibonacci(F, S, L):
    if(L == 0):
        return
    print(F + S, end=" ")
    PrintFibonacci(S, F+S, L-1)

if __name__ == "__main__":
  print(0,1,end=" ")
  PrintFibonacci(0,1,6-2)
def fibonacci(n):
  a=0
  b=1
  print(a,b,sep=' ')
  i=3
  while(i<=n):
    c=a+b
    a=b
    b=c
    print(c,sep=' ')
    i=i+1

fibonacci(10)

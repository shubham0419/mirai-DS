def fun():
  print("hello")

fun()

# this will overwrite the above "Fun" function
def fun(name):
  print(name)

fun("shubham")

def fun2(*args):
  for arg in args:
    print(arg)

fun2(1,"shubham",True)

def fun3(name,arg4,arg2,arg3,arg1):
  print(name,arg1,arg2,arg3,arg4)
  return arg3 + arg2

val = fun3(name="shubham",arg1="argument 1",arg2=True,arg3=3,arg4=[4,4,4,4])
print(val)

def factorial(n):
  if(n<2):
    return n
  return n*factorial(n-1)
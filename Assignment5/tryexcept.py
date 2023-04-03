
try:
  num=int(input("enter the number"))
  a=[2,3,54]
  print(a[num]) #num is the index value
except ValueError:
  print("number enter is not an integer")#throw error when enterd value is not integer 
except IndexError:
  print("Invalid Error") #throw error when the value of num is out of index
else:
  print("run only when try is correct")  #tere is no error

finally:
  print("don't worry i will rum always ")
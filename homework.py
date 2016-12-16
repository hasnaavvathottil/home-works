def table(x,limit):
   for i in range(1,limit+1):
      print ("{:2} x {:2} = {:2}".format(i,x,i*x))

def sq_tables(x):
   for i in range(1, x+1):
      for j in range(1, x+1):
        if(i==2):
           print ("----+",end="")
      if(i==2):
         print ("")
      for j in range(1, x+1):
        print ("{:3} |".format(i*j),end="")
      print ("")

def fizzbizz(x):
   for i in range(1,x+1):
      if(i%15==0):
         print ("fizzbizz")
      elif(i%5==0):
         print ("bizz")
      elif(i%3==0):
         print ("fizz")
      else:
         print(i)

def breakdown(x):
    z = x
    d = [1000,500,100,50,20,10,5,1]
    for c in d:
       y = x//c
       x = x - (y*c)
       if(y>0):
         print ("{:4} x {:4} = {:4} ({:5})".format(c,y,c*y,z-x))


def breakdown2(x,dic):
    z = x
    d = [1000,500,100,50,20,10,5,1]
    for c in d:
       y = x//c
       if(c in dic):
         if(dic[c]>0):
            if(y<=dic[c]):
              dic[c] = dic[c]-y
              x = x - (y*c)
            else:
              y = dic[c] 
              dic[c] = 0
              x = x - (y*c)
            if(y>0):
               print ("{:4} x {:4} = {:4} ({:5})".format(c,y,c*y,z-x))
    if((x)>0):
       print (x," is left over")

def freq(string):
   d={}
   for i in string:
      if i in d:
         d[i]=d[i]+1
      else:
         d[i]=1
   return d

def freq2(string):
   d={}
   for i in string:
      if(i in d):
         d[i]=d[i]+1
      else:
         d[i]=1
   for k in list(d):
      print (k,': ', end="")
      for m in range(d[k]):
        print ("#",end="")
      print ("")    

def panagram(string):
   alpha=['abcdefghijklmnopqrstuvwxyz']
   d={}
   for i in string:
      if(i in d):
         d[i]=d[i]+1
      else:
         d[i]=1
   for a in alpha:
      if((a in d)==False):
         return False
   return True
                     

def panagram(s):
   for i in 'abcdefghijklmnopqrstuvwxyz':
      if i not in s:
         print ("{} is not found".format(s))
         return False
   return True
                     
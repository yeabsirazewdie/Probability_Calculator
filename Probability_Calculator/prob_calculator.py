import copy
import random
# Consider using the modules imported above.

class Hat:
  ledger={}
  contents=[]
  temp=[]
  
  #initialize class Hat
  def __init__(self,**kwargs):
    self.ledger.clear()
    self.contents.clear()
    self.temp.clear()
    self.ledger=kwargs
    for keys in self.ledger.keys():
      for j in range(0,self.ledger[keys]):
        self.contents.append(keys)
        self.temp.append(keys)

  #draw specific number of balls      
  def draw(self,nums):
    start = 0
    dummy =[]
    #self.contents = copy.deepcopy(self.temp)
    if(nums>=len(self.contents)):
      self.contents = copy.deepcopy(self.temp)
      self.contents.sort()
      return self.contents
    
    for i in range(0,nums):
      stop = len(self.contents)
      num = random.randint(0,stop-1)
      b = self.contents.pop(num)
      dummy.append(b)
  
    dummy.sort()
    return dummy
      
  def print(self):
    return self.contents
    

#create experiment
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  exps = 0
  for i in range(0,num_experiments):
    m=0
    dict={}
    b=hat.draw(num_balls_drawn)
    for j in b:
      if j in dict:
        dict[j] = dict[j] + 1
      else:
        dict[j] = 1
    
    for k in dict.keys():
      if k in expected_balls:
        if (dict[k]>=expected_balls[k]):
          m = m + 1

    if (m == len(expected_balls.keys())):
      exps = exps + 1

   # print(dict)
   # print(hat.contents)
  prop = exps  / num_experiments
  return prop

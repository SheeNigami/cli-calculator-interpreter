# DSAA-asdfasdf
## Classes used

### Kaeden
Stack
  push
  pop
  getprev
BinaryTree
  setKey
  getRightTree
  getLeftTree
  inserLeft
  insertRight
  
### colab 
Exp
  ### Sheenhern (Tree logic)
  __init__
    str
    val = None
  parseExp
  __parseExp__
  buildTree
    parseExp(self.str)
  evalExp
    self.val = val
  getVal
  ### Kaeden (sorting (overloading of ops) )
  __lt__
    if self.val != other.val
      return self.val < other.val
    else
      return len(self.str) < len(other.str)
  __str__
     return 'str ==> val'x
  ### Kaeden (printing)

### Kaeden (sort and validate)
def sort:
  do we have to implement our own
  
def validate
  if good
   return True

### SheenHern
Main program
 While True:
   if 1
    input(str)
    if validate(str)
      print(bruh)
    else
      exp = Exp(str)
      exp.buildTree
      exp.evalExp
   elif 2
    input(filename)
    input(what sorting??)
    if validate(str)
      print(bruh)
    else
      file = readFile(filename)
      list = file.split('\n')
      newlist = []
      for i in list:
        exp = Exp(i)
        exp.buildTree
        exp.evalExp
        newlist.apppend(exp)
      sort(newlist)
      prev = None
      output = 'Evaluation and sorting started\n'
      for i in range(len(newlist)):
        exp = newlist[i]
        if exp.getVal != prev
          output += ('words' + exp.getVal + '\n')
        output += output(exp.getExp\n)
        prev = exp.getVal
      print(str)
      writeFile(str)
    elif 3:
      break
      
      
 ## Advanced
ascending descending sort to be crafted manually, no reversing of list
notes for above: pass a parameter for the list and the sorting type

more operators includes logarithm and exponenetial (general mathematical thoingS?)

Automated testing is like nice iguess

Might implement O(1) stack idk

validation handles file inputs properly
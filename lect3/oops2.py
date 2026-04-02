class bankAccount:
  def __init__(self,bank_name,holder_name,balance):
    self.bank_name = bank_name            # public attribute
    self._holder_name = holder_name       # protected attribute 
    self.__balance = balance               # private attribute

  def printBalance(self):
    print(self._holder_name," balnce is ",self.__balance)

  def credit(self,amount):
    self.__balance += amount
    print(amount, " credited.")

  def debit(self,amount):
    if(self.__balance < amount):
      return
    self.__balance -= amount
    print(amount," deducted")


shubham = bankAccount("ICICI","shubham",1000)
print(shubham.bank_name)
print(shubham._holder_name)
# print(shubham.__balance)
shubham.printBalance()
shubham.credit(2000)
shubham.printBalance()
shubham.debit(1000)
shubham.printBalanc()
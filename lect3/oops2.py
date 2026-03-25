class bankAccount:
  def __init__(self,bank_name,holder_name,balance):
    self.bank_name = bank_name            # public attribute
    self._holder_name = holder_name       # protected attribute 
    self.__balance = balance               # private attribute

  def printBalance(self):
    print(self._holder_name," balnce is ",self.__balance)


shubham = bankAccount("ICICI","shubham",1000)
print(shubham.bank_name)
print(shubham._holder_name)
# print(shubham.__balance)
shubham.printBalance()

class bank(bankAccount):
  def __int__(self,branch,bank_name,holder_name,balance):
    self.branch = branch
    super().__init__(bank_name=bank_name,holder_name=holder_name,balance=balance)

hdfc = bank(bank_name="hdfc",holder_name="shubham",balance=1000)
print(hdfc._holder_name)
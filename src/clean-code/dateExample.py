from datetime import datetime
today = datetime.today()
startDay = datetime(1970, 1, 1)
diff = today - startDay


store = '131'
register = '70'
transaccion = '412'

formatedStore = '0' * (4 - len(str(store))) + store
formatedRegister = '0' * (2 - len(str(register))) + register
formatedTransaction = '0' * (4 - len(str(transaccion))) + transaccion
formatedDate = '0' * (8 - len(str(diff.days).strip())) + str(diff.days)
print(formatedStore)
print(formatedRegister)
print(formatedTransaction)
print(formatedDate)
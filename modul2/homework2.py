from datetime import datetime

# 1) Prove "and" operation takes precedence over "or" operation by setting
# parentheses in (False or False and True or True)
print(False or False and True or True)
print((False or False) and (True or True))
print()

# 2) Get from input two different times in the format hh:mm:ss and print
# the difference in seconds between them
firstTime = input('Insert the first time in the format hh:mm:ss:')
print('The first time in the format hh:mm:ss is:', firstTime)
secondTime = input('Insert the second time in the format hh:mm:ss:')
print('Second time in the format hh:mm:ss is:', secondTime)
fmt = '%H:%M:%S'
diff = datetime.strptime(secondTime, fmt) - datetime.strptime(firstTime, fmt)
print(diff)

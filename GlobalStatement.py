def spam():
    global eggs
    print(eggs + ' from inside spam')
    eggs = 'spam'
    print(eggs + ' after local var declaration')


eggs = 'global'
print(eggs)
spam()
print(eggs)
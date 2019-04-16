x=["a","b","c","d"]
for thief in x:
    sum=(thief!='a')+(thief=='c')+(thief=='d')+(thief!='d')
    if sum==3:
        print("小偷是:",thief)
        break
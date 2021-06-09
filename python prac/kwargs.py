def name(**kwargs):
    print(**kwargs)
    if AmaanKhan in kwargs:
        print("present {}".format(kwargs[AmaanKhan]))
res=name('AmaanKhan=')
print(res)

import one
print("Top level code")
one.func()

if __name__ == '__main__':
    print("direct call to two.py")
else:
    print("impoted two.py")
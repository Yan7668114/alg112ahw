from engine import Value

a = Value(2)
b = Value(1)
c = Value(3)

learning_rate = 0.01
max_iterations = 1000

for iteration in range(max_iterations):
    f = a**2 + b**2 + c**2

    print("Iteration:", iteration, "a=", a.data, "b=", b.data, "c=", c.data, "f=", f.data)
    f.backward()

    a.data -= learning_rate * a.grad
    b.data -= learning_rate * b.grad
    c.data -= learning_rate * c.grad

    # Clear gradients for the next iteration
    a.grad = 0
    b.grad = 0
    c.grad = 0

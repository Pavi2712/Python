# from Fibo import fib # It will import Fibo module and fib name from the module.
# fib(10)
import Fibo # It does not import the defined functions and names directly into the current namespace.
Fibo.fib(1000)
print(__name__)
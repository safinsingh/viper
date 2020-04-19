from viper import *
import inspect

def GetSource(func):
    lines = inspect.getsource(func)
    print(lines)
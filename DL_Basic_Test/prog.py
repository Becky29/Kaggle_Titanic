
# coding: utf-8

# In[6]:


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", type = int, help="display a square of a given number")
args = parser.parse_args()
print (args.echo)
print (args.square**2)

from math import sqrt

def velescape (gravity, pradius):
   kmtom = pradius * 1000
   gpr = 2 * (gravity * kmtom)
   return round(sqrt(gpr), 1)

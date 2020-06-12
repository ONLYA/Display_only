wtf = lambda x:lambda t: x+t
a = []

try:
 for _ in range(int("0xFFFFFFFF", 16)):
  try:
   a.append(wtf(_))
  except:
   break
except:
 pass

length = len(a)
n = 10000
every = int(length/n)
diff = length - n*every

ids = []
try:
 for i in range(n):
  try:
   abc = a[i*every:(i+1)*every-1]
  except:
   abc = a[i*every:(i+1)*every-1+diff]
  try:
   for _ in abc:
    try:
     ids.append(id(_))
    except:
     pass
  except:
   pass
except:
 pass

print(hex(max(ids)))

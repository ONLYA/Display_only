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

maxs = []
try:
 for i in range(n):
  try:
   abc = ids[i*every:(i+1)*every-1]
  except:
   abc = ids[i*every:(i+1)*every-1+diff]
  maxs.append(max(abc))
except:
 pass

print(hex(max(maxs))) # Should plus 3 as there are 3 variables totally defined before wtf functions

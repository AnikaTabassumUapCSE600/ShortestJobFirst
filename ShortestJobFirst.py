print("How Many Process? :")
x = int(input())
bts = []
for i in range(0,x):
  print("Enter Burst Time for P"+str(i+1)+" :")
  bt = int(input())
  bts.append(bt)

sum = 0
tmps =[]
indexes = []

t_bts =[]

for bt in bts:
  t_bts.append(bt)

t_bts.sort()

# print(t_bts)
# print(bts)

for i in range(0,x-1):
  min = t_bts[i]    #[2, 3, 6, 21]
  ind =  bts.index(min)   #[21, 3, 6, 2]
  tm = 0  
  for j in range(0,i):
    tm = tm + t_bts[j]
  sum = sum + min+ tm
  tmps.append(min+ tm)
  indexes.append(ind)

print("The Average Waiting time will be = (0+", sep='', end='', flush=True)
for i in range(0,len(tmps)):
  print(str(tmps[i])+"", sep='', end='', flush=True)
  if i != x-2:
    print("+",sep='', end='', flush=True)

print("/"+str(x)+")")
print("\t\t\t\t ="+"{:.2f}".format(sum/x))

print("Grant Chart ", sep=' ', end='', flush=True)
for i in range(0,x):
  if i!=x-1:
    print(" P"+str(indexes[i]+1)+" | "+str(tmps[i])+" " , sep=' ', end='|', flush=True)
  if i==x-1:
    ind =  bts.index(t_bts[i])
    print(" P"+str(ind+1)+" | "+str(tmps[i-1]+t_bts[i])+" " , sep=' ', end='|', flush=True)


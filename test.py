f = open("out.html", "w")

for i in range(20):
  f.write(str(i) + ": Testing")
 
f.close()

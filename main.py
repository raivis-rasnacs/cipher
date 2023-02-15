import string

alfabets = list(string.ascii_lowercase)

burti = (("a", "ā"), 
         ("c", "č"), 
         ("e", "ē"), 
         ("g", "ģ"), 
         ("i", "ī"), 
         ("k", "ķ"), 
         ("l", "ļ"),
         ("n", "ņ"),
         ("s", "š"),
         ("u", "ū"),
         ("z", "ž"),
        )

for vecaisBurts, jaunaisBurts in burti:
  alfabets.insert(alfabets.index(vecaisBurts) + 1, jaunaisBurts)
  
liekieBurti = ["q", "w", "x", "y"]
for burts in liekieBurti:
  alfabets.remove(burts)

teksts = "zivs peld upē"
jaunaisTeksts = str()
k = 3

def switchIndex(idx):
  for _ in range(k):
    if k > 0:
      idx += 1
      if idx >= len(alfabets): 
        idx = 0
    elif k < 0:
      idx -= 1
      if idx < 0: 
        idx = len(alfabets) - 1
    
  return idx

for simbols in teksts:
  if simbols in alfabets:
    indekss = alfabets.index(simbols)
    indekss = switchIndex(indekss)
    
    jaunaisTeksts += alfabets[indekss]
  else: jaunaisTeksts += simbols

print(jaunaisTeksts)
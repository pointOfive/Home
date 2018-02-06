    
# tower of hanoi

from threestack import s3_pop, s3_push, n, strts, tops, ends, where_min, s

def move_disks(n, here, there, beffere):
   if(n < 1):
       return None
   move_disks(n-1, here, there=beffere, beffere=there)
   take = s3_pop(here)
   s3_push(there, take)
   move_disks(n-1, here=beffere, there=there, beffere=here)
   
s3_push(0,4)
s3_push(0,3)
s3_push(0,2)
s3_push(0,1)

move_disks(4,0,2,1)

def get_indices_of_item_weights(weights, length, limit):
   hashMap = {}

   for i in range(len(weights)):
       curr = weights[i]

       if(limit - curr) in hashMap:
            return(i, hashMap[limit-curr])
       else:
            hashMap[curr] = i

   return None

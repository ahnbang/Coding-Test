def solution(participant, completion):
    
    hash_sum = 0
    hash_table = {}
    for i in participant:
        hash_table[hash(i)] = i
        hash_sum += hash(i)
        
    for j in completion:
        hash_sum -= hash(j)
    
    return hash_table[hash_sum]
                    
            
    return answer
  
  '''
  participant = ["mislav", "stanko", "mislav", "ana"]
  completion = ["stanko", "ana", "mislav"]
  return = 	"mislav"
  '''

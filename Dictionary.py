#Dictionary is a collection of key value pairs
#all keys of dictionary are by default unique

score = {"virat": 183 , "Dhoni": 183 , "Sachin": 200 }
print(score,type(score))

print(score["virat"])

score["virat"] = 246  #we can change the value
print(score["virat"])

score["rohit"] = 263 #we can add new key with value
print(score)

for key in score:
     print(key,score[key]) #USING FOR LOOP

for key , value in score.items():
     print(key,value)
word='otman'
sentence='hello i am otman'
sent=sentence.split()
pos= [ind for ind, v in enumerate(sent) if v == word ]
print(pos)
import re 


data = "Thu Feb 15 17:46:04 2007::ustaga@dslfkdslkfj.gov::1190732432-6-8"

data1 = ['bat', 'bit', 'but', 'hat', 'hit', 'hut', 'acd']
patt = '[b|u|h][a|i|u|a]t$'
for str in data1:
	print(re.match(patt,str))
import uuid
import random
import pandas as pd
from random import shuffle

id = uuid.uuid4()

rand_num_list=[]

for i in range(0, 60000):
    rand_num = str('NS5f')+str(random.Random(uuid.uuid1().hex).getrandbits(128))[0:12]+str('.')+str(random.randint(0,id.node))[0:10]
    rand_num_list.append(rand_num)
    
pd.DataFrame(rand_num_list, columns=['new_ids']).to_csv()

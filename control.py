import subprocess
import numpy as np
import tqdm

# 実行回数
COUNT = 250

att_win = 0
output_list = []
for i in tqdm.tqdm(range(COUNT)):
    result = subprocess.check_output(['python', 'sim.py']).decode().strip()
    if int(result) > 0:
        att_win += 1
    output_list.append(int(result))
    
    
print("平均生存者：{}".format(np.mean(output_list)))
print("通過率：{}%".format(att_win / COUNT * 100))

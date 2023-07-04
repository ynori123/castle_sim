import subprocess
import numpy as np
import tqdm

# 実行回数
COUNT = 100

######### initialize ##########
# 攻撃者の人数
attacker_num :int = 1000, # 人
# スタートの座標
start_point :tuple[float] = (0, 0),
# ゴールの座標
goal_point :tuple[float] = (0, 100),
# オフセット 
offset :int = 0, # sec
################################

att_win = 0
output_list = []
from .sim import sim
for i in tqdm.tqdm(range(COUNT)):
    result = sim(
        attacker_num=attacker_num,
        start_point=start_point,
        goal_point=goal_point,
        offset=offset,
    )
    if int(result) > 0:
        att_win += 1
    output_list.append(int(result))
    
    
print("平均生存者：{}".format(np.mean(output_list)))
print("通過率：{}%".format(att_win / COUNT * 100))

import subprocess
import numpy as np
import tqdm

# 実行回数
COUNT = 99999

######### initialize ##########
# 攻撃者の人数
attacker_num :int = 1000 # 人
# スタートの座標
STARTPOINT :tuple[float] = (0, 0)
# ゴールの座標
GOALPOINT :tuple[float] = (0, 100)
# 曲がり角の座標
curvepoint :list[tuple[float]] = []
################################
import sim

att_win = 0
output_list = []
route = []
route.append(STARTPOINT)
for obj in curvepoint:
    route.append(obj)
route.append(GOALPOINT)
def simulates():
    for i in range(len(route)-1):
        simulate(
            start_point=route[i],
            goal_point=route[i+1]
        )
def simulate(start_point,goal_point,):
    for i in tqdm.tqdm(range(COUNT)):
        result = sim.sim(
            attacker_num=attacker_num,
            start_point=start_point,
            goal_point=goal_point,
        )
        if int(result) > 0:
            att_win += 1
        output_list.append(int(result))
    
    
print("平均生存者：{}".format(np.mean(output_list)))
print("通過率：{}%".format(att_win / COUNT * 100))

import csv
import random

########## initialize ##########

# 防衛地点のx座標,y座標,人数をまとめたCSVファイルの場所
SPOT_PATH = './spot.csv'
# 攻撃者の速さ（分速）
ATTACKER_SPEED :float = 1.5 # m/s 
# 一発撃つのにかかる時間
DEFENCE_GUN_RATE :float = 20 # s/発 
# 攻撃者の人数
ATTACKER_COUNT :int = 1000 # 人
# スタートの座標
START_POINT :tuple[float] = (0, 0)
# ゴールの座標
GOAL_POINT :tuple[float] = (0, 100)

################################

# Defence_spot class
class Defence_spot:
    def __init__(self,x,y,count) -> None:
        # Spotのx座標
        self.x = x
        # Spotのx座標
        self.y = y
        # Spotから一回で撃てる弾数
        self.count = count



def main() -> None:
    # 生存している攻撃者
    attacker_alive = ATTACKER_COUNT
    attacker_position :list[tuple] = calc_pos()
    defencer_position :list[tuple] = defence_point()
    for a in attacker_position:
        # その地点での攻撃者からかく防衛地点への距離を計算
        l :list[float] = calc_r(defencer_position, a)
        # 距離の確率を計算
        p = calc_p(l)
        # 確率ごとに生存者を計算
        for i in range(len(defence_spot)):
            for _ in range(defence_spot[i].count):
                # 生存者が負の数の時はbreak(計算効率化)
                if attacker_alive < 0:
                    break
                if random.random() <= p[i]:
                    attacker_alive -= 1
    # 生存者は負の数にならない
    if attacker_alive < 0:
        attacker_alive = 0
    print(attacker_alive)
    

spot_num = 0
defence_spot :list[Defence_spot] = []
spot_position :list[tuple] = []

def defence_point() -> None:
    with open(SPOT_PATH) as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    calc_dat :list[tuple] = []
    for d in data:
        defence_spot.append(Defence_spot(int(d[0]), int(d[1]),int(d[2])))
        calc_dat.append((int(d[0]),int(d[1])))
    spot_num = len(data)
    return calc_dat

import math
# Spotと人間との距離計算
def calc_r(data :list[tuple], pos :tuple) -> list:
    res = []
    r = 0
    r_x = 0
    r_y = 0
    for d in data:
        r_x = (d[0] - pos[0])
        r_y = (d[1] - pos[1])
        r = math.sqrt(r_x**2 + r_y**2)
        res.append(r)
    return res

# 確率計算（in:距離,out:確率)
def calc_p(dis :list[float]) -> list[float]:
    res :list[float] = []
    for d in dis:
        r = (d * -4 / 5) + 120
        if r > 100:
            r = 100
        elif r < 0:
            r = 0
        r = float( r / 100)
        res.append(r)
    
    return res

# 発射する時の攻撃者の場所
def calc_pos() -> list[tuple]:
    res :list[tuple] = []
    start_x = START_POINT[0]
    start_y = START_POINT[1]
    goal_x = GOAL_POINT[0]
    goal_y = GOAL_POINT[1]
    # スタートからゴールまでの距離
    distance = math.sqrt((start_x - goal_x)**2 + (start_y - goal_y)**2)
    # 最短経路を通った時通過するのに何秒かかるか
    time = distance / ATTACKER_SPEED
    # 1秒経過した時のxベクトル
    x_sec = abs(start_x - goal_x) / time
    # 1秒経過した時のyベクトル
    y_sec = abs(start_y - goal_y) / time
    
    from numpy import arange
    now = [start_x,start_y]
    for i in arange(0, time, DEFENCE_GUN_RATE):
        now[0] = float(i) * x_sec
        now[1] = float(i) * y_sec
        res.append(tuple(now))
    return res
    

if __name__ == '__main__':
    main()
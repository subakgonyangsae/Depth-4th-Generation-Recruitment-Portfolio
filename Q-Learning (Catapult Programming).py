import random

# [변수 초기화]
power = 0
q = 0
reward = 0
target_reward = 5
max_power = 100
min_power = 0
epsilon = 0.1
q_table = {}

def update_q_value(state, action, reward, next_state, alpha=0.1, gamma=0.9):
    old_value = q_table.get(state, {}).get(action, 0)
    future_value = max(q_table.get(next_state, {min_power: 0, max_power: 0}).values(), default=0)
    
    # Q-값 업데이트 함수
    new_value = old_value + alpha * (reward + gamma * future_value - old_value)
    if state not in q_table:
        q_table[state] = {}
    q_table[state][action] = new_value

# [루프]
for episode in range(100):
    power = 0
    state = power

    # [반복 (10회)]
    for _ in range(10):  
        # [랜덤 숫자 생성]
        random_value = random.random()
        #[조건 블록]
        if random_value < epsilon:  # 탐험
            # [랜덤 행동 선택]
            action = random.choice([-10, 10])  # -10 또는 +10 선택
        else:  # 이용
            # [Q-테이블에서 최대 Q-값 찾기]
            action = max(q_table.get(state, {min_power: 0, max_power: 0}).items(), key=lambda x: x[1])[0]

        # [행동 수행]
        power = power + action
        power = max(min_power, min(max_power, power))

        # [터치 센서 확인]
        touch_sensor_pressed = random.choice([True, False])
        if touch_sensor_pressed:
            q = power
            reward += target_reward
        else:
            reward -= 1

        # [Q-값 업데이트]
        next_state = power
        update_q_value(state, action, reward, next_state)
        state = next_state

# [종료]
print("최종 Q-테이블:", q_table)

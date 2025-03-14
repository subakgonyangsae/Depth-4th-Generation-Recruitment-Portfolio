from itertools import permutations
import math

# [거리 함수]
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance(path[i], path[i + 1])
    dist += distance(path[-1], path[0])  # 돌아오는 거리
    return dist

# [좌표입력]
def get_coordinates(prompt):
    while True:
        try:
            x, y = map(float, input(prompt).split())
            return (x, y)
        except ValueError:
            print("잘못된 입력입니다. 좌표를 다시 입력하세요. 형식: x y")

def main():
    print("공항 좌표 입력:")
    airport = get_coordinates("공항 (예: 0 0): ")

    print("숙소 좌표 입력:")
    accommodation = get_coordinates("숙소 (예: 2.5 0): ")

    destinations = []
    print("여행지 좌표 입력 (종료하려면 빈 줄을 입력하세요):")
    while True:
        coord = input("여행지 (예: 10 0): ")
        if coord == "":
            break
        destinations.append(get_coordinates(f"여행지 ({coord}): "))

    if len(destinations) < 1:
        print("여행지가 입력되지 않았습니다. 프로그램을 종료합니다.")
        return

    # [모든 가능한 경로 생성]
    all_permutations = permutations(destinations)

    # [최적 경로 찾기]
    best_path = None
    min_distance = float('inf')

    for perm in all_permutations:
        # [숙소에서 출발하고, 순서대로 방문한 후 다시 숙소로 돌아오는 경로]
        path = [accommodation] + list(perm) + [accommodation]
        current_distance = total_distance(path)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = path

    # [결과 출력]
    print("\n최적의 경로:")
    for point in best_path:
        print(point)
    print("총 거리:", min_distance)

if __name__ == "__main__":
    main()
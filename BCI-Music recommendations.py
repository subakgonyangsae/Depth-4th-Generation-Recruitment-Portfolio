import random

pop_songs = ["스토커", "가을 아침", "영화 같던 날", "우주를 줄게", "모든 날, 모든 순간",
             "너 없는 시간들", "어떻게 이별까지 사랑하겠어, 널 사랑하는 거지", "그대라는 시",
             "Fly Away", "Make Up"]
classical_songs = ["캐논", "비창 소나타 (Moonlight Sonata)", "지우개",
                   "클레르 드 린", "아베 마리아", "녹턴", "파반느", "백조의 호수",
                   "겨울", "세레나데"]
ballad_songs = ["Your Song", "Someone Like you", "All of me", "Hello" ,
                "I will always love you", "Hero", "You're Beautiful" ,
                "Don't Know Why", "Stay with Me" ,"Can't pretend"]

# 각 뇌파 유형에 따라 노래 추천하는 함수
def recommend_song(brain_wave):
    if brain_wave in ["알파파", "세타파", "SMR파"]:
        return random.choice(pop_songs), "pop"
    elif brain_wave == "감마파":
        return random.choice(classical_songs), "classical"
    elif brain_wave == "베타파":
        return random.choice(ballad_songs), "ballad"
    return "추천할 곡이 없습니다.", None

# 사용자의 만족도에 따라 추천 확률을 조정하는 함수
def adjust_recommendation_probability(satisfaction, song_list, song):
    if satisfaction >= 4:  # 만족도가 4 이상일 경우
        # 리스트에 해당 곡을 추가하여 더 자주 추천되도록 함
        song_list.append(song)
    elif satisfaction <= 2:  # 만족도가 2 이하일 경우
        # 해당 곡을 리스트에서 제거하여 더 이상 추천되지 않도록 함
        if song in song_list:
            song_list.remove(song)

# 테스트를 위한 사용자 인터페이스
for _ in range(10):  # 노래 추천을 10번 반복
    brain_wave = input("뇌파 상태를 입력해주세요: ")
    recommended_song, genre = recommend_song(brain_wave)  # 장르도 함께 받아옴
    print(f"추천된 노래: {recommended_song}")

    if genre:  # 추천된 노래가 있는 경우에만 만족도를 물어봄
        satisfaction = int(input("노래 추천에 대한 만족도를 1에서 5까지 입력해주세요: "))
        if 1 <= satisfaction <= 5:
            if genre == "pop":
                adjust_recommendation_probability(satisfaction, pop_songs, recommended_song)
            elif genre == "classical":
                adjust_recommendation_probability(satisfaction, classical_songs, recommended_song)
            elif genre == "ballad":
                adjust_recommendation_probability(satisfaction, ballad_songs, recommended_song)
        else:
            print("올바른 만족도를 입력해주세요.")
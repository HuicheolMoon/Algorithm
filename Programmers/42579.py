# Problem : https://programmers.co.kr/learn/courses/30/lessons/42579
# Date : 2021-10-03
# 베스트앨범

def solution(genres, plays):
    answer = []
    plays_for_genres = dict()
    for i, genre in enumerate(genres):
        if genre in plays_for_genres:
            plays_for_genres[genre] += plays[i]
        else:
            plays_for_genres[genre] = plays[i]
    playtimes = sorted(plays_for_genres.items(), key= lambda x: x[1], reverse=True)
    streaming_sites = dict(enumerate(zip(genres, plays)))
    streaming = sorted(streaming_sites.items(), key= lambda x: x[1][1], reverse=True)
    for genre, _ in playtimes:
        times = 0
        for stream in streaming:
            if times == 2:
                break
            if stream[1][0] == genre:
                answer.append(stream[0])
                times += 1
    return answer


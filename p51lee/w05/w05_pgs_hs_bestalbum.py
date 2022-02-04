def solution(genres, plays):
    l = len(genres)
    playNumDict = {}
    songNumDict = {}
    for i in range(l):
        if genres[i] in playNumDict:
            playNumDict[genres[i]] += plays[i]
            songNumDict[genres[i]] += 1
        else:
            playNumDict[genres[i]] = plays[i]
            songNumDict[genres[i]] = 1

    playlist = [(i, genres[i], plays[i]) for i in range(l)]
    playlist.sort(key=lambda song: song[0])
    playlist.sort(key=lambda song: song[2], reverse=True)
    playlist.sort(key=lambda song: playNumDict[song[1]], reverse=True)

    j = 0
    answer = []
    while j < l:
        if songNumDict[playlist[j][1]] == 1:
            answer.append(playlist[j][0])
            j += 1
        elif j == l - 1:
            break
        elif playlist[j][1] == playlist[j+1][1]:
            answer.append(playlist[j][0])
            answer.append(playlist[j+1][0])
            j += songNumDict[playlist[j][1]]
        else:
            j += 1
    return answer
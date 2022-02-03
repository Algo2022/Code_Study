def duration(t1, t2):
    h1, m1 = map(int, t1.split(":"))
    h2, m2 = map(int, t2.split(":"))
    return (h2-h1)*60 + m2 - m1

def full_song(dur, song):
    song_len = len(song)
    full = ""
    for i in range(dur):
        full += song[i % song_len]
    return full

def encode(song):
    return song.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

def solution(m, musicinfos):
    m_rev = encode(m)
    ans = []
    for info in musicinfos:
        t1, t2, title, song = info.split(",") 
        dur = duration(t1, t2)
        if m_rev in full_song(dur, encode(song)):
            ans.append((dur, title))
    if ans:
        ans.sort(key=lambda x: x[0], reverse=True)
        return ans[0][1]
    else:
        return "(None)"
            
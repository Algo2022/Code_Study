from collections import Counter
import re

solution = lambda s: [int(x[0])for x in sorted(Counter(re.compile(r"\d+").findall(s)).items(), key=lambda x: x[1], reverse=True)]
print(solution("{{123}}"))


import re

def solution(user_id, banned_id):

    def banuser(user_id, bannables, deleted):
        ans = 0
        if bannables:
            bannable = bannables.pop()
            invalid = True
            for i, bannee in enumerate(bannable):
                new_user_id = user_id[:]
                new_deleted = deleted.copy()
                if not bannee in user_id:
                    continue
                else:
                    invalid = False
                new_user_id.remove(bannee)
                new_deleted.add(bannee)
                banuser(new_user_id, bannables[:], new_deleted)
            if invalid:
                return
            else:
                return
        else:
            if not deleted in deleted_cases:
                deleted_cases.append(deleted)

    deleted_cases = []
    bannables = []
    for banned in banned_id:
        b = re.compile(banned.replace("*", "."))
        temp = []
        for i, user in enumerate(user_id):
            if b.match(user) and len(user) == len(banned):
                temp.append(i)
        bannables.append(temp)
    banuser(list(range(len(user_id))), bannables, set())
    return len(deleted_cases)


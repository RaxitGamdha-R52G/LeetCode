class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE" and x[2] == "HERE"))
        t_usrs = [0] * numberOfUsers  
        status = [True] * numberOfUsers  
        mentions = [0] * numberOfUsers

        for event in events:
            eventType, t_stmp, details = event
            t_stmp = int(t_stmp)

            # for i in range(numberOfUsers):
            #     if t_usrs[i] <= t_stmp:  
            #         status[i] = True

            if eventType == "OFFLINE":
                user = int(details)
                t_usrs[user] = t_stmp + 60
                status[user] = False

            elif eventType == "MESSAGE":
                if details == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif details == "HERE":
                    for i in range(numberOfUsers):
                        if status[i] or t_usrs[i] <= t_stmp:  
                            mentions[i] += 1
                            t_usrs[i] = t_stmp
                else:
                    user_ids = details.split()
                    for user in user_ids:
                        u = int(user[2:])
                        # if not status[u]:
                            # status[u] = True
                            # t_usrs[u] = t_stmp
                        mentions[u] += 1

        return mentions

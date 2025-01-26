class Solution {
    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        Collections.sort(events, new Comparator<List<String>>() {
            @Override
            public int compare(List<String> list1, List<String> list2) {
                int tStmpCompare = Integer.compare(Integer.parseInt(list1.get(1)), Integer.parseInt(list2.get(1)));
                if (tStmpCompare == 0) {
                    boolean isHere1 = list1.get(0).equals("MESSAGE") && list1.get(2).equals("HERE");
                    boolean isHere2 = list2.get(0).equals("MESSAGE") && list2.get(2).equals("HERE");
                    return Boolean.compare(isHere1, isHere2);
                }

                return tStmpCompare;
            }

        });

        int t_usrs[] = new int[numberOfUsers];
        boolean status[] = new boolean[numberOfUsers];

        for (int i = 0; i < status.length; i++) {
            status[i] = true;
        }

        int mentions[] = new int[numberOfUsers];

        for (int i = 0; i < events.size(); i++) {
            List<String> d = events.get(i);

            String eventType = d.get(0);
            int t_stmp = Integer.parseInt(d.get(1));
            String details = d.get(2);

            if (eventType.equals("OFFLINE")) {
                int user = Integer.parseInt(details);
                t_usrs[user] = t_stmp + 60;
                status[user] = false;
            } else if (eventType.equals("MESSAGE")) {
                if (details.equals("ALL")) {
                    for (int j = 0; j < numberOfUsers; j++) {
                        mentions[j]++;
                    }
                } else if (details.equals("HERE")) {
                    for (int j = 0; j < numberOfUsers; j++) {
                        if (status[j] || t_usrs[j] <= t_stmp) {
                            mentions[j]++;
                            t_usrs[j] = t_stmp;
                        }
                    }
                } else {
                    String user_ids[] = details.split(" ");
                    for (String usr : user_ids) {
                        int user_id = Integer.parseInt(usr.substring(2));
                        mentions[user_id]++;
                    }
                }
            }
        }
        return mentions;
    }    
    
}
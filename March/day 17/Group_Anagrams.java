import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 1){
            // List.of makes anything inside brackets, into an outter list.
            return List.of(List.of(strs[0]));
        }

        // List<String> means a list will hold the type inside <>.
        HashMap <String, List<String>> map = new HashMap<>();
        for (String s: strs){
            char[] cc = s.toCharArray();
            Arrays.sort(cc);
            String key = String.valueOf(cc); // or new String(cc)
            if (!map.containsKey(key)){
                map.put(key, new ArrayList<>()); // Dont need to say type of Array List, inferred from HashMap.
            }
            map.get(key).add(s);
        }
        return new ArrayList<>(map.values()); // Dont need to say type of Array List, inferred from HashMap.
    }
}
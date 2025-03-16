class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        int [] counts = new int[26];
        for (int i = 0; i < s.length(); i++){
            counts[s.charAt(i) - 'a']++;
            counts[t.charAt(i) - 'a']--;
        }
        for (int c : counts){
            if (c != 0) {return false;}
        }
        return true;
    }
}

// flow of algorithm:
// Goal: see if String t is an anagram of String s.
// 1) if lengths are different, return false.
// 2) we make an int array, each index stores count of that letter ( 0 = 'a')
// 3) if at the end, they arent all 0, that means one of the strings isn't an anagram
// 4) return true or false based on that.
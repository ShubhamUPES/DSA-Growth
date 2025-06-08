class Solution {
    public boolean isIsomorphic(String s, String t) {
        List<Integer> patternS = new ArrayList<>();
        List<Integer> patternT = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            patternS.add(s.indexOf(s.charAt(i)));
            patternT.add(t.indexOf(t.charAt(i)));
        }

        return patternS.equals(patternT);
    }

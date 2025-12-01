class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> mp;

        // Count characters in magazine
        for (char c : magazine) {
            mp[c]++;
        }

        // Check ransomNote characters
        for (char c : ransomNote) {
            if (mp[c] == 0) return false;
            mp[c]--;
        }

        return true;
    }
};

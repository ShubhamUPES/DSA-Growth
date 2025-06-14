

class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        Map<Integer, List<String>> map = new HashMap<>();

        for (int i = 0; i < list1.length; i++) {
            for (int j = 0; j < list2.length; j++) {
                if (list1[i].equals(list2[j])) {
                    int indexSum = i + j;

                    // If indexSum is not in map, create new list
                    if (!map.containsKey(indexSum)) {
                        map.put(indexSum, new ArrayList<>());
                    }
                    map.get(indexSum).add(list1[i]);
                }
            }
        }

        // Find the minimum index sum
        int minSum = Collections.min(map.keySet());

        // Convert list to array and return
        List<String> result = map.get(minSum);
        return result.toArray(new String[0]);
    }
}

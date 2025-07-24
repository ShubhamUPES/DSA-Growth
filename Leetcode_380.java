import java.util.*;

class RandomizedSet {
    private Map<Integer, Integer> valToIndex;
    private List<Integer> values;
    private Random rand;

    public RandomizedSet() {
        valToIndex = new HashMap<>();
        values = new ArrayList<>();
        rand = new Random();
    }

    public boolean insert(int val) {
        if (valToIndex.containsKey(val)) {
            return false;
        }
        valToIndex.put(val, values.size());
        values.add(val);
        return true;
    }

    public boolean remove(int val) {
        if (!valToIndex.containsKey(val)) {
            return false;
        }
        int indexToRemove = valToIndex.get(val);
        int lastVal = values.get(values.size() - 1);

        values.set(indexToRemove, lastVal);
        valToIndex.put(lastVal, indexToRemove);

        values.remove(values.size() - 1);
        valToIndex.remove(val);

        return true;
    }

    public int getRandom() {
        int index = rand.nextInt(values.size());
        return values.get(index);
    }
}

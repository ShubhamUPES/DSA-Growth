import java.util.ArrayList;

class MyHashSet {
    private ArrayList<Integer> myHashSet;

    public MyHashSet() {
        myHashSet = new ArrayList<>();
    }

    public void add(int key) {
        if (!myHashSet.contains(key)) {
            myHashSet.add(key);
        }
    }

    public void remove(int key) {
        Integer boxedKey = key; // needed to avoid calling remove by index
        myHashSet.remove(boxedKey);
    }

    public boolean contains(int key) {
        for (int i = 0; i < myHashSet.size(); i++) {
            if (myHashSet.get(i) == key) {
                return true;
            }
        }
        return false;
    }
}


/* Using import java.util.HashSet;

class MyHashSet {
    private HashSet<Integer> set;

    public MyHashSet() {
        set = new HashSet<>();
    }

    public void add(int key) {
        set.add(key);
    }

    public void remove(int key) {
        set.remove(key); // like Python's discard
    }

    public boolean contains(int key) {
        return set.contains(key);
    }
}
*/

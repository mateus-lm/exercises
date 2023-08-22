package mypackage;

import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

public class SetsAndMaps {
public static void main(String[] args) {
// Sets
Set<Integer> mySet = new HashSet<>
(Arrays.asList(1, 2, 3, 4));// Maps (Dictionaries)
Map<String, String> myMap = new HashMap<>();
myMap.put("key1", "value1");
myMap.put("key2", "value2");
System.out.println(myMap);
}
}
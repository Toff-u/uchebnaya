class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class UnorderedMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return len(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        # Check if the key already exists and update
        for kvp in self.buckets[index]:
            if kvp.key == key:
                kvp.value = value
                return
        # If key doesn't exist, add a new key-value pair
        self.buckets[index].append(KeyValuePair(key, value))

    def get(self, key, default=None):
        index = self._hash(key)
        for kvp in self.buckets[index]:
            if kvp.key == key:
                return kvp.value
        return default

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, kvp in enumerate(bucket):
            if kvp.key == key:
                del bucket[i]
                return

    def keys(self):
        all_keys = []
        for bucket in self.buckets:
            for kvp in bucket:
                all_keys.append(kvp.key)
        return all_keys

    def values(self):
        all_values = []
        for bucket in self.buckets:
            for kvp in bucket:
                all_values.append(kvp.value)
        return all_values

    def items(self):
        all_items = []
        for bucket in self.buckets:
            for kvp in bucket:
                all_items.append((kvp.key, kvp.value))
        return all_items

# Example usage:
my_map = UnorderedMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())          # Output: Keys: ['name', 'age', 'city']
print("Values:", my_map.values())      # Output: Values: ['John', 25, 'Example City']
print("Items:", my_map.items())        # Output: Items: [('name', 'John'), ('age', 25), ('city', 'Example City')]

# Accessing values by key
print("Name:", my_map.get("name"))     # Output: Name: John
print("Gender:", my_map.get("gender", "Not specified"))  # Output: Gender: Not specified

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':",  my_map.keys())
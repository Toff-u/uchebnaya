class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * size  # Storage for keys
        self.data = [None] * size    # Storage for values

    # Private method to compute the hash value of a key
    def _hash(self, key):
        # A simple hash function using the built-in hash and modulo operation
        return hash(key) % self.size

    # Public method to add or update a key-value pair
    def put(self, key, value):
        hash_value = self._hash(key)
        # Linear probing for collision resolution
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value  # Update existing value
                return
            hash_value = (hash_value + 1) % self.size
        self.slots[hash_value] = key  # Store the key
        self.data[hash_value] = value  # Store the value

    # Public method to retrieve a value by its key
    def get(self, key, default=None):
        hash_value = self._hash(key)
        # Linear probing to find the key
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                return self.data[hash_value]  # Return the found value
            hash_value = (hash_value + 1) % self.size
        return default  # Return default if key not found

    # Public method to remove a key-value pair
    def remove(self, key):
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                self.slots[hash_value] = None  # Remove the key
                self.data[hash_value] = None    # Remove the value
                return
            hash_value = (hash_value + 1) % self.size

    # Public method to get a list of keys
    def keys(self):
        return [key for key in self.slots if key is not None]

    # Public method to get a list of values
    def values(self):
        return [value for value in self.data if value is not None]

    # Public method to get a list of key-value pairs
    def items(self):
        return [(self.slots[i], self.data[i]) for i in range(self.size) if self.slots[i] is not None]

my_hashmap = HashMap()
my_hashmap.put("name", "John")
my_hashmap.put("age", 25)
my_hashmap.put("city", "Example City")

print("Keys:", my_hashmap.keys())
print("Values:", my_hashmap.values())
print("Items:", my_hashmap.items())

print("Name:", my_hashmap.get("name"))
print("Gender:", my_hashmap.get("gender", "Not specified"))


my_hashmap.remove("age")
print("Keys after removing 'age':", my_hashmap.keys())
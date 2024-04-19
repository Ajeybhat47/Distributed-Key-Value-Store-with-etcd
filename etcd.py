import etcd3

# Connect to the etcd container running on the Docker host
etcd = etcd3.client(host='localhost', port=32774)

# Store a key:value pair in etcd
etcd.put('name', 'Abhinav')

# Retrieve the value of the key from etcd
value, metadata = etcd.get('name')
print("Key: " + metadata.key.decode('utf-8'))
print("Value: " + value.decode('utf-8'))

# List all keys
print("All keys in etcd:", etcd.get_all())

# Get value for a specific key
print("Value for key 'my_key':", etcd.get('name'))

# Put a key-value pair
#etcd_client.put('my_key', 'my_value')



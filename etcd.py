import etcd3

def connect_to_etcd(host, port):
    try:
        # Establish connection to etcd client
        etcd_client = etcd3.client(host=host, port=port)
        print("Connected to etcd successfully.")
        return etcd_client
    except etcd3.exceptions.ConnectionFailedError as e:
        print(f"Connection to etcd failed: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_all_etcd_keys(etcd_client):
    try:
        # Retrieve all keys
        keys = etcd_client.get_all()
        
        # Extract keys from the response
        key_list = [m.key.decode('utf-8') for (_, m) in keys]
        
        return key_list
    except etcd3.exceptions.ConnectionFailedError as e:
        print(f"Connection to etcd failed: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return []
    
def get_etcd_key_value(etcd_client, key):
    try:
        # Retrieve the value for the given key
        value, metadata = etcd_client.get(key)

        # Check if the key exists
        if value is None:
            print(f"Key '{key}' does not exist.")
            return None
        
        return value.decode('utf-8')
    
    except etcd3.exceptions.ConnectionFailedError as e:
        print(f"Connection to etcd failed: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return None
    
def insert_etcd_key_value(etcd_client, key, value):
    try:
        # Insert the key-value pair
        etcd_client.put(key, value)
        print(f"Inserted key '{key}' with value '{value}' successfully.")
        return True
    except etcd3.exceptions.ConnectionFailedError as e:
        print(f"Connection to etcd failed: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return False

def delete_etcd_key(etcd_client, key):
    
    if etcd_client:
        try:
            # Delete the keys
            etcd_client.delete(key)
            print(f"Deleted key '{key}' successfully.")
            return True
        except Exception as e:
            print(f"Error: {e}")
    return False




if __name__ == "__main__":
    etcd_client = connect_to_etcd("localhost",2379)

    key_list = get_all_etcd_keys(etcd_client)
    print(key_list)

    key = key_list[0]

    # delete_etcd_key(etcd_client, key)

    key_list = get_all_etcd_keys(etcd_client)
    print(key_list)

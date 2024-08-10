from client import RusselClient

client = RusselClient("http://127.0.0.1:6022")

# Set a value in the cache
res = client.set("my_cluster", "my_key", "my_value")
print("data:",res)

# Get a value from the cache
value = client.get("my_cluster", "my_key")
print("Value:", value)

# Delete a value from the cache
#client.delete("my_cluster", "my_key")

# Clear a cluster
#client.clear_cluster("my_cluster")

# Get keys of a cluster
#keys = client.get_keys_of_cluster("my_cluster")
#print("Keys:", keys)

# Get all clusters
#clusters = client.get_all_clusters()
#print("Clusters:", clusters)

# Set a cluster
#client.set_cluster("my_cluster")

# Check connection
#status = client.check_connection()
#print("Connection status:", status)

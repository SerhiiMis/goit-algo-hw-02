import queue
import time
import random

# Create a queue for requests
queue = queue.Queue()

# Function to generate new requests
def generate_request():
    while True:
        # Create a new request with a random ID
        new_request = random.randint(1, 1000)
        # Add the request to the queue
        queue.put(new_request)
        print(f"Створено нову заявку: {new_request}")
        # Pause before generating the next request
        time.sleep(random.uniform(0.5, 2))

# Function to process requests from the queue
def process_request():
    while True:
        if not queue.empty():
            # Retrieve a request from the queue
            request = queue.get()
            print(f"Заявка {request} обробляється")
            # Simulate processing time
            time.sleep(random.uniform(1, 3))
        else:
            print("Черга порожня")
        # Pause before checking the queue again
        time.sleep(1)

# Main loop to run both functions
while True:
    # Start generating requests
    # Note: in practice you would use threading or multiprocessing to run these functions concurrently
    generate_request()
    process_request()
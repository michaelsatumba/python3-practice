import time


# Start the timer
start_time = time.time()

# Do some work here
time.sleep(5)  # Sleep for 1 second

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print("Elapsed time:", round(elapsed_time))


import time
import tracemalloc

def measure_performance(func):
    def wrapper(*args, **kwargs):
        # Time complexity measurement
        start_time = time.perf_counter()
        
        # Memory usage measurement
        tracemalloc.start()
        
        result = func(*args, **kwargs)
        
        # Calculate time complexity
        elapsed = time.perf_counter() - start_time
        
        # Calculate space complexity
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        print(f"Time complexity: {elapsed:.6f} seconds")
        print(f"Space complexity:")
        print(f"- Current memory usage: {current / 1024:.2f} KB")
        print(f"- Peak memory usage: {peak / 1024:.2f} KB")
        
        return result
    return wrapper

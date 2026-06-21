#!/usr/bin/env python3
import sys
import fcntl
import time
import os

def safe_write(file_path, payload, timeout=5.0):
    start_time = time.time()
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    
    with open(file_path, 'a') as f:
        while True:
            try:
                # Try to acquire an exclusive lock without blocking
                fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.time() - start_time >= timeout:
                    print(f"Error: Could not acquire lock for {file_path} within {timeout}s", file=sys.stderr)
                    sys.exit(0) # Fail safe, do not crash the calling script or pipeline
                time.sleep(0.1)
        
        try:
            f.write(payload + '\n')
            f.flush()
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 safe_write.py <file_path> <payload>", file=sys.stderr)
        sys.exit(1)
    
    target_file = sys.argv[1]
    data = sys.argv[2]
    safe_write(target_file, data)

# ==============================
# Exercise 1. Threaded Prime Number Checker
# ==============================

import threading

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_range(start, end, result_list, lock):
    for num in range(start, end + 1):
        if is_prime(num):
            with lock:  # to'g'ridan-to'g'ri qo'shish
                result_list.append(num)

if __name__ == "__main__":
    # Input with error handling
    try:
        start_range = int(input("Starting number: "))
        end_range = int(input("Ending number: "))
        thread_count = int(input("Number of Threads: "))
    except ValueError:
        print("Please enter valid integers!")
        exit(1)

    primes = []
    lock = threading.Lock()
    threads = []

    total_numbers = end_range - start_range + 1
    segment = total_numbers // thread_count

    for i in range(thread_count):
        seg_start = start_range + i * segment
        seg_end = end_range if i == thread_count - 1 else seg_start + segment - 1

        t = threading.Thread(target=check_range,
                             args=(seg_start, seg_end, primes, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    primes.sort()
    print("Primes found:")
    print(primes)

# ==============================
# Exercise 2. Threaded File Processing
# ==============================

from collections import Counter

def process_chunk(lines):
    local_counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        local_counter.update(words)
    return local_counter

def threaded_word_count(filename, num_threads=4):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return Counter()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    results = [Counter() for _ in range(num_threads)]
    lock = threading.Lock()

    # Each thread processes its chunk
    def thread_target(i, chunk):
        counter = process_chunk(chunk)
        with lock:
            results[i].update(counter)

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else total_lines
        t = threading.Thread(target=thread_target, args=(i, lines[start:end]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Merge all counters
    total_counter = Counter()
    for c in results:
        total_counter.update(c)
    return total_counter

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    result = threaded_word_count(file_path, num_threads=4)

    if result:
        print("\nWords used more than once:")
        for word, count in result.items():
            if count > 1:
                print(f"{word}: {count}")

        total_words = sum(result.values())
        print("\nTotal number of all words:", total_words)

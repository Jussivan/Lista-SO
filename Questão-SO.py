import random

def fifo(reference_string, num_frames):
    frame_queue = []
    page_faults = 0

    for page in reference_string:
        if page not in frame_queue:
            if len(frame_queue) < num_frames:
                frame_queue.append(page)
            else:
                frame_queue.pop(0)
                frame_queue.append(page)
            page_faults += 1

    return page_faults

def lru(reference_string, num_frames):
    frame_list = []
    page_faults = 0

    for page in reference_string:
        if page in frame_list:
            frame_list.remove(page)
            frame_list.append(page)
        else:
            if len(frame_list) < num_frames:
                frame_list.append(page)
            else:
                frame_list.pop(0)
                frame_list.append(page)
            page_faults += 1

    return page_faults

def generate_reference_string(length):
    return [random.randint(0, 9) for _ in range(length)]

def main():
    reference_string = generate_reference_string(100)
    frame_counts = [2, 3, 4, 5]

    for num_frames in frame_counts:
        fifo_faults = fifo(reference_string, num_frames)
        lru_faults = lru(reference_string, num_frames)

        print(f"Frames: {num_frames}")
        print(f"FIFO Page Faults: {fifo_faults}")
        print(f"LRU Page Faults: {lru_faults}")
        print("=" * 20)

if __name__ == "__main__":
    main()
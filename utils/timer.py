import time

class Timer:
    """A simple timer class to measure latencies between code segments."""

    def __init__(self):
        """Initializes the timer and records the starting time."""
        self.timestamps = []
        self.add("start")

    def add(self, label: str):
        """Adds a timestamp with a given label.

        Args:
            label: A string to identify the timestamp.
        """
        timestamp = time.time()
        self.timestamps.append((label, timestamp))

    def _get_results(self):
        """Processes the timestamps and calculates latencies."""
        if not self.timestamps:
            return [], 0.0

        results = []
        start_time = self.timestamps[0][1]
        previous_time = start_time

        for label, timestamp in self.timestamps:
            time_since_start = timestamp - start_time
            time_since_previous = timestamp - previous_time
            results.append({
                "step": label,
                "time_since_start": time_since_start,
                "time_since_previous": time_since_previous
            })
            previous_time = timestamp
        
        total_time = self.timestamps[-1][1] - start_time
        return results, total_time

    def display(self):
        """Displays the timing results in a formatted table."""
        results, total_time = self._get_results()

        print("Timer Results:")
        print("-" * 60)
        print(f"{'Step':<20} | {'Time Since Start':<20} | {'Time Since Previous':<20}")
        print("-" * 60)

        for res in results:
            print(f"{res['step']:<20} | {res['time_since_start']:.4f}s{'':<15} | {res['time_since_previous']:.4f}s")

        print("-" * 60)
        print(f"Total Time: {total_time:.4f}s")
        print("-" * 60)

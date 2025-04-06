class Jeep:
    """A single Jeep in the service queue."""
    def __init__(self, model, owner_name):
        self.model = model
        self.owner_name = owner_name
        self.next = None


class JeepQueue:
    """A custom queue implementation using a linked list."""
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, model, owner_name):
        """Add a new Jeep to the rear of the queue."""
        new_jeep = Jeep(model, owner_name)
        if not self.rear:
            self.front = self.rear = new_jeep
        else:
            self.rear.next = new_jeep
            self.rear = new_jeep
        self.count += 1
        print(f"Enqueued: {model} (Owner: {owner_name})")

    def dequeue(self):
        """Remove the Jeep at the front of the queue."""
        if self.front is None:
            print("No Jeeps to service.")
            return None

        model = self.front.model
        owner = self.front.owner_name
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        print(f"Serviced Jeep: {model} (Owner: {owner})")
        return model

    def peek(self):
        """Return the Jeep at the front without removing it."""
        if self.front:
            return self.front.model
        return None

    def view_next(self):
        """Print details of the next Jeep in line."""
        if self.front:
            print(f"Next in line: {self.front.model} (Owner: {self.front.owner_name})")
        else:
            print("Queue is empty. No Jeeps waiting.")

    def size(self):
        """Return the total number of Jeeps in the queue."""
        return self.count

    def clear(self):
        """Clear the entire queue."""
        self.front = None
        self.rear = None
        self.count = 0
        print("The queue has been cleared.")

    def print_queue(self):
        """Display all Jeeps currently in the queue."""
        print("\nJeep Queue:")
        if self.front is None:
            print("  (Empty)")
            return

        current = self.front
        index = 1
        while current:
            print(f"  {index}. {current.model} (Owner: {current.owner_name})")
            current = current.next
            index += 1
        print(f"Total Jeeps in queue: {self.count}")


# Demo
if __name__ == "__main__":
    queue = JeepQueue()

    # Add Jeeps to the queue
    queue.enqueue("Wrangler", "Alice")
    queue.enqueue("Cherokee", "Bob")
    queue.enqueue("Gladiator", "Charlie")
    queue.enqueue("Compass", "Diana")

    print()
    queue.view_next()

    print("\nStarting service...")
    queue.dequeue()
    queue.dequeue()

    print()
    queue.print_queue()

    print("\nChecking who's next...")
    queue.view_next()

    print(f"\nTotal Jeeps left: {queue.size()}")

    print("\nClearing the queue...")
    queue.clear()
    queue.print_queue()

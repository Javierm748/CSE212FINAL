# Queues

[← Back to Welcome](0-welcome.md)

## Overview
A **queue** is a First-In-First-Out (FIFO) data structure. Think of a line at a busy restaurant: whoever arrives first gets served first, and new arrivals go to the back of the line.

## Big O Performance

| Operation | Description                               | Big O   |
|-----------|-------------------------------------------|---------|
| `Enqueue` | Add an element to the rear of the queue   | O(1)*   |
| `Dequeue` | Remove an element from the front          | O(1)*   |
| `Peek`    | Return the front element without removing | O(1)    |
| `Count`   | Number of elements in the queue           | O(1)    |

> \*For most implementations, these are amortized constant time.

## Common Errors
1. **Dequeuing an Empty Queue**: Removing an item when none exist (underflow).
2. **Ignoring Boundaries** in fixed-size (array-based) queues.

## Example Problem: Jeep Service Queue
You operate a **Jeep Service Center**. Jeeps line up in the order they arrive.

1. A Jeep arrives named "Wrangler" → Enqueue "Wrangler"  
2. "Cherokee" arrives next → Enqueue "Cherokee"  
3. When a mechanic is free, you Dequeue to service the next waiting Jeep.

### C# Example
```csharp
using System;
using System.Collections.Generic;

namespace JeepServiceQueue
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a queue of string to store Jeep names
            Queue<string> jeepQueue = new Queue<string>();
            
            // Enqueue several Jeeps
            jeepQueue.Enqueue("Wrangler");
            jeepQueue.Enqueue("Cherokee");
            jeepQueue.Enqueue("Gladiator");

            // Peek at the first Jeep in line
            Console.WriteLine("Next Jeep to be serviced: " + jeepQueue.Peek());
            // Output: Wrangler

            // Dequeue to service the first Jeep
            string servicedJeep = jeepQueue.Dequeue();
            Console.WriteLine("Serviced Jeep: " + servicedJeep);
            // Output: Wrangler

            // Display the remaining queue
            Console.WriteLine("\nRemaining Jeeps in queue:");
            foreach (var jeep in jeepQueue)
            {
                Console.WriteLine(jeep);
            }
            // Output:
            // Cherokee
            // Gladiator
        }
    }
}

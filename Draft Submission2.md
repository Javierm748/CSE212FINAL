# Linked Lists

[← Back to Welcome](0-welcome.md)

## Overview
A **linked list** is a linear data structure where each element (or “node”) contains a **data value** and a **pointer/reference** to the next node. This design allows for efficient insertion or deletion without shifting other elements, unlike an array.

### Singly vs. Doubly Linked Lists
- **Singly Linked List**: Each node only points to the next node.
- **Doubly Linked List**: Each node has pointers to both the next and the previous nodes, allowing traversal in both directions.

## Big O Performance

| Operation      | Description                                                 | Big O (Worst) |
|----------------|-------------------------------------------------------------|---------------|
| Insertion      | Adding a new node (at head or tail if known)               | O(1)          |
| Deletion       | Removing a node (if you have a reference to that node)      | O(1)          |
| Search         | Finding a node by value requires traversing from the head   | O(n)          |
| Access by Index| Accessing the k-th element sequentially (head → tail)       | O(n)          |

> Linked lists excel when frequent insertion/deletion is needed, but random access is inefficient.

## Common Errors
1. **Null References**: Not checking if `next` or `prev` is null before dereferencing.
2. **Losing Nodes**: Incorrectly updating references, causing parts of the list to be lost.
3. **Infinite Loops**: Failing to properly update `next` or `prev` in a loop, causing never-ending traversal.

## Example Problem: Music Playlist
Imagine implementing a **music playlist** using a singly linked list. Each node represents a “song,” containing:
- A `Title` (string)
- A pointer to the **next** song in the list

### C# Example

```csharp
using System;

namespace MusicPlaylist
{
    class Song
    {
        public string Title { get; set; }
        public Song Next { get; set; }

        public Song(string title)
        {
            Title = title;
            Next = null;
        }
    }

    class Playlist
    {
        private Song head;

        // Add a song at the end
        public void AddSong(string title)
        {
            Song newSong = new Song(title);
            if (head == null)
            {
                head = newSong;
                return;
            }
            Song current = head;
            while (current.Next != null)
            {
                current = current.Next;
            }
            current.Next = newSong;
        }

        // Remove the first song with the given title
        public void RemoveSong(string title)
        {
            if (head == null) return; // Empty list

            if (head.Title == title)
            {
                head = head.Next;
                return;
            }

            Song current = head;
            while (current.Next != null && current.Next.Title != title)
            {
                current = current.Next;
            }
            if (current.Next != null)
            {
                current.Next = current.Next.Next;
            }
        }

        public void PrintPlaylist()
        {
            Song current = head;
            while (current != null)
            {
                Console.WriteLine(current.Title);
                current = current.Next;
            }
        }
    }

    class Program
    {
        static void Main()
        {
            Playlist playlist = new Playlist();
            playlist.AddSong("Song A");
            playlist.AddSong("Song B");
            playlist.AddSong("Song C");

            Console.WriteLine("Current Playlist:");
            playlist.PrintPlaylist();
            // Output:
            // Song A
            // Song B
            // Song C

            playlist.RemoveSong("Song B");

            Console.WriteLine("\nAfter Removing 'Song B':");
            playlist.PrintPlaylist();
            // Output:
            // Song A
            // Song C
        }
    }
}

class Playlist:
    def __init__(self, length):
        self.length = length
        self.queue = [None] * length
        self.front = -1
        self.rear = -1
    def is_empty(self):
        return self.front == -1
    def is_full(self):
        return (self.rear + 1) % self.length == self.front
    def enqueue(self, item):
        if self.is_full():
            print("Queue is FULL")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.length
        self.queue[self.rear] = item
        print(f"'{item}' added to playlist.")
    def dequeue(self):
        if self.is_empty():
            print("Queue is EMPTY")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.length
        return item
    def delete_song(self, song_name):
        if self.is_empty():
            print("Playlist is empty. Nothing to delete.")
            return
        i = self.front
        found_index = -1
        while True:
            if self.queue[i] == song_name:
                found_index = i
                break
            if i == self.rear:
                break
            i = (i + 1) % self.length
        if found_index == -1:
            print(f"'{song_name}' not found in playlist.")
            return
        j = found_index
        while j != self.rear:
            next_index = (j + 1) % self.length
            self.queue[j] = self.queue[next_index]
            j = next_index
        self.queue[self.rear] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.length) % self.length
        print(f"'{song_name}' deleted from playlist.")
    def display(self):
        if self.is_empty():
            print("Playlist is empty.")
            return
        print("Current Playlist:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.length
        print()
print("=== Music Playlist Queue ===")
size = int(input("Enter playlist size: "))
playlist = Playlist(size)
while True:
    print("\n--- MENU ---")
    print("1. Add Song")
    print("2. Play Song (Loop)")
    print("3. View Playlist")
    print("4. Delete Song by Name")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        song = input("Enter song name: ")
        playlist.enqueue(song)
    elif choice == '2':
        played = playlist.dequeue()
        if played:
            print(f"Now playing: {played}")
            playlist.enqueue(played)  # loop it back
    elif choice == '3':
        playlist.display()
    elif choice == '4':
        song_to_delete = input("Enter song name to delete: ")
        playlist.delete_song(song_to_delete)
    elif choice == '5':
        print("Exiting Playlist...")
        break
    else:
        print("Invalid choice. Please try again.")

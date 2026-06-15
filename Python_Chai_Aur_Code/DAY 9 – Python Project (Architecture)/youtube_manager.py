import json
# json module is used to read and write data in JSON format (text-based storage)

# Function to load existing video data from file
def load_data():
    """
    Loads video data from 'youtube.txt' file.
    If file does not exist, returns an empty list.
    """
    try:
        # Open file in read mode
        with open('youtube.txt', 'r') as file:
            test = json.load(file)   # Load JSON data from file into Python object (list of dicts)
            return test
    except FileNotFoundError:
        # If file does not exist, return empty list
        return []
    
# Helper function to save video data to file
def save_data_helper(videos):
    """
    Saves the videos list into 'youtube.txt' file in JSON format.
    """
    # Open file in write mode
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)  # Convert Python list into JSON and store in file

# Function to list all videos
def list_all_videos(videos):
    """
    Displays all saved YouTube videos with index, name, and duration.
    """
    print("\n")
    print("*" * 70)

    # enumerate gives index + value, start=1 makes index start from 1 instead of 0
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")

    print("\n")
    print("*" * 70)

# Function to add a new video
def add_video(videos):
    """
    Takes input from user and adds a new video to the list.
    """
    name = input("Enter video name: ")   # Get video name
    time = input("Enter video time: ")   # Get video duration

    # Add video as dictionary inside list
    videos.append({'name': name, 'time': time})

    # Save updated list to file
    save_data_helper(videos)

# Function to update an existing video's details
def update_video(videos):
    """
    Updates an existing video's details.
    """
    list_all_videos(videos)  # Show existing videos

    index = int(input("Enter the video number to update"))

    # Check if index is valid
    if 1 <= index <= len(videos):
        name = input("Enter the new video name")
        time = input("Enter the new video time")

        # Update selected video (index-1 because list is 0-based)
        videos[index - 1] = {'name': name, 'time': time}

        save_data_helper(videos)
    else:
        print("Invalid index selected")

# Function to delete a video   
def delete_video(videos):
    """
    Deletes a selected video from the list.
    """
    list_all_videos(videos)  # Show existing videos

    index = int(input("Enter the video number to be deleted"))

    # Validate index
    if 1 <= index <= len(videos):
        del videos[index - 1]   # Remove video from list
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

# Main function to run the YouTube manager app 
def main():
    """
    Main function that runs the menu-driven YouTube manager.
    """
    videos = load_data()  # Load videos when app starts

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = input("Enter your choice: ")

        # if-elif-else chain for Python version compatibility
        if choice == '1':
            list_all_videos(videos)
        elif choice == '2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)
        elif choice == '4':
            delete_video(videos)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")

# This ensures main() runs only when file is executed directly
if __name__ == "__main__":
    main()

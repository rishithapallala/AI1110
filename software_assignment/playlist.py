import tkinter as tk
import numpy as np
import pygame

class AudioPlaylistUI:
    def __init__(self, master):
        self.master = master
        master.title("Audio Playlist")

        self.playlist = tk.Listbox(master, width=50)
        self.playlist.pack(pady=10)

        self.shuffle_play_button = tk.Button(master, text="Shuffle and Play", command=self.shuffle_and_play)
        self.shuffle_play_button.pack(pady=5)

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_interface)
        self.exit_button.pack(pady=5)

        self.file_variables = {}  # Dictionary to store file variables

        self.playlist_index = 0
        self.playing = False

        # Initialize the mixer
        pygame.mixer.init()

        # Default playlist (add your audio files here)
        self.default_playlist = [
            "Downloads/playaudio/IMG_0553.mp3",
            "Downloads/playaudio/IMG_0555.mp3",
            "Downloads/playaudio/IMG_0556.mp3",
            "Downloads/playaudio/IMG_0557.mp3",
            "Downloads/playaudio/IMG_0558.mp3",
            "Downloads/playaudio/IMG_0559.mp3",
            "Downloads/playaudio/IMG_0560.mp3",
            "Downloads/playaudio/IMG_0561.mp3",
            "Downloads/playaudio/IMG_0562.mp3",
            "Downloads/playaudio/IMG_0563.mp3",
            "Downloads/playaudio/IMG_0565.mp3",
            "Downloads/playaudio/IMG_0566.mp3",
            "Downloads/playaudio/IMG_0567.mp3",
            "Downloads/playaudio/IMG_0568.mp3",
            "Downloads/playaudio/IMG_0569.mp3",
            "Downloads/playaudio/IMG_0570.mp3",
            "Downloads/playaudio/IMG_0571.mp3",
            "Downloads/playaudio/IMG_0572.mp3",
            "Downloads/playaudio/IMG_0574.mp3",
            "Downloads/playaudio/IMG_0575.mp3"
        ]

        self.load_default_playlist()

    def load_default_playlist(self):
        for audio_file in self.default_playlist:
            variable = np.random.randint(1, 1000)  # Generate a random variable
            self.file_variables[audio_file] = variable
            self.playlist.insert(tk.END, f"{audio_file} ({variable})")

    def shuffle_and_play(self):
        playlist_items = list(self.playlist.get(0, tk.END))
        np.random.shuffle(playlist_items)
        self.playlist.delete(0, tk.END)
        for item in playlist_items:
            self.playlist.insert(tk.END, item)

        self.playlist_index = 0
        self.playing = True
        self.play_next()

    def play_next(self):
        if self.playing and self.playlist_index < self.playlist.size():
            audio_file = self.playlist.get(self.playlist_index).split(" ")[0]  # Get the audio file path
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
            self.playlist_index += 1
            self.play_next()
        else:
            self.playing = False

    def exit_interface(self):
        self.playing = False
        pygame.mixer.music.stop()
        self.master.destroy()

root = tk.Tk()
playlist_ui = AudioPlaylistUI(root)
root.mainloop()


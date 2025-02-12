import pytubefix.exceptions
from pytubefix import YouTube
import customtkinter as ctk
from tkinter import messagebox, filedialog
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def get_path():
    path = filedialog.askdirectory(initialdir="")
    return path


class TubeSaveApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TubeSave")
        self.geometry("500x200")

        
        self.theme = "dark" # The theme by-default will be 'dark'
        ctk.set_appearance_mode(self.theme)
        ctk.set_default_color_theme("blue") # The default color will be 'blue'

        self.save_video_label = ctk.CTkLabel(self,
                                             text="YouTube Video Downloader",
                                             font=("Helvetica", 25),
                                             )
        self.save_video_label.pack(pady=20)

        self.entry_link = ctk.CTkEntry(self,
                                       placeholder_text="enter link here",
                                       border_color="red",
                                       border_width=1,
                                       width=350)
        self.entry_link.pack(pady=10)

        self.download_button = ctk.CTkButton(self,
                                            text="Download",
                                            fg_color="#ab0f0f",
                                            hover_color="#751414",
                                            width=40,
                                            corner_radius=10,
                                            command=self.go_to_confirmation_page)
        self.download_button.pack(pady=12)

    @staticmethod
    def download_video(yt, path):
        yd = yt.streams.get_highest_resolution()
        yd.download(os.path.dirname(f"{path}/"))

    def show_video_details(self, yt):
        def confirmation():
            is_user_sure = messagebox.askyesno("Are you sure?", "Are you sure you want to download the video?")

            if is_user_sure:
                path = get_path()
                self.download_video(yt, path)
            else:
                messagebox.showinfo("Video was not downloaded.", f"Video {yt.title} was not downloaded")

        video_detail_window = ctk.CTkToplevel()
        video_detail_window.title(f"{yt.title} - YouTube")
        video_detail_window.geometry("440x330")

        details_of_video_frame = ctk.CTkScrollableFrame(video_detail_window,
                                                        width=320,
                                                        orientation="horizontal")
        details_of_video_frame.pack(pady=15)

        title_label = ctk.CTkLabel(details_of_video_frame, text=f"Title: {yt.title}")
        title_label.pack()

        publish_date_label = ctk.CTkLabel(details_of_video_frame, text=f"Publish date: {yt.publish_date}")
        publish_date_label.pack()

        author_label = ctk.CTkLabel(details_of_video_frame, text=f"Author: {yt.author}")
        author_label.pack()

        length_label = ctk.CTkLabel(details_of_video_frame, text=f"Length: {yt.length}")
        length_label.pack()

        views_label = ctk.CTkLabel(details_of_video_frame, text=f"Views: {yt.views}")
        views_label.pack()

        download_button = ctk.CTkButton(video_detail_window,
                                        text="Download",
                                        fg_color="#ab0f0f",
                                        hover_color="#751414",
                                        width=40,
                                        corner_radius=10,
                                        command=confirmation)
        download_button.pack(pady=20)


    def go_to_confirmation_page(self):
        try:
            link = self.entry_link.get()

            if not link:
                raise ValueError

            yt = YouTube(link)

        except pytubefix.exceptions.RegexMatchError:
            messagebox.showerror("Error!", "Error: The provided URL is invalid!")
        except ValueError:
            messagebox.showerror("Error!", "Error: 'link field' is empty!")
        else:
            self.show_video_details(yt)




def main():
    tube_save_app = TubeSaveApp()
    tube_save_app.mainloop()

if __name__ == "__main__":
    main()

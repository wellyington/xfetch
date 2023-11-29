from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from ytdl import get_video, get_mp3
import threading

class MyLayout(Widget):
    url = ObjectProperty(None)

    def get(self, url, spinner):
        if spinner == "Video":
            print("Download Video Logic!")
            get_video(url)
        elif spinner == "Mp3":
            print("Download Mp3 Logic!")
            get_mp3(url)

    def press(self):
        url = self.url.text
        spinner = self.ids.spinner.text

        if url == '':
            print("URL Cannot be empty!")
        else:
            print(f"{url} : {spinner}")
            get = threading.Thread(target=self.get, args=(url, spinner))
            get.start()
            self.url.text = ""

class XfetchApp(App):
    def build(self):
        Window.clearcolor = (31/255,31/255,31/255)
        return MyLayout()

if __name__ == '__main__':
    XfetchApp().run()

from __future__ import unicode_literals
from textwrap import dedent
from plyer import filechooser
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.floatlayout import FloatLayout
from kivy.base import runTouchApp
from kivy.lang import Builder
import moviepy.editor as mp
import pypandoc
from PIL import Image
from kivy.utils import rgba
from kivy.uix.scrollview import ScrollView 
from kivy.core.window import Window 
from kivy.app import runTouchApp
import docx2txt
from fpdf import FPDF
from plyer import notification
from pathlib import Path



class FileChoose(Button):
    '''
    Button that triggers 'filechooser.open_file()' and processes
    the data response from filechooser Activity.
    '''

    selection = ListProperty([])
    lol = ObjectProperty()

    def choose(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.open_file(on_selection=self.handle_selection)


    def handle_selection(self, selection):
        '''how do
        Callback function for handling the selection response from Activity.
        '''
        self.selection = selection

    def on_selection(self, *a, **k):
        '''
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        '''

        try:
            App.get_running_app().root.ids.result.text = str(self.selection)[2:-2]
            your_string = str(self.selection)[2:-2]

            def slicing(file_location = your_string):
                new_list = file_location.split("\\") # this is where my function is lol
                your_file = new_list[-1]
                return your_file


            def slicing_thing(your_file_location):
                index_of_dot = your_file_location.find('.')
                dotmp4 = your_file_location[:index_of_dot]
                return dotmp4


            if self.text == 'Gif to Mp4':
                clip = mp.VideoFileClip(your_string)
                clip.write_videofile(slicing_thing(your_string) + ".mp4")
                my_file = Path(slicing_thing(your_string) + ".mp4")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Mp4 to Gif':
                clip = mp.VideoFileClip(your_string)
                clip.write_gif(slicing_thing(your_string) + ".gif")
                my_file = Path(slicing_thing(your_string) + ".gif")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'HTML to Docx':
                conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert conuot == ""
                my_file = Path(slicing_thing(your_string) + ".docx")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Mp3 to Wav':
                clip = mp.AudioFileClip(your_string)
                clip.write_audiofile(slicing_thing(your_string) + ".wav")
                my_file = Path(slicing_thing(your_string) + ".wav")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Wav to Mp3':
                clip = mp.AudioFileClip(your_string)
                clip.write_audiofile(slicing_thing(your_string) + ".mp3")
                my_file = Path(slicing_thing(your_string) + ".mp3")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'JPEG to PNG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".png", 'PNG')
                my_file = Path(slicing_thing(your_string) + ".png")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'PNG to JPEG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                my_file = Path(slicing_thing(your_string) + ".jpeg")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'JPG to PNG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".png", 'PNG')
                my_file = Path(slicing_thing(your_string) + ".png")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'PNG to JPG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".jpg")
                my_file = Path(slicing_thing(your_string) + ".jpg")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')
             
            elif self.text == 'Md to Docx':
                output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert output == ""
                my_file = Path(slicing_thing(your_string) + ".docx")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Docx to Md':
                output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                assert output == ""
                my_file = Path(slicing_thing(your_string) + ".md")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Md to Epub':
                output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                assert output == ""
                my_file = Path(slicing_thing(your_string) + ".epub")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Epub to Md':
                output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                assert output == ""
                my_file = Path(slicing_thing(your_string) + ".md")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'JPG to JPEG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                my_file = Path(slicing_thing(your_string) + ".jpeg")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'JPEG to JPG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".jpg")
                my_file = Path(slicing_thing(your_string) + ".jpg")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Mp4 to Wav':
                clip = mp.VideoFileClip(your_string)
                clip.audio.write_audiofile(slicing_thing(your_string) + ".wav")
                my_file = Path(slicing_thing(your_string) + ".wav")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Mp4 to Mp3':
                clip = mp.VideoFileClip(your_string)
                clip.audio.write_audiofile(slicing_thing(your_string) + ".mp3")
                my_file = Path(slicing_thing(your_string) + ".mp3")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Docx to Epub':
                output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                assert output == ""
                my_file = Path(slicing_thing(your_string) + ".epub")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Epub to Docx':
                output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert output == ""
                my_file = Path(slicing_thing(your_string) + ".docx")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Docx to HTML':
                output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                assert output == ""
                my_file = Path(slicing_thing(your_string) + ".html")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Md to HTML':
                output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                assert output == ""
                my_file = Path(slicing_thing(your_string) + ".html")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Txt to HTML':
                output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                assert output == ""
                my_file = Path(slicing_thing(your_string) + ".html")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Epub to HTML':
                output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                assert output == ""
                my_file = Path(slicing_thing(your_string) + ".html")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == 'Docx to Txt':
                MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                    print(MY_TEXT, file=text_file)
                my_file = Path(slicing_thing(your_string) + ".txt")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == "Epub to Txt":
                output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert output == ""
                MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                    print(MY_TEXT, file=text_file)
                my_file = Path(slicing_thing(your_string) + ".txt")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == "HTML to Txt":
                conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert conuot == ""
                MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                    print(MY_TEXT, file=text_file)
                my_file = Path(slicing_thing(your_string) + ".txt")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == "Md to Txt":
                output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert output == ""
                MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                    print(MY_TEXT, file=text_file)
                my_file = Path(slicing_thing(your_string) + ".txt")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            elif self.text == "Txt to PDF":
                f = open(your_string, "r")
                x = f.read()

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial",size=30)
                pdf.cell(200,100, txt = x, ln=1, align="C")
                pdf.output(slicing_thing(your_string) + ".pdf") 
                my_file = Path(slicing_thing(your_string) + ".txt")
                if my_file.is_file():
                    notification.notify(title='Easy Convert', message='Your File Is Ready')

            else:
                App.get_running_app().root.ids.result.text = "Wrong file type!"

        except:
            App.get_running_app().root.ids.result.text = "Sorry we're having difficulties right now."

        finally:
            App.get_running_app().root.ids.result.text = "Conversion Complete! We'll notify you when your file is ready. It should be in the same folder as your original file. If you have any questions don't hesitate to contact us, view the help screen, or try the conversion again!"
            print(slicing_thing(your_string))
            print(slicing(your_string))

  

    

        

    


class ChooserApp(App):
    '''
    Application class with root built in KV.
    '''



    def build(self):
        return Builder.load_string(dedent('''
            <FileChoose>:

                font_size: 40
                size_hint: .5, .5
                size_hint_x: None
                width: 350
                size_hint_y: None
                height: 100


            GridLayout:
                cols: 1
                spacing: 20
                orientation: 'horizontal'


                canvas:
                    Color: 
                        rgb: (9/255, 34/255, 52/255, 1)
                    Rectangle:
                        pos: self.pos
                        size: self.size

                GridLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: self.minimum_height
                    row_default_height: 60
                    cols: 2
                    spacing: 20
                    padding: 20

                    canvas:
                        Color: 
                            rgb: 0, 0, 0, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size

                    Label:
                        text:"   Easy Convert - Easy Conversions"
                        size_hint: .1, .07
                        font_size: 40
                        pos_hint: {"x": .3, "top": .9}

                    Button:
                        text: ''
                        size_hint_x: None
                        width: 200
                        size_hint_y: None
                        background_color: 0, 0, 0, 0
                        on_press: root.ids.result.text = "Need help navigating our app? Here are the instructions to do so. Firstly you're going to want to click on any of our buttons on the left to convert your file type to a desired one. Upon selection, you will be prompted to your file directory. Here you will select the file with the filetype you currently have in the conversion. Next, you will be redirected to the Easy Convert main screen and there you will receive a sucess message if your conversion went successful. And that's it! It's as easy as that, your new file should be created and ready to use!"
                        Image:
                            source: "transparent_q.png"
                            center_x: self.parent.center_x
                            center_y: self.parent.center_y


                ScrollView:
              
                    GridLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: self.minimum_height
                        row_default_height: 60
                        cols: 2
                        spacing: 10  
                        padding: 10

                        GridLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: self.minimum_height
                            row_default_height: 60
                            cols: 1
                            spacing: 20
                            padding: 10
                       


                            FileChoose:
                                color: 0, 0, 0 , 1
                                background_color: (242/255, 68/255, 63/255, 1)
                                on_release: self.choose()
                                text: 'JPEG to PNG'
                              

                            FileChoose:
                                color: 0, 0, 0 , 1
                                background_color: (242/255, 68/255, 63/255, 1)
                                on_release: self.choose()
                                text: 'PNG to JPEG'
                                

                            FileChoose:
                                color: 0, 0, 0, 1
                                background_color: (242/255, 68/255, 63/255, 1)
                                on_release: self.choose()
                                text: 'JPG to PNG'
                               

                            FileChoose:
                                color: 0, 0, 0 , 1
                                background_color: (242/255, 68/255, 63/255, 1)
                                on_release: self.choose()
                                text: 'PNG to JPG'
                              

                            FileChoose:
                                color: 0, 0, 0 , 1
                                background_color: (242/255, 68/255, 63/255, 1)
                                on_release: self.choose()
                                text: 'JPG to JPEG'
                            

                            FileChoose:
                                color: 0, 0, 0 , 1
                                background_color: (242/255, 68/255, 63/255, 1)
                                on_release: self.choose()
                                text: 'JPEG to JPG'
                                

                            FileChoose:
                                background_color: (78/255, 38/255, 120/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Gif to Mp4'
                               

                            FileChoose:
                                background_color: (78/255, 38/255, 120/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Mp4 to Gif'
                               

                            FileChoose:
                                background_color: (99/255, 42/255, 84/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Mp3 to Wav'


                            FileChoose:
                                background_color: (99/255, 42/255, 84/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Wav to Mp3'
                              

                            FileChoose:
                                background_color: (99/255, 42/255, 84/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Mp4 to Wav'
                                

                            FileChoose:
                                background_color: (99/255, 42/255, 84/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Mp4 to Mp3'

                            FileChoose:
                                color: 0, 0, 0 , 1
                                background_color: (20/255, 149/255, 156/255, 1)
                                on_release: self.choose()
                                text: 'Md to Docx'
                             

                            FileChoose:
                                color: 0, 0, 0 , 1
                                background_color: (20/255, 149/255, 156/255, 1)
                                on_release: self.choose()
                                text: 'Docx to Md'
                              

                            FileChoose:
                                color: 0, 0, 0 , 1
                                background_color: (20/255, 149/255, 156/255, 1)
                                on_release: self.choose()
                                text: 'Md to Epub'
                               

                            FileChoose:
                                color: 0, 0, 0 , 1
                                background_color: (20/255, 149/255, 156/255, 1)
                                on_release: self.choose()
                                text: 'Epub to Md'
                               


                            FileChoose:
                                color: 0, 0, 0 , 1
                                background_color: (20/255, 149/255, 156/255, 1)
                                on_release: self.choose()
                                text: 'HTML to Docx'
                               


                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Docx to Epub'
                                

                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Epub to Docx'
                               

                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Docx to HTML'
                              

                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Md to HTML'
                               

                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Epub to HTML'
                           

                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Docx to Txt'
                              

                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Epub to Txt'
                            

                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'HTML to Txt'
                            

                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Md to Txt'
                              

                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Txt to PDF'
                               

                            FileChoose:
                                background_color: (20/255, 149/255, 156/255, 1)
                                color: 0, 0, 0 , 1
                                on_release: self.choose()
                                text: 'Txt to HTML'
                               

                                

                        GridLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: self.minimum_height
                            row_default_height: 60
                            cols: 1
                            spacing: 16


                            TextInput:
                                font_size: 30
                                size_hint_x: None
                                width: 250
                                size_hint_y: None
                                height: 1359
                                id: result
                                text: ''
                                hint_text: 'Any App Related Messages Will Appear Here'


                            Button:
                                size_hint_x: None
                                width: 250
                                size_hint_y: None
                                height: 100
                                font_size: 40
                                background_color: 1, 0, 0, 1
                                text: 'Exit'
                                on_press: app.stop()

                           
        
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                    
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5
                            Label:
                                text: ''
                                size_hint: 5, 5


        '''))


if __name__ == '__main__':
    ChooserApp().run()
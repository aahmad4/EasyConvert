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

            elif self.text == 'Mp4 to Gif':
                clip = mp.VideoFileClip(your_string)
                clip.write_gif(slicing_thing(your_string) + ".gif")

            elif self.text == 'HTML to Docx':
                conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert conuot == ""

            elif self.text == 'Mp3 to Wav':
                clip = mp.AudioFileClip(your_string)
                clip.write_audiofile(slicing_thing(your_string) + ".wav")

            elif self.text == 'Wav to Mp3':
                clip = mp.AudioFileClip(your_string)
                clip.write_audiofile(slicing_thing(your_string) + ".mp3")

            elif self.text == 'JPEG to PNG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".png", 'PNG')

            elif self.text == 'PNG to JPEG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')

            elif self.text == 'JPG to PNG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".png", 'PNG')

            elif self.text == 'PNG to JPG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".jpg")

            elif self.text == 'Md to Docx':
                output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert output == ""

            elif self.text == 'Docx to Md':
                output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                assert output == ""

            elif self.text == 'Md to Epub':
                output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                assert output == ""

            elif self.text == 'Epub to Md':
                output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                assert output == ""

            elif self.text == 'JPG to JPEG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')

            elif self.text == 'JPEG to JPG':
                image = Image.open(your_string)
                image.save(slicing_thing(your_string) + ".jpg")

            elif self.text == 'Mp4 to Wav':
                clip = mp.VideoFileClip(your_string)
                clip.audio.write_audiofile(slicing_thing(your_string) + ".wav")

            elif self.text == 'Mp4 to Mp3':
                clip = mp.VideoFileClip(your_string)
                clip.audio.write_audiofile(slicing_thing(your_string) + ".mp3")

            elif self.text == 'Docx to Epub':
                output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                assert output == ""

            elif self.text == 'Epub to Docx':
                output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert output == ""

            elif self.text == 'Docx to HTML':
                output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                assert output == ""

            elif self.text == 'Md to HTML':
                output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                assert output == ""

            elif self.text == 'Txt to HTML':
                output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                assert output == ""

            elif self.text == 'Epub to HTML':
                output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                assert output == ""

            elif self.text == 'Docx to Txt':
                MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                    print(MY_TEXT, file=text_file)

            elif self.text == "Epub to Txt":
                output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert output == ""
                MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                    print(MY_TEXT, file=text_file)

            elif self.text == "HTML to Txt":
                conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert conuot == ""
                MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                    print(MY_TEXT, file=text_file)

            elif self.text == "Md to Txt":
                output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                assert output == ""
                MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                    print(MY_TEXT, file=text_file)

            elif self.text == "Txt to PDF":
                f = open(your_string, "r")
                x = f.read()

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial",size=30)
                pdf.cell(200,100, txt = x, ln=1, align="C")
                pdf.output(slicing_thing(your_string) + ".pdf") 

            elif self.text == "Txt to Epub":
                pass

            elif self.text == "Txt to HTML":
                pass

            elif self.text == "Txt to Md":
                pass


            else:
                App.get_running_app().root.ids.result.text = "Wrong file type!"

        except:
            App.get_running_app().root.ids.result.text = "Sorry we're having difficulties right now."

        finally:
            App.get_running_app().root.ids.result.text = "Finished rendering files! If you don't see your converted file, look at the same folder as your original file, or try the conversion again."
            print(your_string)
            print(slicing(your_string))

  

    

        

    


class ChooserApp(App):
    '''
    Application class with root built in KV.
    '''



    def build(self):
        return Builder.load_string(dedent('''
            <FileChoose>:

                font_size: 20
                size_hint: .5, .5


            BoxLayout:
                id: b1
                orientation: 'horizontal'
                padding: 10, 10
                row_default_height: '48dp'
                row_force_default: True
                spacing: 10, 10

                canvas:
                    Color: 
                        rgb: (.046875, .0390625, .2109375)
                    Rectangle:
                        pos: self.pos
                        size: self.size

                ScrollView:

                    GridLayout:
                        cols: 1
                        spacing: 20
                        orientation: 'horizontal'

                        GridLayout:
                            orientation: 'horizontal'
                            size_hint_y: None
                            height: self.minimum_height
                            row_default_height: 60
                            cols: 2
                            spacing: 10

                            canvas:
                                Color: 
                                    rgb: 0, 0, 0, 1
                                Rectangle:
                                    pos: self.pos
                                    size: self.size

                            Label:
                                text: 'EzConvert Developed By The Stemmovators'
                                font_name: 'DejaVuSans'
                                size_hint: .1, .07
                                font_size: 20
                                pos_hint: {"x": .3, "top": .9}

                            Button:
                                text: ''
                                size_hint_x: None
                                width: 100
                                background_color: 0, 0, 0, 0
                                on_press: app.stop()
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

                                GridLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: self.minimum_height
                                    row_default_height: 60
                                    cols: 1
                                    spacing: 10                  

                               

                                    FileChoose:
                                        color: 0, 0, 0 , 1
                                        background_color: (117/256, 52/256, 247/256, 1)
                                        on_release: self.choose()
                                        text: 'Md to Docx'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        color: 0, 0, 0 , 1
                                        background_color: (117/256, 52/256, 247/256, 1)
                                        on_release: self.choose()
                                        text: 'Docx to Md'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        color: 0, 0, 0 , 1
                                        background_color: (117/256, 52/256, 247/256, 1)
                                        on_release: self.choose()
                                        text: 'Md to Epub'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        color: 0, 0, 0 , 1
                                        background_color: (117/256, 52/256, 247/256, 1)
                                        on_release: self.choose()
                                        text: 'Epub to Md'
                                        size_hint_x: None
                                        width: 250


                                    FileChoose:
                                        color: 0, 0, 0 , 1
                                        background_color: (117/256, 52/256, 247/256, 1)
                                        on_release: self.choose()
                                        text: 'HTML to Docx'
                                        size_hint_x: None
                                        width: 250


                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Docx to Epub'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Epub to Docx'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Docx to HTML'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Md to HTML'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Txt to HTML'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Epub to HTML'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Docx to Txt'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Epub to Txt'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'HTML to Txt'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Md to Txt'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Txt to PDF'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Txt to Epub'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Txt to HTML'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Txt to Md'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        color: 0, 0, 0 , 1
                                        background_color: (117/256, 52/256, 247/256, 1)
                                        on_release: self.choose()
                                        text: 'JPEG to PNG'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        color: 0, 0, 0 , 1
                                        background_color: (117/256, 52/256, 247/256, 1)
                                        on_release: self.choose()
                                        text: 'PNG to JPEG'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        color: 0, 0, 0, 1
                                        background_color: (117/256, 52/256, 247/256, 1)
                                        on_release: self.choose()
                                        text: 'JPG to PNG'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        color: 0, 0, 0 , 1
                                        background_color: (0, 153/256, 159/256, 1)
                                        on_release: self.choose()
                                        text: 'PNG to JPG'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        color: 0, 0, 0 , 1
                                        background_color: (0, 153/256, 159/256, 1)
                                        on_release: self.choose()
                                        text: 'JPG to JPEG'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        color: 0, 0, 0 , 1
                                        background_color: (0, 153/256, 159/256, 1)
                                        on_release: self.choose()
                                        text: 'JPEG to JPG'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Gif to Mp4'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Mp4 to Gif'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Mp3 to Wav'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Wav to Mp3'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Mp4 to Wav'
                                        size_hint_x: None
                                        width: 250

                                    FileChoose:
                                        background_color: (0, 153/256, 159/256, 1)
                                        color: 0, 0, 0 , 1
                                        on_release: self.choose()
                                        text: 'Mp4 to Mp3'
                                        size_hint_x: None
                                        width: 250

                                GridLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: self.minimum_height
                                    row_default_height: 60
                                    cols: 1
                                    spacing: 10 


                                    TextInput:
                                        size_hint_x: None
                                        width: 250
                                        id: result
                                        text: ''
                                        hint_text: 'dont type here shiva'


                                    Button:
                                        size_hint_x: None
                                        width: 250
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
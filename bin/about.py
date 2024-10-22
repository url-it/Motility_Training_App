from ipywidgets import Output
from IPython.display import display, HTML
import os
class AboutTab(object):

    def __init__(self):
        # self.tab = Output(layout={'height': '600px'})
        self.tab = Output(layout={'height': 'auto'})
        # Change
        # self.tab.append_display_data(HTML(filename='../Motility_Training_App/doc/about.html'))
        # Another change
        # For some reason the path is not working online so we need to use the os module to get the path
        base_path = os.path.dirname(os.path.abspath(__file__))
        about_html_path = os.path.abspath(os.path.join(base_path, '../doc/about.html'))
        self.tab.append_display_data(HTML(filename=about_html_path))
        

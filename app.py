import time
from threading import Thread

from mss import mss

from tkinter import Tk, Label, Button, BOTH, Text, END
from tkinter.font import Font


class App:
    """
    Application main class.
    """
    params = {
        'title': 'PyTimerScreenshotApp v0.1A',
        'geometry': '325x140+700+400',
        'resizable': False
    }

    background_styles = {
        'bg': '#282828',
        'fg': '#FFFFFF',
        'font family': 'Segoe UI',
        'font weight': 'bold',
        'font size': 14
    }

    fields_styles = {
        'bg': '#202020',
        'fg': '#FFFFFF',
        'font family': 'Segoe UI',
        'font weight': 'normal',
        'font size': 12
    }

    def __init__(self):
        self.root = Tk()
        self.root.title(
            self.params['title']
        )
        self.root.geometry(
            self.params['geometry']
        )
        self.root.resizable(
            width=self.params['resizable'],
            height=self.params['resizable']
        )
        self.root.config(
            bg=self.background_styles['bg']
        )
        self.root.attributes("-alpha", 0.8)

        # setup widgets for window
        self.widgets = {

            'target_time_label': Label(
                text='Таймер ММ:СС',
                bg=self.background_styles['bg'],
                fg=self.background_styles['fg'],
                font=Font(
                    family=self.background_styles['font family'],
                    size=self.background_styles['font size'],
                    weight=self.background_styles['font weight']
                )
            ),

            'target_time': Text(
                height='1',
                bg=self.fields_styles['bg'],
                fg=self.fields_styles['fg'],
                font=Font(
                    family=self.fields_styles['font family'],
                    size=self.fields_styles['font size'],
                    weight=self.fields_styles['font weight']
                )
            ),

            'start button': Button(
                text='Поехали!',
                bg=self.fields_styles['bg'],
                fg=self.fields_styles['fg'],
                font=Font(
                    family=self.fields_styles['font family'],
                    size=self.fields_styles['font size'],
                    weight=self.fields_styles['font weight']),
                command=lambda: Thread(daemon=True, target=self.wait_for_screenshot).start()
            ),

            'author label': Label(
                text='pavlenko.aa1@dns-shop.ru',
                bg=self.background_styles['bg'],
                fg=self.background_styles['fg'],
                font=Font(
                    family=self.background_styles['font family'],
                    size=9,
                    weight=self.background_styles['font weight']
                )
            )

        }

        """
        Widgets placing at window
        """

        # make a greed
        for widget in self.widgets:
            self.widgets[widget].pack(padx=3, pady=3, fill=BOTH)

    def wait_for_screenshot(self):
        self.widgets['start button'].config(state='disabled')
        target_time_str = self.widgets['target_time'].get(1.0, END)
        target_times = target_time_str.split(':')
        minutes = int(target_times[0])
        seconds = int(target_times[1])
        seconds += minutes * 60
        time.sleep(seconds)

        with mss() as sct:
            print(sct.shot())

    def run(self) -> None:
        """
        Run GUI application.
        :return: None
        """
        self.root.mainloop()


App().run()

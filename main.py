#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Spectrum: The Open Source Autism Screening Tool

In this app, users will use supervised learning
to diagnose Autistic Spectrum Disorder (ASD)
based on behavioral features and individual
characteristics through a Keras neural network
and TensorFlow backend.

Author: Alexander A. Laurence
Last modified: January 2019
Website: www.alexanderlaurence.co.uk
"""

import ttk
from Tkinter import *
from ttk import *

from screenTest import *

import logging
import threading

class TextHandler(logging.Handler):
    """This class allows you to log to a Tkinter Text or ScrolledText widget"""
    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

class Autoresized_Notebook(Notebook):
  def __init__(self, master=None, **kw):

    Notebook.__init__(self, master, **kw)
    self.bind("<<NotebookTabChanged>>", self._on_tab_changed)

  def _on_tab_changed(self,event):
    event.widget.update_idletasks()

    tab = event.widget.nametowidget(event.widget.select())
    event.widget.configure(height=tab.winfo_reqheight())

if __name__== "__main__":
    from Tkinter import Frame, Tk
    root = Tk()
    root.resizable(width=False, height=False)
    root.title("Spectrum (2019.1): The Autism Screening Tool")

    # Create main menu bar
    menu_bar = Menu(root)

    # Create the submenu (tearoff is if menu can pop out)
    file_menu = Menu(menu_bar, tearoff=0)

    # Add commands to submenu
    file_menu.add_command(label="Quit!", command=root.destroy)
    file_menu.add_command(label="Exit!", command=root.destroy)
    file_menu.add_command(label="End!", command=root.destroy)

    # Add the "File" drop down sub-menu in the main menu bar
    menu_bar.add_cascade(label="File", menu=file_menu)

    notebook = Autoresized_Notebook(root)

    tab_control = ttk.Notebook(root)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    notebook.add(tab1, text="New")
    notebook.add(tab2, text="Load")

    a1 = StringVar()
    a2 = StringVar()
    a3 = StringVar()
    a4 = StringVar()
    a5 = StringVar()
    a6 = StringVar()
    a7 = StringVar()
    a8 = StringVar()
    a9 = StringVar()
    a10 = StringVar()
    age = StringVar()
    gen = StringVar()
    eth = StringVar()
    jau = StringVar()
    pdd = StringVar()
    res = StringVar()
    app = StringVar()
    score = StringVar()
    age_group = StringVar()
    rel = StringVar()
    asd = StringVar()

    report = StringVar(root, value="")

    radpadx, radpady = 0, 0
    labpadx = 20
    fieldpadx = 0


    def clicked():
        print(a1.get())


    """""
    TAB 1
    """""

    lbl1 = Label(tab1, text='')
    lbl1.grid(column=0, row=0)

    a1_text = Label(tab1, text='Question 1:')
    a1_text.grid(column=0, row=1, padx=(labpadx, 0))
    a1_1 = Radiobutton(tab1, text='0', value=0, variable=a1, command=clicked)
    a1_2 = Radiobutton(tab1, text='1', value=1, variable=a1, command=clicked)
    a1_1.grid(column=1, row=1)
    a1_2.grid(column=2, row=1)

    a2_text = Label(tab1, text='Question 2:')
    a2_text.grid(column=0, row=2, padx=(labpadx, 0))
    a2_1 = Radiobutton(tab1, text='0', value=0, variable=a2, command=clicked)
    a2_2 = Radiobutton(tab1, text='1', value=1, variable=a2, command=clicked)
    a2_1.grid(column=1, row=2)
    a2_2.grid(column=2, row=2)

    a3_text = Label(tab1, text='Question 3:')
    a3_text.grid(column=0, row=3, padx=(labpadx, 0))
    a3_1 = Radiobutton(tab1, text='0', value=0, variable=a3, command=clicked)
    a3_2 = Radiobutton(tab1, text='1', value=1, variable=a3, command=clicked)
    a3_1.grid(column=1, row=3, padx=(radpadx, 0))
    a3_2.grid(column=2, row=3, padx=(radpady, 0))

    a4_text = Label(tab1, text='Question 4:')
    a4_text.grid(column=0, row=4, padx=(labpadx, 0))
    a4_1 = Radiobutton(tab1, text='0', value=0, variable=a4, command=clicked)
    a4_2 = Radiobutton(tab1, text='1', value=1, variable=a4, command=clicked)
    a4_1.grid(column=1, row=4, padx=(radpadx, 0))
    a4_2.grid(column=2, row=4, padx=(radpady, 0))

    a5_text = Label(tab1, text='Question 5:')
    a5_text.grid(column=0, row=5, padx=(labpadx, 0))
    a5_1 = Radiobutton(tab1, text='0', value=0, variable=a5, command=clicked)
    a5_2 = Radiobutton(tab1, text='1', value=1, variable=a5, command=clicked)
    a5_1.grid(column=1, row=5, padx=(radpadx, 0))
    a5_2.grid(column=2, row=5, padx=(radpady, 0))

    a6_text = Label(tab1, text='Question 6:')
    a6_text.grid(column=0, row=6, padx=(labpadx, 0))
    a6_1 = Radiobutton(tab1, text='0', value=0, variable=a6, command=clicked)
    a6_2 = Radiobutton(tab1, text='1', value=1, variable=a6, command=clicked)
    a6_1.grid(column=1, row=6, padx=(radpadx, 0))
    a6_2.grid(column=2, row=6, padx=(radpady, 0))

    a7_text = Label(tab1, text='Question 7:')
    a7_text.grid(column=0, row=7, padx=(labpadx, 0))
    a7_1 = Radiobutton(tab1, text='0', value=0, variable=a7, command=clicked)
    a7_2 = Radiobutton(tab1, text='1', value=1, variable=a7, command=clicked)
    a7_1.grid(column=1, row=7, padx=(radpadx, 0))
    a7_2.grid(column=2, row=7, padx=(radpady, 0))

    a8_text = Label(tab1, text='Question 8:')
    a8_text.grid(column=0, row=8, padx=(labpadx, 0))
    a8_1 = Radiobutton(tab1, text='0', value=0, variable=a8, command=clicked)
    a8_2 = Radiobutton(tab1, text='1', value=1, variable=a8, command=clicked)
    a8_1.grid(column=1, row=8, padx=(radpadx, 0))
    a8_2.grid(column=2, row=8, padx=(radpady, 0))

    a9_text = Label(tab1, text='Question 9:')
    a9_text.grid(column=0, row=9, padx=(labpadx, 0))
    a9_1 = Radiobutton(tab1, text='0', value=0, variable=a9, command=clicked)
    a9_2 = Radiobutton(tab1, text='1', value=1, variable=a9, command=clicked)
    a9_1.grid(column=1, row=9, padx=(radpadx, 0))
    a9_2.grid(column=2, row=9, padx=(radpady, 0))

    a10_text = Label(tab1, text='Question 10:')
    a10_text.grid(column=0, row=10, padx=(labpadx, 0))
    a10_1 = Radiobutton(tab1, text='0', value=0, variable=a10, command=clicked)
    a10_2 = Radiobutton(tab1, text='1', value=1, variable=a10, command=clicked)
    a10_1.grid(column=1, row=10, padx=(radpadx, 0))
    a10_2.grid(column=2, row=10, padx=(radpady, 0))

    age_text = Label(tab1, text='Age:')
    age_text.grid(column=0, row=11, padx=(labpadx, 0))
    age_txt = Entry(tab1, width=16, textvariable=age)
    age_txt.grid(column=1, row=11, columnspan=2)

    gender_text = Label(tab1, text='Gender:')
    gender_text.grid(column=0, row=12, padx=(labpadx, 0))
    gender_combo = Combobox(tab1, width=15, textvariable=gen)
    gender_combo['values'] = ("", "m", "f")
    gender_combo.current(0)  # set the selected item
    gender_combo.grid(column=1, row=12, columnspan=2)

    ethnicity_text = Label(tab1, text='Ethnicity:')
    ethnicity_text.grid(column=0, row=13, padx=(labpadx, 0))
    ethnicity_combo = Combobox(tab1, width=15, textvariable=eth)
    ethnicity_combo['values'] = ('Asian',
                                'Black',
                                'Hispanic',
                                'Latino',
                                'Middle Eastern',
                                'Others',
                                'Pasifika',
                                'South Asian',
                                'Turkish',
                                'White-European')
    ethnicity_combo.current(0)  # set the selected item
    ethnicity_combo.grid(column=1, row=13, columnspan=2)

    jaundice_text = Label(tab1, text='Born With Jaundice?')
    jaundice_text.grid(column=0, row=14, padx=(labpadx, 0))
    jaundice_combo = Combobox(tab1, width=15, textvariable=jau)
    jaundice_combo['values'] = ('no', 'yes')
    jaundice_combo.current(0)  # set the selected item
    jaundice_combo.grid(column=1, row=14, columnspan=2)

    autism_text = Label(tab1, text='Family Member With PDD?')
    autism_text.grid(column=0, row=15, padx=(labpadx, 0))
    autism_combo = Combobox(tab1, width=15, textvariable=pdd)
    autism_combo['values'] = ('no', 'yes')
    autism_combo.current(0)  # set the selected item
    autism_combo.grid(column=1, row=15, columnspan=2)

    country_of_res_text = Label(tab1, text='Country of Residence:')
    country_of_res_text.grid(column=0, row=16, padx=(labpadx, 0))
    country_of_res_combo = Combobox(tab1, width=15, textvariable=res)
    country_of_res_combo['values'] = ('Afghanistan',
                                     'Argentina',
                                     'Armenia',
                                     'Australia',
                                     'Austria',
                                     'Bahrain',
                                     'Bangladesh',
                                     'Bhutan',
                                     'Brazil',
                                     'Bulgaria',
                                     'Canada',
                                     'China',
                                     'Costa Rica',
                                     'Egypt',
                                     'Europe',
                                     'Georgia',
                                     'Germany',
                                     'Ghana',
                                     'India',
                                     'Iraq',
                                     'Ireland',
                                     'Isle of Man',
                                     'Italy',
                                     'Japan',
                                     'Jordan',
                                     'Kuwait',
                                     'Latvia',
                                     'Lebanon',
                                     'Libya',
                                     'Malaysia',
                                     'Malta',
                                     'Mexico',
                                     'Nepal',
                                     'Netherlands',
                                     'New Zealand',
                                     'Nigeria',
                                     'Oman',
                                     'Pakistan',
                                     'Philippines',
                                     'Qatar',
                                     'Romania',
                                     'Russia',
                                     'Saudi Arabia',
                                     'South Africa',
                                     'South Korea',
                                     'Sweden',
                                     'Syria',
                                     'Turkey',
                                     'U.S. Outlying Islands',
                                     'United Arab Emirates',
                                     'United Kingdom',
                                     'United States')
    country_of_res_combo.current(0)  # set the selected item
    country_of_res_combo.grid(column=1, row=16, columnspan=2)

    used_app_before_text = Label(tab1, text='Used App Before?')
    used_app_before_text.grid(column=0, row=17, padx=(labpadx, 0))
    used_app_before_combo = Combobox(tab1, width=15, textvariable=app)
    used_app_before_combo['values'] = ('no', 'yes')
    used_app_before_combo.current(0)  # set the selected item
    used_app_before_combo.grid(column=1, row=17, columnspan=2)

    result_text = Label(tab1, text='Screening Score:')
    result_text.grid(column=0, row=18, padx=(labpadx, 0))
    result_entry = Entry(tab1, width=16, textvariable=score)
    result_entry.grid(column=1, row=18, columnspan=2)

    age_desc_text = Label(tab1, text='Age Description:')
    age_desc_text.grid(column=0, row=19, padx=(labpadx, 0))
    age_desc_combo = Combobox(tab1, width=15, textvariable=age_group)
    v = StringVar(root, value="4-11 years")
    age_group = v
    result_entry = Entry(tab1, width=16, textvariable=age_group, state='disabled')
    result_entry.grid(column=1, row=19, columnspan=2)

    relation_text = Label(tab1, text='Who Completed Test:')
    relation_text.grid(column=0, row=20, padx=(labpadx, 0))
    relation_combo = Combobox(tab1, width=15, textvariable=rel)
    relation_combo['values'] = ('Health care professional','Parent','Relative','Self')
    relation_combo.current(0)  # set the selected item
    relation_combo.grid(column=1, row=20, columnspan=2)

    class_text = Label(tab1, text='Class/ASD:')
    class_text.grid(column=0, row=21, padx=(labpadx, 0))
    class_combo = Combobox(tab1, width=15, textvariable=asd)
    class_combo['values'] = ('NO', 'YES')
    class_combo.current(0)  # set the selected item
    class_combo.grid(column=1, row=21, columnspan=2)

    whitespace2 = Label(tab1, text='test')
    whitespace2.grid(column=1, row=22, columnspan=2)

    #Fill in the rows of the temp csv file
    def newtest():
        #clear contents
        open('temp.csv', 'w').close()
        #now add in data
        with open("temp.csv", "a") as f:
            f.write('A1_Score' +','+
                    'A2_Score' + ','+
                    'A3_Score' + ','+
                    'A4_Score' + ','+
                    'A5_Score' + ','+
                    'A6_Score' + ','+
                    'A7_Score' + ','+
                    'A8_Score' + ',' +
                    'A9_Score' + ',' +
                    'A10_Score'+ ',' +
                    'age' + ',' +
                    'gender' ',' +
                    'ethnicity' + ',' +
                    'jundice' + ',' +
                    'austim' + ',' +
                    'contry_of_res' + ',' +
                    'used_app_before' + ',' +
                    'result' + ',' +
                    'age_desc' + ',' +
                    'relation' + ',' +
                    'class'
                    "\n" +
                    str(a1.get()) + "," +
                    str(a2.get()) + "," +
                    str(a3.get()) + "," +
                    str(a4.get()) + "," +
                    str(a5.get()) + "," +
                    str(a6.get()) + "," +
                    str(a7.get()) + "," +
                    str(a8.get()) + "," +
                    str(a9.get()) + "," +
                    str(a10.get()) + "," +
                    str(age.get()) + "," +
                    str(gen.get()) + "," +
                    str(eth.get()) + "," +
                    str(jau.get()) + "," +
                    str(pdd.get()) + "," +
                    str(res.get()) + "," +
                    str(app.get()) + "," +
                    str(score.get()) + "," +
                    str(age_group.get()) + "," +
                    str(rel.get()) + "," +
                    str(asd.get())
                    )
        #Run the screening test
        run()
        #switch to report view
        notebook.select(tab2)

        import tkMessageBox
        tkMessageBox.showinfo('Screening Test Complete!', 'Please review the results.')

        try:
            from cStringIO import StringIO  # Python 2
        except ImportError:
            from io import StringIO

        log_stream = StringIO()
        logging.basicConfig(stream=log_stream, level=logging.INFO)

        logging.warn('hello world')

        # Log some messages
        logger.warn(log_stream.getvalue())

    btn1 = Button(tab1,  width=15, text="Screening Test", command=newtest)
    btn1.grid(column=1, row=22, columnspan=2)

    btn2 = Button(tab1, width=15, text="Reset")
    btn2.grid(column=1, row=23, columnspan=2)

    """""
    TAB 2
    """""

    btn3 = Button(tab2, width=15, text="Browse")
    btn3.grid(column=0, row=0)
    path_entry = Entry(tab2, width=16, textvariable=score)
    path_entry.grid(column=1, row=0, columnspan=2)

    import ScrolledText

    # Create a ScrolledText widget
    #st = ScrolledText.ScrolledText(tab2, width=50, height=600, state='disabled')
    #st.configure(font='TkFixedFont')
    #st.grid(column=0, row=1)
    #st.pack()

    # Create textLogger
    #text_handler = TextHandler(st)

    # Add the handler to logger
    #logger = logging.getLogger()
    #logger.addHandler(text_handler)


    def center_window(width=300, height=200):
        # get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    center_window(425, 645)
    root.config(menu=menu_bar)
    notebook.pack()
    root.mainloop()
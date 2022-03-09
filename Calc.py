import tkinter as tk
from tkinter import Menu, FALSE
import datetime
import sys
import os
import platform
from Calcul import Calcul
from copy import deepcopy
from functools import partial
from json import load as json_load
from json import dump as json_dump


Timing = datetime.datetime.now()

class Calc(object):
 

    def __init__(self, root):
        self.root = root
        self.calc = Calcul()

        self.settings = self._load_settings()

        if platform.system() == 'Darwin':
            self.theme = self._get_theme('Default Theme For MacOS')
        else:
            self.theme = self._get_theme(self.settings['current_theme'])

        self.root.title('Calculator')  #Title Window
        self.root.iconphoto(False, tk.PhotoImage(file='assets/Logo1.png')) #Window Logo
        self.root.maxsize(width=335, height=415)
        self.root.minsize(width=335, height=415)
        self.root.geometry('-150+100')
        self.root['bg'] = self.theme['root_bg']

       
        self._frame_input = tk.Frame(self.root, bg=self.theme['frame_bg'], pady=4)
        self._frame_input.pack()

        self._frame_buttons = tk.Frame(self.root, bg=self.theme['frame_bg'], padx=2)
        self._frame_buttons.pack()

 
        self._create_input(self._frame_input)
        self._create_buttons(self._frame_buttons)
        self._create_menu(self.root)

    @staticmethod
    def _load_settings():
        with open('settings/settings.json', mode='r', encoding='utf-8') as f:
            settings = json_load(f)
        
        return settings

    def _get_theme(self, name='Dark'):
      

        list_of_themes = self.settings['themes']

        found_theme = None
        for t in list_of_themes:
            if name == t['name']:
                found_theme = deepcopy(t)
                break
        
        return found_theme
        
    def _create_input(self, root):
        self._entrada = tk.Entry(root, cnf=self.theme['INPUT'])
        self._entrada.insert(0,0)
        self._entrada.pack()

    def _create_menu(self, root):
        self.root.option_add('*tearOff', FALSE)
        calc_menu = Menu(self.root)

        self.root.config(menu=calc_menu)

        config = Menu(calc_menu)
        theme = Menu(config)


        theme_incompatible = ['Default Theme For MacOS']
        for t in self.settings['themes']:

            name = t['name']
            if name in theme_incompatible: 
                continue
            else:
                theme.add_command(label=name, command=partial(self._change_theme_to, name))
        try:
            calc_menu.add_cascade(label='Settings', menu=config)

        finally:
            Log = open("LogReport/log.txt", 'a+')
            Log.write(
                f"\n Timing :{'Day : ' + str(Timing.day), 'Month : ' + str(Timing.month)}\t {'Hour : ' + str(Timing.hour), 'Min : ' + str(Timing.minute), 'Sec : ' + str(Timing.second)}\t : Calcualator Settings clicked...")
            Log.close()


        try:

            config.add_cascade(label='Change Theme', menu=theme)

        finally:

            Log = open("LogReport/log.txt", 'a+')
            Log.write(
                f"\n Timing :{'Day : ' + str(Timing.day), 'Month : ' + str(Timing.month)}\t {'Hour : ' + str(Timing.hour), 'Min : ' + str(Timing.minute), 'Sec : ' + str(Timing.second)}\t : Calcualator change theme clicked...")
            Log.close()



        config.add_separator()
        try:
            config.add_command(label='Exit', command=self._exit)

        finally:
              pass

    def _change_theme_to(self, name='Dark'):
        self.settings['current_theme'] = name

        with open('settings/settings.json', 'w+') as outfile:
            json_dump(self.settings, outfile, indent=4)

        self.reload()
        
    def _create_buttons(self, root):
    

        self.theme['BTN_NUMERICO'].update(self.settings['global'])

        self._BTN_NUM_0 = tk.Button(root, text=0, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_1 = tk.Button(root, text=1, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_2 = tk.Button(root, text=2, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_3 = tk.Button(root, text=3, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_4 = tk.Button(root, text=4, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_5 = tk.Button(root, text=5, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_6 = tk.Button(root, text=6, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_7 = tk.Button(root, text=7, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_8 = tk.Button(root, text=8, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_9 = tk.Button(root, text=9, cnf=self.theme['BTN_NUMERICO'])

      
        self.theme['BTN_OPERADOR'].update(self.settings['global'])

        self._BTN_SOMA = tk.Button(root, text='+', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_SUB = tk.Button(root, text='-', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_DIV = tk.Button(root, text='/', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_MULT = tk.Button(root, text='*', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_EXP = tk.Button(root, text='^', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_RAIZ = tk.Button(root, text='√', cnf=self.theme['BTN_OPERADOR'])

        self.theme['BTN_DEFAULT'].update(self.settings['global'])
        self.theme['BTN_CLEAR'].update(self.settings['global'])

      
        self._BTN_ABRE_PARENTESE = tk.Button(root, text='(', cnf=self.theme['BTN_DEFAULT'])
        self._BTN_FECHA_PARENTESE = tk.Button(root, text=')', cnf=self.theme['BTN_DEFAULT'])
        self._BTN_CLEAR = tk.Button(root, text='C', cnf=self.theme['BTN_DEFAULT'])
        self._BTN_DEL = tk.Button(root, text='<', cnf=self.theme['BTN_CLEAR'])
        self._BTN_RESULT = tk.Button(root, text='=', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_DOT = tk.Button(root, text='.', cnf=self.theme['BTN_DEFAULT'])

        self._BTN_VAZIO1 = tk.Button(root, text='', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_VAZIO2 = tk.Button(root, text='', cnf=self.theme['BTN_OPERADOR'])


        self._BTN_CLEAR.grid(row=0, column=0, padx=1, pady=1)
        self._BTN_ABRE_PARENTESE.grid(row=0, column=1, padx=1, pady=1)
        self._BTN_FECHA_PARENTESE.grid(row=0, column=2, padx=1, pady=1)
        self._BTN_DEL.grid(row=0, column=3, padx=1, pady=1)


        self._BTN_NUM_7.grid(row=1, column=0, padx=1, pady=1)
        self._BTN_NUM_8.grid(row=1, column=1, padx=1, pady=1)
        self._BTN_NUM_9.grid(row=1, column=2, padx=1, pady=1)
        self._BTN_MULT.grid(row=1, column=3, padx=1, pady=1)


        self._BTN_NUM_4.grid(row=2, column=0, padx=1, pady=1)
        self._BTN_NUM_5.grid(row=2, column=1, padx=1, pady=1)
        self._BTN_NUM_6.grid(row=2, column=2, padx=1, pady=1)
        self._BTN_SUB.grid(row=2, column=3, padx=1, pady=1)


        self._BTN_NUM_1.grid(row=3, column=0, padx=1, pady=1)
        self._BTN_NUM_2.grid(row=3, column=1, padx=1, pady=1)
        self._BTN_NUM_3.grid(row=3, column=2, padx=1, pady=1)
        self._BTN_SOMA.grid(row=3, column=3, padx=1, pady=1)


        self._BTN_DOT.grid(row=4, column=0, padx=1, pady=1)
        self._BTN_NUM_0.grid(row=4, column=1, padx=1, pady=1)
        self._BTN_RESULT.grid(row=4, column=2, padx=1, pady=1)
        self._BTN_DIV.grid(row=4, column=3, padx=1, pady=1)


        self._BTN_VAZIO1.grid(row=5, column=0, padx=1, pady=1)
        self._BTN_VAZIO2.grid(row=5, column=1, padx=1, pady=1)
        self._BTN_EXP.grid(row=5, column=2, padx=1, pady=1)
        self._BTN_RAIZ.grid(row=5, column=3, padx=1, pady=1)


        self._BTN_NUM_0['command'] = partial(self.input_values, 0)
        self._BTN_NUM_1['command'] = partial(self.input_values, 1)
        self._BTN_NUM_2['command'] = partial(self.input_values, 2)
        self._BTN_NUM_3['command'] = partial(self.input_values, 3)
        self._BTN_NUM_4['command'] = partial(self.input_values, 4)
        self._BTN_NUM_5['command'] = partial(self.input_values, 5)
        self._BTN_NUM_6['command'] = partial(self.input_values, 6)
        self._BTN_NUM_7['command'] = partial(self.input_values, 7)
        self._BTN_NUM_8['command'] = partial(self.input_values, 8)
        self._BTN_NUM_9['command'] = partial(self.input_values, 9)


        self._BTN_SOMA['command'] = partial(self._set_operator_in_input, '+')
        self._BTN_SUB['command'] = partial(self._set_operator_in_input, '-')
        self._BTN_MULT['command'] = partial(self._set_operator_in_input, '*')
        self._BTN_DIV['command'] = partial(self._set_operator_in_input, '/')
        self._BTN_EXP['command'] = partial(self._set_operator_in_input, '**')
        self._BTN_RAIZ['command'] = partial(self._set_operator_in_input, '**(1/2)')



        self._BTN_DOT['command'] = partial(self._set_dot_in_input, '.')
        self._BTN_ABRE_PARENTESE['command'] = self._set_open_parent
        self._BTN_FECHA_PARENTESE['command'] = self._set_close_parent
        self._BTN_DEL['command'] = self.input_del
        self._BTN_CLEAR['command'] = self._clear_input
        self._BTN_RESULT['command'] = self.input_data

    def input_values(self, value):

        if self._entrada.get() == 'Err':
            self._entrada.delete(0, len(self._entrada.get()))

        if self._entrada.get() == '0':
            self._entrada.delete(0)
            self._entrada.insert(0 ,value)
        elif self._lenght_max(self._entrada.get()):
            self._entrada.insert(len(self._entrada.get()) ,value)
    
    def _set_dot_in_input(self, dot):

        if self._entrada.get() == 'Err':
            return 

        if self._entrada.get()[-1] not in '.+-/*' and self._lenght_max(self._entrada.get()):
            self._entrada.insert(len(self._entrada.get()) ,dot)

    def _set_open_parent(self):

        if self._entrada.get() == 'Err':
            return 

        if self._entrada.get() == '0':
            self._entrada.delete(0)
            self._entrada.insert(len(self._entrada.get()), '(')
        elif self._entrada.get()[-1] in '+-/*' and self._lenght_max(self._entrada.get()):
            self._entrada.insert(len(self._entrada.get()), '(')
    
    def _set_close_parent(self):

        if self._entrada.get() == 'Err':
            return

        if self._entrada.get().count('(') <= self._entrada.get().count(')'):
            return
        if self._entrada.get()[-1] not in '+-/*(' and self._lenght_max(self._entrada.get()):
            self._entrada.insert(len(self._entrada.get()), ')')

    def _clear_input(self):
      try:
            self._entrada.delete(0, len(self._entrada.get()))
            self._entrada.insert(0,0)

      finally:
          Log = open("LogReport/log.txt", 'a+')
          Log.write(
              f"\n Timing :{'Day : ' + str(Timing.day), 'Month : ' + str(Timing.month)}\t {'Hour : ' + str(Timing.hour), 'Min : ' + str(Timing.minute), 'Sec : ' + str(Timing.second)}\t : Calcualator input were cleared...")
          Log.close()
    def input_del(self):

        if self._entrada.get() == 'Err':
            return

        if len(self._entrada.get()) == 1:
            self._entrada.delete(0)
            self._entrada.insert(0,0)
        else:
            self._entrada.delete(len(self._entrada.get()) - 1)
    
    def _set_operator_in_input(self, operator):

        if self._entrada.get() == 'Err':
            return

        if self._entrada.get() == '':

            return

        if self._entrada.get()[-1] not in '+-*/' and self._lenght_max(self._entrada.get()):
            self._entrada.insert(len(self._entrada.get()) ,operator)
            
    def input_data(self):

        if self._entrada.get() == 'Err':
            return

        result = self.calc.Cal(self._entrada.get())
        self.input_result(result=result)

    def input_result(self, result=0):

        if self._entrada.get() == 'Err':
            return

        self._entrada.delete(0, len(self._entrada.get()))
        self._entrada.insert(0, result)

    def _lenght_max(self, data_in_input):
        if len(str(data_in_input)) >= 15:
            return False
        return True
            
    def start(self):
        try:
           self.root.mainloop()
        finally:
            Log = open("LogReport/log.txt", 'a+')
            Log.write( f"\n Timing :{'Day : ' + str(Timing.day), 'Month : ' + str(Timing.month)}\t {'Hour : ' + str(Timing.hour), 'Min : ' + str(Timing.minute), 'Sec : ' + str(Timing.second)}\t : Calcualator Successfully Started...")
            Log.close()

    def reload(self):

        python = sys.executable
        os.execl(python, python, * sys.argv)

    def _exit(self):
        try:
           exit()
        finally:
                Log = open("LogReport/log.txt", 'a+')
                Log.write(
                    f"\n Timing :{'Day : ' + str(Timing.day), 'Month : ' + str(Timing.month)}\t {'Hour : ' + str(Timing.hour), 'Min : ' + str(Timing.minute), 'Sec : ' + str(Timing.second)}\t : Calcualator Successfully Exited...")
                Log.close()


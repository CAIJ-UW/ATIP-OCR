""" File: OCR-GUI.py
Author: Kevin Dick
Date: 2020-05-18
---
Description: Simple GUI wrapper for the conversion script
to ease usage on those unfamiliar with the command line.
"""
import PySimpleGUI as sg
import os, sys

sg.LOOK_AND_FEEL_TABLE['CAIJ-UW-Theme'] = {'BACKGROUND': '#eeeeee',
                                           'TEXT': '#000000',
                                           'INPUT': '#ffffff',
                                           'TEXT_INPUT': '#000000',
					   'SCROLL': '#cccccc',
                                           'BUTTON': ('white', '#e41128'),
					   'PROGRESS': ('#01826B', '#D0D0D0'),
                                           'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                           }
sg.theme('CAIJ-UW-Theme')

layout = [[sg.Text('Enter Scanned PDF File to Convert & Folder to Save Results')],
          [sg.Text('PDF to Convert'), sg.Input(), sg.FileBrowse()],
	  [sg.Text('Results Folder'), sg.Input(key='-USER FOLDER-'), sg.FolderBrowse(target='-USER FOLDER-')],
          [sg.Submit(), sg.Exit()],
	  [sg.Text('Alexander Luscombe, Kevin Dick, Jamie Duncan, Kevin Walby')],
	  [sg.Text('Centre for Access to Information and Justice, University of Winnipeg')]
	 ]

window = sg.Window('Scanned PDF to TXT', layout)

event, values = window.read()
if event in  (None, 'Exit') or event == 'Quit': sys.exit(0)
print(event,values)
print(values.keys()) 

# Involk the OCR conversion script!
cmd = f'python3 OCR-converter.py -i {values["Browse"]} -o {values["Browse0"]}'
print(f'Running {cmd}')
sg.popup(f'Beginning the conversion...')
os.system(cmd)
sg.popup(f'Conversion Complete.\nExiting now.')

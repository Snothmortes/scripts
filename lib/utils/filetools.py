"""
Imports:
    - os:           For file path manipulations and file operations.
    - tempfile:     For temporary file generation
    - atexit:       For file cleanup
    - commentjson:  For parsing and processing JSON content if applicable.
    - tkinter:      For creating a graphical user interface (GUI) for file browsing 
                    and user interaction.
    - filedialog:   For system-specific parameters and functions.
"""

import os
import re
import tempfile
import atexit
import commentjson
import tkinter as tk

from tkinter import filedialog, messagebox

from lib.pyhelpers.pytools import clear_history_folder

JSON_PATH = 'C:/Users/glenj/OneDrive/Codebase/ByLanguage/Python/AddHeaderSlashes/res'

JSON_EMPTY_ERROR = "Empty file. No modification."
JSON_INVALID_ERROR = "Error: Invalid JSON content in the file:"
JSON_SEL_ABORTED = "File selection aborted."

GENERAL_ERROR = "An error occured:"

SAVE_PROMPT_TITLE = "Save or Discard Changes"
SAVE_PROMPT_QUESTION = "Do you want to save the modifications?"

SAVE_SUCCESS_MSG = 'Modifications successfull.'
SAVE_ABORTED_MSG = 'Aborted'


def cleanup():
    temp_file.close()
    os.remove(temp_file.name)
    clear_history_folder()


def main():
    global temp_file, json_file

    os.system('cls')

    temp_file = tempfile.NamedTemporaryFile(
        mode='w+t', delete=False, encoding='utf-8')

    atexit.register(cleanup)

    browse_for_json_file()

    verify_json()

    lines = read_json_by_lines()
    lines = [re.sub(r" +\n", "\n", line) for line in lines]

    for n, line in enumerate(lines):
        if not '//' in line or re.search(r'\w+', line): # JSON line
            max_length = 0
            continue
        elif not '\u2588' in line: # FULL BLOCK comment border
            lines[n] = "{}{}\n".format(
                line[:4],
                (120 - len(line)) * '/'
            )
        else: # FULL BLOCK comment line
            max_length = max(len(line) for line in lines[n:n+5]) \
                if max_length == 0 \
                else max_length
            lines[n] = "{}{}{}{}  //\n".format(
                line[:4],
                (120 - len(line) - (max_length - len(line)) - 4) * '/',
                line[4:-1],
                (max_length - len(line)) * ' '
            )

        # modify_lines = [line +
        #                 (max_length - len(line) + 2) * ' ' + 2 * '/'
        #                 if '\u2588' in line else line for line in modify_lines]

    temp_file.seek(0)

    with open('./res/settings.3.json', 'w', encoding='utf-8') as file:
        file.writelines(lines)

    # open_temp_file(temp_file.name)

    # prompt_save_discard(temp_file.name, json_file)


def browse_for_json_file():
    global temp_file, json_file
    root = tk.Tk()
    root.withdraw()
    json_file = filedialog.askopenfilename(
        initialdir=JSON_PATH,
        initialfile="settings.2.json",
        filetypes=[(
            "JSON files with comments",
            "*.json")
        ]
    )
    root.destroy()

    if not json_file:
        print(JSON_SEL_ABORTED)
        os._exit(1)


def verify_json():
    global json_file
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            file_content = file.read()
            try:
                commentjson.loads(file_content)
            except ValueError as e:
                print(JSON_INVALID_ERROR, str(e))
                exit
        pass
    except Exception as e:
        print(JSON_SEL_ABORTED + ': ' + f'{e}.')
        os._exit(1)


def read_json_by_lines():
    global json_file
    with open(json_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def modify_line(line):
    return line + '/' * (120 - len(line)) + '\n'


def open_temp_file(file_path):
    global json_file
    modal_window = tk.Tk()
    modal_window.title("Preview: " + str.split(json_file, '/')[-1])

    with open(file_path, 'r', 'utf-8') as file:
        file_contents = file.read()

    text_widget = tk.Text(modal_window,
                          width=(modal_window.winfo_screenwidth() // 2) // 8,
                          height=modal_window.winfo_screenheight() // 20,
                          wrap="none")
    text_widget.insert('1.0', file_contents)

    vertical_scrollbar = tk.Scrollbar(modal_window, command=text_widget.yview)
    text_widget.config(yscrollcommand=vertical_scrollbar.set)

    horizontal_scrollbar = tk.Scrollbar(
        modal_window, orient="horizontal", command=text_widget.xview)
    text_widget.config(xscrollcommand=horizontal_scrollbar.set)

    vertical_scrollbar.pack(side="right", fill="y")
    horizontal_scrollbar.pack(side="bottom", fill="x")
    text_widget.pack(side="left", fill="both", expand=True)

    modal_window.attributes("-topmost", True)
    modal_window.focus_set()
    modal_window.mainloop()


def prompt_save_discard(source_file, destination_file):
    if messagebox.askyesno(SAVE_PROMPT_TITLE, SAVE_PROMPT_QUESTION):
        print(SAVE_SUCCESS_MSG)
        try:
            with open(source_file, 'r', encoding='utf-8') as source:
                content = source.read()
                with open(destination_file, 'w', encoding='utf-8') as destination:
                    destination.write(content)
        except Exception as e:
            print(GENERAL_ERROR, str(e))
        # save file
    else:
        print(SAVE_ABORTED_MSG)


if __name__ == "__main__":
    main()

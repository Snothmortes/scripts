<h1>Table of contents</h1>

- [Add Header Slashes](#add-header-slashes)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage/Examples](#usageexamples)
  - [Dev. Progress](#dev-progress)

# Add Header Slashes
Fills in my section headers ASCII art with slashes

## Features

- Import jsonc file
- Preview changes
- Save or discard

## Installation

Install my-project with python

```bash
  python.exe -m build
  . "./.venv/Scripts/activate"
  python.exe -m pip install .
```
    
## Usage/Examples

```bash
  python.exe -m AddHeaderShashes
```

## Dev. Progress
<ol>
  <li style="margin-bottom: 15px">&#x2705; <b>Browse for File</b>: Prompt the user to select or enter the file path  containing the text to be manipulated.
  </li>
  <li style="margin-bottom: 15px">&#x2705; <b>Load File</b>: Using Python's file I/O capabilities, load the selected file   for reading and manipulation.
  </li>
  <li style="margin-bottom: 15px">&#x2705; <b>Verify File Load</b>: Confirm that the file has been successfully loaded  into the program.
  </li>
  <li style="margin-bottom: 15px">&#x2705; <b>Verify File Format</b>: Check that the file format and extension adhere to  the expected .jsonc format and extension. This step is primarily for   validation purposes.
  </li>
  <li style="margin-bottom: 15px">&#x2705; <b>Read Line</b>: Read the content of the file line by line, considering the   file's size and memory constraints.
  </li>
  <li style="margin-bottom: 15px">&#x2705; <b>Match Line with Comment</b>: Utilize the "re" module to match each line   with the desired comment pattern using regular expressions.
  </li>
  <li style="margin-bottom: 15px">&#x2705; <b>Modify Line</b>: If a matching line is found, apply the necessary   modifications, such as adding a number of '/' to the line for visual  purposes.
  </li>
  <li style="margin-bottom: 15px">&#x2705; <b>Repeat Matching and Modification</b>: Iterate through each line of the file   to continue identifying and modifying the lines matched with the  comment pattern until the end of the file is reached.
  </li>
  <li style="margin-bottom: 15px"><b>Show Preview</b>: Display a preview of the modified content on the screen   to provide visual feedback.
  </li>
  <li style="margin-bottom: 15px"><b>Prompt Save or Discard</b>: Prompt the user with the option to "Save File"  or "Discard Changes" based on the preview, allowing choices to persist   the changes or revert to the original.
  </li>
  <li><b>Restart or Exit</b>: Provide an option to either restart the process from the file browsing step or exit the program.
  </li>
</ol>
#!/bin/bash


# Get a list of directories
cd /home/ibrahim/git-projects
directories=$(ls -d ./*)

# Create an array of menu options
options=()
for dir in $directories; do
    options+=("$dir" "")
done

# Use dialog to display the menu and store the selected directory
selected=$(dialog --clear --title "Directory Menu" --menu "Select a directory:" 0 0 0 "${options[@]}" 2>&1 >/dev/tty)


if [ -z $selected ]; then 
       exit 
fi       

# Launch VS Code
code -n $selected


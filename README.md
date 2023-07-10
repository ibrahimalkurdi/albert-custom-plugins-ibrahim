# albert-custom-plugins-ibrahim

This is an Albert plugin, which will add new TODO item to a todo list in a specific file by execute shell script.
The TODO file is managed by TODO visual studio code plugin, it works for me on Ubuntu 22.04 LTS.

## Prerequisites:

1- Albert installation

2- Visual Studio Code installation

3- Install todo-plus plugin in Visual Studio Code https://github.com/fabiospampinato/vscode-todo-plus

4- Create a new file called **my-schedule-tasks.todo** in a specific location on your machine and add this line in the top of it:
```
my-albert-tasks:
```

5- Update the `automated_todo_list.sh` script with the `my-schedule-tasks.todo` file path.

6- Copy the `scripts/automated_todo_list.sh` to specific location on your machine.

7- Update the `__init__.py` file in the plugins directory with the automated_todo_list.sh file path.

8- Enable albert custom plugins in albert config:
```
cp albert.conf /home/<user>/.config/albert.conf
```


## Installation:

1- Copy the todo directory to this path on your machine `/usr/share/albert/python/plugins/`
```
cp -r plugins/todo /usr/share/albert/python/plugins/
```

2- Restart Albert

# Add Custom Keyboard shortcut:

Install this package:
```
sudo apt install xdotool
```
Then:
Add Keyboard shortcuts as defined in this file: **keyboard-shortcut.md**

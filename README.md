# albert-todo-list-plugin

This is an Albert plugin, which will add new TODO item to a todo list in a specific file by execute shell script.
The TODO file is managed by TODO visual studio code plugin, it works for me on Ubuntu 22.04 LTS.

## Prerequisites:

1- Install Visual Studio Code

2- Install TODO list plugin https://github.com/fabiospampinato/vscode-todo-plus

3- Create new file called **automated-tasks.todo** in a specific location on your machine.

4- Update the automated_todo_list.sh script with the automated-tasks.todo file path.

5- Copy the automated_todo_list.sh to specific location on your machine.

6- Update the `__init__.py` file in the plugins directory with the automated_todo_list.sh file path.

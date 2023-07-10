#!/bin/bash

my_todo_list_file="/home/<user>/Documents/<usere>-workspace/Visual-Studio-code/my-schedule-tasks.todo"
current_date="$(date +%d/%m/%Y)"
ensure_date_existence=$(grep ${current_date} ${my_todo_list_file} | wc -l)

if [[ ! -z $@ ]]; then
  if [[ ${ensure_date_existence} -eq 0 ]]; then
    echo -e "\n${current_date}:" >> ${my_todo_list_file}
    echo -e "    ☐ $@" >> ${my_todo_list_file}
  else
    echo -e "    ☐ $@" >> ${my_todo_list_file}
  fi
fi

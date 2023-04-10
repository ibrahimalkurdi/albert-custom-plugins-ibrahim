#!/bin/bash

if [[ ! -z $@ ]]; then
	echo -e "    ☐ $@" >> ~/automated-tasks.todo
fi

exit 1

# albert-custom-plugins-ibrahim

My custom [Albert](https://albertlauncher.github.io) plugins (Albert 35+, Python interface `md_iid 5.0`), tested on Ubuntu 26.04.

| Shortcut | Plugin | Does |
|---|---|---|
| `help ` | myshortcuts | Lists these shortcuts; Enter opens the chosen one |
| `mylist ` | mylist | Shows `my-schedule-tasks.todo` in a popup |
| `todo <task>` | todo | Adds a task to `my-schedule-tasks.todo` |
| `vsrepo ` | vsrepo | Picks a Git repo and opens it in VS Code |
| `prayer` | prayer | Opens https://alsakina.pages.dev |

## Install

1. Install Albert, `zenity`, VS Code and its [todo-plus](https://github.com/fabiospampinato/vscode-todo-plus) extension.
2. Copy the scripts and set your paths in them (`<user>` placeholders):
   ```
   mkdir -p ~/scripts && cp scripts/*.sh ~/scripts/
   ```
3. Create `my-schedule-tasks.todo` at the path used in `automated_todo_list.sh`, starting with the line `my-albert-tasks:`.
4. Copy the plugins to the user plugin dir (not `/usr/share/albert`, the package owns it):
   ```
   mkdir -p ~/.local/share/albert/python/plugins && cp -r plugins/* ~/.local/share/albert/python/plugins/
   ```
5. In Albert Settings > Plugins enable **Python plugins**, then each plugin above, or add to `~/.config/albert/config` while Albert is closed:
   ```
   [python]
   enabled=true

   [python.mylist]
   enabled=true
   ```
   (same for `python.myshortcuts`, `python.prayer`, `python.todo`, `python.vsrepo`)

Optional: hide the extra "Configuration: Enabled, State: Loaded" rows with
```
[pluginregistry]
global_handler_enabled=false
```

Keyboard shortcuts: see [keyboard-shortcut.md](keyboard-shortcut.md) (needs `sudo apt install xdotool`).

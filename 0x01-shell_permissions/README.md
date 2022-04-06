# Shell - permissions

Commands covered:
* `chmod`
* `sudo`
* `su`
* `chown`
* `chgrp`
* `id`
* `groups`
* `whoami`
* `adduser`
* `useradd`
* `addgroup`

## Learning Objectives:
### 1. Permissions
- What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can’t a normal user `chown` a file
- How to run a command with root privileges
- How to change user ID or become superuser

### 2. Other Man Pages
- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid

## Project Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l` file should print 2)
- All your files should end with a new line (why?)
- The first line of all your files should be exactly `#!/bin/bash`
- A `README.md` file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use backticks, `&&`, `||` or `;`
- All your files must be executable

## Project Tasks
### 0. My name is Betty
**Description:** Create a script that switches the current user to the user `betty`.
- You should use exactly 8 characters for your command (+1 character for the new line).
- You can assume that the user `betty` will exist when we will run your script.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `0-iam_betty` <br>

### 1. Who am I
**Description:** Write a script that prints the effective username of the current user.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `1-who_am_i` <br>

### 2. Groups
**Description:** Write a script that prints all the groups the current user is part of.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `2-groups` <br>

### 3. New owner
**Description:** Write a script that changes the owner of the file `hello` to the user `betty`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `3-new_owner` <br>

### 4. Empty!
**Description:** Write a script that creates an empty file called `hello`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `4-empty` <br>

### 5. Execute
**Description:** Write a script that adds execute permission to the owner of the file `hello`.
- The file `hello` will be in the working directory

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `5-execute` <br>

### 6. Multiple permissions
**Description:** Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.
- The file `hello` will be in the working directory

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `6-multiple_permissions` <br>

### 7. Everybody!
**Description:** Write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`
- The file `hello` will be in the working directory
- You are not allowed to use commas for this script

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `7-everybody` <br>

### 8. James Bond
**Description:** Write a script that sets the permission to the file `hello` as follows:
- Owner: no permission at all
- Group: no permission at all
- Other users: all the permissions

The file `hello` will be in the working directory You are not allowed to use commas for this script.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `8-James_Bond` <br>

### 9. John Doe
**Description:** Write a script that sets the mode of the file `hello` to this: <br>
```-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello```
- The file `hello` will be in the working directory
- You are not allowed to use commas for this script

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `9-John_Doe` <br>

### 10. Look in the mirror
**Description:** Write a script that sets the mode of the file `hello` the same as `olleh`’s mode.
- The file `hello` will be in the working directory
- The file `olleh` will be in the working directory

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `10-mirror_permissions` <br>

### 11. Directories
**Description:** Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `11-directories_permissions` <br>

### 12. More directories
**Description:** Create a script that creates a directory called `my_dir` with permissions 751 in the working directory.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `12-directory_permissions` <br>

### 13. Change group
**Description:** Write a script that changes the group owner to `school` for the file `hello`
- The file `hello` will be in the working directory

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `13-change_group` <br>

### 14. Owner and group (advanced task)
**Description:** Write a script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `100-change_owner_and_group` <br>

### 15. Symbolic links (advanced task)
**Description:** Write a script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively.
- The file `_hello` is in the working directory
- The file `_hello` is a symbolic link

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `101-symbolic_link_permissions` <br>

### 16. If only (advanced task)
**Description:** Write a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.
- The file `hello` will be in the working directory

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `102-if_only` <br>

### 17. Star Wars (advanced task)
**Description:** Write a script that will play the StarWars IV episode in the terminal.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x01-shell_permissions` <br>
File: `103-Star_Wars` <br>

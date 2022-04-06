# Shell - I/O Redirections & Filters

Commands covered:
* `echo`
* `cat`
* `head`
* `tail`
* `find`
* `wc`
* `sort`
* `uniq`
* `grep`
* `tr`
* `rev`
* `cut`
* `passwd (5)` (i.e. `man 5 passwd`)

## Learning Objectives:
### 1. Shell, I/O Redirection
- What do the commands `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, `tr` do
- How to redirect standard output to a file
- How to get standard input from a file instead of the keyboard
- How to send the output from one program to the input of another program
- How to combine commands and filters with redirections

### 2. Special Characters
- What are special characters
- Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them

### 3. Other Man Pages
- How to display a line of text
- How to concatenate files and print on the standard output
- How to reverse a string
- How to remove sections from each line of files
- What is the `/etc/passwd` file and what is its format
- What is the `/etc/shadow` file and what is its format

## Project Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l` file should print 2)
- All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
- The first line of all your files should be exactly `#!/bin/bash`
- A `README.md` file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use backticks, `&&`, `||` or `;`
- All your files must be executable
- You are not allowed to use `sed` or `awk`

### More Info
Read your `/etc/passwd` and `/etc/shadow` files.

**Note:** You do not have to learn about `fmt`, `pr`, `du`, `gzip`, `tar`, `lpr`, `sed` and `awk` yet.

## Project Tasks
### 0. Hello World
**Description:** Write a script that prints “Hello, World”, followed by a new line to the standard output.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `0-hello_world` <br>

### 1. Confused smiley
**Description:** Write a script that displays a confused smiley `"(Ôo)'`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `1-confused_smiley` <br>

### 2. Let's display a file
**Description:** Display the content of the `/etc/passwd` file.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `2-hellofile` <br>

### 3. What about 2?
**Description:** Display the content of `/etc/passwd` and `/etc/hosts`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `3-twofiles` <br>

### 4. Last lines of a file
**Description:** Display the last 10 lines of `/etc/passwd`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `4-lastlines` <br>

### 5. I'd prefer the first ones actually
**Description:** Display the first 10 lines of `/etc/passwd`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `5-firstlines` <br>

### 6. Line #2
**Description:** Write a script that displays the third line of the file `iacta`. The file iacta will be in the working directory
- You’re not allowed to use `sed`

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `6-third_line` <br>

### 7. It is a good file that cuts iron without making a noise
**Description:** Write a shell script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `7-file` <br>

### 8. Save current state of directory
**Description:** Write a script that writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `8-cwd_state` <br>

### 9. Duplicate last line
**Description:** Write a script that duplicates the last line of the file `iacta`.
- The file `iacta` will be in the working directory

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `9-duplicate_last_line` <br>

### 10. No more javascript
**Description:** Write a script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `10-no_more_js` <br>

### 11. Don't just count your directories, make your directories count
**Description:** Write a script that counts the number of directories and sub-directories in the current directory.
- The current and parent directories should not be taken into account
- Hidden directories should be counted

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `11-directories` <br>

### 12. What’s new
**Description:** Create a script that displays the 10 newest files in the current directory. <br>
Requirements:
- One file per line
- Sorted from the newest to the oldest

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `12-newest_files` <br>

### 13. Being unique is better than being perfect
**Description:** Create a script that takes a list of words as input and prints only words that appear exactly once.
- Input format: One line, one word
- Output format: One line, one word
- Words should be sorted

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `13-unique` <br>

### 14. It must be in that file
**Description:** Display lines containing the pattern “root” from the file `/etc/passwd`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `14-findthatword` <br>

### 15. Count that word
**Description:** Display the number of lines that contain the pattern “bin” in the file `/etc/passwd`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `15-countthatword` <br>

### 16. What's next?
**Description:** Display lines containing the pattern “root” and 3 lines after them in the file `/etc/passwd`.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `16-whatsnext` <br>

### 17. I hate bins
**Description:** Display all the lines in the file `/etc/passwd` that do not contain the pattern “bin”.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `17-hidethisword` <br>

### 18. Letters only please
**Description:** Display all lines of the file `/etc/ssh/sshd_config` starting with a letter.
- include capital letters as well

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `18-letteronly` <br>

### 19. A to Z
**Description:** Replace all characters `A` and `c` from input to `Z` and `e` respectively.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `19-AZ` <br>

### 20. Without C, you would live in hiago
**Description:** Create a script that removes all letters `c` and `C` from input.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `20-hiago` <br>

### 21. esreveR
**Description:** Write a script that reverse its input.

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `21-reverse` <br>

### 22. DJ Cut Killer
**Description:** Write a script that displays all users and their home directories, sorted by users.
- Based on the the `/etc/passwd` file

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `22-users_and_homes` <br>

### 23. Empty casks make the most noise (advanced task)
**Description:** Write a command that finds all empty files and directories in the current directory and all sub-directories.
- Only the names of the files and directories should be displayed (not the entire path)
- Hidden files should be listed
- One file name per line
- The listing should end with a new line
- You are not allowed to use basename, `grep`, `egrep`, `fgrep` or `rgrep`

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `100-empty_casks` <br>

### 24. A gif is worth ten thousand words (advanced task)
**Description:** Write a script that lists all the files with a `.gif` extension in the current directory and all its sub-directories.
- Hidden files should be listed
- Only regular files (not directories) should be listed
- The names of the files should be displayed without their extensions
- The files should be sorted by byte values, but case-insensitive (file `aaa` should be listed before file `bbb`, file `.b` should be listed before file `a`, and file `Rona` should be listed after file `jay`)
- One file name per line
- The listing should end with a new line
- You are not allowed to use `basename`, `grep`, `egrep`, `fgrep` or `rgrep`

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `101-gifs` <br>

### 25. Acrostic (advanced task)
**Description:** An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. <br>
Create a script that decodes acrostics that use the first letter of each line.
- The ‘decoded’ message has to end with a new line
- You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `102-acrostic` <br>

### 26. The biggest fan (advanced task)
**Description:** Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
- Order by number of requests, most active host or IP at the top
- You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`
Format:
```
host    When possible, the hostname making the request. Uses the IP address if the hostname was unavailable.
logname Unused, always -
time    In seconds, since 1970
method  HTTP method: GET, HEAD, or POST
url Requested path
response    HTTP response code
bytes   Number of bytes in the reply
```

GitHub repository: `alx-system_engineering-devops` <br>
Directory: `0x02-shell_redirections` <br>
File: `103-the_biggest_fan` <br>

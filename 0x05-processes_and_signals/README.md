# Shell - Processes and signals

Commands covered
* `ps`
* `pgrep`
* `pkill`
* `kill`
* `exit`
* `trap`

## Learning Objectives:
- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

## Project Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
* **GitHub repository:** `alx-system_engineering-devops`
* **Directory:** `0x05-processes_and_signals`

## Project Tasks
### 0. What is my PID
Write a Bash script that displays its own PID.

**File:** `0-what-is-my-pid`

### 1. List your processes
Write a Bash script that displays a list of currently running processes.
- Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
- Show process hierarchy

**File:** `1-list_your_processes`

### 2. Show your Bash PID
Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.
- You cannot use `pgrep`
- The third line of your script must be `# shellcheck disable=SC2009`

**File:** `2-show_your_bash_pid`

### 3. Show your Bash PID made easy
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.
- You cannot use `ps`

**File:** `3-show_your_bash_pid_made_easy`

### 4. To infinity and beyond
Write a Bash script that displays `To infinity and beyond` indefinitely.
- In between each iteration of the loop, add a `sleep 2`

**File:** `4-to_infinity_and_beyond`

### 5. Don't stop me now!
We stopped our `4-to_infinity_and_beyond` process using `ctrl+c` in the previous task, there is actually another way to do this.

Write a Bash script that stops `4-to_infinity_and_beyond` process.
- You must use `kill`

**File:** `5-dont_stop_me_now`

### 6. Stop me if you can
Write a Bash script that stops `4-to_infinity_and_beyond` process.
- You cannot use `kill` or `killall`

**File:** `6-stop_me_if_you_can`

### 7. Highlander
Write a Bash script that displays:
- `To infinity and beyond` indefinitely
- With a `sleep 2` in between each iteration
- `I am invincible!!!` when receiving a SIGTERM signal

Make a copy of your `6-stop_me_if_you_can` script, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.

**File:** `7-highlander`

### 8. Beheaded process
Write a Bash script that kills the process `7-highlander`.

**File:** `8-beheaded_process`

### 9. Process and PID file (advanced task)
Write a Bash script that:
- Creates the file `/var/run/myscript.pid` containing its PID
- Displays `To infinity and beyond` indefinitely
- Displays `I hate the kill command` when receiving a SIGTERM signal
- Displays `Y U no love me?!` when receiving a SIGINT signal
- Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

**File:** `100-process_and_pid_file`

### 10. Manage my process (advanced task)
Read:
- [&](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)
- [init.d](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)
- [Daemon](https://en.wikipedia.org/wiki/Daemon_%28computing%29)
- [Positional parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)

man: `sudo`

Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: `start`, `restart` and `stop`. The most popular way of doing so on Unix system is to use the init scripts.

Write a `manage_my_process` Bash script that:
- Indefinitely writes `I am alive!` to the file `/tmp/my_process`
- In between every `I am alive!` message, the program should pause for 2 seconds

Write Bash (init) script `101-manage_my_process` that manages `manage_my_process`. (both files need to be pushed to git)

Requirements:
- When passing the argument `start`:
  - Starts `manage_my_process`
  - Creates a file containing its PID in `/var/run/my_process.pid`
  - Displays `manage_my_process started`
- When passing the argument `stop`:
  - Stops `manage_my_process`
  - Deletes the file `/var/run/my_process.pid`
  - Displays `manage_my_process stopped`
- When passing the argument `restart`
  - Stops `manage_my_process`
  - Deletes the file `/var/run/my_process.pid`
  - Starts `manage_my_process`
  - Creates a file containing its PID in `/var/run/my_process.pid`
  - Displays `manage_my_process restarted`
- Displays `Usage: manage_my_process {start|stop|restart}` if any other argument or no argument is passed

Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing `./101-manage_my_process start`, in our case it will simply create a new process instead of saying that it is already started.

**File:** `101-manage_my_process`, `manage_my_process`

### 11. Zombie (advanced task)
Read what a [zombie process](https://zombieprocess.wordpress.com/what-is-a-zombie-process/) is.

Write a C program that creates 5 zombie processes.
- For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
- Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`
- When your code is done creating the parent process and the zombies, use the function below

```
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
```

**File:** `102-zombie.c`

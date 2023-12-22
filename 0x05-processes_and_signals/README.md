# 0x05. Processes and signals

This directory contains Bash scripts that demonstrate how to work with processes and signals in Linux.

## Learning objectives

- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the signals that cannot be ignored

## Files

- `0-what-is-my-pid`: Bash script that displays its own PID.
- `1-list_your_processes`: Bash script that displays a list of currently running processes.
  - Shows all processes, for all users, including those without a TTY.
  - Displays in a user-oriented format.
  - Shows process hierarchy.
- `2-show_your_bash_pid`: Bash script that displays lines containing the `bash` word, allowing you to easily get the PID of your Bash process.
  - Uses the `ps` command.
- `3-show_your_bash_pid_made_easy`: Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.
  - Uses the `pgrep` command.
- `4-to_infinity_and_beyond`: Bash script that displays `To infinity and beyond` indefinitely with a `sleep 2` in between each iteration.
- `5-kill_me_now`: Bash script that kills `4-to_infinity_and_beyond` process.
  - Uses the `kill` command.
- `6-kill_me_now_made_easy`: Bash script that kills `4-to_infinity_and_beyond` process.
  - Uses the `pkill` command.
- `7-highlander`: Bash script that displays `To infinity and beyond` indefinitely with a `sleep 2` in between each iteration.
  - Displays `I am invincible!!!` when receiving a `SIGTERM` signal.
- `8-beheaded_process`: Bash script that kills the process `7-highlander`.
  - Uses the `kill` command.

## Author

Saheed Kehinde Yuusuf <[Da4midable](^1^)>
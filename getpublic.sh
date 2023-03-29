tmux new-session -d -s GET-IP
tmux send-keys -t GET-IP "bash" C-m
tmux send-keys -t GET-IP "python3 /data/getIP-public-indihome/start.py" C-m

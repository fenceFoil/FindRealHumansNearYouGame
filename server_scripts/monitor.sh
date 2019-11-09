#!/bin/bash
source activate tensorflow_p36
pip install flask_apscheduler tqdm torch transformers
./stop_all.sh

read -r -d '' TMUX_CONFIG <<HEREDOC
################################################################################
##                              MOUSE CONFIGURATION                           ##
################################################################################

## ENABLE MOUSE
setw -g mouse on


## Mouse scroll
## If already in copy mode send mouse event x3
## else if program is capturing mouse, simulate mouse with up strokes
## else (in normal tmux) enter copy mode
bind-key -n WheelUpPane \
 if-shell -Ft= "#{?pane_in_mode,1,#{?mouse_button_flag}}" \
  "send-keys -Mt=; send-keys -Mt=; send-keys -Mt=" \
  "if-shell -Ft= '#{alternate_on}' \
   'send-keys -t= ^y ^y ^y' \
   'copy-mode -e -t='"
bind-key -n WheelDownPane \
 if-shell -Ft= "#{?pane_in_mode,1,#{?mouse_button_flag}}" \
  "send-keys -Mt=; send-keys -Mt=; send-keys -Mt=" \
  "send-keys -t= ^e ^e ^e"


## Create new window on right click on the status bar on any other window
unbind-key -n MouseDown3Status
bind-key -n MouseDown3Status new-window -a -t=


## Drag windows on the status bar
bind-key -n MouseDrag1Status swap-window -t=


## Drag panes (interchange them)
bind-key -n MouseDrag1Pane swap-pane -dt=


## Close pane with mouse wheel (when released)
bind-key -n MouseUp2Pane kill-pane -t=


## Close window whith wheel (released)
bind-key -n MouseUp2Status kill-window -t=


## Enable mouse with 'm' and disable with 'M'
unbind m
bind m \
 set -g mouse on \;\
 display 'Mouse: ON'
unbind M
bind M \
 set -g mouse off \;\
 display 'Mouse: OFF'
 
 
## ZOOM: toggle with right click on pane
unbind-key -n MouseDown3Pane
bind-key -n MouseDown3Pane  resize-pane -Z -t=
HEREDOC
echo $TMUX_CONFIG > ~/.tmux.conf 
tmux kill-server

SESSION=$USER
tmux -2 new-session -d -s $SESSION

# Setup a window for tailing log files
tmux new-window -t $SESSION:1 -n 'MONITOR'
tmux split-window -h
tmux select-pane -t 0
tmux send-keys "./start_gpt2_api.sh &" C-m
tmux select-pane -t 1
tmux send-keys "./start_flask_api.sh &" C-m
tmux split-window -v
tmux resize-pane -D 10
tmux send-keys "echo 'Welcome to FindRealHumansNearMe Monitor Script\n' && man tmux" C-m
# Setup a CoffeeScript compiler/watchdog pane
tmux select-pane -t 0
tmux split-window -v
tmux resize-pane -D 10
tmux send-keys "watch -n 1 netstat -plnt" C-m

# Setup a MySQL window
tmux new-window -t $SESSION:2 -n 'echo "Another Window"'

# Set default window
tmux select-window -t $SESSION:1

# Attach to session
tmux -2 attach-session -t $SESSION
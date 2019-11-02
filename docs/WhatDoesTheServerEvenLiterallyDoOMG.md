# What the server does

Every .1 seconds   
    switch on gamescheduler.currgamestate:
        PICKUP WRITING:
            if all pickup lines are in or StateTimeoutTime has passed:
                move to SWIPE TIME, 
                choose new StateTimeoutTime
        SWIPE TIME:
            if all players are finished swiping or StateTimeoutTime has passed:
                move to PICKUP WRITING, choose new StateTimeoutTime
                increment round number




## Screens
```plantuml
(Landing) --> (ProfileSetup): Click Start Game
(ProfileSetup) --> (PickupLine): Click submit
(PickupLine) -> (SwipeTime): Submit final pickup line OR pickup timeout detected
(SwipeTime) --> (RoundResults): Finish swiping OR Swipe time ending detected
(RoundResults) -> (PickupLine): Click next
(RoundResults) -> (SwipeTime): Pickup timeout detected

(RoundResults) -u-> (Landing): Click next at end of game
```

## PickupLine

```plantuml
:Enter prompt;
:Press submit;
:If implants > 0: Get choices back;
:Select choice;
```

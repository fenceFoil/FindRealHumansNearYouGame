# Phone Messages (REST API):

## Lobby 

(TODO: Lobby interactions and getting to that setup screen)

* POST RestartGame (From Master Robot)

## Game Starting

* POST Create Profile (From Phone)
    * Name
    RETURN
    * PlayerID

* GET Profile (From Phone)
    * PlayerID
    RETURN
    Your whole profile

## Pickup Time

* GET Generate Pickup Completions (From Phone)
    * HumanWords
    * NumScreedsNeeded
    * PlayerID
    RETURN
    * List of bot screed options

* POST Commit New Message (From Phone)
    * PlayerID
    * HumanWords
    * BotScreed

* GET MoveToSwipeTime (From Phone) // phone will poll this
    RETURNS
    * IsItTime

## Swipe Time!

* GET Prospects (From Phone)
  * List of players (the computer shuffled them):
    * Pickup Line
    * Name
    * WaifuImageURL

* POST Swipe (From Phone)
  * PlayerID
  * TargetID
  * Action (string: LEFT or RIGHT)

* POST FinishedSwiping (From Phone)
  * PlayerID

* GET ResultsTime (From Phone)  // phone will poll this
    RETURNS
    * IsItTime

## Results Time!

* GET RoundResults
  * RoundNum (int)
  * IsFinalResults (bool)
  * NumBotsDated (int)
  * NumHumansDated (int)
  * NewHearts (int)
  * NewImplants (int)
  * YouDated (list)
    * WaifuImageURL
    * Name
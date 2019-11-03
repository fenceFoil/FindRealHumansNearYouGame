# Stored Data

Profiles: // note creepy bots also get creepy profiles that are CCs of people cloned instantly after creepy game starts in a cyber vat
* PlayerID                  // unique. aboslutely unique.
* IsRobot (bool)
* Name (string)             // would be cloned
* WaifuImageURL (string)    // completely random
* Hearts (int)
* Implants (int)

PickupLines:
* PlayerID
* RoundNum
* HumanWords (string)
* BotScreed (string)

Likes
* SourcePlayerID
* DestPlayerID
* RoundNum
* Action (string: LEFT or RIGHT)

GameScheduler (just global variables)
* CurrGameState
* RoundNumber
* StateTimeoutTime
* GameOver (bool)

OPTIONAL PlayerHistory:
* Player
* MapOfHeartsByRoundNumber
* MapOfImplantsByRoundNumber
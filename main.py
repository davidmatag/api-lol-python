#!/usr/bin/env python3.6

import apiV4.summoner as sumV4
import apiV4.champMastery as chaMasV4
import apiV4.spectator as specV4
import apiV4.match as matV4
import apiV4.league as leaV4
import apiV3.champion as chaV3
import apiV3.lolStatus as staV3

#You must to have your own api key
apiKey = ""
#Region for the queries
reg = ""

summonerName = "example"
account = sumV4.sumByName(reg, summonerName, apiKey)
matV4.allMatch(reg, account["accountId"], apiKey)

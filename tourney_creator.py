import sys
import asyncio
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import aiohttp
import time
import random
import string

def generate_unique_name():
    """Generate a unique tournament name"""
    random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"Tournament_{random_suffix}"

def get_tournament_payload():
    min_players = int(input("Enter minimum number of players: "))
    players_per_table = int(input("Enter players per table: "))
    # Get current time in milliseconds
    current_time_ms = int(time.time() * 1000)

    # Registration time: current time + 1 minute
    registration_time = current_time_ms + (1 * 60 * 1000)

    # Tournament start time: current time + 3    minutes
    tournament_start_time = current_time_ms + (3 * 60 * 1000)

    return {
        "tournamentName": generate_unique_name(),
        "channelVariation": "Texas Hold’em",
        "tournamentType": "NORMAL",
        "isPotLimit": False,
        "chipsType": "Real Money",
        "isGuaranteed": False,
        "entryFees": 10,
        "houseFees": 0,
        "isBounty": False,
        "totalBuyIn": 100000,
        "turnTime": 15,
        "chips": 10000,
        "playerPerTable": players_per_table,
        "minPlayers": min_players,
        "maxPlayers": 200,
        "tournamentStartTime": tournament_start_time,
        "tournamentDuration": 1,
        "registrationStartTime": registration_time,
        "deRegisterTime": 1,
        "breakId": 5,
        "timeBank": 10,
        "registrationBufferTime": 0,
        "timeBankId": "TB-zqLoErzlun7ebMyN",
        "isLateRegistrationAllowed": False,
        "lateRegistrationTime": 15,
        "isRebuyAllowed": False,
        "numberOfRebuyAllowed": 0,
        "isAddOnAllow": False,
        "noOfAddOn": 0,
        "addOnTime": [],
        "isRecuring": False,
        "isPrivateTable": False,
        "tablePassword": "",
        "noOfRecuring": 1,
        "recuringData": [],
        "smallBlind": 100,
        "bigBlind": 200,
        "blindDuration": 1,
        "priceStructure": "Silver",
        "isRabbit": False,
        "maxEntries": 0,
        "anteStartLevel": 0,
        "breakDuration": 5,
        "rebuyTime": 5,
        "rebuyEndLevel": 1,
        "parentTournament": "",
        "tournamentCancelTime": 0
    }, registration_time, tournament_start_time


async def create_tournament():
    url = "https://staging.gamebadlo.com:3000/api/v1/tournament-management/create-tournament"
    payload, reg_time, start_time = get_tournament_payload()

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1YTRhMTE1MjI5YTIxMDkxNjA2MTQ5MzYiLCJuYW1lIjoiU3VwZXJBZG1pbiIsInVzZXJOYW1lIjoiTWFnbmV0QWRtaW4iLCJlbWFpbCI6ImFkbWluQHBva2VybWFnbmV0LmNvbSIsInJvbGUiOnsibmFtZSI6ImFkbWluIiwibGV2ZWwiOjd9LCJ1c2VyVHlwZSI6ImFkbWluIiwibW9iaWxlTnVtYmVyIjo4NDU5ODI0ODg1LCJsb2dJbkRhdGUiOjE3NDcwMzEzMjc2NzAsImlhdCI6MTc0NzAzMTMyNywiZXhwIjo0MzM5MDMxMzI3fQ.1Df9A-GEtc3BgyR7kLobYmy_dlzIOCdsvjhEOQgxvKI"
    }

    print(f"Creating tournament: {payload['tournamentName']}")
    print(f"Registration time: {time.ctime(reg_time / 1000)}")
    print(f"Tournament start time: {time.ctime(start_time / 1000)}")

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            status = response.status
            text = await response.text()
            if status in [200, 201]:
                print("Tournament created successfully!")
                print("Response:", text)
            else:
                print(f"Failed to create tournament. Status: {status}")
                print("Response:", text)

if __name__ == "__main__":
    asyncio.run(create_tournament())

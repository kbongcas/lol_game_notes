import Game
import Note
import requestHandler

def test(game , note):
    print(game)
    print(note)

game = Game.Game('yes','top', 'riven', '4/5/6', '200', '15000')
note = Note.Note(game, 'ya i did good')

test(game, note)

accountId = requestHandler.getAccountID('kevinismyname')
print('My account id is' + str(accountId))
gameId = requestHandler.getRecentGameID(accountId)
playerStats = requestHandler.getPlayerStats(gameId, accountId)
print(requestHandler.getGameStatsFormGame(playerStats, accountId, gameId))



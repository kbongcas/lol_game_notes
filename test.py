import Game
import Note
import requestHandler

def test(game , note):
    print(game)
    print(note)

game = Game.Game('yes','top', 'riven', '4/5/6', '200')
note = Note.Note(game, 'ya i did good')

test(game, note)

print(requestHandler.getRecentGameID(requestHandler.getSumID('kevinismyname')))



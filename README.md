# BeamNgChatIntegration
TikTok Interactive mod for BeamNgDrive. Actions in game are triggered by local webhooks (e.g. Tikfinity) 

Tutorial:
- You need pycharm community edition or something like this.
- Install dependencies (Flask and BeamNGpy).
- Input the correct game path in main.py:
game_path = r"D:\SteamLibrary\steamapps\common\BeamNG.drive"

- Before running api.py set launch=True
  bng.open(launch=True), and run api.py
- After everything is running and you spawned on a map inside a vehicle,
  run api.py setting launch=False before running api.py. (Everytime you change the vehicle you need to run api.py again, I will probably improve this in the future)
- When launch is set to True it's trying to start BeamNG the game.

Webhooks:
- http://127.0.0.1:5000/break
- http://127.0.0.1:5000/boost
- http://127.0.0.1:5000/kaputt
- http://127.0.0.1:5000/reset

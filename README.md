# BeamNgChatIntegration
TikTok Interactive mod for BeamNg. Actions in game are triggered by local webhooks (e.g. Tikfinity) 

Tutorial:
- You need pycharm community edition or something like this.
- Install dependencies (Flask and BeamNGpy).
- Input the correct game path in main.py:
game_path = r"D:\SteamLibrary\steamapps\common\BeamNG.drive"

- Run api.py with launch=True
  bng.open(launch=True)
- After everything is running and you spawned on a map inside a vehicle,
  run api.py again with launch=False.
- 


Webhooks:
http://127.0.0.1:5000/break
http://127.0.0.1:5000/boost
http://127.0.0.1:5000/kaputt
http://127.0.0.1:5000/reset

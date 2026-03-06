import time

from beamngpy import BeamNGpy, Vehicle, Scenario

game_path = r"D:\SteamLibrary\steamapps\common\BeamNG.drive"
bng = BeamNGpy('localhost', 64251, home=game_path)
player_car = None


def deflate_tires(vehicle: Vehicle):
    for i in range(4):
        vehicle.deflate_tire(i)
        # print(vehicle.get_part_options())


def spawn_vehicle(v: Vehicle):
    try:
        p_pos = v.get_center_of_gravity()
    except AttributeError:
        bbox = v.get_bbox()
        p_pos = bbox[list(bbox.keys())[0]]

    spawn_pos = (p_pos[0] + 10, p_pos[1], p_pos[2] + 0.5)
    print(f"Spawne NPC bei {spawn_pos}...")

    # DER FIX: Wir geben {autoEnterVehicle=false} als zweites Argument mit!
    lua_spawn_cmd = f"core_vehicles.spawnNewVehicle('sunburst2', {{autoEnterVehicle=false}}, vec3({spawn_pos[0]}, {spawn_pos[1]}, {spawn_pos[2]}), quat(0,0,0,1))"
    bng.queue_lua_command(lua_spawn_cmd)


def spawn_ramp_in_front(bng:BeamNGpy):
    lua_cmd = """
    local player = be:getPlayerVehicle(0)
    if player then
        local pos = player:getPosition()
        local dir = player:getDirectionVector()
        local rot = player:getRotation()
        local spawnPos = vec3(pos.x + (dir.x * 30), pos.y + (dir.y * 30), pos.z + 0.5)
        core_vehicles.spawnNewVehicle('metal_ramp', {autoEnterVehicle=false}, spawnPos, rot)
    end
    """

    # Jetzt macht das replace('\n', ' ') nichts mehr kaputt!
    bng.queue_lua_command(lua_cmd.replace('\n', ' '))

def breake_hinges(veh: Vehicle):
    veh.queue_lua_command("beamstate.breakHinges()")

def boost(veh: Vehicle, strength=20):
    n = 5
    for i in range(n):
        veh.queue_lua_command(f"""
            local vel = obj:getVelocity()
            local dir = obj:getDirectionVector()
            local currentSpeed = vel:dot(dir)
            thrusters.applyVelocity(dir * (currentSpeed + {float(strength/n)}))
        """)
        time.sleep(0.1)

# https://games.mathkuro.com/en/beamng/beamng-commands-2/#toc5
def parking_break(veh: Vehicle):
    veh.queue_lua_command('input.event("parkingbrake", 1, 1)')


def break_breakgroups(veh: Vehicle):
    veh.queue_lua_command("beamstate.breakAllBreakgroups(); beamstate.breakHinges()")
    # print(veh.get_part_config().keys())


def explode(veh: Vehicle):
    veh.queue_lua_command("fire.explodeVehicle()")
    break_breakgroups(veh)


def reset(veh: Vehicle, bng:BeamNGpy):
    bng.queue_lua_command("""
    for vid, veh in activeVehiclesIterator() do
  veh:requestReset()
  veh:resetBrokenFlexMesh()
end
    """)


def get_player_vehicle(bng: BeamNGpy):
    global player_car
    vehicles = bng.get_current_vehicles()
    if len(vehicles) > 0:
        player_id = 'thePlayer'
        player_car = vehicles[player_id]
        player_car.connect(bng)

    return player_car


if __name__ == '__main__':
    bng.open(launch=False)


# -*- coding: utf-8 -*-

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        #传入房间名，进入房间，获取value值。
        return self.paths.get(direction)
        # return self.paths.get(direction, None)#默认值是None，应该可以不写

    def add_paths(self, paths):
        #在paths字典中增加一组键值对
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
                        """The Gothons of Planet Percal #25 have invaded your ship ...

                        You're running down the ...""")

laser_weapon_armory = Room("Laser Weapon Armory",
                           """Lucky for you they mode you laren Gothon Gothon insults in hte academy.
                           ...
                           You do a dive roll into the Weapon Armory, ...""")

the_bridge = Room("The Birdge",
                  """
                  The container clicks open and the seal breaks, letting gas out.
                  ...
                  You brust onto the Bridge ...
                  """)

escape_pod = Room("Escape Pod",
              """
              You point your blaster at the bomb ...
              You rush through the ship...
              """)

the_end_winner = Room("The End",
                      """
                      You jump into pod 2 and ...

                      """)

the_end_loser = Room("The End",
                     """
                     You jump into a random pod and ...
                     """)

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '1032': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = central_corridor


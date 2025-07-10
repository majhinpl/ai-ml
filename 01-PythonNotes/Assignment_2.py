import time

def vacuum_agent(dirt_status, vacuum_position):

    # Continue cleaning until both rooms are clean


    while any(dirt_status):  # any() returns True if at least one room has dirt

        # Current room based on vacuum position
        current_room = "A" if vacuum_position[0] else "B"

        print(f"\nVacuum is in Room {current_room}")
        time.sleep(1)

        # Check if current room is dirty        
        room_index = 0 if current_room == "A" else 1

        if dirt_status[room_index]:
            print(f"Found dirt in Room {current_room}!")
            time.sleep(1)

            print(f"Cleaning Room {current_room}...")
            time.sleep(2)

            # Clean current room
            dirt_status[room_index] = False
            print(f"Room {current_room} is now clean!")
            time.sleep(1)

        else:
            print(f"No dirt found in Room {current_room}")
            time.sleep(1)
        
        # Move to the other room
        print(f"\nMoving to other room...")
        time.sleep(2)


        # Update vacuum position (switch rooms)
        vacuum_position[0] = not vacuum_position[0]  # Toggle Room A status
        vacuum_position[1] = not vacuum_position[1]  # Toggle Room B status

    # Final status
    print("\nBoth rooms are clean!")
    print("Mission complete!")

def main():
    # True means dirt is present, False means clean
    dirt_status = [True, True]  # [RoomA, RoomB]

    # True means vacuum is in that room (starting in Room B)
    vacuum_position = [False, True]  # [RoomA, RoomB]

    vacuum_agent(dirt_status, vacuum_position)


if __name__ == "__main__":
    main()
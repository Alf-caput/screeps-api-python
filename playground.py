###########################################
# Destroy structure
###########################################
# Replace this code's shard, structure_id and room_name variables with yours
# _id = 'room'
# room_name = 'E17S26'
# action = 'destroyStructure'
# shard = 'shard3'
# structure_id = '5beef69780a5196874bb6987'
# intent = [{'id': structure_id}]
# response = api.add_object_intent(_id=_id,
#                                 room=room_name,
#                                 intent=intent,
#                                 name=action,
#                                 shard=shard).json()
# print(json.dumps(response, indent=4))

###########################################
# Send console command
###########################################
# Replace this code's expression and shard variables with yours
# shard = 'shard3'
# expression = 'console.log("Hello world!")'
# response = api.console(expression=expression, 
#                        shard=shard).json()
# print(json.dumps(response, indent=4))

###########################################
# Retrieve objects in the room
###########################################
# room_name = 'E17S26'
# shard = 'shard3'
# response = api.room_objects(room=room_name, shard=shard).json()
# print(json.dumps(response, indent=4))
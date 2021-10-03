statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(the_online):
    numofkey = len(the_online)
    count_online = 0
    for key in the_online:
        if the_online[key] == "online":
          count_online += 1
    return count_online
    
online_count(statuses)
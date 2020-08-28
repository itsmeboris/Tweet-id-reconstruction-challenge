import datetime

def sequence_id(id):
    # Return the first 12 bits using a mask
    # the sequence id is composed of the first 12 bits
        return id & 0b111111111111

def machine_id(id): 
    # right bitshift 12 and apply an AND mask to get 10 rightmost bits
    # this is a combination of server id and datacenter id
    return (id >> 12) & 0b1111111111

def server_id(id):
    # right bitshift 12 and apply an AND mask to get the next 5 rightmost bits
    # the server id is composed of bits 13-17 (starting from the right)
    return (id >> 12) & 0b11111

def datacenter_id(id):
    # right bitshift 17 and apply an AND mask to get the next 5 rightmost bits
    # the datacenter id is composed of bits 18-22 (starting from the right)
    return (id >> 17) & 0b11111

def creation_time(id):
    # right bitshift 22 and apply Snowflake offset
    # the epoch time (in milliseconds) are the first 22 MSB bits (first 22 bits starting from the left)
    return ((id >> 22) + 1288834974657)

def tweet_components(tweet_id):
    tweet_id = int(tweet_id) # Convert to int if str is accidentally passed in
    c = {} # Components
    c['sequence_id'] = sequence_id(tweet_id)
    c['machine_id'] = machine_id(tweet_id)
    # c['server_id'] = server_id(tweet_id)
    # c['datacenter_id'] = datacenter_id(tweet_id)
    # c['creation_time_milli'] = creation_time(tweet_id)
    return(c['machine_id'], c['sequence_id'])

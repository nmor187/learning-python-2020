def parrot_trouble(talking, hour):
#if parrot is talking and hours after 20 or before 7 then we are in trouble
  if talking and hour > 20 or hour < 7:
    return True
#if anything else besides trouble then we are not in trouble
  else:
    return False
    

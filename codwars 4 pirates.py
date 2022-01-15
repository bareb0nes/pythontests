def cannons_ready(gunners):
    problem = 0
    for yell in gunners.values():
        if yell != "aye":
            problem += 1
    if problem >= 1:
        return "Shiver me timbers!"
    else:
        return "Fire!"
                     
  # Fire! or Shiver me timbers!

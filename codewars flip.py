def flip(d, a):
    # Do some magic
    cubes = a
    if d == "R":
        cubes.sort()
    if d == "L":
        cubes.sort(reverse=True)
    return cubes

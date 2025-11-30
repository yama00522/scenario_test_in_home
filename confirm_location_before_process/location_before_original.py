def analyze_location_before(
        pos_a,
        dir_a,
        lane_a,
        road_location_a, 
        pos_b,
        dir_b,
        lane_b,
        road_location_b) -> str:
    if dir_a == dir_b:
        if abs(lane_b - lane_a) == 1:
            return "adjacent_lane"
        elif lane_b == lane_a:
            return "same_lane"
        else:
            return "same_dir_but_not_same_or_adjacent_lane"
    elif pos_a == dir_b or dir_a == pos_b:
        return "opposite_lane"
    elif ((dir_a == 'N' and dir_b == 'E') or 
          (dir_a == 'N' and dir_b == 'W') or
          (dir_a == 'S' and dir_b == 'E') or
          (dir_a == 'S' and dir_b == 'W') or
          (dir_a == 'E' and dir_b == 'N') or
          (dir_a == 'E' and dir_b == 'S') or
          (dir_a == 'W' and dir_b == 'N') or
          (dir_a == 'W' and dir_b == 'S')):
        return "cross_street"
    else:
        return "unmatched_case"
    

print(analyze_location_before("N", "N", 1, "SINGLE", "N", 'N', 2, "SINGLE"))
print(analyze_location_before("S", "N", 3, "SINGLE", "S", 'N', 1, "SINGLE",))
print(analyze_location_before("S", "N", 3, "SINGLE", "W", 'E', 3, "SINGLE",))
print(analyze_location_before("S", "S", 5, "SINGLE", "S", 'S', 4, "SINGLE",))
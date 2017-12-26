#贪婪算法求集合覆盖问题
#找出覆盖全美50个州的最小广播台集合

#列表表示要覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut"])
#可供选择的广播台清单
stations = {}
stations["kone"] = set(["id","nv","ut"])#表示该广播电台包含的州
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])

#存储最终选择的广播台
final_stations = set()

while states_needed:
	#从中选择覆盖最多州的广播台
	best_station = None
	states_covered =  set()#该广播台覆盖的所有未覆盖州
	for station, states_for_station in stations.items():
		covered = states_needed & states_for_station
		if len(covered) > len(states_covered):
			best_station = station
			states_covered = covered

	states_needed -= states_covered
	final_stations.add(best_station)

print(final_stations)

#!/usr/bin/env python3
my_list = ["192.168.0.5", 5060, "UP"]
print("The fierst item in the list(IP): " + my_list[0])
print("The second item in the list is (port): " + str(my_list[1]))
print("The third item in the list is (state): " + my_list[2])

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

print("When I " + new_list[5] + " into IP address "  + new_list[3] +  " or "\
 +  new_list[4]  +  ", I am unable to ping ports " +  str(new_list[0]))
print("When I %s into IP addrdess %s or %s , I am unable to ping ports %s" % (new_list[5], new_list[3], new_list[4], str(new_list[0])))


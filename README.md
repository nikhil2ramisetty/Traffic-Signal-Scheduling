# Signaling Traffic Signals based on Traffic Density
Gave an algorithm to the traffic signals at a signal junction based on the number of vehicles in each direction. Thus, it favors the direction that has the highest traffic, considered that no direction should be waiting for much time or left out completely. The algorithm we proposed performed better than round robin scheduling and priority scheduling algorithms.

The Idea is that whenever a singal is supposed to be allocated to one of the directions, it captures the photos in each direction and measures the vehicles in each direction.
Implementation:
The time for each signal is given as 10 seconds. After every 10 seconds the photos, the photos from four directions are taken and their waiting times are calculated. Waiting time of a direction is that how long it has been waiting since it got green signal last time
Then a product starvation time/waiting time and vehicle count is calculated, and the direction which has the highest product will be given the green signal
Implemented using Tkinter GUI.

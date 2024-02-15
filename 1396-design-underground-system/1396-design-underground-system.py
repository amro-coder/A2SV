class UndergroundSystem:

    def __init__(self):
        self.start_station_for_id=[('',0)]*(10**6+1)    
        self.num_journeys=defaultdict(int)
        self.total_time=defaultdict(int)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start_station_for_id[id]=(stationName,t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station_Name,check_in_time=self.start_station_for_id[id]
        self.num_journeys[(start_station_Name,stationName)]+=1
        self.total_time[(start_station_Name,stationName)]+=t-check_in_time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.total_time[(startStation,endStation)]/self.num_journeys[(startStation,endStation)]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
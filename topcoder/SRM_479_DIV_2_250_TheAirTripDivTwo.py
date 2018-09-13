class TheAirTripDivTwo:
	def find(self, flights, fuel):
		maxFlights, totalFuel = 0, 0 
		for flight in list(flights):
			totalFuel += flight
			if totalFuel <= fuel:
				maxFlights += 1
			else:
				break
		return maxFlights


"""

C# CODE

public class TheAirTripDivTwo
{
	public int find(int[] flights, int fuel)
	{
		int m = 0;
		int t = 0;
		
		foreach(int flight in flights)
		{	
			t += flight;
			if(t <= fuel)
			{
				m++;
			}
			else
			{
				break;
			}
		}
		return m;
	}
}

"""		
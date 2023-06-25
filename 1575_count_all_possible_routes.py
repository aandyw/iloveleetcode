class Solution:
    mem = {}
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.mem = {}
        sol = self.solve_rec(locations, locations[start], locations[finish], fuel)
        return sol % (10**9 + 7)
        

    def solve_rec(self, locations: List[int], start_city: int, finish_city: int, fuel: int):
        count = 0
        if start_city == finish_city:
            count = 1

        if fuel <= 0:
            return count

        if (start_city, finish_city, fuel) in self.mem:
            return self.mem[(start_city, finish_city, fuel)]

        for loc in locations:
            # loc represents city i
            # check all surrounding cities
            if loc != start_city:
                f_usage = abs(loc - start_city)

                if fuel < f_usage:
                    continue

                count += self.solve_rec(locations, loc, finish_city, fuel - f_usage)
        
        self.mem[(start_city, finish_city, fuel)] = count

        return count
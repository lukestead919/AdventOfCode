from utils import read_data_file_as_lines

class FishPopulation:
    def __init__(self, fish_timers):
        pop = [0] * 9
        for fish_timer in fish_timers:
            pop[fish_timer] += 1
        self.pop = pop

    def generation(self):
        newpop = self.pop[1:] + self.pop[0:1]
        newpop[6] += self.pop[0]
        self.pop = newpop

    def total_pop(self):
        return sum(self.pop)


def run_pop_for_days(fish_timers: list[int], days: int):
    fish_pop = FishPopulation(fish_timers)
    for _ in range(days):
        fish_pop.generation()
    return fish_pop.total_pop()


data = read_data_file_as_lines(6)[0]
fish_timers = [int(s) for s in data.split(",")]

print("part 1", run_pop_for_days(fish_timers, 80))
print("part 2", run_pop_for_days(fish_timers, 256))


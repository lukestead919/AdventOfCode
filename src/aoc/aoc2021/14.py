from utils import read_data_file_as_lines
from collections import Counter


class PolymerFactory:
    def __init__(self, rules: dict):
        self.rules = rules

    def polymer_after_steps(self, template: str, num: int) -> str:
        polymer = template
        for _ in range(num):
            polymer = self.apply(polymer)
        return polymer

    def apply(self, polymer) -> str:
        pairs = [polymer[i: i+2] for i in range(len(polymer) - 1)]
        new_polymer = [''] * 2 * len(polymer)
        for i, pair in enumerate(pairs):
            new_polymer[2*i] = pair[0]
            new_polymer[2*i + 1] = self.rules.get(pair)
        new_polymer[-1] = polymer[-1]
        return ''.join(new_polymer)

    def elements_after_steps(self, template: str, num: int) -> Counter:
        pairs = [template[i: i+2] for i in range(len(template) - 1)]
        pair_count = PairCounts(Counter(pairs))
        for _ in range(num):
            pair_count = pair_count.get_next_pair_count(self.rules)
        return pair_count.get_element_counts(template)


class PairCounts:
    def __init__(self, counts: Counter):
        self.counts = counts

    def get_next_pair_count(self, rules: dict):
        new_pair_counts = Counter()
        for pair, count in self.counts.items():
            insert = rules.get(pair)
            new_pair_counts[pair[0] + insert] += count
            new_pair_counts[insert + pair[1]] += count
        return PairCounts(new_pair_counts)

    def get_element_counts(self, original_template: str) -> Counter:
        elements = Counter()
        for pair, count in self.counts.items():
            elements[pair[0]] += count
            elements[pair[1]] += count

        # every element except the first and last is counted twice in the pair counts
        # fortunately, the first and last elements never change
        elements.update((original_template[0], original_template[-1]))

        for element in elements.keys():
            elements[element] //= 2

        return elements


def part_a(template, polymer_factory):
    new_polymer = polymer_factory.polymer_after_steps(template, 10)
    element_counts = Counter(new_polymer).most_common()
    print("part 1", (element_counts[0][1] - element_counts[-1][1]))


def part_b(template, polymer_factory):
    elements = polymer_factory.elements_after_steps(template, 40)
    sorted_elements = elements.most_common()
    print("part 2", (sorted_elements[0][1] - sorted_elements[-1][1]))


def main():
    data = read_data_file_as_lines(14)
    template, rules = data[0], data[2:]
    rules = dict([(a, b) for a, b in [line.split(" -> ") for line in rules]])
    polymer_factory = PolymerFactory(rules)

    part_a(template, polymer_factory)
    part_b(template, polymer_factory)


main()

from utils import read_data_file_as_lines
from functools import reduce


def bin(str):
    return int(str, 2)


class Packet:
    def __init__(self, version: int, type: int, value: int, subpackets: list):
        self.version = version
        self.type = type
        self.value = value
        self.subpackets = subpackets

    def version_recursive(self):
        v = self.version
        for sub in self.subpackets:
            v += sub.version_recursive()
        return v

    def total_value(self):
        subpacket_values = [p.total_value() for p in self.subpackets]
        if self.type == 0:
            return reduce((lambda x, y: x + y), subpacket_values)
        elif self.type == 1:
            return reduce((lambda x, y: x * y), subpacket_values)
        elif self.type == 2:
            return min(subpacket_values)
        elif self.type == 3:
            return max(subpacket_values)
        elif self.type == 4:
            return self.value
        elif self.type == 5:
            return subpacket_values[0] > subpacket_values[1]
        elif self.type == 6:
            return subpacket_values[0] < subpacket_values[1]
        elif self.type == 7:
            return subpacket_values[0] == subpacket_values[1]


def parse_packets(data: str, to_parse: int=0) -> (list[Packet], str):
    packets = []
    s = data
    while len(s) > 0 and (len(packets) < to_parse or to_parse == 0) and bin(s) > 0:
        packet, s = parse_next_packet(s)
        packets.append(packet)
    return packets, s


def parse_next_packet(data: str) -> (Packet, str):
    version = bin(data[:3])
    type = bin(data[3:6])

    if type == 4:
        value_str = data[6:]
        num = ''

        while value_str[0] == '1':
            num += value_str[1:5]
            value_str = value_str[5:]
        num += value_str[1:5]
        value_str = value_str[5:]

        value = int(num, 2)
        return Packet(version, type, value, []), value_str
    else:
        len_type = data[6]
        subpackets = []
        remaining_str = ''
        if len_type == '0':
            bit_length = bin(data[7:22])
            subpackets, _ = parse_packets(data[22:22+bit_length])
            remaining_str = data[22+bit_length:]
        elif len_type == '1':
            subpacket_length = bin(data[7:18])
            subpackets, remaining_str = parse_packets(data[18:], subpacket_length)
        return Packet(version, type, 0, subpackets), remaining_str


def main():
    data = read_data_file_as_lines(16)[0]
    binary = f"{int(data,  16):b}"
    binary_length = len(binary)
    if binary_length % 4 > 0:
        binary = binary.zfill(binary_length + 4-(binary_length % 4))

    packets, _ = parse_packets(binary)
    packet = packets[0]
    print("part 1", packet.version_recursive())
    print("part 2", packet.total_value())


main()

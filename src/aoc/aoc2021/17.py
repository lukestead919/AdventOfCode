from utils import Point, read_data_file_as_lines, flatten

data = read_data_file_as_lines(17)[0]
target_x, target_y = data.replace("x=", "").replace("y=", "").replace(",", "").split(" ")[2:]
x_low, x_high = target_x.split("..")
y_low, y_high = target_y.split("..")

target_low = Point(int(x_low), int(y_low))
target_high = Point(int(x_high), int(y_high))


def definite_miss(p: Point, v: Point):
    return (p.x > target_high.x or p.y < target_low.y) \
         or (p.x < target_low.x and v.x == 0)


def hit_target(p: Point):
    return target_low.x <= p.x <= target_high.x and target_low.y <= p.y <= target_high.y


def sgn(i: int):
    if i == 0:
        return 0
    else:
        return i // abs(i)


class Trajectory:
    def __init__(self, velocity: Point):
        self.velocity = velocity

    def highest_point(self):
        current_pos = Point(0, 0)
        velocity = self.velocity
        points = []
        while not definite_miss(current_pos, velocity):
            points.append(current_pos)
            if hit_target(current_pos):
                return max(p.y for p in points)
            current_pos += velocity
            velocity = velocity + Point(-sgn(velocity.x), -1)
        return None


def main():
    velocities = flatten([[Point(i, j) for i in range(1, target_high.x + 1)] for j in range(target_low.y, abs(target_low.y))])
    highest_points = [Trajectory(v).highest_point() for v in velocities]
    print("part 1", max(h for h in highest_points if h is not None))
    print("part 2", len([h for h in highest_points if h is not None]))


main()

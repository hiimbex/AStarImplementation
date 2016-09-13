# Here is where our A Star Implementation should live :)
# Point Class code here:
class Point:
    xValue = 0
    yValue = 0
    def getCoord(self):
        return (xValue, yValue)

start = Point()
start.xValue = 0
start.yValue = 0

input = [start, end, barriers]
# Priority queues Open and Closed begin empty.
open = []
closed = []
start = (0,0)
# Put S into Open with priority f(s) = g(s) + h(s)
open.append(input.pop(0))
# Is Open empty?
while open.length != 0:
    for x in range(start.x - 1, start.x + 1):
        for y in range(start.y - 1, start.y + 1):
            if (x, y) ! in open:
                open.append((x,y))
    open.sort() # by f values
# Yes? No solution.
# No. Remove node with lowest f(n). Call it n.
    if open.pop() = input.end:
        # goal reached!
    else:
        closed.append(open.pop(0))
# If n is a goal, stop and report success (for pathfinding, return the path)
# Otherwise, expand n. For each n’ in successors(n)
# Let f’ = g(n’) + h(n’) = g(n) + cost (n, n’) + h(n’)
# If n’ not seen before or n’ previously expanded with f(n’) > f’ or n’ currently in Open with f(n’) > f’
# Then place or promote n’ on Open with priority f’
# Else ignore n’
# Place record for n in Closed

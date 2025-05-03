class CyclePathFindingStrategy():
    def findPath(self):
        print("finding path for cycles")

class CarPathFindingStrategy():
    def findPath(self):
        print("finding path for car")
    
class PathFinder:
    def findPath(self, strategy):
        print("finding path")
        strategy.findPath()


def main():
    pathFinder = PathFinder()
    pathFinder.findPath(CyclePathFindingStrategy())

main()
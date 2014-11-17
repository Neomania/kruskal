#-------------------------------------------------------------------------------
# Name:        Kruskal
# Purpose:     Simple visual demonstration of Kruskal's algorithm for finding a shortest path
#
# Author:      Neomania
#
# Created:     17/11/2014
# Copyright:   (c) Timothy 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import pygame, sys, os, random
    clock = pygame.time.Clock()
    pygame.init()
    FPS = 60
    DEVPINK = (255,0,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    YELLOW = (0,255,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    mainSurface = pygame.display.set_mode((1366,768))
    nodeCount = 50 #number of nodes - 1
    showPathFinding = False
    edgeThickness = 1
    finalEdgeThickness = 3
    unconnectedNodes = []
    connectedNodes = []
    edgeArray = []
    connectedEdgeArray = []
    shortestDistance = 0.0
    currentDistance = 0.0
    superShortestEdge = Edge

    #init
    for i in range(0,nodeCount):
        unconnectedNodes.append(Node(random.randint(1,1365),random.randint(1,768)))
        for eachnode in unconnectedNodes:
            pygame.draw.circle(mainSurface,WHITE,(eachnode.xPos,eachnode.yPos),5,0)
        pygame.display.update()
        clock.tick(FPS)
    #find starting point
    shortestDistance = 999999.0
    for i in range(0,nodeCount):
        for j in range(i + 1,nodeCount):
            mainSurface.fill(BLACK)
            if unconnectedNodes[i] == unconnectedNodes[j]:
                pass
            else:
                currentDistance = (((unconnectedNodes[i].xPos - unconnectedNodes[j].xPos) ** 2) + ((unconnectedNodes[i].yPos - unconnectedNodes[j].yPos) ** 2)) ** 0.5
                edgeArray.append(Edge(unconnectedNodes[i],unconnectedNodes[j]))
                if currentDistance < shortestDistance:
                    superShortestEdge = Edge(unconnectedNodes[i],unconnectedNodes[j])
                    shortestn1 = unconnectedNodes[i]
                    shortestn2 = unconnectedNodes[j]
                    shortestDistance = currentDistance
            for line in edgeArray:
                pygame.draw.line(mainSurface,BLUE,(line.xPos1,line.yPos1),(line.xPos2,line.yPos2),edgeThickness)
            pygame.draw.line(mainSurface,GREEN,(superShortestEdge.xPos1,superShortestEdge.yPos1),(superShortestEdge.xPos2,superShortestEdge.yPos2),edgeThickness)
            for eachnode in unconnectedNodes:
                pygame.draw.circle(mainSurface,WHITE,(eachnode.xPos,eachnode.yPos),5,0)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            clock.tick(FPS)
    clock.tick(1)
    edgeArray = []
    for i in range(0,nodeCount):
        for j in range(i + 1, nodeCount):
            edgeArray.append(Edge(unconnectedNodes[i],unconnectedNodes[j]))
    connectedNodes.append(shortestn1)
    connectedNodes.append(shortestn2)
    unconnectedNodes.remove(shortestn1)
    unconnectedNodes.remove(shortestn2)
    connectedEdgeArray.append(superShortestEdge)

    while len(unconnectedNodes) > 0:
        shortestDistance = 999999.0
        for startNode in connectedNodes:
            for endNode in unconnectedNodes:
                currentDistance = (((startNode.xPos - endNode.xPos) ** 2) + ((startNode.yPos - endNode.yPos) ** 2)) ** 0.5
                if currentDistance < shortestDistance:
                    shortestDistance = currentDistance
                    shortestn1 = startNode
                    shortestn2 = endNode
                for connectedEdge in connectedEdgeArray:
                    pygame.draw.line(mainSurface,GREEN,(connectedEdge.xPos1,connectedEdge.yPos1),(connectedEdge.xPos2,connectedEdge.yPos2),finalEdgeThickness)
                pygame.draw.line(mainSurface,DEVPINK,(startNode.xPos,startNode.yPos),(endNode.xPos,endNode.yPos),edgeThickness)
                for eachnode in unconnectedNodes:
                    pygame.draw.circle(mainSurface,WHITE,(eachnode.xPos,eachnode.yPos),5,0)
                for eachnode in connectedNodes:
                    pygame.draw.circle(mainSurface,WHITE,(eachnode.xPos,eachnode.yPos),5,0)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                if showPathFinding == True:
                    clock.tick(FPS)
        connectedEdgeArray.append(Edge(shortestn1,shortestn2))
        connectedNodes.append(shortestn2)
        unconnectedNodes.remove(shortestn2)
        mainSurface.fill(BLACK)
        for line in edgeArray:
            pygame.draw.line(mainSurface,BLUE,(line.xPos1,line.yPos1),(line.xPos2,line.yPos2),edgeThickness)
        for connectedEdge in connectedEdgeArray:
            pygame.draw.line(mainSurface,GREEN,(connectedEdge.xPos1,connectedEdge.yPos1),(connectedEdge.xPos2,connectedEdge.yPos2),finalEdgeThickness)
        for eachnode in unconnectedNodes:
            pygame.draw.circle(mainSurface,WHITE,(eachnode.xPos,eachnode.yPos),5,0)
        for eachnode in connectedNodes:
            pygame.draw.circle(mainSurface,WHITE,(eachnode.xPos,eachnode.yPos),5,0)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS)
    mainSurface.fill(BLACK)
    for line in edgeArray:
        pygame.draw.line(mainSurface,BLUE,(line.xPos1,line.yPos1),(line.xPos2,line.yPos2),edgeThickness)
    for connectedEdge in connectedEdgeArray:
        pygame.draw.line(mainSurface,GREEN,(connectedEdge.xPos1,connectedEdge.yPos1),(connectedEdge.xPos2,connectedEdge.yPos2),finalEdgeThickness)
    for eachnode in unconnectedNodes:
        pygame.draw.circle(mainSurface,WHITE,(eachnode.xPos,eachnode.yPos),5,0)
    for eachnode in connectedNodes:
        pygame.draw.circle(mainSurface,WHITE,(eachnode.xPos,eachnode.yPos),5,0)
    pygame.display.update()
    while True: #final loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(5)
class Node():
    import random
    xPos = 0
    yPos = 0
    def __init__(self,xPos,yPos):
        self.xPos = xPos
        self.yPos = yPos
class Edge():
    xPos1 = 0
    xPos2 = 0
    yPos1 = 0
    yPos2 = 0
    def __init__(self,node1,node2):
        self.xPos1 = node1.xPos
        self.yPos1 = node1.yPos
        self.xPos2 = node2.xPos
        self.yPos2 = node2.yPos

if __name__ == '__main__':
    from pygame.locals import *
    main()

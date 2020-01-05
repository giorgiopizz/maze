# Maze
What's a maze? Well for this project a maze is just a bunch of streets that connect the start point with the end point, each street being delimited by walls. The complexity, namely the number of turns and walls can be modified. 
The project is made mainly of two files: the maze generator and the maze solver. Obviously what the first does is to create a maze, the way it does it is with a backtracking algorithm, which means that we begin with a matrix, i.e. the map of the maze, full of walls, with no street in it. The job of the algorithm is to create streets leaving the walls in order not to have adjacent streets. 
The solver is pretty dumb. If he finds a free block on his right, he goes to the right, otherwise, if he can go forward he will go forward, otherwise left, finally, if the only possible move is to go back he will go back. He uses this method for each block e moves to, all the way to the endpoint.
To let us see what is the path of the solution the solver draws some little grey dot on the streets, meaning he passed there at some point. 
# Car Logger
This project aims to track cars that drive past a camera and collect their details

Each frame will be analysed to find all the cars, their images will then be passed to another NN which identifies the cars number plate. Then the image, numberplate and tiemstamp are saved to disk.

This data really needs further processing to be used, a good way would be to iterate through the data and create a new output of when a car first enters the frame and leaves (which can then be presented as time of arival, depature and in frame)

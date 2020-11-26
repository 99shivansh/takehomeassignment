<h1>Parking Lot Software</h1>

<h2>Problem Statement</h2>
We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.

When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket issuing process includes:- 
1. We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.
2. And we are allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are kind enough to always park in the slots allocated to them).

The customer should be allocated a parking slot that is nearest to the entry. At the exit, the customer returns the ticket, marking the slot they were using as being available.
Due to government regulation, the system should provide us with the ability to find out:-
- Vehicle Registration numbers for all cars which are parked by the driver of a certain age,
- Slot number in which a car with a given vehicle registration plate is parked.
- Slot numbers of all slots where cars of drivers of a particular age are parked.

We interact with the system via a file-based input system, i.e. it should accept a filename as an input. The file referenced by filename will contain a set of commands separated by a newline, we need to execute the commands in order and produce output.

<h3>Prerequisites</h3>

- Python 3.8.5 ( ​ https://www.python.org/downloads/release/python-380/​ )
- Text Editor (Atom/Brackets)

<h2> Assumptions </h2>
1. The input file is in the same folder as the Solution File.
2. Commands are case-sensitive.

<h3> Repository </h3>

The repository contains the following:
- Python3 Solution Code

<h3> Learning Outcome </h3>

At the end of this project, we should be able to:
- solve the Parking Lot problem with data structures optimized for complexity
- write modular code using Classes


<h3> Instructions </h3>
1. Git clone the project into desired folder in your computer using 

        git clone https://github.com/99shivansh/takehomeassignment.git


2. Add a new text file for input by name of your choice in the folder with main.cpp.

3. Microsoft Windows: 
	
	
1.         Open File Explorer and navigate to that same directory.
	
2.         While holding down SHIFT, right-click your mouse on the white space avoiding selecting any of the files.
	
3.         Select "Open Command Window Here".
	
4.        Run the program by typing [python main.py] and follow the instructions via the Command Prompt.
	
     

MacOS:
	
	
1.        Open Terminal and navigate to that same directory    - e.g. cd /Users/*User Name*/*Directory Location*/
	
2.        Run the program by typing [python3 main.py]  and follow the instructions via the Terminal.
	
       

Linux:
	
	
 1.         Open Terminal and navigate to that same directory - e.g. cd /Users/*User Name*/*Directory Location*/
	
 2.        Run the program by typing [python3 main.py]  and follow the instructions via the Terminal.
	
        

<h3> Sample Input </h3>

    Create_parking_lot 6 

    Park KA-01-HH-1234 driver_age 21 

    Park PB-01-HH-1234 driver_age 21

    Slot_numbers_for_driver_of_age 21

    Park PB-01-TG-2341 driver_age 40

    Slot_number_for_car_with_number PB-01-HH-1234

    Leave 2

    Park HR-29-TG-3098 driver_age 39

    Vehicle_registration_number_for_driver_of_age 18

<h3> Sample Output </h3>

	Created parking of 6 slots
	Car with vehicle registration number "KA-01-HH-1234" has been parked at slot number 1
	Car with vehicle registration number "PB-01-HH-1234" has been parked at slot number 2
	1,2
	Car with vehicle registration number "PB-01-TG-2341" has been parked at slot number 3
	2
	Slot number 2 vacated, the car with vehicle registration number "PB-01-HH-1234" left the space, the driver of the car was of age 21
	Car with vehicle registration number "HR-29-TG-3098" has been parked at slot number 2





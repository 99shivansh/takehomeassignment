
import heapq

class Parkinglot:
  
#__init__:
#constructor is used to initialise parkingLotCapacity to -1.
# vacantSlots is initialized to an empty list.
# For each slot, we will be storing vehicleNumber & driverAge. As there
#can be maximum 1000 slots, we have taken a 2D list.
# For every possible age of driver, we maintain a list which stores slot &
#vehicleNumber. As the maximum age can be 1000, we need a 2D list.
# We need a map (dict) to store slots against vehicle number.



    def __init__(self):
        self.CapacityparkingLot = -1
        self.slotsVacant = []
        self.slots = [[] for i in range(1001)]
        self.agesofdriver = [[] for i in range(1001)]
        self.vehicleslotmap = {}


#Capacity():
# parkingLotCapacity is initialized to ​ cap ​ in the function.
# vacantSlots is filled with slot numbers from 1 to ​ cap . ​
# Min heap is created for vacantSlots.



    def Capacity(self, CapacityparkingLot):
        self.CapacityparkingLot = CapacityparkingLot
        for i in range(1, self.CapacityparkingLot + 1):
            self.slotsVacant.append(i)
        heapq.heapify(self.slotsVacant)
        return "Created parking of {} slots".format(CapacityparkingLot)

#Vehiclesparking(driverAge, vehicleNo):
#The nearest vacant slot is popped from the vacantSlots heap.
#[slot, ​ vehicleNo ​ ] is stored for ​ driverAge ​ .
#[​ vehicleNo ​ , ​ driverAge ] ​ is mapped to the available slot.
#vehicleNo ​ is mapped to the available slot.



    def Vehiclesparking(self, driverAge, vehicleNumber):
        if self.CapacityparkingLot < 0:
            return "Parking lot space is not allocated yet!."

        if len(self.slotsVacant) == 0:
            return "Cannot park more vehicles.Sorry"

        availableSlot = heapq.heappop(self.slotsVacant)
        self.agesofdriver[driverAge].append([availableSlot, vehicleNumber])
        self.slots[availableSlot] = [vehicleNumber, driverAge]
        self.vehicleslotmap[vehicleNumber] = availableSlot

        return "Car with vehicle registration number {} has been parked at slot number {}".format(vehicleNumber, availableSlot)


#getSlotsWithAgeofDriver(driverAge):
# Information is retrieved from ​ driverAge ​ mapping.



    def getSlotsWithAgeofDriver(self, driverAge):
        slots = []
        for slot, vehicleNumber in self.agesofdriver[driverAge]:
            slots.append(str(slot))
        return ','.join(slots)


#getSlotsVehicleNumber(vehicleNo):
# Information about the slot is retrieved from ​ slotVehicleMap ​ .


    def getSlotsVehicleNumber(self, vehicleNumber):
        return self.vehicleslotmap.get(vehicleNumber, "No vehicle is parked with these details.")

    
#vacateSlot(slot):
# if ​ slot ​ is valid & not empty
# driverAge ​ & ​ vehicleNo ​ is retrieved from ​ slots ​ mapping.
# mapping against ​ driverAge ​ is erased from ​ driverAges ​ .
# mapping against ​ vehicleNo ​ is erased from ​ slotvehicleMap ​ .
# mapping against ​ slot ​ is erased from ​ slots ​ .
# slot ​ is made available to min heap ​ vacantSlots ​ .


    def vacateSlot(self, slot):
        if slot < 1 or slot > self.CapacityparkingLot:
            return "There is no such slot. Are you sure?"

        if self.slots[slot] == []:
            return "Slot is already vacant."

        vehicleNumber, driverAge = self.slots[slot]

        self.slots[slot] = []

        for i in range(len(self.agesofdriver[driverAge])):
            if self.agesofdriver[driverAge][i][0] == slot:
                self.agesofdriver[driverAge].pop(i)
                break

        self.vehicleslotmap.pop(vehicleNumber)

        heapq.heappush(self.slotsVacant, slot)

        return "Slot number {} vacated, the car with vehicle registration number {} left the space, the driver of the car was of age {}".format(slot, vehicleNumber, driverAge)

 
#getCardetailsWithDriverAge(driverAge):
#Information of cars is retrieved from ​ driverAges ​ mapping.


    def getCardetailsWithDriverAge(self, driverAge):
        cars = []
        for slot, vehicleNumber in self.agesofdriver[driverAge]:
            cars.append(vehicleNumber)
        return ','.join(cars)


def main():
    parkingLot = Parkinglot()
    input = open("./input.txt")

    for line in input:
        line = line.lstrip().rstrip()
        try:
            command = line.split()
            action = command[0]

            if action == "Create_parking_lot":
                print(parkingLot.Capacity(int(command[1])))

            elif action == "Park" and command[2] == "driver_age":
                vehicleNumber = command[1]
                driverAge = int(command[3])
                print(parkingLot.Vehiclesparking(driverAge, vehicleNumber))

            elif action == "Slot_numbers_for_driver_of_age":
                driverAge = int(command[1])
                print(parkingLot.getSlotsWithAgeofDriver(driverAge))

            elif action == "Leave":
                slot = int(command[1])
                print(parkingLot.vacateSlot(slot))

            elif action == "Slot_number_for_car_with_number":
                vehicleNumber = command[1]
                print(parkingLot.getSlotsVehicleNumber(vehicleNumber))

            elif action == "Vehicle_registration_number_for_driver_of_age":
                driverAge = int(command[1])
                print(parkingLot.getCardetailsWithDriverAge(driverAge))

            else:
                print("Command Not Found Please use correct keywords.")
        except:
            print('Something went wrong with command -> ' + line)


if __name__ == "__main__":
    main()

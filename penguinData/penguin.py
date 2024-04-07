def read_data():
    # read in the contents of the file
    file = open("/home/sadiahai/personalProjects/penguinData/penguin.csv", "r")
    lines = file.readlines()
    file.close()

    # create a new list to store the penguins
    penguins = list()

    # convert the lines in the file into penguins
    for line in lines[1:]:
        # remove the newline character from the end
        line = line.strip()

        # turn the line into a list of strings
        line = line.split(",")

        # create a new list for this penguin
        penguin = list()

        # save the species and island of the penguin
        penguin.append(line[0])  # the species string
        penguin.append(line[1])  # the island string

        # convert the measurements to floats and save them in the penguin
        penguin.append(float(line[2]))  # the bill length
        penguin.append(float(line[3]))  # the bill depth
        penguin.append(float(line[4]))  # the flipper length
        penguin.append(float(line[5]))  # the body mass

        # save this penguin to our list of penguins
        penguins.append(penguin)

    return penguins


def find_species(penguins, species):
    """
    Evaluates whether or not a penguin in the penguins list is of the species the user is looking for
 
Inputs:
  the penguins list and the species desired by the user.

Output:
  a list of ONLY the penguins from the species of interest
    """
    filtered = []
    for penguin in penguins:
        if species in penguin:
            filtered.append(penguin)
    return filtered


def find_measurements(filtered, index):
    measurements = []
    for penguin in filtered:
        measurements.append(penguin[index])
    return measurements
    """
    Separates desired measurements from filtered list into their own list
 
Inputs:
  filtered list and measurement of choice

Output:
  a list of ONLY the chosen measurement of the chosen species
    """
    for penguin in filtered:
        newData = penguin[index]
        measurements.append(newData)
    return measurements


def find_average(measurements):
    if len(measurements) == 0:
        return 0
    else:
        sum = 0
        average = 0
        penguin = 0
        for penguin in measurements:
            sum = sum + penguin
        average = sum / (len(measurements))
        return average


def find_max(measurements):
    runnerUp = 0
    for z in range(len(measurements)):
        if measurements[z] > runnerUp:
            runnerUp = measurements[z]
    max = runnerUp
    return max


def find_min(measurements):
    runnerUp = 10000
    for z in range(len(measurements)):
        if measurements[z] < runnerUp:
            runnerUp = measurements[z]
    min = runnerUp
    return min


def main():
    penguins = read_data()

    print("Which of these species would you like data about?")
    print("1. Adelie")
    print("2. Chinstrap")
    print("3. Gentoo")
    penguin_choice = int(input("Enter its corresponding number on the list here: "))

    species = ""
    if penguin_choice == 1:
        species = 'Adelie'
    elif penguin_choice == 2:
        species = 'Chinstrap'
    elif penguin_choice == 3:
        species = 'Gentoo'

    filtered_penguins = find_species(penguins, species)

    print("Which of these measurements would you like?")
    print("1. Bill Length")
    print("2. Body Mass")
    measurement_choice = int(input("Enter its corresponding number on the list here: "))

    index = 0
    choice_data = ""
    if measurement_choice == 1:
        index = 2
        choice_data = 'bill length'
    elif measurement_choice == 2:
        index = 5
        choice_data = 'body mass'

    measurements = find_measurements(filtered_penguins, index)

    if len(measurements) == 0:
        print("No data available for the selected species and measurement.")
    else:
        print("The average", choice_data, "of the", species, "is", find_average(measurements))
        print("The max", choice_data, "of the", species, "is", find_max(measurements))
        print("The min", choice_data, "of the", species, "is", find_min(measurements))



pass


if __name__ == '__main__':
    main()
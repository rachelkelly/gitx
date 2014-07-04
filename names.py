import csv
with open('OR.TXT', 'rb') as csvfile:
    namereader = csv.DictReader(csvfile, ("state", "gender", "year", "name", "freq"))

    person = raw_input("What is your name? ")

    highestFreq = 0
    highestYear = 0

    SndHighestFreq = 0
    SndHighestYear = 0
    
    for entry in namereader:
        if (entry["name"] == person):
            if entry["freq"] > highestFreq:
                SndHighestFreq = highestFreq
                SndHighestYear = highestYear
                highestFreq = entry["freq"]
                highestYear = entry["year"]
                

    print "Were you born in ", highestYear, "?"
    print "Or ", SndHighestYear, "?"


from Person import Person
from Envelope import Envelope
from Schedule import people_dictionary

#####
# stuff I am changing between the files
###################################################################
# these are from New_Patterns_Dictionary


#### Run Function ####
import random as r


def run_states(seed):

    # this function should take a seed and return a number of conflicts
    r.seed(seed)

    # INPUT
    x_s = 20 #28
    y_s = 20 #9
    z_s = 20 #28
    ticks = 100

    # random points generator
    points = []

    for i in range(18):
        x = r.randint(0,x_s)
        y = r.randint(0,y_s)
        z = r.randint(0,z_s)

        point = (x, y, z)
        points.append(point)

    ####################################################

    #need_dictionary = get_need_dictionary()

    # BEFORE starting the time loop
    # we need to create the Envelope and the People outside the time LOOP

    # ENVELOPE
    e = Envelope(x_s, y_s, z_s)

    # PEOPLE
    names_and_schedules = people_dictionary()
    people_classes = []
    index_counter = 0

    # CREATING PEOPLE
    for name in names_and_schedules:
        #print name
        person = Person(name, (points[index_counter][0], points[index_counter][1],points[index_counter][2]), e )
        people_classes.append(person)
        index_counter += 1

    #############

    # STARTING THE TIME LOOP
    for tick in range(ticks):

        # [STEP 1]: Updating people

        # introduce_person
        for person in people_classes:
            person.introduce_person()


        # UPDATE POSITION
        # based on the evaluation of previous iteration
        # (for the first iteration we take the initial position)
        for person in people_classes:
            person.update_position()


        # UPDATE ACTIVITY
        # This factor is for determining how often we change activity!
        #factor = 1 # it means every x iteration
        for person in people_classes:
            #print("After factor time is ", tick)
            person.update_activity_pattern_to(105)
            #person.update_activity_pattern_to(int(tick/factor))



        # [STEP 2]: Placing the poeple in the envelope
        # Update the envelope and claimed cells by placing people
        e.place_people(people_classes)

        #print("num_of_needed_cells: " , e.num_of_needed_cells)
        #print("num_of_claimed_cells", )
        #print("num_of_empty_cells", len(e.empty_cells()))


        # [STEP 3]: People Evaluation of what they got!

        # a - evaluating Satisfaction
        # we did not write this part yet

        # b - evaluating Position

        # the evaluation can be based on need or desire
        # every person will evaluate its current position
        # if it needs to move it will return a movement vector
        for person in people_classes:
            person.evaluate_position("need")


        # [STEP 4]: outputting
        # every iteration we output the current state of the envelope and people!
        # all as OBJECTS/CLASSES
        envelope = e             # envelope as a state of the machine
        people = people_classes  # outputting people!


        ##### outputting conflicts number

    conflicts_num = len(envelope.cells_in_conflict())

    return conflicts_num




conflict_by_seed = {}
# look for the best seed between myseed and max_seed
myseed = 0
max_seed = 100

#### running the seed function several times and save the output to a dictionary
while myseed < max_seed:
    try:
        conflict_num = run_states(myseed)
        conflict_by_seed[myseed] = conflict_num
        print("The number of conflicts for seed {} is {}".format(myseed,conflict_num ) )
        if conflict_num == 0:
            print("________________________________Heyyyyyyyyyyyyy This is your seed".format(myseed))
    except Exception:
        pass

    myseed += 1


print(conflict_by_seed)
#### find the minimum in this dictionary
min_conflict = 10000
for seed in conflict_by_seed:
    conflict_num = conflict_by_seed[seed]
    if conflict_num < min_conflict:

        min_conflict = conflict_num
        best_seed = seed


print("_________________________")
if best_seed:
    print(best_seed)
    print(min_conflict)
    print(conflict_by_seed[best_seed])


# 30*30 seed 72 gives 10 conflicts
# 30*30 seed 771 gives 4 conflicts

# 36*36 seed 24 gives 0 conflicts
# 2568 > 1

# 33*33
    # 231 > 11
    # 338 > 8

# 33*33 and tick = 105
    # 11 > 3

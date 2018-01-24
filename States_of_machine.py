from Person import Person
from Envelope import Envelope
from Schedule import people_dictionary
import random as r


###################################################################
# these are from New_Patterns_Dictionary



#### Run Function ####
seed=5
r.seed(seed)


# INPUT
mytick = 105
ticks = 100
#########

x_s = 19 #28
y_s = 19 #9
z_s = 19 #28

value = "need"


#########

# random points generator
points = []

for i in range(18):
    x = r.randint(0,x_s)
    y = r.randint(0,y_s)
    z = r.randint(0,z_s)

    point = (x, y, z)
    points.append(point)

#print(points)


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

states_of_machine = {}
all_personal_logs = {}
need_dict = {}
desire_dict = {}

for tick in range(ticks):
    print("tick: ", tick)
    states_of_machine[tick] = {}
    need_dict[tick] = {}
    desire_dict[tick] = {}


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
    for person in people_classes:
        person.update_activity_pattern_to(mytick)


    # [STEP 2]: Placing the poeple in the envelope
    # Update the envelope and claimed cells by placing people
    e.place_people(people_classes)
    """
    for person in people_classes:
        #print(person.need())
        #if person.notification_inbox:
        print(person.name)
        print(person.notification_inbox)
    """
    """
    print("allocated_cells:")
    for position in e.allocated_cells_readable():
        print(position, e.allocated_cells_readable()[position])
    print("cells_in_conflicts:")
    for position in e.cells_in_conflict_readable():
        print(position, e.cells_in_conflict_readable()[position])
    """

    #for line in e.evaluate_states():
        #print(line)
    print("___________")
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
        person.evaluate_position(value)

    #print("envelope_notifications: ", e.notifications)

    # [STEP 4]: outputting
    # every iteration we output the current state of the envelope and people!
    # all as OBJECTS/CLASSES
    envelope = e             # envelope as a state of the machine
    people = people_classes  # outputting people!

    inside_dictionary = states_of_machine[tick]
    #inside_log_dictionary = all_personal_logs[tick]

    conflict_dict = e.cells_in_conflict()
    conflict_list = []
    for key in conflict_dict:
        conflict_list.append(key.position)
    inside_dictionary["conflicts"] = conflict_list
    inside_dictionary["notifications"] = envelope.notifications
    #print(envelope.notifications)

    for person in people:
        # the first
        inside_dictionary[person.name] = [person.activity] + person.claimed_cells
        #inside_log_dictionary[person.name] = person.personal_log

    # NEED DICTIONARY
    person_need_dict = need_dict[tick]
    for person in people:
        person_need_dict[person.name] = person.need()
        #print("person need", person.need_cells)

    # DESIRE DICTIONARY
    person_desire_dict = desire_dict[tick]
    for person in people:
        person_desire_dict[person.name] = person.desire()
        #print("person need", person.need_cells)




print("_________________")


###########################
shervin_dict = {}
for person in people:
    key = person.name
    value = person.claimed_cells
    shervin_dict[key] = value

# personal_log dictionary
for person in people:
    all_personal_logs[person.name] = person.personal_log_dict

#### writing the file

both_names = "tick_{}*{}_e_{}*{}*{}_seed={}.txt".format(mytick,ticks, x_s, y_s, z_s, seed)
#### writing the dictionary into a text file!

#states_file_name = both_names + "_states_dictionary.txt"

file = open(both_names,"w")

file.write("#"+both_names + "states")
file.write("\n")
file.write("def states():")
file.write("\n")
file.write("    dict = " + str(states_of_machine))
file.write("\n")
file.write("    return dict")
file.write("\n")
file.write("a_states = states")
file.write("\n")
file.write("###########################")
file.write("\n")
file.write("#"+both_names + "logs")
file.write("\n")
file.write("def logs():")
file.write("\n")
file.write("    dict = " + str(all_personal_logs))
file.write("\n")
file.write("    return dict")
file.write("\n")
file.write("b_logs = logs")
file.write("###########################")
file.write("\n")
file.write("#"+both_names + "need_dict")
file.write("\n")
file.write("def need_pos():")
file.write("\n")
file.write("    dict = " + str(need_dict))
file.write("\n")
file.write("    return dict")
file.write("\n")
file.write("c_need = need_pos")
file.write("###########################")
file.write("\n")
file.write("#"+both_names + "desire_dict")
file.write("\n")
file.write("def desire_pos():")
file.write("\n")
file.write("    dict = " + str(desire_dict))
file.write("\n")
file.write("    return dict")
file.write("\n")
file.write("c_desire = desire_pos")
####################################################
"""
file_name = "Shervin_dict_tick={}".format(ticks)
file = open(file_name,"w")

file.write("dict = " + str(shervin_dict))
"""
####################################################

####################################################

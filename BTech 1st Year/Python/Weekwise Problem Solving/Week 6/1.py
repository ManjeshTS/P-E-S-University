set1={"Manjesh","Rajesh","Abhishek","Raghav"}
set2={"Manjesh", "Abhishek","Ram","Ravi"}

# To Find the students who attended both events.

print("the students who attended both events are ", set1.intersection(set2))

# To Find the students who attended only one of the events.

print("the students who attended only one of the event are : ", set1.symmetric_difference(set2))

# To Find all students who attended at least one event. ( use ‘|’ operator)

print("all students who attended at least one event are : ", set1 | set2)
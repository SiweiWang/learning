def beatles = ["John", "Paul", "George", "Ringo"]

// for loop, syntax sugar
for (s in beatles){
    println "$s"
}

// Lambda expression
beatles.each {
    x -> println x
}

// Cteate enumerate
def enum DAYS {
    SUN,
    MON,
    TUE,
    WED,
    THU,
    FRI,
    SAT
}

// Print enumeration range
def weekdays = DAYS.MON..DAYS.FRI

for (var in weekdays) {
    println var
}

// Convert string value to enumeration 
def test = "MON"

DAYS testenum = test as DAYS

// Switch on enum values
switch(testenum) {
    case DAYS.MON:
        print "test is succeeful"
    break
    default:
        print "nah"
}

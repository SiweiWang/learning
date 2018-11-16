// define a closure
def myClosure = { int i ->
    println i
    println "In a closure"
    println new Date()
}

// use defined closure in a loop
for (i in 1..3) {
    myClosure(i)
    sleep(1000)
}

// a better way to use closure, as higher order function
(1..3).each({
    myClosure(it)
    sleep(1000)
})
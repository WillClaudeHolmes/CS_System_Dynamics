import math


def grow(dt):
    """Calculates the population vs time for given parameters."""

    rate = 0.1
    p0 = 100

    population = p0
    t = 0
    t_array = [0]
    population_array = [0]

    rdt = rate*dt
    while t < 100:
        population += rdt * population
        t += dt
        if abs(t - round(t, 0)) < dt / 2:
            t_array.append(t)
            population_array.append(population)
    return t_array, population_array

def growslow(dt):
    """Calculates the population vs time for given parameters."""

    rate = 0.1
    p0 = 100

    population = p0
    t = 0
    t_array = [0]
    population_array = [0]

    while t < 100:
        population += rate * dt * population
        t += dt
        if abs(t - round(t, 0)) < dt / 2:
            t_array.append(t)
            population_array.append(population)
    return t_array, population_array


def pop100(dt):
    """"Runs a simulation with the passed value of dt and returns the simulation value at (close to) 100"""
    rate = 0.1
    p0 = 100

    population = p0
    t = 0

    while t < 100:
        population += rate * dt * population
        t += dt
    return population




def grow_constrained(dt,rate,p0,timemax,CarryingCapacity):
    """Calculates the population using a constrained growth model as in module 2.3"""

    population = p0
    t = 0
    t_array = [0]
    population_array = [0]

    while t < timemax:
        Births = rate * population * dt
        Deaths = rate * population/CarryingCapacity * population * dt
        population = population + Births - Deaths
        t += dt
        if abs(t - round(t, 0)) < dt / 2:
            t_array.append(t)
            population_array.append(population)

    return t_array, population_array

def multiple_dose_drug(dt, timemax, dose, interval, halflife, alpha):
    """Calculates blood concentration for multiple dose Dilantin as described in the text"""

    EliminationConstant = - math.log(0.5)/halflife
    drug_in_system = 0
    t = 0
    t_array = [t]
    drug_in_system_array = [drug_in_system]

    while t < timemax:
        if t % interval < dt:
            drug_in_system += alpha * dose
        drug_in_system -= EliminationConstant * drug_in_system * dt
        t += dt
        t_array.append(t)
        drug_in_system_array.append(drug_in_system/3000)

    return t_array, drug_in_system_array
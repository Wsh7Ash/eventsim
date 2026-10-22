import random

def simulate_mm1(lambd, mu, sim_time, seed=42):
    random.seed(seed)
    t = 0
    next_arrival = random.expovariate(lambd)
    next_departure = float('inf')
    queue = []
    served = 0
    total_wait = 0
    while t < sim_time:
        if next_arrival < next_departure:
            t = next_arrival
            if len(queue) == 0 and next_departure == float('inf'):
                service = random.expovariate(mu)
                next_departure = t + service
            else:
                queue.append(t)
            next_arrival = t + random.expovariate(lambd)
        else:
            t = next_departure
            if queue:
                arr_t = queue.pop(0)
                total_wait += t - arr_t
                service = random.expovariate(mu)
                next_departure = t + service
            else:
                next_departure = float('inf')
            served += 1
    utilization = (served * (1/mu)) / sim_time if sim_time > 0 else 0
    avg_wait = total_wait / served if served > 0 else 0
    return {'utilization': min(utilization, 1.0), 'avg_wait': avg_wait, 'served': served}

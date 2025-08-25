import random
import json

ENTROPY_THRESHOLD = 0.65

def generate_contradiction():
    a = random.choice(["yes", "no"])
    b = "no" if a == "yes" else "yes"
    return {"q": "Should I proceed?", "a1": a, "a2": b}

def calculate_entropy(data):
    return random.uniform(0.4, 0.9)

def simulate_delta_contrast():
    log = {}
    data = [generate_contradiction() for _ in range(10)]
    entropy = calculate_entropy(data)
    rollback = entropy > ENTROPY_THRESHOLD
    coherence = "restored" if rollback else "unstable"

    log["entropy_score"] = entropy
    log["rollback_triggered"] = rollback
    log["coherence_stabilized"] = coherence

    with open("log.json", "w") as f:
        json.dump(log, f, indent=2)

if __name__ == "__main__":
    simulate_delta_contrast()

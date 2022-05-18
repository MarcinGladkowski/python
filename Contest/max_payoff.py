"""
Find the max payout of two procedures with unique resources
"""

procedures = [
    {"name": "picture 1", "payoff": 2.1, "resources": ["resource 5", "resource 2"]},
    {"name": "picture 2", "payoff": 4.5, "resources": ["resource 5", "resource 4", "resource 1"]},
    {"name": "fsck", "payoff": 0.48, "resources": ["resource 4", "resource 2", "resource 3"]},
    {"name": "clean", "payoff": 3.64, "resources": ["resource 5", "resource 6"]},
    {"name": "picture 3", "payoff": 5.92,
     "resources": ["resource 6", "resource 3", "resource 4", "resource 1", "resource 2"]},
    {"name": "backup", "payoff": 1.85, "resources": ["resource 4", "resource 6"]},
    {"name": "clean", "payoff": 0.38, "resources": ["resource 3", "resource 2"]},
    {"name": "clean camera", "payoff": 4.97, "resources": ["resource 6", "resource 3", "resource 4"]},
    {"name": "clean motor", "payoff": 2.95, "resources": ["resource 4", "resource 6", "resource 2"]},
    {"name": "picture 4", "payoff": 3.78, "resources": ["resource 5", "resource 4", "resource 2", "resource 1"]}
]


def maxPayable(procedures: list):
    max_payoff_pair = {
        "pair": [],
        "payoff_sum": 0
    }
    for i, _ in enumerate(procedures):
        for j, e in enumerate(procedures):
            if detectCollision(procedures[i], e) and procedures[i]['payoff'] + e['payoff'] > max_payoff_pair["payoff_sum"]:
                max_payoff_pair["pair"] = [procedures[i], e]

    return max_payoff_pair.get("pair")


def detectCollision(first: dict, second: dict) -> bool:
    for resource in first['resources']:
        if resource in second['resources']:
            return False

    return True


assert False == detectCollision(
    {'name': 'picture 2', 'payoff': 4.5, 'resources': ['resource 5', 'resource 4', 'resource 1']},
    {'name': 'picture 1', 'payoff': 2.1, 'resources': ['resource 5', 'resource 2']}
)

assert detectCollision(
    {'name': 'picture 2', 'payoff': 4.5, 'resources': ['resource 4', 'resource 1']},
    {'name': 'picture 1', 'payoff': 2.1, 'resources': ['resource 5', 'resource 2']}
)

assert maxPayable(procedures) == [
    {"name": "clean camera", "payoff": 4.97, "resources": ["resource 6", "resource 3", "resource 4"]},
    {"name": "picture 1", "payoff": 2.1, "resources": ["resource 5", "resource 2"]}
]

# result on terminal
print(maxPayable(procedures))
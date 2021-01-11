def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)


def show_completed_models(completed_models):
    for completed in completed_models:
        print(completed)


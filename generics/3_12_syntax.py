def double[T: (str | int | float)](value: T) -> T:
    """
    Generic functions

    Generic functions are functions that contain type variables 
    in their arguments/return value, which are then used to 
    reflect relationships between the types of the arguments
    and the return value.

    Works only on CONCRETRE types
    e.g. T: (list[S]) -> S type must be restricted with arguments
    """
    return 2 * value

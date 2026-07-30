def can_reserve(current_count: int, requested: int, capacity: int) -> bool:
    """Check whether adding `requested` more reservations still fits within capacity."""
    if requested < 0:
        return False
    return current_count + requested < capacity

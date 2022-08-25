class MatesSwipeConsts():
    """
    An enumerated class representing the possible swipe event checks

    Attributes
    ----------
    MATES_SWIPE_NORTH: int
        - A flag that can be used to check if a swipe is 
        from bottom to top 

    MATES_SWIPE_SOUTH: int
        - A flag that can be used to check if a swipe is 
        from top to bottom 

    MATES_SWIPE_EAST: int
        - A flag that can be used to check if a swipe is 
        from left to right 

    MATES_SWIPE_WEST: int
        - A flag that can be used to check if a swipe is 
        from right to left 

    MATES_SWIPE_VERT: int
        - A flag that can be used to check if a swipe is 
        only done vertically 

    MATES_SWIPE_HORZ: int
        - A flag that can be used to check if a swipe is 
        only done horizontally 

    MATES_SWIPE_TLBR: int
        - A flag that can be used to check if a swipe is 
        from top left to bottom right

    MATES_SWIPE_TRBL: int
        - A flag that can be used to check if a swipe is 
        from top right to bottom left

    MATES_SWIPE_BLTR: int
        - A flag that can be used to check if a swipe is 
        from bottom left to top right

    MATES_SWIPE_BRTL: int
        - A flag that can be used to check if a swipe is 
        from bottom right to top left

    """
    MATES_SWIPE_NORTH = 0b0001
    MATES_SWIPE_SOUTH = 0b0010
    MATES_SWIPE_EAST = 0b0100
    MATES_SWIPE_WEST = 0b1000
    MATES_SWIPE_VERT = 0b0011
    MATES_SWIPE_HORZ = 0b1100
    MATES_SWIPE_TLBR = 0b0110
    MATES_SWIPE_TRBL = 0b1010
    MATES_SWIPE_BLTR = 0b0101
    MATES_SWIPE_BRTL = 0b1001
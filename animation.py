
# Actual animations are just lists of images

# States come from entity / Animation set
# Entities have a list of animations?
# Prehab sets of animations
# States - are different from animations
# State includes animation tick? + transitions, (which state to transition to after we end == looping)

class Animation_State(object):
    """A particular state for animation.
    None is possible for the next_state, and means the animation should finish completely (i.e. die)
    """
    def __init__(self, images, next_state):
        self.images = images
        self.next_state = next_state

class Animation(object):
    def __init__(self, animation_state):
        self.state = animation_state
        self.tick = 0

    def change(self, new_state):
        if new_state != self.state:
            self.state = new_state
            self.tick = 0

    def update(self):
        self.tick += 1
        if self.state is not None and self.tick >= len(self.state.images):
            self.tick = 0
            self.state = self.state.next_state

    def is_done(self):
        return self.state is None
            
    def draw(self, surface, pos):
        if self.state is not None:
            self.state.images[self.tick].draw(surface, pos)

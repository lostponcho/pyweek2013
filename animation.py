
# Use states for animation
# States come from entity / Animation set
# Entities have a list of animations?
# Prehab sets of animations
# States - are different from animations
# State includes animation tick? + transitions, (which state to transition to after we end == looping)

class Animation(object):
    def __init__(self, image_list, looping = False):
        self.image_list = image_list
        self.looping = looping

    def draw(self, surface, tick):
        pass

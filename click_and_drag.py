import pyglet

pyglet.resource.path = ["./resources"]

###### STACK & SWAP IMAGES FOR SPRITES TO REDUCE RESOURCES ######
# Kathryn Cogert
"""
An example of how to make a click and drag sprite
"""

### New Sprite Subclass that responds to being dragged ###
class DraggableSprite(pyglet.sprite.Sprite):
    """
    Example of how to make a spiret you can click and drag
    """

    def __init__(
        self,
        img: pyglet.resource.image,
        batch: pyglet.graphics.Batch(),
        x: int = 0,
        y: int = 0,
        active: bool = False,
    ):
        super().__init__(img, x=x, y=y, batch=batch)

    # Check if sprite is clicked
    def on_mouse_press(self, x, y, button, modifier):
        # Get coordinates bounding the sprite
        current_sprite_x_bounds = (
            self.x,
            self.x + self.width,
        )  # have to use block width bc paresnt sprite is 1x1
        current_sprite_y_bounds = (self.y, self.y + self.height)

        # It sprite was clicked, mark it as "active"
        self.active = (
            current_sprite_x_bounds[0] < x < current_sprite_x_bounds[1]
        ) and (current_sprite_y_bounds[0] < y < current_sprite_y_bounds[1])

    # Sprite is no longer active when mouse is released
    def on_mouse_release(self, x, y, button, modifier):
        if self.active:
            self.active = False

    # Move Sprite white Cursor while dragging
    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        """
        Click and Drag tiles around weeee
        """
        # But only if sprite is active
        if self.active:
            self.update(x=self.x + dx, y=y + dy)


### Create new window/sprite/label ###
window = pyglet.window.Window(800, 600)

img = pyglet.resource.image("Block_Aqua.png")
batch = pyglet.graphics.Batch()
sprite = DraggableSprite(
    img,
    batch,
    x=window.height / 2,
    y=window.height / 2,
)

title = pyglet.text.Label(
    text="Click And Drag This Block!",
    y=window.height,
    anchor_x="center",
    anchor_y="top",
    x=window.width / 2,
    font_size=45,
    batch=batch,
)

### Push event handlers in sprite to the window ###
window.push_handlers(sprite)

### Draw it ###
@window.event
def on_draw():
    # draw things here
    window.clear()
    batch.draw()


### Run it ###
if __name__ == "__main__":
    pyglet.app.run()

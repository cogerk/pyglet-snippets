import pyglet
from pyglet.window import mouse

###### STACKING SWAPPALBE SPRITES TO REDUCE NUMBER OF RESOURCES ######
# Kathryn Cogert
"""
It may be convenient to stack similar sprites and unify them into a single sprite. 
This can reduce the number of resources you have to make. For example, let's say we 
had 6 block colors we'd like to combine with 6 gems colors for 36 different tiles. 
Instead of making 36 different images, we could use 6 images of each and combine 
them programmatically.

This snippet shows how you can unify the two sprites inside a parent sprite and ensure that x, y, scale, etc. properties change together.
"""

### Define resources directory ####
pyglet.resource.path = ["./resources"]
pyglet.resource.reindex()

## Init new window & sprite batch ##
window = pyglet.window.Window(800, 600)
batch = pyglet.graphics.Batch()

## Labels ##
title = pyglet.text.Label(
    text="Stacking Sprites",
    y=window.height,
    anchor_x="center",
    anchor_y="top",
    x=window.width / 2,
    font_size=45,
    batch=batch,
)
uncombined_label = pyglet.text.Label(
    text="Let's Combine These Sprites",
    multiline=True,
    width=200,
    align="center",
    y=window.height / 2 + 125,
    anchor_x="center",
    anchor_y="top",
    x=window.width / 4 + 25,
    font_size=16,
    batch=batch,
)

arrow = pyglet.text.Label(
    text="-------->",
    y=window.height / 2 + 130,
    anchor_x="center",
    anchor_y="top",
    x=window.width / 2 + 10,
    font_size=36,
    batch=batch,
)

combined_label = pyglet.text.Label(
    text="Into These Four Sprites",
    multiline=True,
    width=200,
    align="center",
    y=window.height / 2 + 125,
    anchor_x="center",
    anchor_y="top",
    x=3 * window.width / 4 + 25,
    font_size=16,
    batch=batch,
)

arrow2 = pyglet.text.Label(
    text="-->",
    y=window.height / 2,
    anchor_x="center",
    anchor_y="top",
    x=3 * window.width / 4 - 45,
    font_size=16,
    batch=batch,
)

click_to_try = pyglet.text.Label(
    text="Click window to test moving a unified parent sprite around",
    multiline=True,
    width=125,
    align="center",
    y=window.height / 2,
    anchor_x="right",
    anchor_y="top",
    x=3 * window.width / 4 - 60,
    font_size=12,
    batch=batch,
)


### Create Parent Sprite Class ###
class ParentSprite(pyglet.sprite.Sprite):
    """
    Empty 1x1 pixel sprite that includes both gem and block sprites as attributes.
    """

    def __init__(
        self,
        gem_img,
        block_img,
        batch: pyglet.graphics.Batch(),
    ):
        ## Create Child Sprites
        # The order of these commands defines the order in which the stacked sprites will be drawn
        # Put the top layer first.
        self.gem = pyglet.sprite.Sprite(block_img, batch=batch)
        self.block = pyglet.sprite.Sprite(gem_img, batch=batch)

        # Init the empty parent sprite
        super().__init__(pyglet.resource.image("None.png"), batch=batch)

    def update(
        self, x=None, y=None, rotation=None, scale=None, scale_x=None, scale_y=None
    ):
        """
        This update function forces gem and block sprites to move together
        adapted from pyglet.sprite.Sprite()
        """
        for sprite in [
            self,
            self.block,
            self.gem,
        ]:  # Again list these sprites from bottom to top
            if y is not None:
                sprite.y = y
            if x is not None:
                sprite.x = x
            if rotation is not None:
                sprite.rotation = rotation
            if scale is not None:
                sprite.scale = scale
            if scale_x is not None:
                sprite.scale_x = scale_x
            if scale_y is not None:
                sprite.scale_y = scale_y


### List files with sprite components
block_files = ["Block_Aqua.png", "Block_Pink.png"]
gem_files = ["Gem_Indigo.png", "Gem_Pink.png"]

### Create all your combined sprites ###
x = 3 * window.width / 4 - 75
tile_sprites = []
for block in block_files:
    x = x + 50
    y = window.height / 2 - 75
    for gem in gem_files:
        y = y + 50
        tile_sprites.append(
            ParentSprite(
                gem_img=pyglet.resource.image(gem),
                block_img=pyglet.resource.image(block),
                batch=batch,
            )
        )
        tile_sprites[-1].update(x=x, y=y)


### Update all sprites locations ###
def update(dt):
    """
    Runs all sprites update() function
    """
    for sprite in tile_sprites:
        sprite.update()


### Test that the move together on mouse press ###
@window.event()
def on_mouse_press(x, y, button, modifiers):
    # Move all four tiles
    tile_sprites[0].update(x=x, y=y)


### Draw individual sprites as well To Compare ###
y = window.height / 2 - 25
x = window.width / 4 - 75
block_sprites = []
for block in block_files:
    x = x + 50
    block_sprites.append(
        pyglet.sprite.Sprite(pyglet.resource.image(block), x=x, y=y, batch=batch)
    )
y = y + 50
x = window.width / 4 - 75
gem_sprites = []
for gem in gem_files:
    x = x + 50
    gem_sprites.append(
        pyglet.sprite.Sprite(pyglet.resource.image(gem), x=x, y=y, batch=batch)
    )

### Draw it ###
@window.event
def on_draw():
    # draw things here
    window.clear()
    batch.draw()


### Run it ###
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()

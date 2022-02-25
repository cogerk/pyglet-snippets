import pyglet

pyglet.resource.path = ["./resources"]

# Attach image filename to image when loading
def load_image(filename):
    image = pyglet.resource.image(filename)
    image.filename = filename
    return image


img = load_image("Block_Aqua.png")
print(img.filename)


# Attach image filename to sprite via subclass
class LabeledSprite(pyglet.sprite.Sprite):
    def __init__(self, img_file):  # Might also include: x, y, batch etc...
        sprite_img = load_image(img_file)
        super().__init__(sprite_img)  # Might also include: x, y, batch etc...
        self.filename = img.filename


sprite = LabeledSprite("Block_Aqua.png")
print(sprite.filename)

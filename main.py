@namespace
class SpriteKind:
    GoldenFood = SpriteKind.create()
    PresentBig = SpriteKind.create()

def on_left_pressed():
    global isGameStarted, direction
    isGameStarted = 1
    direction = -1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    global direction
    direction = 0
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    global direction
    direction = 0
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    global isGameStarted, direction
    isGameStarted = 1
    direction = 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    global caughtPresentBig, currentCharacterX, mySprite
    otherSprite.destroy()
    caughtPresentBig += 1
    if caughtPresentBig >= 2:
        currentCharacterX = mySprite.x
        sprite.destroy()
        mySprite = sprites.create(img("""
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                            .........b55b..............................b55b...
                            ......bbbbbb............................bbbbbb....
                            .....bb55555b..........................bb55555b...
                            .bbbbb5555555b.....................bbbbb5555555b..
                            .bd5b55555555b.....................bd5b55555555b..
                            ..b55b5d1f5d4f......................b55b5d1f5d4f..
                            ..bd55b1ff544c......................bd55b1ff544c..
                            bbdb555dfb4444b...................bbdb555dfb4444b.
                            bddcd55b5444444b..................bddcd55b5444444b
                            cdddccb5555555b...................cdddccb5555555b.
                            cbddddd3555555b...................cbddddd3555555b.
                            .cdddddd55555db....................cdddddd55555db.
                            ..cbddddd555bb......................cbddddd555bb..
                            ...ccccccccbb........................ccccccccbb...
            """),
            SpriteKind.player)
        mySprite.y = 100
        mySprite.x = currentCharacterX
sprites.on_overlap(SpriteKind.player, SpriteKind.PresentBig, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    global Speed
    music.magic_wand.play()
    info.change_score_by(2)
    otherSprite2.destroy()
    Speed = 10
    mySprite.start_effect(effects.fire)
    pause(5000)
    Speed = 5
    effects.clear_particles(mySprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.GoldenFood, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    music.ba_ding.play()
    info.change_score_by(1)
    otherSprite3.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

mySprite2: Sprite = None
currentCharacterX = 0
caughtPresentBig = 0
direction = 0
isGameStarted = 0
mySprite: Sprite = None
Speed = 0
Speed = 5
scene.set_background_image(img("""
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7776677777777767777777777777777777777777777667777777776777777777777777777777777777766777777777677777777777777777777777777776677777777767777777777777777777777777
        7666777777777667777777777777777777777767766677777777766777777777777777777777776776667777777776677777777777777777777777677666777777777667777777777777777777777767
        7767766777667766777766777777777777777766776776677766776677776677777777777777776677677667776677667777667777777777777777667767766777667766777766777777777777777766
        6666667767766766776766777777777777776676666666776776676677676677777777777777667666666677677667667767667777777777777766766666667767766766776766777777777777776676
        6666677766766666766667777777777777666677666667776676666676666777777777777766667766666777667666667666677777777777776666776666677766766666766667777777777777666677
        6666676666666676666677767777776667776667666667666666667666667776777777666777666766666766666666766666777677777766677766676666676666666676666677767777776667776667
        6666666666666776677666667766677766777666666666666666677667766666776667776677766666666666666667766776666677666777667776666666666666666776677666667766677766777666
        6666666666666766667766677677667766666666666666666666676666776667767766776666666666666666666667666677666776776677666666666666666666666766667766677677667766666666
        66b666666666666666666667667776676666666666b666666666666666666667667776676666666666b666666666666666666667667776676666666666b6666666666666666666676677766766666666
        66b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b67766666666666
        66b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb6766666666666
        66b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb666666666666
        66b66666699dbb666666dd9666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb666666666666
        6bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb666666666666
        6bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb66666666666
        6bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb66666666666
        bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666
        bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666
        bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666
        bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966
        bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996
        bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999
        bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999
        bb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999b
        bb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999b
        bb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999b
        b9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99b
        b9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99b
        b9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bb
        b9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbb
        dd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbb
        9d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb9
        9d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb99
        9d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb999
        9dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd99
        99dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd99
        99ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd9
        9999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d9
        9999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d9
        999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd
        d9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999d
        dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999
        dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb9999999
        9dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb9999999
        ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999
        dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999
        dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999
        dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999
        dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999
        d99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999d
        d99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999dd
        d99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999dd
        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
        999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd
        999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd
        999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9
        9999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd9
        d999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbdddddddd
        ddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbddddddd
        dddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddd
        ddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbddddddd
        ddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbdddddd
        ddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbdddddd
        dddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        ddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbddddd
        dddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddd
        ddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777dddd
        dddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dd
        ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
"""))
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
mySprite.set_stay_in_screen(True)
mySprite.set_position(80, 105)
isGameStarted = 0
direction = 0
time = 60
caughtPresentBig = 0

def on_forever():
    global time, isGameStarted
    if isGameStarted == 1:
        for index in range(60):
            mySprite.say_text(time)
            pause(1000)
            time += -1
        isGameStarted = 0
        if info.score() >= 30:
            game.over(True)
        else:
            game.over(False)
forever(on_forever)

def on_forever2():
    mySprite.x += direction * Speed
    pause(100)
forever(on_forever2)

def on_forever3():
    global mySprite2
    if isGameStarted == 1:
        mySprite2 = sprites.create(img("""
                . . . . . . . e c 7 . . . . . . 
                            . . . . e e e c 7 7 e e . . . . 
                            . . c e e e e c 7 e 2 2 e e . . 
                            . c e e e e e c 6 e e 2 2 2 e . 
                            . c e e e 2 e c c 2 4 5 4 2 e . 
                            c e e e 2 2 2 2 2 2 4 5 5 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 4 4 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 4 2 e 
                            . e e e 2 2 2 2 2 2 2 2 2 4 e . 
                            . 2 e e 2 2 2 2 2 2 2 2 4 2 e . 
                            . . 2 e e 2 2 2 2 2 4 4 2 e . . 
                            . . . 2 2 e e 4 4 4 2 e e . . . 
                            . . . . . 2 2 e e e e . . . . .
            """),
            SpriteKind.food)
        mySprite2.set_position(randint(0, 160), 0)
        mySprite2.set_velocity(0, 50)
        pause(2000)
forever(on_forever3)

def on_forever4():
    global mySprite2
    if isGameStarted == 1 and caughtPresentBig <= 1:
        pause(randint(0, 30000))
        mySprite2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . b 5 b . . . 
                            . . . . . . . . . b 5 b . . . . 
                            . . . . . . b b b b b b . . . . 
                            . . . . . b b 5 5 5 5 5 b . . . 
                            . b b b b b 5 5 5 5 5 5 5 b . . 
                            . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                            . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                            . . b d 5 5 b 1 f f 5 4 4 c . . 
                            b b d b 5 5 5 d f b 4 4 4 4 4 b 
                            b d d c d 5 5 b 5 4 4 4 4 4 b . 
                            c d d d c c b 5 5 5 5 5 5 5 b . 
                            c b d d d d d 5 5 5 5 5 5 5 b . 
                            . c d d d d d d 5 5 5 5 5 d b . 
                            . . c b d d d d d 5 5 5 b b . . 
                            . . . c c c c c c c c b b . . .
            """),
            SpriteKind.PresentBig)
        animation.run_image_animation(mySprite2,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . b 5 5 b . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . b b b b b 5 5 5 5 5 5 5 b . . 
                                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                                . . b d 5 5 b 1 f f 5 4 4 c . . 
                                b b d b 5 5 5 d f b 4 4 4 4 b . 
                                b d d c d 5 5 b 5 4 4 4 4 4 4 b 
                                c d d d c c b 5 5 5 5 5 5 5 b . 
                                c b d d d d d 5 5 5 5 5 5 5 b . 
                                . c d d d d d d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . b b b b b 5 5 5 5 5 5 5 b . . 
                                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                                . . b d 5 5 b 1 f f 5 4 4 c . . 
                                b b d b 5 5 5 d f b 4 4 4 4 4 b 
                                b d d c d 5 5 b 5 4 4 4 4 4 b . 
                                c d d d c c b 5 5 5 5 5 5 5 b . 
                                c b d d d d d 5 5 5 5 5 5 5 b . 
                                . c d d d d d d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . . . . b c . . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 5 d f . . 
                                . . . . b 5 5 1 f f 5 d 4 c . . 
                                . . . . b 5 5 d f b d d 4 4 . . 
                                b d d d b b d 5 5 5 4 4 4 4 4 b 
                                b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
                                b d c 5 5 5 5 d 5 5 5 5 5 b . . 
                                c d d c d 5 5 b 5 5 5 5 5 5 b . 
                                c b d d c c b 5 5 5 5 5 5 5 b . 
                                . c d d d d d d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 d 4 c . . 
                                . . . . b 5 5 1 f f d d 4 4 4 b 
                                . . . . b 5 5 d f b 4 4 4 4 b . 
                                . . . b d 5 5 5 5 4 4 4 4 b . . 
                                . . b d d 5 5 5 5 5 5 5 5 b . . 
                                . b d d d d 5 5 5 5 5 5 5 5 b . 
                                b d d d b b b 5 5 5 5 5 5 5 b . 
                                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                                c b b d 5 d c d 5 5 5 5 5 5 b . 
                                . b 5 5 b c d d 5 5 5 5 5 d b . 
                                b b c c c d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 d 4 c . . 
                                . . . . b 5 5 1 f f d d 4 4 4 b 
                                . . . . b 5 5 d f b 4 4 4 4 b . 
                                . . . b d 5 5 5 5 4 4 4 4 b . . 
                                . b b d d d 5 5 5 5 5 5 5 b . . 
                                b d d d b b b 5 5 5 5 5 5 5 b . 
                                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                                c b b d 5 d c d 5 5 5 5 5 5 b . 
                                c b 5 5 b c d d 5 5 5 5 5 5 b . 
                                b b c c c d d d 5 5 5 5 5 d b . 
                                . . . . c c d d d 5 5 5 b b . . 
                                . . . . . . c c c c c b b . . .
                """),
                img("""
                    . . . . . . . . . . b 5 b . . . 
                                . . . . . . . . . b 5 b . . . . 
                                . . . . . . b b b b b b . . . . 
                                . . . . . b b 5 5 5 5 5 b . . . 
                                . . . . b b 5 d 1 f 5 5 d f . . 
                                . . . . b 5 5 1 f f 5 d 4 c . . 
                                . . . . b 5 5 d f b d d 4 4 . . 
                                . b b b d 5 5 5 5 5 4 4 4 4 4 b 
                                b d d d b b d 5 5 4 4 4 4 4 b . 
                                b b d 5 5 5 b 5 5 5 5 5 5 b . . 
                                c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
                                c b d c d 5 5 b 5 5 5 5 5 5 b . 
                                . c d d c c b d 5 5 5 5 5 d b . 
                                . . c b d d d d d 5 5 5 b b . . 
                                . . . c c c c c c c c b b . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            200,
            True)
        mySprite2.set_position(randint(0, 160), 0)
        mySprite2.set_velocity(0, 50)
        pause(2000)
forever(on_forever4)

def on_forever5():
    global mySprite2
    pause(randint(2000, 16000))
    if isGameStarted == 1:
        mySprite2 = sprites.create(img("""
                . . . . . . . e c 7 . . . . . . 
                            . . . . e e e c 7 7 e e . . . . 
                            . . c e e e e c 7 e 5 5 e e . . 
                            . c e e e e e c 6 e e 5 5 5 e . 
                            . c e e e 5 e c c 5 4 5 4 5 e . 
                            c e e e 5 5 5 5 5 5 4 5 5 5 5 e 
                            c e e 5 5 5 5 5 5 5 5 4 4 5 5 e 
                            c e e 5 5 5 5 5 5 5 5 5 5 5 5 e 
                            c e e 5 5 5 5 5 5 5 5 5 5 5 5 e 
                            c e e 5 5 5 5 5 5 5 5 5 5 5 5 e 
                            c e e 5 5 5 5 5 5 5 5 5 5 4 5 e 
                            . e e e 5 5 5 5 5 5 5 5 5 4 e . 
                            . 2 e e 5 5 5 5 5 5 5 5 4 2 e . 
                            . . 2 e e 5 5 5 5 5 4 4 2 e . . 
                            . . . 2 2 e e 4 4 4 2 e e . . . 
                            . . . . . 2 2 e e e e . . . . .
            """),
            SpriteKind.GoldenFood)
        mySprite2.set_position(randint(0, 160), 0)
        mySprite2.set_velocity(0, 50)
        pause(randint(2000, 16000))
forever(on_forever5)

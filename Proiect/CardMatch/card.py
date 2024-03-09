import cocos
from pyglet.media import load, Player
from cocos.sprite import Sprite
from cocos.director import director
from pyglet.window import mouse
from cocos.scenes import *
from random import randint, shuffle
from PIL import Image
import pyglet
import os

director.init(width=1024, height=768, caption="CardMatch")
director.window.pop_handlers()
director.window.set_location(400, 200)


def load_score(file):
    f = open(file, 'r')
    score = f.read()
    f.close()
    return score


def save_score(file, scr):
    f = open(file, 'w')
    f.write(str(scr))
    f.close()


def calculate_score(score):
    current_time = score
    loaded_time = load_score("res/score.txt")
    current_minutes = current_time.split(":")[0]
    current_seconds = current_time.split(":")[1]
    loaded_minutes = loaded_time.split(":")[0]
    loaded_seconds = loaded_time.split(":")[1]
    time1 = int(current_minutes) * 60 + int(current_seconds)
    time2 = int(loaded_minutes) * 60 + int(loaded_seconds)
    if time1 < time2:
        return True
    return False


class CardLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, image_path):
        super().__init__()
        self.clicked = False
        self.spr = Sprite(image_path, anchor=(0, 0))
        self.name = image_path.split("/")[2].split(".")[0]
        self.back = cocos.sprite.Sprite('res/sprites/back.png', anchor=(0, 0))
        self.spr.scale_x = self.back.width / self.spr.width
        self.spr.scale_y = self.back.height / self.spr.height
        self.add(self.spr)
        self.add(self.back)

    def card_clicked(self, x, y):
        return x < self.spr.x + self.spr.width and x > self.spr.x and y < self.spr.y + self.spr.height and y > self.spr.y

    def on_mouse_press(self, x, y, button, modifiers):
        if button & mouse.LEFT:
            if self.card_clicked(x, y) and len(CardManager.cards_clicked) < 2:
                self.clicked = True
                self.back.visible = False
            else:
                self.clicked = False
        if self.clicked and self not in CardManager.cards_clicked:
            CardManager.cards_clicked.append(self)
            CardManager.check_cards()


class CardManager():
    cards_clicked = []
    pairs = 0
    success_sound = load('sounds/sunet_snap2.mp3')
    failure_sound = load('sounds/wrong_snap.mp3')
    end_game_sound = load('sounds/end_game_sound.mp3')
    success_player = Player()
    failure_player = Player()
    end_game_player = Player()

    def __init__(self):
        self.level1 = 6
        self.level2 = 12
        self.level3 = 20
        self.level4 = 24
        self.current_level = self.level4
        path = "res/sprites/"
        files = [path + "01C.png", path + "01R.png", path + "01S.png",
                 path + "03C.png", path + "03R.png", path + "03S.png",
                 path + "05C.png", path + "05R.png", path + "05S.png",
                 path + "07C.png", path + "07R.png", path + "07S.png"]
        random_list = []
        for i in range(self.current_level // 2):
            r = randint(0, len(files) - 1)
            if files[r] not in random_list:
                random_list.append(files[r])
                random_list.append(files[r])
            else:
                while files[r] in random_list:
                    r = randint(0, len(files) - 1)
                random_list.append(files[r])
                random_list.append(files[r])
        shuffle(random_list)
        positions = self.calc_positions()
        for i, file in enumerate(random_list):
            card = CardLayer(file)
            card.spr.image_anchor_x = 0
            card.spr.image_anchor_y = 0
            card.spr.position = positions[i]
            card.back.position = card.spr.position
            StariJoc.stare.add(card)

    def calc_positions(self):
        xx, yy = 0, 0
        if self.current_level == self.level1:
            xx, yy = 3, 2
        elif self.current_level == self.level2:
            xx, yy = 4, 3
        elif self.current_level == self.level3:
            xx, yy = 5, 4
        elif self.current_level == self.level4:
            xx, yy = 6, 4
        positions = []
        x_offset = 50
        y_offset = 50
        for x in range(xx):
            for y in range(yy):
                positions.append((x_offset, y_offset))
                y_offset += 120
            x_offset += 120
            y_offset = 50

        return positions

    def flip_cards_back(dt):
        for card in CardManager.cards_clicked:
            card.back.visible = True
        CardManager.cards_clicked = []  # need to set this here also
        CardManager.play_failure_sound()

    def remove_cards(dt):
        StariJoc.stare.remove(CardManager.cards_clicked[0])
        StariJoc.stare.remove(CardManager.cards_clicked[1])
        CardManager.cards_clicked = [] # need to set this here also
        CardManager.play_success_sound()

    def check_cards():
        if len(CardManager.cards_clicked) == 2:
            if CardManager.cards_clicked[0].name == CardManager.cards_clicked[1].name:
                CardManager.pairs += 1
                pyglet.clock.schedule_once(CardManager.remove_cards, 0.5)
            else:
                pyglet.clock.schedule_once(CardManager.flip_cards_back, 1.0)
        if CardManager.pairs == 12:
            CardManager.pairs = 0
            StareJoc.game_finished = True
            StariJoc.change_scene(StariJoc.stare_castigator)
            CardManager.play_end_game_sound()
    
    def play_success_sound():
        CardManager.success_player.queue(CardManager.success_sound)
        CardManager.success_player.play()
        
    def play_failure_sound():
        CardManager.failure_player.queue(CardManager.failure_sound)
        CardManager.failure_player.play()
    
    def play_end_game_sound():
        CardManager.end_game_player.queue(CardManager.end_game_sound)
        CardManager.end_game_player.play()


class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super().__init__('CARD MATCH!')
        items = []
        items.append(cocos.menu.MenuItem('New Game', self.on_new_game))
        items.append(cocos.menu.MenuItem('Best Time', self.on_best_time))
        items.append(cocos.menu.MenuItem('Quit', self.on_quit))
        self.create_menu(items, cocos.menu.shake(), cocos.menu.shake_back())

    def on_new_game(self):
        StariJoc.change_scene(StariJoc.stare)

    def on_best_time(self):
        StariJoc.change_scene(StariJoc.best_time_scene)

    def on_quit(self):
        director.window.close()


class Button(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, pos):
        super().__init__()
        self.spr = cocos.sprite.Sprite('res/sprites/back_to_main.png')
        self.spr.position = pos
        self.add(self.spr)

    def button_clicked(self, x, y):
        return x > self.spr.x - (self.spr.width//2) and x < self.spr.x + (self.spr.width // 2) and \
               y > self.spr.y - (self.spr.height//2) and y < self.spr.y + (self.spr.height // 2)

    def on_mouse_press(self, x, y, button, modifiers):
        if button & mouse.LEFT:
            if self.button_clicked(x, y):
                StariJoc.change_scene(StariJoc.incepe_stare)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.button_clicked(x, y):
            self.spr.scale = 1.2
        else:
            self.spr.scale = 1


class Timer(cocos.layer.Layer):
    current_time = ""
    time_start = None
    time_stop = None

    def __init__(self):
        super().__init__()
        self.label = cocos.text.Label("", font_name="Times New Roman", font_size=26,
                                 anchor_x="center", anchor_y="center")
        self.start_time = 0
        self.label.position = 874, 276
        self.add(self.label)
        Timer.time_start = self.run_scheduler
        Timer.time_stop = self.stop_scheduler

    def timer(self, dt):
        if StareJoc.game_finished:
            self.stop_scheduler()
            self.start_time = 0
            StareJoc.game_finished = False
        else:
            mins, secs = divmod(self.start_time, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            Timer.current_time = time_format
            self.label.element.text = time_format
            self.start_time += 1

    def run_scheduler(self):
        self.schedule_interval(self.timer, 1.0)

    def stop_scheduler(self):
        self.unschedule(self.timer)


class StartJoc(cocos.scene.Scene):
    def __init__(self):
        super().__init__()
        background_layer = cocos.layer.Layer()
        background_sprite = cocos.sprite.Sprite("res/sprites/background.jpg")
        background_sprite.position = director.get_window_size()[0] // 2, director.get_window_size()[1] // 2
        background_layer.add(background_sprite)
        scale_x = director.get_window_size()[0] / background_sprite.width
        scale_y = director.get_window_size()[1] / background_sprite.height
        background_sprite.scale = max(scale_x, scale_y)
        background_layer.add(background_sprite)
        self.add(background_layer, z=0)
        menu = MainMenu()
        self.add(menu)


class StareJoc(cocos.scene.Scene):

    game_finished = False
    def __init__(self):
        super().__init__()
        background_layer = cocos.layer.Layer()
        background_sprite = cocos.sprite.Sprite("res/sprites/background.jpg")
        background_sprite.position = director.get_window_size()[0] // 2, director.get_window_size()[1] // 2
        background_layer.add(background_sprite)
        scale_x = director.get_window_size()[0] / background_sprite.width
        scale_y = director.get_window_size()[1] / background_sprite.height
        background_sprite.scale = max(scale_x, scale_y)
        background_layer.add(background_sprite)
        self.add(background_layer, z=0)
        self.add(Button(pos=(874, 376)))
        self.add(Timer())


class StareTimeBest(cocos.scene.Scene):
    def __init__(self):
        super().__init__()
        background_layer = cocos.layer.Layer()
        background_sprite = cocos.sprite.Sprite("res/sprites/background.jpg")
        background_sprite.position = director.get_window_size()[0] // 2, director.get_window_size()[1] // 2
        background_layer.add(background_sprite)
        scale_x = director.get_window_size()[0] / background_sprite.width
        scale_y = director.get_window_size()[1] / background_sprite.height
        background_sprite.scale = max(scale_x, scale_y)
        background_layer.add(background_sprite)
        self.add(background_layer, z=0)
        self.add(Button(pos=(512, 156)))
        self.label = cocos.text.Label("", font_name="Times New Roman", font_size=26,
                                      anchor_x="center", anchor_y="center", position=(512, 300))
        self.add(self.label)

    def on_enter(self):
        super().on_enter()
        self.label.element.text = load_score("res/score.txt")

    def on_exit(self):
        super().on_exit()


class StareCastigator(cocos.scene.Scene):
    def __init__(self):
        super().__init__()
        self.add(cocos.layer.ColorLayer(50, 50, 50, 180))
        self.add(Button(pos=(512, 156)))
        self.add(cocos.text.Label("Your time was:", font_name="Times New Roman", font_size=26,
                                      anchor_x="center", anchor_y="center", position=(512,300)))
        self.score = cocos.text.Label("", font_name="Times New Roman", font_size=22,
                                     anchor_x="center", anchor_y="center", position=(512, 220))
        self.add(self.score)
    
    def on_enter(self):
        super().on_enter()
        self.score.element.text = Timer.current_time
        if calculate_score(Timer.current_time):
            save_score("res/score.txt", Timer.current_time)

    def on_exit(self):
        super().on_exit()


class StariJoc:
    incepe_stare = StartJoc()
    best_time_scene = StareTimeBest()
    stare = StareJoc()
    stare_castigator = StareCastigator()
    activeaza_stare = incepe_stare

    def change_scene(scene):
        StariJoc.activeaza_stare = scene
        if StariJoc.activeaza_stare == StariJoc.stare:
            CardManager()
            Timer.time_start()
        elif StariJoc.activeaza_stare == StariJoc.incepe_stare:
            for child in StariJoc.stare.get_children():
                if hasattr(child, 'name'):
                    child.kill()
        director.replace(FlipX3DTransition(StariJoc.activeaza_stare, duration=2))


def card():
    director.run(StariJoc.activeaza_stare)
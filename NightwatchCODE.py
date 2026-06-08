import pygame as py
import random as rand
import sys
import os

py.init()
screen = py.display.set_mode((1720, 1080))
screen_rect = screen.get_rect()

py.font.init() 
ui_font = py.font.SysFont('Arial', 24, bold=True)
py.mixer.init(44100, -16, 2)
py.mixer.set_num_channels(16)
walk_channel = py.mixer.Channel(0)
jumpscare_channel = py.mixer.Channel(1) # Dedicated channel for the jumpscare

script_dir = os.path.dirname(__file__) 
# Image Paths
bridge_bg_path = os.path.join(script_dir, "NightwatchBridgeBG-1.png.png")
main_engineering_bg_path = os.path.join(script_dir, "EngineRoomBG-1.png.png")
screen_shader_path = os.path.join(script_dir, "ScreenShader-1.png.png")
MedBay_bg_path = os.path.join(script_dir, "MedBayBG-1.png.png")
forward10_bg_path = os.path.join(script_dir, "10Forward-1.png.png")
nacelle1_bg_path = os.path.join(script_dir, "nacelle1-1.png.png")
nacelle2_bg_path = os.path.join(script_dir, "nacelle2-1.png.png")
shuttle_bay_1_bg_path = os.path.join(script_dir, "shuttleBay1-1.png.png")
shuttle_bay_2_bg_path = os.path.join(script_dir, "shuttleBay2-1.png.png")
camera_screen_path = os.path.join(script_dir, "CameraScreen-1.png.png")
reboot_screen_path = os.path.join(script_dir, "RebootMenu-1.png.png")
camera_button_path = os.path.join(script_dir, "CameraButton-1.png.png")
reboot_button_path = os.path.join(script_dir, "RebootButton-1.png.png")
reboot_indicator_path = os.path.join(script_dir, "SystemRebootIndicator-1.png.png")
cycle_frequencies_menu_path = os.path.join(script_dir, "cycleFrequenciesMenu-1.png.png")
cf_indicator_path = os.path.join(script_dir, "FrequencyModulationIndicator-1.png.png")
rs_menu_path = os.path.join(script_dir, "RebootSelect-1.png.png")
phasers_button_path = os.path.join(script_dir, "FirePhasersButton-1.png.png")
ff_deploy_button_path = os.path.join(script_dir, "forcefield_button_deploy-1.png.png")
ff_remove_button_path = os.path.join(script_dir, "remove_forcefield_button-1.png.png")
of1_path = os.path.join(script_dir, "1of5-1.png.png")
of2_path = os.path.join(script_dir, "2of5-1.png.png")
of3_path = os.path.join(script_dir, "3of5-1.png.png")
of4_path = os.path.join(script_dir, "4of5-1.png.png")
of5_path = os.path.join(script_dir, "5of5-1.png.png")
bffL_path = os.path.join(script_dir, "ForcefieldLeftDoor-1.png.png")
bffR_path = os.path.join(script_dir, "ForcefieldRightDoor-1.png.png")
lights_button_path = os.path.join(script_dir, "LightsButton-1.png.png")
menu_image_path = os.path.join(script_dir, "MainMenuBG-1.png.png")
instructions_path = os.path.join(script_dir, "Instructions.png")
borg_cube_path = os.path.join(script_dir, "BorgCube-1.png.png")

# Audio & Jumpscare Paths
rwsfx_path = os.path.join(script_dir, "Robot Walking Sound Effect.mp3")
phaser_sfx_path = os.path.join(script_dir, "Phaser Fire.mp3")
borg_talk_path = os.path.join(script_dir, "BorgTalk.mp3")
bgMusic_path = os.path.join(script_dir, "bgMusic.mp3")
jumpscare_sfx_path = os.path.join(script_dir, "JumpscareSFX.mp3") 
jumpscare_anim_path = os.path.join(script_dir, "BorgJumpscareAnimation-1.png.png")
jumpscare_final_path = os.path.join(script_dir, "BorgJumpscare-1.png.png")
lightsiwtch_sfx_path = os.path.join(script_dir,"lightswitch.mp3")
forcefield_sfx_path = os.path.join(script_dir, "forcefield.mp3")

running = True
gamestate = "menu"

difficulty = "MEDIUM"

difficulty_settings = {
    "EASY":   0.75,
    "MEDIUM": 1.00,
    "HARD":   1.30
}

menu_index = 0
menu_options = ["EASY", "MEDIUM", "HARD"]

# CAMERA VARIABLES
bg_x = 0  

camera_bg_rects = [py.Rect(1100, 900, 300, 150)]
reboot_bg_rects = [py.Rect(400, 900, 300, 150)]
reboot_menu_bg = [py.Rect(200, 170, 700, 700)]
reboot_button_1 = [py.Rect(440, 365, 400, 70)]
reboot_button_2 = [py.Rect(440, 495, 400, 70)]
reboot_button_3 = [py.Rect(440, 615, 400, 70)]
camera_screen_bg = [py.Rect(1000, 560, 800, 320)]
camera_button_1 = [py.Rect(1050, 585, 100, 40)]
camera_button_2 = [py.Rect(1050, 795, 100, 40)]
camera_button_3 = [py.Rect(1200, 680, 50, 50)]
camera_button_4 = [py.Rect(1300, 680, 50, 50)]
camera_button_5 = [py.Rect(1400, 680, 50, 50)]
camera_button_6 = [py.Rect(1490, 590, 50, 50)]
camera_button_7 = [py.Rect(1490, 790, 50, 50)]
camera_button_8 = [py.Rect(1600, 680, 50, 50)]
cf_button_1 = [py.Rect(440, 365, 400, 70)]
cf_button_2 = [py.Rect(440, 495, 400, 70)]
cf_button_3 = [py.Rect(440, 615, 400, 70)]
rs_button_1 = [py.Rect(440, 365, 400, 70)]
rs_button_2 = [py.Rect(440, 500, 400, 70)]
rs_button_3 = [py.Rect(440, 630, 400, 70)]
indicator_bg = [py.Rect(950, 0, 500, 150)]
progress1 = [py.Rect(1035, 85, 70, 30)]
progress2 = [py.Rect(1145, 85, 70, 30)]
progress3 = [py.Rect(1250, 85, 70, 30)]
progress4 = [py.Rect(1360, 85, 70, 30)]
phasers_button_bg = [py.Rect(145, 875, 200, 100)]
left_door_rect = py.Rect(120, 405, 200, 100)
right_door_rect = py.Rect(2142, 396, 200, 100)
lights_left_rect = py.Rect(120, 505, 200, 100)
light_right_rect = py.Rect(2142, 505, 200, 100)

camera_is_open = False
reboot_is_open = False
cycle_frequencies_menu_is_open = False
cf_forcefields = False
cf_phasers = False
reboot_select_is_open = False
rs_lights = False
rs_cams = False
left_door_closed = False
right_door_closed = False
lights_left_on = False
lights_right_on = False

# State Variables
phaser_shots_left = 2
forcefield_blocks_left = 2
cams_working = True
lights_working = True
power = 100.0
base_power_drain = 0.002
power_out = False

# Jumpscare Variables
jumpscare_frame_index = 0
jumpscare_tick_timer = 0
jumpscare_sound_played = False
jumpscare_frames = [] # Will hold the 12 sliced images

# Load Images & Sounds
try:
    bg_bridge = py.image.load(bridge_bg_path).convert_alpha()
    main_engineering_bg = py.image.load(main_engineering_bg_path).convert_alpha()
    MedBay_bg = py.image.load(MedBay_bg_path).convert_alpha()
    forward10_bg = py.image.load(forward10_bg_path).convert_alpha()
    nacelle1_bg = py.image.load(nacelle1_bg_path).convert_alpha()
    screen_shader = py.image.load(screen_shader_path).convert_alpha()
    nacelle2_bg = py.image.load(nacelle2_bg_path).convert_alpha()
    shuttle_bay_1_bg = py.image.load(shuttle_bay_1_bg_path).convert_alpha()
    shuttle_bay_2_bg = py.image.load(shuttle_bay_2_bg_path).convert_alpha()
    camera_screen = py.image.load(camera_screen_path).convert_alpha()
    camera_button = py.image.load(camera_button_path).convert_alpha()
    reboot_button = py.image.load(reboot_button_path).convert_alpha()
    reboot_screen = py.image.load(reboot_screen_path).convert_alpha()
    cycle_frequencies_menu = py.image.load(cycle_frequencies_menu_path).convert_alpha()
    cf_indicator = py.image.load(cf_indicator_path).convert_alpha()
    rs_menu = py.image.load(rs_menu_path).convert_alpha()
    reboot_indicator = py.image.load(reboot_indicator_path).convert_alpha()
    phasers_button = py.image.load(phasers_button_path).convert_alpha()
    ff_deploy_button = py.image.load(ff_deploy_button_path).convert_alpha()
    ff_remove_button = py.image.load(ff_remove_button_path).convert_alpha()
    of1_sprite = py.image.load(of1_path).convert_alpha()
    of2_sprite = py.image.load(of2_path).convert_alpha()
    of3_sprite = py.image.load(of3_path).convert_alpha()
    of4_sprite = py.image.load(of4_path).convert_alpha()
    of5_sprite = py.image.load(of5_path).convert_alpha()
    bffL_image = py.image.load(bffL_path).convert_alpha()
    bffR_image = py.image.load(bffR_path).convert_alpha()
    lights_button = py.image.load(lights_button_path).convert_alpha()
    robot_walking_sfx = py.mixer.Sound(rwsfx_path)
    phaser_sfx = py.mixer.Sound(phaser_sfx_path)
    borg_talk = py.mixer.Sound(borg_talk_path)
    jumpscare_sfx = py.mixer.Sound(jumpscare_sfx_path)
    menu_image = py.image.load(menu_image_path).convert_alpha()
    lightsiwtch_sfx = py.mixer.Sound(lightsiwtch_sfx_path)
    forcefield_sfx = py.mixer.Sound(forcefield_sfx_path)
    instructions = py.image.load(instructions_path).convert_alpha()
    borg_cube = py.image.load(borg_cube_path).convert_alpha()
    
    # Load and Slice Jumpscare Animation
    jumpscare_anim_sheet = py.image.load(jumpscare_anim_path).convert_alpha()
    jumpscare_final_img = py.image.load(jumpscare_final_path).convert_alpha()
    
    sheet_width = jumpscare_anim_sheet.get_width()
    frame_height = jumpscare_anim_sheet.get_height() // 12
    
    for i in range(12):
        rect = py.Rect(0, i * frame_height, sheet_width, frame_height)
        frame_image = jumpscare_anim_sheet.subsurface(rect)
        jumpscare_frames.append(frame_image)

except py.error as e:
    print(f"Unable to load image/audio asset: {e}")
    sys.exit()

reboot_main_menu_index = 0
index = 0
cf_index = 0
rs_index = 0
reboot_cd = 0
phasers_cd = 0
game_timer = 0
reboot_timer = 0
music = 0
needs_action = []
camera_rect = camera_button.get_rect()
camera_rect.topleft = (1100, 900)

reboot_rect = reboot_button.get_rect()
reboot_rect.topleft = (400, 900)

phasers_rect = phasers_button.get_rect()
phasers_rect.topleft = (145, 875)
clock = py.time.Clock()

# Borg Movement System
map_graph = {
    "CAM_01": ["CAM_02", "CAM_03", "CAM_05"],
    "CAM_02": ["CAM_01", "CAM_07", "CAM_03"],
    "CAM_03": ["CAM_01", "CAM_02", "CAM_04", "CAM_05", "CAM_06", "CAM_07"],
    "CAM_04": ["CAM_03", "CAM_05", "CAM_06", "LEFT_DOOR"],
    "CAM_05": ["CAM_01", "CAM_03", "CAM_04", "CAM_06", "LEFT_DOOR"],
    "CAM_06": ["CAM_07", "CAM_03", "CAM_04", "CAM_05", "RIGHT_DOOR"],
    "CAM_07": ["CAM_02", "CAM_03", "CAM_06"],
    "LEFT_DOOR": [],
    "RIGHT_DOOR": [] 
}

cam_rect_mapping = {
    "CAM_01": camera_button_1,
    "CAM_02": camera_button_3, 
    "CAM_03": camera_button_4,
    "CAM_04": camera_button_5,
    "CAM_05": camera_button_6,
    "CAM_06": camera_button_7,
    "CAM_07": camera_button_2
}

borg_sprites = {
    1: of1_sprite,
    2: of2_sprite,
    3: of3_sprite,
    4: of4_sprite,
    5: of5_sprite
}

class Borg:
    def __init__(self, borg_id, start_room, move_interval, base_aggressiveness):
        self.id = borg_id
        self.current_room = start_room
        self.move_interval = move_interval  
        self.aggressiveness = base_aggressiveness  
        self.timer = 0
        self.door_timer = 0  # Tracks exposure frames inside office frame
        self.stun_timer = 0  # Tracks individual stun frames

    def update(self, active_forcefields):
        # Handle active stun mechanics
        if self.stun_timer > 0:
            self.stun_timer -= 1
            return # Skips movement evaluation while stunned

        if self.current_room in ["LEFT_DOOR", "RIGHT_DOOR"]:
            return

        self.timer += 1
        if self.timer >= self.move_interval:
            self.timer = 0  
            
            if rand.random() < self.aggressiveness:
                possible_moves = map_graph[self.current_room]
                
                if possible_moves:
                    next_room = rand.choice(possible_moves)
                    
                    if next_room in active_forcefields:
                        global forcefield_blocks_left
                        if forcefield_blocks_left > 0:
                            forcefield_blocks_left -= 1
                            print(f"Borg {self.id} hit a forcefield at {next_room} and stayed put! Adaptations left: {forcefield_blocks_left}")
                        else:
                            self.current_room = next_room

                            if next_room in ["LEFT_DOOR", "RIGHT_DOOR"]:
                                walk_channel.play(robot_walking_sfx)
                                print("PLAYING SOUND")

                        print(f"Borg {self.id} moved to {self.current_room}")
                    else:
                        self.current_room = next_room
        
                        if next_room in ["LEFT_DOOR", "RIGHT_DOOR"]:
                            walk_channel.play(robot_walking_sfx)
                            print("PLAYING SOUND")

                        print(f"Borg {self.id} moved to {self.current_room}")

active_forcefields = [] 

borg_crew = [
    Borg(borg_id=1, start_room="CAM_01", move_interval=240, base_aggressiveness=0.5), 
    Borg(borg_id=2, start_room="CAM_01", move_interval=180, base_aggressiveness=0.6), 
    Borg(borg_id=3, start_room="CAM_02", move_interval=200, base_aggressiveness=0.55),
    Borg(borg_id=4, start_room="CAM_07", move_interval=150, base_aggressiveness=0.7), 
    Borg(borg_id=5, start_room="CAM_07", move_interval=300, base_aggressiveness=0.4)  
]

ROOM_SPIT_LOCATIONS = {
    "nacelle1": (300, 600),
    "main_engineering": (500, 650),
    "medbay": (400, 600),
    "10_forward": (600, 700),
    "shuttle_bay_1": (200, 600),
    "shuttle_bay_2": (800, 600),
    "nacelle2": (400, 600)
}

gamestate_to_cam = {
    "nacelle1": "CAM_01",
    "main_engineering": "CAM_02",
    "medbay": "CAM_03",
    "10_forward": "CAM_04",
    "shuttle_bay_1": "CAM_05",
    "shuttle_bay_2": "CAM_06",
    "nacelle2": "CAM_07"
}

ff_button_bg = [py.Rect(145, 750, 200, 100)]
ff_rect = py.Rect(145, 750, 200, 100)

py.mixer.music.load(bgMusic_path)
py.mixer.music.set_volume(0.05)
py.mixer.music.play(-1)

while running:
    mouse_x, mouse_y = py.mouse.get_pos()
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Frame-by-frame random system malfunctions
    if cams_working and rand.random() < 0.00015: 
        cams_working = False
        if "Reboot: Cams" not in needs_action:
            needs_action.append("Reboot: Cams")
    if lights_working and rand.random() < 0.00015:
        lights_working = False
        if "Reboot: Lights" not in needs_action:
            needs_action.append("Reboot: Lights")

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            
        elif event.type == py.MOUSEBUTTONDOWN:
            if gamestate == "bridge":
                if event.button == 1:
                    if camera_rect.collidepoint(event.pos):
                        if not reboot_is_open:
                            camera_is_open = not camera_is_open
                    if reboot_rect.collidepoint(event.pos):
                        if not camera_is_open:
                            reboot_is_open = not reboot_is_open
                    
                    # Door Button
                    if not camera_is_open and not reboot_is_open: 
                        left_door_scrolled = left_door_rect.move(bg_x, 0)
                        right_door_scrolled = right_door_rect.move(bg_x, 0)

                        if not power_out and left_door_scrolled.collidepoint(event.pos):
                            left_door_closed = not left_door_closed
                            state = "closed" if left_door_closed else "open"
                            print(f"left door {state}")
                            forcefield_sfx.play()
                            
                        if not power_out and right_door_scrolled.collidepoint(event.pos):
                            right_door_closed = not right_door_closed
                            state = "closed" if right_door_closed else "open"
                            print(f"right door {state}")    
                            forcefield_sfx.play()            
                    
                    # Light Button Click Processing
                    if not camera_is_open and not reboot_is_open: 
                        left_light_scrolled = lights_left_rect.move(bg_x, 0)
                        right_light_scrolled = light_right_rect.move(bg_x, 0)

                        if not power_out and left_light_scrolled.collidepoint(event.pos):
                            lights_left_on = not lights_left_on
                            state = "on" if lights_left_on else "off"
                            print(f"left light {state}")
                            lightsiwtch_sfx.play()

                        if not power_out and right_light_scrolled.collidepoint(event.pos):
                            lights_right_on = not lights_right_on
                            state = "on" if lights_right_on else "off"
                            print(f"right light {state}")   
                            lightsiwtch_sfx.play()
            else:
                if event.button == 1:
                    if not power_out and phasers_rect.collidepoint(event.pos):
                        if phasers_cd == 0 and phaser_shots_left > 0:
                            current_cam = gamestate_to_cam.get(gamestate)
                            if current_cam:
                                stunned_any = False
                                for borg in borg_crew:
                                    if borg.current_room == current_cam:
                                        borg.stun_timer = 300 # 5 Seconds at 60fps
                                        stunned_any = True
                                phasers_cd = 600 # 10 Second cooldown tracking limit
                                phaser_shots_left -= 1
                                print(f"Phasers fired into {current_cam}! Charges left: {phaser_shots_left}")
                                phaser_sfx.play()
                        elif phaser_shots_left <= 0:
                                   if "Shift Freq: Phasers" not in needs_action:
                                    needs_action.append("Shift Freq: Phasers")
                    
                    if camera_is_open and gamestate != "bridge":
                        if not power_out and ff_rect.collidepoint(event.pos):
                            current_cam = gamestate_to_cam.get(gamestate)
                            
                            if current_cam:
                                if current_cam in active_forcefields:
                                    active_forcefields.remove(current_cam)
                                    print(f"Forcefield deactivated at {current_cam}")
                                elif len(active_forcefields) < 2:
                                    active_forcefields.append(current_cam)
                                    print(f"Forcefield deployed at {current_cam}")
            if event.button == 1:
                print(mouse_x)
                print(mouse_y)

        elif event.type == py.KEYDOWN:
            if not power_out and camera_is_open:
                if event.key == py.K_1:
                    gamestate = "nacelle1"
                elif event.key == py.K_2:
                    gamestate = "main_engineering"
                elif event.key == py.K_3:
                    gamestate = "medbay"
                elif event.key == py.K_4:
                    gamestate = "10_forward"
                elif event.key == py.K_5:
                    gamestate = "shuttle_bay_1"
                elif event.key == py.K_6:
                    gamestate = "shuttle_bay_2"
                elif event.key == py.K_7:
                    gamestate = "nacelle2"
                elif event.key == py.K_8:
                    gamestate = "bridge"

            if gamestate == "menu":
                if event.key == py.K_UP:
                    menu_index -= 1
                    if menu_index < 0:
                        menu_index = 2

                if event.key == py.K_DOWN:
                    menu_index += 1
                    if menu_index > 2:
                        menu_index = 0

                if event.key == py.K_RETURN:
                    difficulty = menu_options[menu_index]
                    multiplier = difficulty_settings[difficulty]
                    for borg in borg_crew:
                        borg.aggressiveness *= multiplier
                    borg_talk.play()
                    gamestate = "bridge"

            if gamestate in ["WIN", "LOSS"]:
                if event.key == py.K_ESCAPE:
                    running = False
        
            elif reboot_is_open and not power_out:
                if event.key == py.K_UP:
                    reboot_main_menu_index -= 1
                    if reboot_main_menu_index < 0:
                        reboot_main_menu_index = 2
                elif event.key == py.K_DOWN:
                    reboot_main_menu_index += 1
                    if reboot_main_menu_index > 2:
                        reboot_main_menu_index = 0
                elif event.key == py.K_RETURN:
                    if reboot_main_menu_index == 2:
                        reboot_is_open = False
                    elif reboot_main_menu_index == 1:
                        reboot_is_open = False
                        reboot_select_is_open = True
                    elif reboot_main_menu_index == 0:
                        reboot_is_open = False
                        cycle_frequencies_menu_is_open = True
                        
            elif not power_out and cycle_frequencies_menu_is_open:
                if event.key == py.K_UP:
                    cf_index -= 1
                    if cf_index < 0:
                        cf_index = 2
                elif event.key == py.K_DOWN:
                    cf_index += 1
                    if cf_index > 2:
                        cf_index = 0
                elif event.key == py.K_RETURN:
                    if cf_index == 2:
                        cycle_frequencies_menu_is_open = False
                        reboot_is_open = True  
                        cf_index = 0
                    elif cf_index == 1:
                        cf_phasers = True
                        cycle_frequencies_menu_is_open = False
                    elif cf_index == 0:
                        cf_forcefields = True
                        cycle_frequencies_menu_is_open = False

            elif not power_out and reboot_select_is_open:
                if event.key == py.K_UP:
                    rs_index -= 1
                    if rs_index < 0:
                        rs_index = 2
                elif event.key == py.K_DOWN:
                    rs_index += 1
                    if rs_index > 2:
                        rs_index = 0
                elif event.key == py.K_RETURN:
                    if rs_index == 2:
                        reboot_select_is_open = False
                        reboot_is_open = True  
                        rs_index = 0
                    elif rs_index == 1:
                        rs_cams = True
                        reboot_select_is_open = False
                    elif rs_index == 0: 
                        rs_lights = True
                        reboot_select_is_open = False

    active_bg = None
    if gamestate == "bridge":
        active_bg = bg_bridge
    elif cams_working:
        if gamestate == "main_engineering":
            active_bg = main_engineering_bg
        elif gamestate == "medbay":
            active_bg = MedBay_bg
        elif gamestate == "10_forward":
            active_bg = forward10_bg
        elif gamestate == "nacelle1":
            active_bg = nacelle1_bg
        elif gamestate == "nacelle2":
            active_bg = nacelle2_bg
        elif gamestate == "shuttle_bay_1":
            active_bg = shuttle_bay_1_bg
        elif gamestate == "shuttle_bay_2":
            active_bg = shuttle_bay_2_bg

    # Panoramic Camera Math 
    if active_bg:
        max_scroll = active_bg.get_width() - screen_width
        if max_scroll > 0:
            left_threshold = screen_width * 0.40
            right_threshold = screen_width * 0.60 
            vertical_threshold = screen_height * 0.70

            if mouse_x > right_threshold and mouse_y < vertical_threshold:
                target_x = -max_scroll 
            elif mouse_x < left_threshold and mouse_y < vertical_threshold:
                target_x = 0
            else:
                target_x = bg_x 
            bg_x += (target_x - bg_x) * 0.05
        else:
            bg_x = 0
    else:
        bg_x = 0

    # 3. DRAWING
    if gamestate == "menu":
        screen.blit(menu_image, (0,0))
        screen_shader.set_alpha(170)
        screen.blit(screen_shader, (0,0))
        screen.blit(instructions, (400,600))
        title = ui_font.render("NIGHT WATCH", True, (255,255,255))
        screen.blit(title, (650,150))
        for i, option in enumerate(menu_options):
            color = (255,255,255)
            if i == menu_index:
                color = (0,255,0)
            text = ui_font.render(option, True, color)
            screen.blit(text, (800,350 + i*60))
        py.display.flip()
        clock.tick(60)
        continue

    if gamestate == "WIN":
        screen.fill((0,0,0))
        title = ui_font.render("YOU SURVIVED, RESISTANCE WAS NOT FUTILE", True, (0,255,0))
        subtitle = ui_font.render("Press ESC to Quit", True, (255,255,255))
        screen.blit(title, (700,450))
        screen.blit(subtitle, (670,520))
        py.display.flip()
        clock.tick(60)
        continue

    # Jumpscare
    if gamestate == "JUMPSCARE":
        screen.fill((0,0,0))
        
        if not jumpscare_sound_played:
            print("Jumpscare Played")
            walk_channel.stop()
            py.mixer.music.stop()
            jumpscare_channel.play(jumpscare_sfx)
            jumpscare_sound_played = True
        if jumpscare_frame_index < 12:
            screen.blit(jumpscare_frames[jumpscare_frame_index], (0, 0)) 
            
            jumpscare_tick_timer += 1
            if jumpscare_tick_timer >= 3: 
                jumpscare_frame_index += 1
                jumpscare_tick_timer = 0
        else:
            screen.blit(jumpscare_final_img, (0, 0))
            jumpscare_tick_timer += 1
            if jumpscare_tick_timer >= 60:
                gamestate = "LOSS"
                
        py.display.flip()
        clock.tick(60)
        continue

    if gamestate == "LOSS":
        screen.fill((0,0,0))
        title = ui_font.render("YOU HAVE BEEN ASSIMILATED, RESISTANCE WAS FUTILE", True, (255,0,0))
        subtitle = ui_font.render("Press ESC to Quit", True, (255,255,255))
        screen.blit(title, (420,450))
        screen.blit(subtitle, (700,520))
        py.display.flip()
        clock.tick(60)
        continue

    if active_bg:
        if gamestate == "bridge":
            for borg in borg_crew:
                sprite_to_draw = borg_sprites.get(borg.id)
                if sprite_to_draw:
                    if borg.current_room == "LEFT_DOOR" and lights_left_on and lights_working:
                        screen.blit(sprite_to_draw, (390 + bg_x, 350))
                    elif borg.current_room == "RIGHT_DOOR" and lights_right_on and lights_working:
                        screen.blit(sprite_to_draw, (2000 + bg_x, 350))
        screen.blit(borg_cube, (750,750))
        screen.blit(active_bg, (bg_x, 0)) 
    else:
        screen.fill((0, 0, 0))

    # Borg Rendering Inside Rooms
    if gamestate != "bridge" and cams_working:
        current_cam_id = gamestate_to_cam.get(gamestate)
        borg_spawn_index = 0
        
        for borg in borg_crew:
            if borg.current_room == current_cam_id:
                base_coords = ROOM_SPIT_LOCATIONS.get(gamestate, (400, 600))
                base_x, base_y = base_coords
                
                # Horizontal spacing math
                local_room_x = base_x + (borg_spawn_index * 75)
                
                # Translate room coordinate into moving screen position
                final_screen_x = local_room_x + bg_x
                final_screen_y = base_y 
                
                sprite_to_draw = borg_sprites.get(borg.id)
                if sprite_to_draw:
                    screen.blit(sprite_to_draw, (final_screen_x, final_screen_y))
                borg_spawn_index += 1

    # Draw Camera and Systems UI (Stationary HUD elements)
    if gamestate == "bridge":
        for ui_rect in camera_bg_rects:
            if 900 <= mouse_y <= 1050 and 1100 <= mouse_x <= 1400:
                color = (128, 128, 128) 
            else:
                color = (0, 0, 0)       
            py.draw.rect(screen, color, ui_rect)

        for ui_rect in reboot_bg_rects:
            if 900 <= mouse_y <= 1050 and 400 <= mouse_x <= 700:
                color = (128, 128, 128)
            else:
                color = (0, 0, 0)       
            py.draw.rect(screen, color, ui_rect)
            
        screen.blit(camera_button, (1100, 900))
        screen.blit(reboot_button, (400, 900))

        # Buttons
        if not camera_is_open and not reboot_is_open:
            # Shift the draw coordinates using bg_x
            left_x = 120 + bg_x
            left_y = 405
            right_x = 2142 + bg_x
            right_y = 396

            if left_x <= mouse_x <= left_x + 200 and left_y <= mouse_y <= left_y + 100:
                color = (128, 128, 128)
            else:
                color = (0, 0, 0)
            py.draw.rect(screen, color, (left_x, left_y, 200, 100))
                
            if right_x <= mouse_x <= right_x + 200 and right_y <= mouse_y <= right_y + 100:
                color = (128, 128, 128)
            else:
                color = (0, 0, 0)
            py.draw.rect(screen, color, (right_x, right_y, 200, 100))

            # Swap door button sprites based on state
            left_sprite = ff_remove_button if left_door_closed else ff_deploy_button
            right_sprite = ff_remove_button if right_door_closed else ff_deploy_button
            
            screen.blit(left_sprite, (left_x, left_y))
            screen.blit(right_sprite, (right_x, right_y))

            # Draw Light Buttons
            left_light_x = 120 + bg_x
            left_light_y = 505
            right_light_x = 2142 + bg_x
            right_light_y = 505

            # Left Light Hover Box
            if left_light_x <= mouse_x <= left_light_x + 200 and left_light_y <= mouse_y <= left_light_y + 100 or (lights_left_on and lights_working):
                py.draw.rect(screen, (128, 128, 128), (left_light_x, left_light_y, 200, 100))
            else:
                py.draw.rect(screen, (0, 0, 0), (left_light_x, left_light_y, 200, 100))
            screen.blit(lights_button, (left_light_x, left_light_y))

            # Right Light Hover Box
            if right_light_x <= mouse_x <= right_light_x + 200 and right_light_y <= mouse_y <= right_light_y + 100 or (lights_right_on and lights_working):
                py.draw.rect(screen, (128, 128, 128), (right_light_x, right_light_y, 200, 100))
            else:
                py.draw.rect(screen, (0, 0, 0), (right_light_x, right_light_y, 200, 100))
            screen.blit(lights_button, (right_light_x, right_light_y))

    # Camera Overlap Draw Logic
    if camera_is_open:
        for ui_rect in camera_screen_bg:
            color = (0, 0, 0)       
            py.draw.rect(screen, color, ui_rect)
        
        for ui_rect in camera_button_1:
            color = (128, 128, 128) if gamestate == "nacelle1" else (0, 0, 0)       
            py.draw.rect(screen, color, ui_rect)

        for ui_rect in camera_button_2:
            color = (128, 128, 128) if gamestate == "nacelle2" else (0, 0, 0) 
            py.draw.rect(screen, color, ui_rect) 

        for ui_rect in camera_button_3:
            color = (128, 128, 128) if gamestate == "main_engineering" else (0, 0, 0)       
            py.draw.rect(screen, color, ui_rect)

        for ui_rect in camera_button_4:
            color = (128, 128, 128) if gamestate == "medbay" else (0, 0, 0)       
            py.draw.rect(screen, color, ui_rect)

        for ui_rect in camera_button_5:
            color = (128, 128, 128) if gamestate == "10_forward" else (0, 0, 0)       
            py.draw.rect(screen, color, ui_rect)

        for ui_rect in camera_button_6:
            color = (128, 128, 128) if gamestate == "shuttle_bay_1" else (0, 0, 0)       
            py.draw.rect(screen, color, ui_rect)

        for ui_rect in camera_button_7:
            color = (128, 128, 128) if gamestate == "shuttle_bay_2" else (0, 0, 0)     
            py.draw.rect(screen, color, ui_rect)

        for ui_rect in camera_button_8:
            color = (128, 128, 128) if gamestate == "bridge" else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)

        for field in active_forcefields:
            color = (0, 45, 120)
            if field == "CAM_01":
                py.draw.rect(screen, color, camera_button_1[0])
            elif field == "CAM_02":
                py.draw.rect(screen, color, camera_button_3[0])
            elif field == "CAM_03":
                py.draw.rect(screen, color, camera_button_4[0])
            elif field == "CAM_04":
                py.draw.rect(screen, color, camera_button_5[0])
            elif field == "CAM_05":
                py.draw.rect(screen, color, camera_button_6[0])
            elif field == "CAM_06":
                py.draw.rect(screen, color, camera_button_7[0])
            elif field == "CAM_07":
                py.draw.rect(screen, color, camera_button_2[0])

        screen.blit(camera_screen, (1000, 540))

    # Reboot Overlay Draw Logic
    if reboot_is_open:
        for ui_rect in reboot_menu_bg:
            py.draw.rect(screen, (0, 0, 0), ui_rect)
        for ui_rect in reboot_button_1:
            color = (128, 128, 128) if reboot_main_menu_index == 0 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        for ui_rect in reboot_button_2:
            color = (128, 128, 128) if reboot_main_menu_index == 1 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        for ui_rect in reboot_button_3:
            color = (128, 128, 128) if reboot_main_menu_index == 2 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)

        screen.blit(reboot_screen, (200, 150))
    
    if cycle_frequencies_menu_is_open:
        for ui_rect in reboot_menu_bg:
            py.draw.rect(screen, (0, 0, 0), ui_rect)
        for ui_rect in cf_button_1:
            color = (128, 128, 128) if cf_index == 0 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        for ui_rect in cf_button_2:
            color = (128, 128, 128) if cf_index == 1 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        for ui_rect in cf_button_3:
            color = (128, 128, 128) if cf_index == 2 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)

        screen.blit(cycle_frequencies_menu, (200, 160))

    if reboot_select_is_open:
        for ui_rect in reboot_menu_bg:
            py.draw.rect(screen, (0, 0, 0), ui_rect)
        for ui_rect in rs_button_1:
            color = (128, 128, 128) if rs_index == 0 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        for ui_rect in rs_button_2:
            color = (128, 128, 128) if rs_index == 1 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        for ui_rect in rs_button_3:
            color = (128, 128, 128) if rs_index == 2 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        if not power_out:
            screen.blit(rs_menu, (200, 160))
        
    # Active Progress Bar Tracking Indicator UI
    if cf_forcefields or cf_phasers or rs_lights or rs_cams:
        for ui_rect in indicator_bg:
            py.draw.rect(screen, (0, 0, 0), ui_rect)
            
        # Squares activate incrementally based on frames climbed from 0
        for ui_rect in progress1:
            color = (128, 128, 128) if reboot_timer >= 30 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        for ui_rect in progress2:
            color = (128, 128, 128) if reboot_timer >= 60 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        for ui_rect in progress3:
            color = (128, 128, 128) if reboot_timer >= 90 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        for ui_rect in progress4:
            color = (128, 128, 128) if reboot_timer >= 120 else (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)

        if cf_forcefields or cf_phasers:
            screen.blit(cf_indicator, (950, 0))
        elif rs_lights or rs_cams:
            screen.blit(reboot_indicator, (950, 0))

    # Phaser button display condition checks
    if gamestate != "bridge" and phasers_cd == 0 and phaser_shots_left > 0:
        for ui_rect in phasers_button_bg:
            if 145 <= mouse_x <= 345 and 875 <= mouse_y <= 975:
                color = (128, 128, 128)
            else:
                color = (0, 0, 0)
            py.draw.rect(screen, color, ui_rect)
        screen.blit(phasers_button, (145, 875))

    # Forcefield Action Deploy Controls
    if gamestate != "bridge" and camera_is_open:
        current_cam = gamestate_to_cam.get(gamestate)
        if len(active_forcefields) < 2 or current_cam in active_forcefields:
            for ui_rect in ff_button_bg:
                if 145 <= mouse_x <= 345 and 750 <= mouse_y <= 850:
                    color = (128, 128, 128)
                else:
                    color = (0, 0, 0)
                py.draw.rect(screen, color, ui_rect)

        if current_cam in active_forcefields:
            screen.blit(ff_remove_button, (145, 750)) 
        else:
            screen.blit(ff_deploy_button, (145, 750))

    # Deployed Forcefield Graphics
    if left_door_closed:
        left_door_x = 320 + bg_x
        left_door_y = 405
        bffL_image.set_alpha(110)
        screen.blit(bffL_image, (left_door_x,left_door_y))  
    if right_door_closed:
        right_door_x = 1950 + bg_x
        right_door_y = 405
        bffR_image.set_alpha(110)
        screen.blit(bffR_image, (right_door_x,right_door_y)) 
    if not power_out:
        screen_shader.set_alpha(80) 
        screen.blit(screen_shader, (0, 0))
    else:
        screen_shader.set_alpha(170) 
        screen.blit(screen_shader, (0, 0))

    # Timer Process Tracking Logic
    if cf_forcefields or cf_phasers or rs_lights or rs_cams:
        if reboot_timer < 120:
            reboot_timer += 1
        else:
            if cf_forcefields:
                forcefield_blocks_left = 2
                if "Shift Freq: Forcefields" in needs_action:
                    needs_action.remove("Shift Freq: Forcefields")

            if cf_phasers:
                phaser_shots_left = 2
                if "Shift Freq: Phasers" in needs_action:
                    needs_action.remove("Shift Freq: Phasers")

            if rs_lights:
                lights_working = True
                if "Reboot: Lights" in needs_action:
                    needs_action.remove("Reboot: Lights")

            if rs_cams:
                cams_working = True
                if "Reboot: Cams" in needs_action:
                    needs_action.remove("Reboot: Cams")

            # ONLY RESET HERE
            cf_forcefields = False
            cf_phasers = False
            rs_lights = False
            rs_cams = False
            reboot_timer = 0
            reboot_cd = 60

    if reboot_cd > 0:
        reboot_cd -= 1

    if phasers_cd > 0:
        phasers_cd -= 1
    
    # POWER MANAGEMENT
    if not power_out:

        drain = base_power_drain

        if left_door_closed:
            drain += 0.0035

        if right_door_closed:
            drain += 0.0035

        if lights_left_on:
            drain += 0.0015

        if lights_right_on:
            drain += 0.0015

        if camera_is_open:
            drain += 0.0005

        if reboot_is_open:
            drain += 0.0005

        power -= drain

        if power <= 0:
            power = 0
            power_out = True

            left_door_closed = False
            right_door_closed = False
            lights_left_on = False
            lights_right_on = False

            print("SHIP POWER FAILURE")

    # Tick the Borg AI forward and evaluate doorway defense mechanics
    # Tick the Borg AI forward and evaluate doorway defense mechanics
    if gamestate not in ["JUMPSCARE", "LOSS", "WIN"]:
        for borg in borg_crew:
            borg.update(active_forcefields)

            if borg.current_room == "LEFT_DOOR":
                if left_door_closed:
                    print(f"Borg {borg.id} hit the left shield door and was pushed back!")
                    borg.current_room = "CAM_04"
                    borg.door_timer = 0
                else:
                    borg.door_timer += 1
                    if borg.door_timer >= 420:
                        print("A Borg breached the left entry! Game Over.")
                        gamestate = "JUMPSCARE"

            elif borg.current_room == "RIGHT_DOOR":
                if right_door_closed:
                    print(f"Borg {borg.id} hit the right shield door and was pushed back!")
                    borg.current_room = "CAM_06"
                    borg.door_timer = 0
                else:
                    borg.door_timer += 1
                    if borg.door_timer >= 420:
                        print("A Borg breached the right entry! Game Over.")
                        gamestate = "JUMPSCARE"

    if gamestate not in ["JUMPSCARE", "LOSS", "WIN"]:
        if game_timer < 21600:
            game_timer += 1
        else:
            print("You Survived!")
            gamestate = "WIN"

    seconds_left = max(0, (21600 - game_timer) // 60)

    minutes = seconds_left // 60
    seconds = seconds_left % 60

    if power_out and gamestate not in ["JUMPSCARE", "LOSS", "WIN"]:
        camera_is_open = False
        gamestate = "bridge"
        reboot_is_open = False
        cycle_frequencies_menu_is_open = False

    if needs_action and not power_out:
        alert_message = "ALERT - " + " | ".join(needs_action)

        text_surface = ui_font.render(alert_message, True, (255, 255, 255))

        text_rect = text_surface.get_rect()
        text_rect.topleft = (20, 20) 
        screen.blit(text_surface, text_rect)
    else:
        ok_surface = ui_font.render("All Systems Nominal", True, (255, 255, 255))
        screen.blit(ok_surface, (20, 20))
    if not power_out:
        power_text = ui_font.render(
            f"Power: {int(power)}%",
            True,
            (255,255,255)
        )
        timer_text = ui_font.render(
        f"Survive: {minutes:02}:{seconds:02}",
        True,
        (255,255,255)
        )

        screen.blit(timer_text, (20,100))
        screen.blit(power_text, (20, 60))

    py.display.flip()
    clock.tick(60)
py.quit()
sys.exit()
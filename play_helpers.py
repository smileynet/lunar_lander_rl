import pygame
from pygame.locals import (
    K_UP, K_LEFT, K_RIGHT, K_w, K_a, K_d, K_ESCAPE, K_SPACE
)

# Constants for scaling and display
SCALE_FACTORS = {
    'x': 10,
    'y': 6.666,
    'vx': 5,
    'vy': 7.5,
    'angle': 1,  # radians, no need to scale
    'angular_velocity': 2.5  # radians/second
}

FPS = 60  # Frames per second for rendering
speed_multiplier = 0.5  # Start at half speed

def get_framerate():
    global speed_multiplier
    return FPS * speed_multiplier

def print_instructions():
    """Prints the game instructions."""
    print("Control the lander using the following keys:")
    print("Up Arrow or W: Fire main engine (upward thrust)")
    print("Left Arrow or A: Fire right engine (rotate counterclockwise)")
    print("Right Arrow or D: Fire left engine (rotate clockwise)")
    print("Spacebar: Toggle between half and full speed (default is half speed)")
    print("Press ESC to quit the game")

def handle_controls():
    """
    Handles user input and returns the action to take and speed multiplier.
    Also checks for game exit conditions.
    """
    action = 0  # Default action: Do nothing
    done = False
    speed_changed = False
    global speed_multiplier  # Access the global speed_multiplier variable

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
            elif event.key == K_SPACE:
                toggle_speed()
                speed_changed = True

    keys = pygame.key.get_pressed()

    if keys[K_UP] or keys[K_w]:
        action = 2  # Fire main thruster (upward thrust)
    elif keys[K_LEFT] or keys[K_a]:
        action = 1  # Fire right thruster (rotate counterclockwise)
    elif keys[K_RIGHT] or keys[K_d]:
        action = 3  # Fire left thruster (rotate clockwise)

    return action, done, speed_changed

def toggle_speed():
    """Toggles the game speed between half and full speed."""
    global speed_multiplier
    if speed_multiplier == 0.5:
        speed_multiplier = 1.0
    else:
        speed_multiplier = 0.5

def display_stats(screen, font, obs, cumulative_score):
    """
    Displays the state variables and cumulative score on the screen.
    """
    global speed_multiplier  # Add this line to access the global variable

    # Unpack observation state variables
    x, y, vx, vy, angle, angular_velocity, _, _ = obs

    # Apply scaling factors
    x_scaled = x * SCALE_FACTORS['x']
    y_scaled = y * SCALE_FACTORS['y']
    vx_scaled = vx * SCALE_FACTORS['vx']
    vy_scaled = vy * SCALE_FACTORS['vy']
    angular_velocity_scaled = angular_velocity * SCALE_FACTORS['angular_velocity']

    # Prepare state text for display
    state_text = [
        f"x: {x_scaled:.2f} units",
        f"y: {y_scaled:.2f} units",
        f"vx: {vx_scaled:.2f} units/second",
        f"vy: {vy_scaled:.2f} units/second",
        f"angle: {angle:.2f} radians",
        f"angular velocity: {angular_velocity_scaled:.2f} radians/second",
        f"Score: {cumulative_score:.2f}",
        f"Speed: {'Full' if speed_multiplier == 1.0 else 'Half'}"  # Add this line
    ]

    # Render and display the text overlay
    for i, text in enumerate(state_text):
        rendered_text = font.render(text, True, (255, 255, 255))  # White text
        screen.blit(rendered_text, (10, 10 + i * 20))

def is_off_screen(obs, screen_width, screen_height):
    """
    Check if the lander is off-screen based on its x and y coordinates.
    """
    x, y, _, _, _, _, _, _ = obs
    x_scaled = x * SCALE_FACTORS['x']
    y_scaled = y * SCALE_FACTORS['y']

    margin = 10  # Allow 10 pixels of margin
    return (x_scaled < -margin or x_scaled > screen_width + margin or
            y_scaled < -margin or y_scaled > screen_height + margin)

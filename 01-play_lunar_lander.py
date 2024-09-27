import pygame
import gymnasium as gym
import numpy as np
from play_helpers import print_instructions, handle_controls, display_stats, get_framerate, is_off_screen


def main():
    """Main function to run the Lunar Lander game."""
    # Initialize the environment with 'rgb_array' render mode
    env = gym.make("LunarLander-v2", render_mode="rgb_array")
    env.reset()

    # Get the initial image to determine the screen size
    image = env.render()
    screen_width, screen_height = image.shape[1], image.shape[0]

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Lunar Lander Controls")

    # Print game instructions
    print_instructions()

    # Pygame font setup
    font = pygame.font.SysFont("Arial", 18)

    clock = pygame.time.Clock()
    cumulative_score = 0  # Initialize cumulative score

    while True:
        # Handle user input and game controls
        action, done, _ = handle_controls()
        if done:
            break

        # Step through the environment with the chosen action
        obs, reward, terminated, truncated, info = env.step(action)

        # Check if the lander is off-screen
        if is_off_screen(obs, screen_width, screen_height):
            print(f"Lander went off-screen! Game over. Final score: {cumulative_score:.2f}")
            terminated = True

        # Accumulate the score
        cumulative_score += reward

        # Get the image from the environment
        image = env.render()

        # Convert the image to a pygame surface
        image = np.transpose(image, (1, 0, 2))  # Swap axes 0 and 1
        surface = pygame.surfarray.make_surface(image)

        # Blit the surface onto the screen
        screen.blit(surface, (0, 0))

        # Display state variables and score
        display_stats(screen, font, obs, cumulative_score)

        # Update the pygame display
        pygame.display.flip()

        # Ensure the loop runs at the defined FPS adjusted by speed multiplier
        clock.tick(get_framerate())

        # Reset the environment if the game is done or truncated
        if terminated or truncated:
            print(f"Game over! Final score: {cumulative_score:.2f}")
            obs, info = env.reset()
            cumulative_score = 0  # Reset the cumulative score

    # Quit pygame and close the environment
    pygame.quit()
    env.close()

if __name__ == "__main__":
    main()
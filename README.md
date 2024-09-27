# Lunar Lander Reinforcement Learning Project 🚀

Welcome to the **Lunar Lander RL** project! In this project, you'll train an AI agent to play the Lunar Lander game using Reinforcement Learning (RL) techniques. 

It is recommended  set up your environment using **Mamba**, a fast version of Conda, for managing dependencies.

## Prerequisites

Before you get started, ensure you have the following installed on your machine:

1. **Mamba** (recommended) or **Conda**:  
   Mamba is a drop-in replacement for Conda that significantly speeds up environment creation and package installation.  
   You can install Mamba following [this guide](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html).

   If you prefer to stick with Conda, just replace `mamba` with `conda` in the commands provided in this README.

2. **Git**:  
   Make sure Git is installed so you can clone the project repository.

## Getting Started

Follow these steps to set up your environment and run the project:

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/smileynet/lunar-lander-rl.git
cd lunar-lander-rl
```

### 2. Create the Environment with Mamba

To set up the project environment, you’ll need to create it using the provided `environment.yml` file. This file includes all the dependencies required for the project, including Python, Gymnasium, Stable Baselines 3, and Pygame.

Run the following command to create the environment using **Mamba**:

```bash
mamba env create -f environment.yml
```

If you’re using **Conda** instead of Mamba, you can run:

```bash
conda env create -f environment.yml
```

### 3. Activate the Environment

Once the environment is created, activate it:

```bash
mamba activate lunar_lander_rl
```

### 4. Verify Installation

To verify that the environment is set up correctly, you can run the following command to list installed packages:

```bash
mamba list
```

Make sure all the key packages (like `gymnasium`, `stable-baselines3`, and `pygame`) are installed.

### 5. Running the Code

Once the environment is activated, you can run the provided scripts to experiment with Lunar Lander and Reinforcement Learning.

For example, try launching the game in Human Mode to play manually:

```bash
python 01-play_lunarlander.py
```

## Updating the Environment

If you add new dependencies to the `environment.yml` file, you can update your environment by running:

```bash
mamba env update --file environment.yml --prune
```

This will install any new dependencies and remove unused ones.

## Deactivating the Environment

When you're done working on the project, deactivate the environment by running:

```bash
mamba deactivate
```

## Removing the Environment

If you ever need to remove the environment entirely, run:

```bash
mamba env remove -n lunar_lander_rl
```

---

## Additional Resources

- [Stable Baselines 3 Documentation](https://stable-baselines3.readthedocs.io/en/master/)
- [Gymnasium Documentation](https://gymnasium.farama.org/)
- [Pygame Documentation](https://www.pygame.org/docs/)

---

Happy landings! 🌕🚀
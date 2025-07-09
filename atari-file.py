import gymnasium as gym

# Create environment
env = gym.make('FrozenLake-v1', render_mode='human')
obs, info = env.reset()

print("Starting FrozenLake-v1 Environment")
print("Action space:", env.action_space)
print("Observation space:", env.observation_space)
print("-" * 40)

total_reward = 0
step_count = 0

# Main loop
while True:
    step_count += 1
    
    # Take random action
    action = env.action_space.sample()
    
    # Step environment
    next_state, reward, done, truncated, info = env.step(action)
    
    # Update total reward
    total_reward += reward
    
    # Print required information
    print(f"Step {step_count}:")
    print(f"  Action taken: {action}")
    print(f"  Next state: {next_state}")
    print(f"  Reward: {reward}")
    print(f"  Total reward: {total_reward}")
    print(f"  Done: {done}")
    print(f"  Truncated: {truncated}")
    
    # Check termination
    if done or truncated:
        print(f"\nEpisode finished after {step_count} steps")
        print(f"Final reward: {total_reward}")
        if done:
            print("Goal reached or fell in hole!")
        if truncated:
            print("Max steps exceeded!")
        break

env.close()
print("Environment closed")
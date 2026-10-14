# Important Notes

## Huggingface Deep RL Course
### UNIT 1

- The goal of any RL agent is to maximize its *expected cumulative reward* (also called *expected return*)
- Discounting is the idea that a reward you get in the future is worth a little less than a reward you can get right now as they are more likely to happen as they are more predictable.
- Gamma is a number between 0 and 1 that controls how much we care about future rewards compared to immediate rewards.
- There are two ways to find your optimal policy:  
By training your policy directly: policy-based methods.  
By training a value function that tells us the expected return the agent will get at each state and use this function to define our policy: value-based methods.
- *Markov Property* : action taken by agent is conditional on present state and is independent of past states and actions.

---
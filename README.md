# gym_dm_control

gym_dm_control is a small wrapper to make [DeepMind Control Suite](https://github.com/deepmind/dm_control) environments available for [OpenAI Gym](https://github.com/openai/gym).

modify the code from https://github.com/martinseilair/dm_control2gym

## Installation

```shell
$ git clone https://github.com/adwardlee/gym_dm_control/
$ cd gym_dm_control
$ pip install .
```

Tested with Python 3.6.4 and Ubuntu 17.04.

## Quick start

```python
import gym
import gym_dm_control

# make the dm_control environment
env = gym_dm_control.make(domain_name="cartpole", task_name="balance")

# use same syntax as in gym
env.reset()
for t in range(1000):
    observation, reward, done, info = env.step(env.action_space.sample()) # take a random action
    env.render(mode='human')

```

## Short documentation

### Spaces and Specs

The dm_control specs are converted to spaces. If there is only one entity in the observation dict, the original shape is used for the corresponding space. Otherwise, the observations are vectorized and concatenated.
Note, that the pixel observation is processed separately through the render routine.

The difference between the `Discrete` and the corresponding `ArraySpec` with type `np.int`, is that the domain `ArraySpec` is arbitrary and of that the domain of `Discrete` always starts at 0. Therefore, the domain is shifted  to obtain a valid `Discrete` space.

### Rendering
Three rendering modes are available by default:

* `human`: Render scene and show it
* `return`: only return it as rgb array


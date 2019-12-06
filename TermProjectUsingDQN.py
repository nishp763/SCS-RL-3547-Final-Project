#!/usr/bin/env python
# coding: utf-8

# In[3]:



# In[1]:


#  A car is on a one-dimensional track, positioned between two "mountains".
#  The goal is to drive up the mountain on the right; however,
#  the car's engine is not strong enough to scale the mountain in a single pass. Therefore,
#  the only way to succeed is to drive back and forth to build up momentum.


import gym
import random
from keras import Sequential
from collections import deque
from keras.layers import Dense
from keras.optimizers import adam
import matplotlib.pyplot as plt
from keras.activations import relu, linear
from keras import models

import numpy as np
env = gym.make('LunarLander-v2')
env.seed(0)
np.random.seed(0)


class DQN:

    """ Implementation of deep q learning algorithm """

    def __init__(self, action_space, state_space):

        self.action_space = action_space
        self.state_space = state_space
        self.epsilon = 1.0
        self.gamma = .99
        self.batch_size = 64
        self.epsilon_min = .01
        self.lr = 0.001
        self.epsilon_decay = .996
        self.after_time_steps_update_weights =100
        self.memory = deque(maxlen=1000000)
        self.model = self.build_model()
        self.clonemodel = self.build_clone_model()

    def build_clone_model(self):
        model = Sequential()
        model.add(Dense(100, input_dim=self.state_space, activation=relu))
        model.add(Dense(50, activation=relu))
        model.add(Dense(self.action_space, activation=linear))
        model.compile(loss='mse', optimizer=adam(lr=self.lr))
        print(model.summary())
        return model
    def build_model(self):

        model = Sequential()
        model.add(Dense(100, input_dim=self.state_space, activation=relu))
        model.add(Dense(50, activation=relu))
        model.add(Dense(self.action_space, activation=linear))
        model.compile(loss='mse', optimizer=adam(lr=self.lr))
        print(model.summary())
        return model

    def add_to_replay_mem(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act_state(self, state):
    # action is selected through exploration or exploitation
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_space)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self):

        if len(self.memory) < self.batch_size:
            return


        minibatch = random.sample(self.memory, self.batch_size)
        states = np.array([i[0] for i in minibatch])
        actions = np.array([i[1] for i in minibatch])
        rewards = np.array([i[2] for i in minibatch])
        next_states = np.array([i[3] for i in minibatch])
        dones = np.array([i[4] for i in minibatch])

        states = np.squeeze(states)
        next_states = np.squeeze(next_states)

        #once we have q* function in this case targets, we can determine the optimal
        # policy by applying reinforcement learning to find the action that maximizes q* for each state
        targets = rewards + self.gamma*(np.amax(self.clonemodel.predict_on_batch(next_states), axis=1))*(1-dones)
        # policy network
        targets_full = self.clonemodel.predict_on_batch(states)
        ind = np.array([i for i in range(self.batch_size)])
        targets_full[[ind], [actions]] = targets
        self.model.fit(states, targets_full, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

def train_dqn(episode):

    loss = []
    agent = DQN(env.action_space.n, env.observation_space.shape[0])
    counter =0
    for e in range(episode):
        state = env.reset()
        state = np.reshape(state, (1, 8))
        score = 0
        max_steps = 3000
        for i in range(max_steps):
            action = agent.act_state(state)
            env.render()
            next_state, reward, done, _ = env.step(action)
            score += reward
            next_state = np.reshape(next_state, (1, 8))
            agent.add_to_replay_mem(state, action, reward, next_state, done)
            state = next_state
            agent.replay()
            counter +=1
            if done:
                print("episode: {}/{}, score: {}".format(e, episode, score))
                break
            if agent.after_time_steps_update_weights == counter:
                modelsweights = np.array(agent.model.get_weights())
                clonemodel_weights = np.array(agent.clonemodel.get_weights())
                agent.clonemodel.set_weights(modelsweights)
                counter =0
        loss.append(score)

        # Average score of last 100 episode
        is_solved = np.mean(loss[-100:])
        if is_solved > -5:
            print('\n Task Completed! \n')
            env.close()
            break
        print("Average over last 100 episode: {0:.2f} \n".format(is_solved))
    return loss


if __name__ == '__main__':
    print(env.observation_space)
    print(env.action_space)
    episodes = 400
    loss = train_dqn(episodes)
    plt.plot([i+1 for i in range(0, len(loss), 2)], loss[::2])
    plt.show()


# In[ ]:





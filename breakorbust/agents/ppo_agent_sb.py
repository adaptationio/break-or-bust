import time

import gym
import numpy as np
import os
import datetime
import csv
import argparse
from functools import partial

from stable_baselines.common.policies import MlpLnLstmPolicy, FeedForwardPolicy, LstmPolicy, CnnPolicy
from stable_baselines.common.vec_env import DummyVecEnv, SubprocVecEnv,VecNormalize 
from stable_baselines.common import set_global_seeds
from stable_baselines import ACKTR, PPO2
from stable_baselines.deepq import DQN
from ..env import Template_Gym
from ..agents.policy import *

timestamp = datetime.datetime.now().strftime('%y%m%d%H%M%S')

class PPO2_SB():
    def __init__(self):
        self.love = 'Ramona'
        self.env_fns = [] 
        self.env_names = []
    
    def make_env(self, env_id, rank, seed=0):
        """
        Utility function for multiprocessed env.
    
        :param env_id: (str) the environment ID
        :param num_env: (int) the number of environment you wish to have in subprocesses
        :param seed: (int) the inital seed for RNG
        :param rank: (int) index of the subprocess
        """
        def _init():
            env = Template_Gym()
            env.seed(seed + rank)
            return env
        set_global_seeds(seed)
        return _init
    

    def train(self, num_e=1, n_timesteps=1000000, save='saves/agent4'):
        env_id = "default"
        num_e = 1  # Number of processes to use
        # Create the vectorized environment
        #env = DummyVecEnv([lambda: env])
        

        self.env = SubprocVecEnv([self.make_env(env_id, i) for i in range(num_e)])
        self.env = VecNormalize(self.env, norm_obs=True, norm_reward=True)
        #self.model = PPO2(policy=CnnPolicy,
                      #env=SubprocVecEnv(self.env_fns),
                      #n_steps=8192,
                      #nminibatches=8,
                      #lam=0.95,
                      #gamma=0.99,
                      #noptepochs=4,
                      #ent_coef=0.001,
                      #learning_rate=lambda _: 2e-5,
                      #cliprange=lambda _: 0.2,
                      #verbose=1,
                      #tensorboard_log="./breakorbust")
        self.model = PPO2(CustomPolicy, env=self.env, verbose=0, learning_rate=1e-5, tensorboard_log=save )
        for i in range(10):
            self.model.learn(n_timesteps)
            self.model.save(save)
    
    
    def evaluate(self, num_env=1, num_steps=14400):
        """
        Evaluate a RL agent
        :param model: (BaseRLModel object) the RL Agent
        :param num_steps: (int) number of timesteps to evaluate it
        :return: (float) Mean reward
        """
        env_id = "default"
        num_e = 1
        self.env = SubprocVecEnv([self.make_env(env_id, i) for i in range(num_e)])
        self.model = PPO2.load('saves/agent.pkl', self.env, policy=CustomPolicy, tensorboard_log="./ppocnn/" )
        

        episode_rewards = [[0.0] for _ in range(self.env.num_envs)]
        obs = self.env.reset()
        for i in range(num_steps):
            # _states are only useful when using LSTM policies
            actions, _states = self.model.predict(obs)
            # # here, action, rewards and dones are arrays
            # # because we are using vectorized env
            obs, rewards, dones, info = self.env.step(actions)
      
      # Stats
            for i in range(self.env.num_envs):
                episode_rewards[i][-1] += rewards[i]
                if dones[i]:
                    episode_rewards[i].append(0.0)

        mean_rewards =  [0.0 for _ in range(self.env.num_envs)]
        n_episodes = 0
        for i in range(self.env.num_envs):
            mean_rewards[i] = np.mean(episode_rewards[i])     
            n_episodes += len(episode_rewards[i])   

    # Compute mean reward
        mean_reward = np.mean(mean_rewards)
        print("Mean reward:", mean_reward, "Num episodes:", n_episodes)

        return mean_reward

        
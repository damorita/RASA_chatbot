# This file let's you interact with the bot to teach it new stories.
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.train import online


logger = logging.getLogger(__name__)


def run_online(interpreter,domain_file="./domain.yml",training_data_file='./backend/stories.md'):					  
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), KerasPolicy()],
                  interpreter=interpreter) 
    				  
    data = agent.load_data(training_data_file)
    agent.train(data,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)				   
    online.serve_agent(agent)
    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current')
    run_online(nlu_interpreter)
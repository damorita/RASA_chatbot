# This code run's the chat bot script
# This Section, imports required packages
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

import logging
logger = logging.getLogger(__name__)

# disables all warnings
import warnings
warnings.filterwarnings("ignore")

# disables the CPU warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Talk to the agent (bot)
def run_bot(serve_forever=True):
    #Load Trained NLu and Model to Agent
    nlu_interpreter = RasaNLUInterpreter('./backend/models/nlu/default/current')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./backend/models/dialogue', interpreter = nlu_interpreter, action_endpoint=action_endpoint)
    
    print("Your bot is ready to talk! Type your messages here or send 'stop'")
    while True:
        a = input()
        if a == 'stop':
            break
        responses = agent.handle_message(a)
        for response in responses:
            print(response["text"])
    return agent        


if __name__ == '__main__':
	run_bot()
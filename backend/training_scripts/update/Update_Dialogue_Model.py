# This updates the directory: ./models/dialogue

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = './backend/domain.yml',
					model_path = './backend/models/dialogue',
					training_data_file = './backend/stories.md'):
	fallback = FallbackPolicy(fallback_action_name="utter_unclear", core_threshold=0.1, nlu_threshold=0.1)				
	agent = Agent(domain_file, policies = [fallback, MemoizationPolicy(), KerasPolicy()])
	data = agent.load_data(training_data_file)	
	agent.train(
				data,
				epochs = 200,
				batch_size = 50,
				validation_split = 0.2)
				
	agent.persist(model_path)
	return agent
	
train_dialogue()
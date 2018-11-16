from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):  # Trains the NLU model using the intent file, config file, and nlu model location as inputs
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	trainer.persist(model_dir, fixed_model_name = 'current')
	
def run_nlu(message): # Send the nlu model a message to parse.
	interpreter = Interpreter.load('./backend/models/nlu/default/current') 
	print(interpreter.parse(message))
	
if __name__ == '__main__': #Run the above functions	
	train_nlu('./backend/chatbot_nlu_def.md', './backend/config.yml', './backend/models/nlu')  #Alternative command: train_nlu('./chatbot_nlu_def.md', 'config.yml', './models/nlu')
	run_nlu("Hello")
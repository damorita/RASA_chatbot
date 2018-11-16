# RASA_chatbot
---
The following rasa chatbot are based on the templates provided by the following blogs by Justina and Jason:

https://jpboost.com/2018/02/06/creating-a-chatbot-with-rasa-nlu-and-rasa-core/

http://smithstrategy.com/index.php/2018/02/28/chatbot-tutorial-using-rasa-and-docker/

https://github.com/tmbo/rasa-demo-pydata18

---
## Pre Req
Build Tools for Visual Studio 2017:    https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2017
pip install rasa_core
pip install rasa_nlu
pip install tensorflow

---
## Run Your Chatbot App

All scripts related to running your app are located in backend/app_scripts/
To run your (flask) chatbot app you can either...

+ run *app_scripts/Run_All.ps1* 

or take the following steps:

1. Start the Action Server: *backend/app_scripts/1_Start_Action_Server.ps1*
2. Start the Rasa Chatbot Server: *backend/app_scripts/2_Start_Rasa_Engine.ps1*
3. Start the FrontEnd: *frontend/flask/app.py*
4. Open a browser and enter: http://localhost:8080/
5. Start chatting!

---
## Training Your Chatbot

When training your chat bot, there are two major components: **1) Training the NLU (Natural Language Understanding)** & **2) Training the Dialogue (How the Bot needs to respond after a user input)**
The training scripts are all located under *backend/training_scripts* . To update the training files and model for both NLU & Dialogue of your chatbot, you can just run *training_scripts/1_Run_Build_Scripts* & *training_scripts/2_Run_Update_Scripts*
To train each sections individually, read the next section.

### Training NLU:
To train the nlu of the chatbot, you will need to update files pertaining to intents (includes entities & slots), synonyms and regex. All of this get aggregated into the chatbot_nlu_def.md file.
1. Under the backend/nlu/ folder, you will find folders for intents, regex, and synonyms. Add new md files for new nlu. Otherwise you can edit existing files.
2. Run the *training_scripts/build/build_nlu_file.py* to update the chatbot_nlu_def.md file
3. Run the the *training_scripts/update/Update_NLU_Model.py* to update the model with the new contents that were written to chatbot_nlu_def.md

### Training Dialogue:
To train the dialogue of the chatbot, you will need to update files pertaining to stories (includes entities & slots),  and domain. All of this get aggregated into the stories.md and domain.yml file.
1. Under the backend/domain/ folder, you will find folders for utterances and files for actions, slots, entities and intents. Add new yml files for new content. Otherwise you can edit existing files.
2. Run the *training_scripts/build/build_domain_file.py* to update the domain.yml file. 
3. If you would like to train your bot and add new stories by conversation, run the *training_scripts/train_online.py*. Otherwise Run the the *training_scripts/update/Update_Dialogue_Model.py* to update the model with the new contents

### Talk to Your Trained Chatbot:
Once your chatbot is adequately trained, you can run the scripts under the *training_scripts/start/* folder, or just run *training_scripts/3_Run_Start_Scripts*

1. Start the Action Server by running *training_scripts/start/Start_Action_Server.ps1*. This registers any custom actions in action.py
2. Start the Chat in terminal by running *training_scripts/start/Start_Chat_Terminal.py*
3. If Chatbot is not responding with appropriate response, you can teach it by running *training_scripts/Train_Online.py*

---

## Important Files

+ **actions.py:** 
    + Contains custom scripts chatbot will call. Ex) API calls, SQL queries, etc.  The run_action_server script registers the actions in action.py
+ **chatbot_nlu_def.md:** 
    + Contains training samples of intents, synonyms, regex text a user might input. Entites are also defined in this file. This file is an aggregation of all the files located in backend/nlu
+ **config_spacy.json:**
    + Defines the pipeline configuration for the natural language and machine learning options. Spacy is an open source nlu library. sklearn is a collection of python machine learning packages.
+ **domain.yml:**
    + Defines all intents, actions, slots, entities, and utterance options the bot is allowed to use.
+ **endpoints.yml:**
    + Defines the location of where to send action server requests
+ **stories.md:**
    + Defines the sequence of responses a conversation between a user and the bot can go.

---

## Folder Structure
+ backend
    - /**app_scripts:**
        + Contains scripts necessary to run your chatbot app
    - /**domain:** 
        + Contains Domain files to define what actions, intents, responses the chatbot will have
    - /**models:**
        + Contains nlu model and the dialogue model configurations the chatbot will use to conversate
        + models/nlu/ contains the most current trained nlu files the chatbot will use to *understand* user input
        + models/dialogue/ model contains trained dialogue files the chatbot will use to *respond* to the user
    - /**nlu:**
        + Contains the NLU TRAINING data to teach the chatbot natural language such as intents, synonyms, regex
    - /**training_scripts:**
        + Contains scripts necessary to train your chatbot with new information


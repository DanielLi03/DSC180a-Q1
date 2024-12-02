# DSC180a

## Project Overview
My Quarter 1 Guardrail Replication Project focused on implementing a profanity and toxicity guardrail on basic English to French translation app. The LLM I used was Helsinki-NLP/opus-mt-en-fr on hugging face, which is a powerful translation LLM that is part of the Opus family, hosted on hugging face. The particular model I used translates English language to French. My intended idea of the translation app is so that you can use it to translate tweets from English to French, while censoring toxic or hateful tweets during the translation process. This way, I can promote a positive social media environment across multi-lingual barriers, even in an app like Twitter. As such, I focused on toxicity guardrails that were trained on twitter datasets, which classified each tweet as toxic or not. I used two guardrails called Detoxify and Profanity_check. Detoxify is ML model trained on the Jigsaw Unintended Bias in Toxicity Classification Dataset and the Toxic Comment Classification Challenge, both on Kaggle. Profanity_check is an ML model trained on a curated dataset hosted on github at t-davidson/hate-speech-and-offensive-language, as well as the Toxic Comment Classification Challenge on Kaggle. My project shows the effectiveness of both guardrails, as well as their synergy together to provide an efficient and function guardrail for a translation app

## Files Overview

## How to Install and Setup
First we need to clone the respository. So open up a terminal, navigate to the desired folder and clone the respository as follows:

```
git clone https://github.com/DanielLi03/DSC180a-Q1.git
```

Next we need to create a conda environment. So open up an anaconda terminal, and run the following command (replace [name] with the name the your envirnment that you'd like)

```
conda create -n [name]
```

We also need to install the dependencies, so we first activate the conda environment in the ananconda terminal as follows:
```
conda activate [name]
```

Now that our conda environment is active, in the same terminal, run the following to install all the dependencies:
```
pip install -r requirements.txt
```

All our packages should be installed in our anaconda environment so we should be ready to run the code now

## How to Run Tests
To run both the short and long toxic tests, activate the anaconda environment that you've created above. Navigate the github repo on your local device in the conda terminal, and run the python file as follows:
```
python short_toxic_test.py
```

For the long_toxic_test.py, simply run in your conda environment.
```
python long_toxic_test.py
```

Note: these tests will take several minutes to run, and might download some ML model if it's your first time running it. There will also be warnings, but they shouldn't affect the ability to run the code at all. Ignoring the warnings, the expected output after running both python in the terminal should be two dictionaries containing various metrics on the accuracy of the toxicitiy classification of detoxify and profanity_check. The first dictionary corresponds to the results of profanity_check, and the second more detailed dictionary corresponds to the results of detoxify. If run correctly, we should expect the following results in the terminal:


## How to Run App.py

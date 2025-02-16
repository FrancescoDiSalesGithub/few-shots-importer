# few-shots-importer
does a few shots prompt by using command instruction on a ollama modelfile

# How to create the dataset
It is important to create a json like the following:
```
{

"prompts":[
    {"who is the famous superhero that climbs on walls?":"spiderman"},
    {"who is the famous superhero that turns green when he is angry?":"HULK"}
  ]

}

```

# How to run
Just run the python script as the following:

```
python3 few-shots-importer.py OLLAMA_MODEL PATH_MODELFILE your-dataset.json

```

Where:
* OLLAMA_MODEL is the model you are going to use (mistral,deepseek,qwen and so on)
* PATH_MODELFILE the path where the new generated modelfile will be saved

Example:

```
python3 few-shot-importer.py mistral /home/myuser/Modelfile dataset.json

```
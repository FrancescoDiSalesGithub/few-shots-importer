import sys
import json

if __name__ == "__main__":


    if len(sys.argv) < 3:
        print("No or few parameters have been passed")
        print("Run this script as the following:")
        print("python3 few-shots-importer.py OLLAMA_MODEL PATH_MODELFILE your-dataset.json")
    else:
        with open(sys.argv[3],"r") as json_file:
            dataset_to_save=json.load(json_file)
            
            with open(sys.argv[2],"w") as modelfile:
                modelfile.write("from "+sys.argv[1]+"\n")
                for item in dataset_to_save["prompts"]:
                    item_key=list(item.keys())
                    item_value=list(item.values())
                    modelfile.write("message user "+item_key[0]+"\n")
                    modelfile.write("message assistant "+item_value[0]+"\n")

        print("few-shot import completed!")    


   

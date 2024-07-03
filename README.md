## Kestra Script Repo
Allows me to make scripts, deploy them and access them dynamically on kestra


Can use pipreqs for generating requirements

pip install pipreqs

// Inside the directory of the script to insall dependencies
pipreqs ./


Then tell kestra with

pip install -r requirements.txt > /dev/null
# WINE QUALITY PREDITION WITH ML FLOW 


### Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py


# Steps To Run?

### STEP 01- Clone the repository

```bash
https://github.com/Anshidtp/Mechine-Learning-Project-with-ML-flow.git
```
### STEP 02- Create a conda environment after opening the repository

```bash
conda create -n <env_name> python=3.8 -y
```

```bash
conda activate <env_name>
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### DagsHub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Anshidtp/Mechine-Learning-Project-with-ML-flow.mlflow \
MLFLOW_TRACKING_USERNAME=Anshidtp \
MLFLOW_TRACKING_PASSWORD=033086fc4cab9d5f891e7ab7e877cf8c49ca4a46 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Anshidtp/Mechine-Learning-Project-with-ML-flow.mlflow

export MLFLOW_TRACKING_USERNAME=Anshidtp

export MLFLOW_TRACKING_PASSWORD=033086fc4cab9d5f891e7ab7e877cf8c49ca4a46

```

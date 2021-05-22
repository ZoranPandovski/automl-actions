# AutoML GitHub Action

>**Easly do data analysis, train new model and get the prediction as an output using :bear:MindsDB:bear: inside GitHub Actions.**

## Usage

Inside your workflow.yml file add:

```yaml
job_name:
  runs-on: ubuntu-latest
  name: A job to train new model
  steps:
  - name: Train new model
    id: train
    uses: ZoranPandovski/automl-actions@main
    with:
      dataset: "home_rentals.csv"
      target: "price"
      when: "{sqft: 500, rooms: 5}"
```

### Inputs

| Name 	| Required 	| Description 	|  	|  	|
|-	|-	|-	|-	|-	|
| dataset 	| Yes 	| The path or URL to data. Can be path to the data file inside the repository or any public acessible URL as path to s3 file, raw github file, public JSON API etc. 	|  	|  	|
| target 	| Yes 	| The name of the variable that needs to be predicted. 	|  	|  	|
| when 	| Yes 	| The data that you want to make a prediction for e.g {"key" : "value", "key": "value"} 	|  	|  	|
| stop_training 	| No 	| Stop model training after X seconds. 	|  	|  	|

### Outputs

| Name 	| Description 	|  	  	
|-	|-	|
| prediction 	| The predicted value 	|  	


### :construction_worker:  :construction:  Roadmap :construction_worker:  :construction: 

- [X] **v1.0.0**
    * POC
    * Accept input as dataset, target variable, query.
    * Return prediction as output.
- [ ] **v2.0.0**
    * Add option for batch prediction using data in repo file or public accesible data.
    * Add option for data analysis as output.
    * Accept timeseries parameters as input e.g order_by, group_by.
- [ ] **v3.0.0**
    * Add option to upload a model to s3, GitHub repo, azure blob storage etc.

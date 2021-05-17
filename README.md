# AutoML GitHub Action


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
      dataset: "URL to data"
      target: "target_var"
```

### Inputs

| Name 	| Required 	| Description 	|  	|  	|
|-	|-	|-	|-	|-	|
| dataset 	| Yes 	| The path or URL to data. Can be path to the data file inside the repository or any public acessible URL as path to s3 file, raw github file, public JSON API etc. 	|  	|  	|
| target 	| Yes 	| The name of the variable that needs to be predicted. 	|  	|  	|
| stop_training 	| No 	| Stop model training after X seconds. 	|  	|  	|

### Outputs



## Diabetes Analysis & Prediction 

### Description

Analysis and prediction of the diabetes dataset.

### Installation

NOTE: Python3 must be already installed.
```shell
git clone https://github.com/Vasyl-Poremchuk/diabetes-analysis-and-prediction
cd diabetes_analysis_and_prediction
python -m venv venv
venv\Scripts\activate (Windows) or source venv/bin/activate (Linux or macOS)
pip install -r requirements.txt
```

### Diabetes Dataset
A dataset from the **Mendeley Data** website was taken to analyze and predict diabetes. You can check more detailed information about the dataset, namely about the author, about the description, about the license and other data at this [link](https://data.mendeley.com/datasets/wj9rwkp9c2/1).
<br>NOTE: This dataset is used for education purposes only. No data was changed.

### Data Analysis & Prediction

* This part consists of:
    * Load the diabetes dataset;
    * Clean and preprocess dataframe;
    * Exploratory Data Analysis;
    * Prepare data for modeling | Model Training | Model Evaluation (Decision Trees Model);
    * Prepare data for modeling | Model Training | Model Evaluation (Random Forest Model);
    * Conclusion.

### Running the application on the local machine

```shell
python -m app
```

### Running the application from a Dockerfile

Build the Docker image:

```shell
docker build -t diabetes-analysis-and-prediction .
```

Run the container:

```shell
docker run -p 5000:5000 diabetes-analysis-and-prediction
```

### Demo
![prediction_demo_image](/static/images/prediction.png)

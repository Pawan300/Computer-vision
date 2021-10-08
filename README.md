<h1>Content based recommendation for Chingari</h1>

Project Structure
```
├── README.md                       <- The top-level README for developers using this project.
├── config
│   ├── constant.json               <- This file will contain all the constant which we will use in the python code.
|
├── dags                            <- This folder will contain all the file which is required for a airflow dag to run.
|   ├── mongo_connect.py            <- This file will help you operate mongo.
|   ├── gen_reco_content_base.py    <- This is the main content base recommendation file.
│   ├── dag_content_base.py         <- This is containing file for airflow for a cron service.
|
├── notebooks          <- Jupyter notebooks. This for testing purpose.
```

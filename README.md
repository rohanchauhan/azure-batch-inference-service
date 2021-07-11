# Lead Scoring Pyspark Batch Inference Pipeline
In this project, we [UCI Bank Marketing](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing) dataset for lead scoring. Lead classification is used to score leads based on the information we gather. It is different from lead qualification which is used to identify ideal customers. Lead scoring helps sales and marketing team focus their efforts on customers who are most likely to buy.

## Model Selection
| **Model**               | **Accuracy** | **Area under ROC** | **Area under PR** |
|-------------------------|--------------|--------------------|-------------------|
| Logistic Regression     | 0.891        | 0.878              | 0.488             |
| SVM                     | 0.905        | 0.933              | 0.581             |
| Decision Tree           | 0.916        | 0.638              | 0.421             |
| Random Forest           | 0.913        | 0.915              | 0.658             |
| Gradient Boosting Trees | 0.919        | 0.948              | 0.663             |


# -Student-Performance-Prediction-Using-Linear-Regression

## Project Overview
This project analyzes student performance using linear regression techniques to identify key factors influencing academic achievement. By analyzing a dataset of student attributes and performance metrics, we can predict performance outcomes and identify the most important factors affecting student success.

## Dataset
The project uses the `Student_Performance.csv` dataset, which contains various metrics about students including:
- Study time
- Performance index
- Extracurricular activities participation
- Sleep hours
- Practice with sample question papers
- And other relevant features

## Features
- **Data Preprocessing**: Cleaning and preparing the dataset for analysis
- **Feature Engineering**: Encoding categorical variables and selecting relevant features
- **Model Development**: Implementation of a linear regression model to predict student performance
- **Performance Evaluation**: Assessing the model's accuracy and reliability
- **Data Visualization**: Illustrating model predictions and feature importance

## Technical Details
- **Python Libraries**:
  - NumPy for numerical computations
  - Pandas for data manipulation
  - Matplotlib for data visualization
  - Scikit-learn for machine learning algorithms

- **Machine Learning Techniques**:
  - Linear Regression for predicting student performance
  - Feature importance analysis
  - Train-test split validation

## Project Structure
- `student_lec15.py`: Main script containing data processing, model building, and visualization
- `Student_Performance.csv`: Dataset with student metrics
- `README.md`: Project documentation

## Results

The project demonstrates:
1. How various factors correlate with student performance
2. The accuracy of linear regression in predicting student outcomes
3. Which features have the strongest impact on performance:
   - Features such as Previous Scores (0.91 correlation) and Hours Studied (0.37) had the strongest influence on student performance
4. The model achieved a score of 0.9857 on the test data.

## Visualizations
The project includes two key visualizations:
1. A scatter plot comparing actual vs. predicted performance
2. A bar chart showing the importance of each feature in predicting performance

## Getting Started
To run this project:

1. Clone the repository
2. Ensure you have Python and the required libraries installed
3. Run the main script:
```
python student_analysis.py
```

## Future Improvements
Potential enhancements to the project:
- Implement more advanced regression techniques
- Perform cross-validation for more robust evaluation
- Add interactive visualizations
- Explore additional feature engineering opportunities

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author has dedicated any and all copyright interest in the software to the public domain worldwide by waiving all of those rights to the extent allowed by law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

## Author
mohammed abdulkareem

---

*This project was created as part of a data science learning journey and is intended for educational purposes.*


from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('PNR_Confirmation.pkl')

@app.route('/')
def home():
    return render_template('index.html')

def outlier_capping(dataframe: pd.DataFrame, outliers:list):
    df = dataframe.copy()
    for i in outliers:
        q1 = df[i].quantile(0.25)
        q3 = df[i].quantile(0.75)
        iqr = q3 - q1
        upper_limit = q3 + 1.5 *iqr
        lower_limit = q1 - 1.5 *iqr
        df.loc[df[i] >upper_limit, i] = upper_limit
        df.loc[df[i] <lower_limit, i] = lower_limit
    return df



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return "No file"

        # Read the CSV file into a DataFrame
        data = pd.read_csv(file)
        data.drop('pk',axis=1,inplace=True)
        data['QT']=data['QT'].replace({'GN':0,'RL':1,'PQ':2})
        data = outlier_capping(dataframe = data, outliers = data.columns)
        features=['CURP', 'GROP', 'CUCA', 'NDTD', 'GRCA', 'ODD', 'CANP', 'JD', 'CCA',
       'RPW', 'ODS', 'JS']
        df=data[features]

        # Assuming the input features are the same as during training
        predictions = model.predict(df)

        # Add predictions to the DataFrame
        data['predictions'] = predictions

        # Save the DataFrame with predictions to a CSV
        data.to_csv('predictions.csv', index=False)

        return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
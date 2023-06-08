from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import RandomizedSearchCV
rf_clf = 0
mms = 0
x_test = 0

def db_create(dict):
    db = pd.DataFrame(dict)
    return db

def train():
    global rf_clf, mms, x_test

    db = 'https://raw.githubusercontent.com/akarshsnair/Dataset-cart/main/heart%20(1).csv'
    df = pd.read_csv(db)
    df=df.dropna(axis=0)

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = LabelEncoder().fit_transform(df[col])

    df = df[df['RestingBP'] != 0]

    xdf = df.drop("HeartDisease", axis = 1)
    ydf = df["HeartDisease"]
    x_train,x_test,y_train,y_test=train_test_split(xdf,ydf,test_size=0.005)

    mms = MinMaxScaler(feature_range = (0, 1))
    x_train=mms.fit_transform(x_train)
    x_train=pd.DataFrame(x_train)

    rf_clf = RandomForestClassifier(n_estimators=1000, random_state=62)
    rf_clf.fit(x_train, y_train)
    
def predictor(data):
    
    test_data = pd.concat([x_test, data], axis = 0)
    test_data = mms.fit_transform(test_data)
    test_data = pd.DataFrame(test_data)

    prediction = rf_clf.predict(test_data)
    return prediction[-1]

info = {}
train()

root = Tk()
root.title('Heart Failure Predictor')
# icon = PhotoImage(file = '.png')
# root.iconphoto(False, icon)
out_font = font.Font(family = 'Helvetica', size = 25, weight = 'bold')
font = font.Font(family = 'Helvetica', size = 13)

def info_collect():
    global info

    for i in root.winfo_children():
        i.destroy()

    div = {
        0: Label(root, text = ' :\t'),
        1: Label(root, text = ' :\t'),
        2: Label(root, text = ' :\t'),
        3: Label(root, text = ' :\t'),
        4: Label(root, text = ' :\t'),
        5: Label(root, text = ' :\t'),
        6: Label(root, text = ' :\t'),
        7: Label(root, text = ' :\t'),
        8: Label(root, text = ' :\t'),
        9: Label(root, text = ' :\t'),
        10: Label(root, text = ' :\t')
    }

    age_lbl = Label(root, text = 'Age', font = font)
    age = Entry(root, width = 30, font = font)

    gender_lbl = Label(root, text = 'Gender', font = font)
    gender = IntVar()
    gender_1 = Radiobutton(root, text = 'Male', variable = gender, value = 1, font = font)
    gender_2 = Radiobutton(root, text = 'Female', variable = gender, value = 0, font = font)
    gender.set(None)

    chest_pain_lbl = Label(root, text = 'Chest Pain Type', font = font)
    chest_pain = IntVar()
    chest_pain_1 = Radiobutton(root, text = 'Typical Angina', variable = chest_pain, value = 3, font = font)
    chest_pain_2 = Radiobutton(root, text = 'Atypical Angina', variable = chest_pain, value = 1, font = font)
    chest_pain_3 = Radiobutton(root, text = 'Non-Anginal Pain', variable = chest_pain, value = 2, font = font)
    chest_pain_4 = Radiobutton(root, text = 'Asymptomatic', variable = chest_pain, value = 0, font = font)
    chest_pain.set(None)

    bp_lbl = Label(root, text = 'Diastolic Blood Pressure (mm Hg)', font = font)
    bp = Entry(root, width = 30, font = font)

    cholesterol_lbl = Label(root, text = 'Cholesterol (mg/dL)', font = font)
    cholesterol = Entry(root, width = 30, font = font)

    bs_lbl = Label(root, text = 'Fasting Blood Sugar', font = font)
    bs = IntVar()
    bs_1 = Radiobutton(root, text = '> 120 mg/dL', variable = bs, value = 1, font = font)
    bs_2 = Radiobutton(root, text = '<= 120 mg/dL', variable = bs, value = 0, font = font)
    bs.set(None)

    ecg_lbl = Label(root, text = 'Resting ECG', font = font)
    ecg = IntVar()
    ecg_1 = Radiobutton(root, text = 'Normal', variable = ecg, value = 1, font = font)
    ecg_2 = Radiobutton(root, text = 'ST-T Wave Abnormality', variable = ecg, value = 2, font = font)
    ecg_3 = Radiobutton(root, text = 'Left Ventricular Hypertrophy (LVH)', variable = ecg, value = 0, font = font)
    ecg.set(None)

    hr_lbl = Label(root, text = 'Maximum Heart Rate', font = font)
    hr = Entry(root, width = 30, font = font)

    ex_ang_lbl = Label(root, text = 'Exercise-induced Angina', font = font)
    ex_ang = IntVar()
    ex_ang_1 = Radiobutton(root, text = 'Yes', variable = ex_ang, value = 1, font = font)
    ex_ang_2 = Radiobutton(root, text = 'No', variable = ex_ang, value = 0, font = font)
    ex_ang.set(None)

    oldpeak_lbl = Label(root, text = 'Oldpeak', font = font)
    oldpeak = Entry(root, width = 30, font = font)

    st_slope_lbl = Label(root, text = 'Slope of peak exercise ST Segment', font = font)
    st_slope = IntVar()
    st_slope_1 = Radiobutton(root, text = 'Upsloping', variable = st_slope, value = 2, font = font)
    st_slope_2 = Radiobutton(root, text = 'Flat', variable = st_slope, value = 1, font = font)
    st_slope_3 = Radiobutton(root, text = 'Downsloping', variable = st_slope, value = 0, font = font)
    st_slope.set(None)

    def data():
        try:
            info['Age'] = [int(age.get())]
            info['Sex'] = [gender.get()]
            info['ChestPainType'] = [chest_pain.get()]
            info['RestingBP'] = [int(bp.get())]
            info['Cholesterol'] = [cholesterol.get()]
            info['FastingBS'] = [bs.get()]
            info['RestingECG'] = [ecg.get()]
            info['MaxHR'] = [int(hr.get())]
            info['ExerciseAngina'] = [ex_ang.get()]
            info['Oldpeak'] = [float(oldpeak.get())]
            info['ST_Slope'] = [st_slope.get()]

        except:
            messagebox.showinfo('Alert', 'Insufficient or Invalid Data')
            return

        age['state'] = 'disabled'
        gender_1['state'] = 'disabled'
        gender_2['state'] = 'disabled'
        chest_pain_1['state'] = 'disabled'
        chest_pain_2['state'] = 'disabled'
        chest_pain_3['state'] = 'disabled'
        chest_pain_4['state'] = 'disabled'
        bp['state'] = 'disabled'
        cholesterol['state'] = 'disabled'
        bs_1['state'] = 'disabled'
        bs_2['state'] = 'disabled'
        ecg_1['state'] = 'disabled'
        ecg_2['state'] = 'disabled'
        ecg_3['state'] = 'disabled'
        hr['state'] = 'disabled'
        ex_ang_1['state'] = 'disabled'
        ex_ang_2['state'] = 'disabled'
        oldpeak['state'] = 'disabled'
        st_slope_1['state'] = 'disabled'
        st_slope_2['state'] = 'disabled'
        st_slope_3['state'] = 'disabled'

        input = db_create(info)
        result(input)

    reset = Button(root, text = ' Reset ', command = info_collect, font = font)
    submit = Button(root, text = 'Submit', command = data, font = font, bg = 'blue', fg = 'white')

    age_lbl.grid(row = 0, column = 0, sticky = W, pady = 10)
    gender_lbl.grid(row = 1, column = 0, sticky = W, pady = 10)
    chest_pain_lbl.grid(row = 2, column = 0, sticky = W, pady = 10)
    bp_lbl.grid(row = 3, column = 0, sticky = W, pady = 10)
    cholesterol_lbl.grid(row = 4, column = 0, sticky = W, pady = 10)
    bs_lbl.grid(row = 5, column = 0, sticky = W, pady = 10)
    ecg_lbl.grid(row = 6, column = 0, sticky = W, pady = 10)
    hr_lbl.grid(row = 7, column = 0, sticky = W, pady = 10)
    ex_ang_lbl.grid(row = 8, column = 0, sticky = W, pady = 10)
    oldpeak_lbl.grid(row = 9, column = 0, sticky = W, pady = 10)
    st_slope_lbl.grid(row = 10, column = 0, sticky = W, pady = 10)

    for i in div.keys():
        div[i].grid(row = i, column = 1, pady = 10)

    age.grid(row = 0, column = 2, sticky = W, pady = 10)
    gender_1.grid(row = 1, column = 2, sticky = W, pady = 10)
    gender_2.grid(row = 1, column = 3, sticky = W, pady = 10)
    chest_pain_1.grid(row = 2, column = 2, sticky = W, pady = 10)
    chest_pain_2.grid(row = 2, column = 3, sticky = W, pady = 10)
    chest_pain_3.grid(row = 2, column = 4, sticky = W, pady = 10)
    chest_pain_4.grid(row = 2, column = 5, sticky = W, pady = 10)
    bp.grid(row = 3, column = 2, sticky = W, pady = 10)
    cholesterol.grid(row = 4, column = 2, sticky = W, pady = 10)
    bs_1.grid(row = 5, column = 2, sticky = W, pady = 10)
    bs_2.grid(row = 5, column = 3, sticky = W, pady = 10)
    ecg_1.grid(row = 6, column = 2, sticky = W, pady = 10)
    ecg_2.grid(row = 6, column = 3, sticky = W, pady = 10)
    ecg_3.grid(row = 6, column = 4, sticky = W, pady = 10)
    hr.grid(row = 7, column = 2, sticky = W, pady = 10)
    ex_ang_1.grid(row = 8, column = 2, sticky = W, pady = 10)
    ex_ang_2.grid(row = 8, column = 3, sticky = W, pady = 10)
    oldpeak.grid(row = 9, column = 2, sticky = W, pady = 10)
    st_slope_1.grid(row = 10, column = 2, sticky = W, pady = 10)
    st_slope_2.grid(row = 10, column = 3, sticky = W, pady = 10)
    st_slope_3.grid(row = 10, column = 4, sticky = W, pady = 10)

    reset.grid(row = 11, column = 3, sticky = W, pady = 15)
    submit.grid(row = 12, column = 3, sticky = W, pady = 5)


def result(input):
    prediction = predictor(input)

    if prediction == 1:
        failure()

    else:
        no_failure()

def failure():
    out1 = Label(root, text = 'High Possibility', fg = 'red', font = out_font)
    out2 = Label(root, text = 'of Heart Failure', fg = 'red', font = out_font)

    out1.grid(row = 13, column = 2, sticky = E, pady = 30)
    out2.grid(row = 13, column = 3, sticky = W, pady = 30)

def no_failure():
    out1 = Label(root, text = 'Low Possibility', fg = 'green', font = out_font)
    out2 = Label(root, text = 'of Heart Failure', fg = 'green', font = out_font)

    out1.grid(row = 13, column = 2, sticky = E, pady = 30)
    out2.grid(row = 13, column = 3, sticky = W, pady = 30)

info_collect()

root.mainloop()
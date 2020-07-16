import pandas as pd
import numpy as np
from numpy import matrix
import math
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
import statsmodels.api as sm
# import statsmodels.api as st
import statsmodels.formula.api as smf
import statistics

dat = pd.read_csv("PatientDiseaseList1orMore_copy_original.csv")
# dat = pd.read_csv("PatientDiseaseList1orMore.csv")
# dat= dat[0:6000]

#Encode age and sex columns:
cleanup_nums = {"sex": {"Female": 1, "Male": 0},"age": {"elder": 3,
            "middleAge": 2, "adult": 2, "youngAdult": 1, "adolescent": 1, "child": 1}}
dat.replace(cleanup_nums, inplace=True)
dat.SocioeconomicStatus[dat[dat.SocioeconomicStatus==3].index]=0
dat.SocioeconomicStatus[dat[dat.SocioeconomicStatus==4].index]=0
dat.SocioeconomicStatus[dat[dat.SocioeconomicStatus==5].index]=1
print("dat=",dat)
data1=dat
# Check the count of values for each column
for i in range(len(dat.columns)):
    print("count of value\n", dat[dat.columns[i]].value_counts())

#To get a frequency count based on two columns(variables)
# dat_filtered = dat[(dat.sex == 2)]
# dat = dat_filtered
# print(dat.groupby(["age", "sex"]).size())
# print(dat.groupby(["age", "SocioeconomicStatus"]).size())

#Create Dummy Variables
datatemp=dat
dat_vars=['age']
for var in dat_vars:
    dat_list='var'+'_'+var
    dat_list = pd.get_dummies(datatemp[var], prefix=var, drop_first=True)
    data1=datatemp.join(dat_list)
    datatemp=data1
dat_dat=datatemp.columns.values.tolist()
to_keep=[i for i in dat_dat if i not in dat_vars]

dat_dummy=datatemp[to_keep]
print("dat_dummy.columns=",dat_dummy.columns.values)
print("dat.columns=",dat.columns.values)

#number of diseases
NumofDiseases=10
#Main code for backend,frontend system
from flask import Flask, render_template, make_response, request, send_from_directory
import csv
import json

app = Flask(__name__, template_folder='template', static_url_path='/static')

def get_field_value(body, fieldname):
    for item in body:
        if fieldname in item:
            item = item.split("=")
            return item[1]

# @app.route('/get_data_matrix')
# def MatrixData():
#     with open('datdat.json') as json_data:
#         print(type(json_data))
#         data_dict = json.load(json_data)
#         data_matrix= json.dumps(data_dict)
#         return data_matrix

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/')
def index():
    return render_template("index_matrix.html")


###############################################################################
@app.route('/process_dat', methods=['POST'])
def process_dat():
    output = None
    body = request.get_data()
    body = body.decode().split("&")
    d1 = get_field_value(body, 'd1')
    d2 = get_field_value(body, 'd2')
    d3 = get_field_value(body, 'd3')
    d4 = get_field_value(body, 'd4')
    d5 = get_field_value(body, 'd5')
    d6 = get_field_value(body, 'd6')
    d7 = get_field_value(body, 'd7')
    d8 = get_field_value(body, 'd8')
    d9 = get_field_value(body, 'd9')
    d10 = get_field_value(body, 'd10')
    age_val = get_field_value(body, 'age_val')
    sex_val = get_field_value(body, 'sex_val')
    socioeconomic_val = get_field_value(body, 'socioeconomic_val')
    charttype_val = get_field_value(body, 'charttype_val')
    matrixtype_val = get_field_value(body, 'matrixtype_val')
    print("charttype=", charttype_val)
    print("matrix,type_val" ,matrixtype_val)
    samplesize = []
    df=dat
#########################################################################
    # To rename the columns of disease1 to disease10 and change them to numbers 1 to 10
    dat_dummy.rename(columns={'Hypertension': '1', 'Diabetes': '2', 'Bronchitis': '3', 'Hyperlipidemia': '4', 'Cancer': '5',
    'CardiovascularDisease': '6', 'Depression': '7', 'Arthritis': '8', 'Thyroid': '9', 'MusculoskeletalProblem': '10'}, inplace=True)

    dat.rename(columns={'Hypertension': '1', 'Diabetes': '2', 'Bronchitis': '3', 'Hyperlipidemia': '4', 'Cancer': '5',
    'CardiovascularDisease': '6', 'Depression': '7', 'Arthritis': '8', 'Thyroid': '9', 'MusculoskeletalProblem': '10'},inplace=True)

    shrinkdat = dat_dummy
    # To earn dataset with selected variables but all cases the same as the original data
    listAll = [int(d1), int(d2), int(d3), int(d4), int(d5), int(d6), int(d7), int(d8)
        , int(d9), int(d10), int(sex_val), int(socioeconomic_val), int(age_val)]
    listAllDis = listAll[0:10]
    print("listAll= ", listAll)
    print("listAllDis", listAllDis)
    colname = shrinkdat.columns

    for i in range(0, 13):
        if listAll[i] == 99:
            shrinkdat = shrinkdat.drop(colname[i], axis=1)
        if listAll[i] == 100:
            shrinkdat = shrinkdat.drop(["age_2", "age_3"], axis=1)
        if listAll[i] == 101:
            shrinkdat = shrinkdat.drop(["SocioeconomicStatus"], axis=1)

    print("Shrinkdata is=\n", shrinkdat)
    # print("---------------------------------")

    # To fit the logit model for Prevalence_Bar chart
    shricol = list(shrinkdat.columns)

    # to keep one dummy variable from age and one dummy variable from socioeconomic and remove other dummy variables from shricol
    if "age_2" in shricol:
        shricol.remove("age_3")
    # if "SocioeconomicStatus_2" in shricol:
    #     shricol.remove("SocioeconomicStatus_3")

    print("shricol=", shricol)
    data_10_ds = dat.iloc[:, 0:10]
    org_10D_list = data_10_ds.columns
    print("data_10_ds.columns=", data_10_ds.columns)

    listAllName = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'sex', 'SocioeconomicStatus', 'age_2']
    varval = [None] * len(shricol)
    varvaloriginal = [None] * len(shricol)
    Prob = [None] * len(data_10_ds.columns)

    # print("---------------------------------")
    for w in range(len(shricol)):
        for j in range(len(listAllName)):
            if shricol[w] == listAllName[j]:
                varval[w] = listAll[j]
                varvaloriginal[w] = listAll[j]
    varval = list(varval)
    varvaloriginal = list(varvaloriginal)
    varvaloriginal = np.array(varvaloriginal)
    # for i in range(varvaloriginal):
    #     if int(varvalloriginal[i])>=2:
    #         int(varvalloriginal[i]) = int(varvalloriginal[i])-1

    print("varvaloriginal=", varvaloriginal)

 ##############################################################################

    for i in range(len(varval)):
        if varval[i] == 2:
            insert_list = [0, 0]
            pos = i
            for j in range(len(insert_list)):
                varval.insert(j + pos, insert_list[j])
            varval.remove(varval[pos + len(insert_list)])
        if varval[i] == 3:
            insert_list = [1, 0]
            pos = i
            for j in range(len(insert_list)):
                varval.insert(j + pos, insert_list[j])
            varval.remove(varval[pos + len(insert_list)])
        if varval[i] == 4:
            insert_list = [0, 1]
            pos = i
            for j in range(len(insert_list)):
                varval.insert(j + pos, insert_list[j])
            varval.remove(varval[pos + len(insert_list)])
    varval=np.array(varval)
    print("varvalNew=", varval)

#########################################################################
    TotallNumofCases = [dat.shape[0]]  # To pass the total number of observations (patients) to the frontend to be used in logit model-based bar chart
    print("TotallNumofCases", TotallNumofCases)
    #if condition on the type of chart
    if int(charttype_val) ==1: #count-based bar chart
    #To calculate conditional probabilities for prevalence part based on filtered data:
        if int(age_val) == 2:
            df_filtered = df[(df.age == 1)]
            df = df_filtered
        if int(age_val) == 3:
            df_filtered = df[(df.age == 2)]
            df = df_filtered
        if int(age_val) == 4:
            df_filtered = df[(df.age == 3)]
            df = df_filtered

        if int(sex_val) == 1:
            df_filtered = df[(df.sex == 1)]
            df = df_filtered
        if int(sex_val) == 0:
            df_filtered = df[(df.sex == 0)]
            df = df_filtered
        if int(socioeconomic_val) == 1:
            df_filtered = df[(df.SocioeconomicStatus == 1)]
            df = df_filtered
        if int(socioeconomic_val) == 0:
            df_filtered = df[(df.SocioeconomicStatus == 0)]
            df = df_filtered

        if int(d1) == 1:
            df_filtered = df[(df[df.columns[0]]== 1)]
            df = df_filtered
        if int(d1) == 0:
            df_filtered = df[(df[df.columns[0]]== 0)]
            df = df_filtered

        if int(d2) == 1:
            df_filtered = df[(df[df.columns[1]]== 1)]
            df = df_filtered
        if int(d2) == 0:
            df_filtered = df[(df[df.columns[1]]== 0)]
            df = df_filtered

        if int(d3) == 1:
            df_filtered = df[(df[df.columns[2]]== 1)]
            df = df_filtered
        if int(d3) == 0:
            df_filtered = df[(df[df.columns[2]]== 0)]
            df = df_filtered

        if int(d4) == 1:
            df_filtered = df[(df[df.columns[3]]== 1)]
            df = df_filtered
        if int(d4) == 0:
            df_filtered = df[(df[df.columns[3]]== 0)]
            df = df_filtered

        if int(d5) == 1:
            df_filtered = df[(df[df.columns[4]]== 1)]
            df = df_filtered
        if int(d5) == 0:
            df_filtered = df[(df[df.columns[4]]== 0)]
            df = df_filtered
        if int(d6) == 1:
            df_filtered = df[(df[df.columns[5]]== 1)]
            df = df_filtered
        if int(d6) == 0:
            df_filtered = df[(df[df.columns[5]]== 0)]
            df = df_filtered
        if int(d7) == 1:
            df_filtered = df[(df[df.columns[6]]== 1)]
            df = df_filtered
        if int(d7) == 0:
            df_filtered = df[(df[df.columns[6]]== 0)]
            df = df_filtered
        if int(d8) == 1:
            df_filtered = df[(df[df.columns[7]]== 1)]
            df = df_filtered
        if int(d8) == 0:
            df_filtered = df[(df[df.columns[7]]== 0)]
            df = df_filtered
        if int(d9) == 1:
            df_filtered = df[(df[df.columns[8]]== 1)]
            df = df_filtered
        if int(d9) == 0:
            df_filtered = df[(df[df.columns[8]]== 0)]
            df = df_filtered
        if int(d10) == 1:
            df_filtered = df[(df[df.columns[9]]== 1)]
            df = df_filtered
        if int(d10) == 0:
            df_filtered = df[(df[df.columns[9]]== 0)]
            df = df_filtered

        #print("df is = \n" , df)
        samplesize = [df.shape[0]] #To update the sample size after filtering on df for using on count-based bar chart
        print("samplesize_1", samplesize)
        ListofMeans=[]
        for i in range(NumofDiseases):
            ListofMeans.append(statistics.mean(df[df.columns[i]]))
        output = ListofMeans
        print("ListofMeans=", output)
    elif int(charttype_val) == 3: #logit-based bar chart
        for k in range(0, 10):
            if (org_10D_list[k] not in shricol):
                y = dat[org_10D_list[k]]
                x = shrinkdat.copy()
                x['intercept'] = 1.0
                # print("shrinkdat-type=", type(shrinkdat))
                print("x=\n", x)
                model = sm.Logit(y, x)
                result = model.fit()
                Beta = np.array(result.params.drop('intercept'))
                print("result.params\n", result.params)

                ####################################################################################
                varval = np.array(varval)
                print("varval_nparray=", varval)
                logodds = varval.dot(Beta) + result.params['intercept']
                print("logodds=", varval @ Beta)
                # multip=np.multiply(varval, Beta)
                # logodds=sum(multip)+ result.params['intercept']
                # print("type of logodds=", type(logodds))
                # logodds=np.dot(varval, Beta, out=None)
                # print("---------------------------------")
                print("logodds=", logodds)
                Prob[k] = 1 / (1 + math.exp(-logodds))
                print("Prob=", Prob[k] )
                # print("________________________________________-")
            elif listAllDis[k] == 1:
                Prob[k] = 1
            else:
                Prob[k] = 0
        print("LogitProbsForPrevalenceBarCnart=" , Prob)
        output = Prob
        samplesize = TotallNumofCases
        print("samplesize_2", samplesize)

    else:  # Decision tree model for bar chart
        Tree_Prob = [None] * len(data_10_ds.columns)
        x = shrinkdat.copy()
        x_train = x
        if "age_2" in x_train.columns:
            x_train = x_train.drop(["age_2", "age_3"], axis=1)
            x_train['age'] = data1.age
            x_train['age']= x_train.age +1 #values of age categories should be matched with the drop down labels for age in frontend
        for k in range(0, 10):
            if (org_10D_list[k] not in shricol):
                y = dat[org_10D_list[k]]
                dt = DecisionTreeClassifier(max_depth=3, min_samples_leaf=1000)
                dt.fit(x_train, y)
                print("x_train=\n", x_train)
                # print("x_test=\n",x_test)
                # y_pred = dt.predict(x_test)
                varvaloriginal = np.array(varvaloriginal)

                varvaloriginal = varvaloriginal.reshape(1, -1)
                probability_tree = dt.predict_proba(varvaloriginal)[:, 1]
                Tree_Prob[k] = probability_tree
                Tree_Prob[k] = list(Tree_Prob[k])
            elif listAllDis[k] == 1:
                Tree_Prob[k] = 1
            else:
                Tree_Prob[k] = 0
        output = Tree_Prob
        samplesize = TotallNumofCases
        print("Tree_Prob_list=", output)
#############################################################################################
    # To make the 45 pairs (columns) of 10 diseases
    count = 9
    DataPair=dat.iloc[:,0:10]
    for i in range(0, 10):
        for j in range(i + 1, 10):
            count = count + 1
            DataPair[count] = ((DataPair[DataPair.columns[i]]) * 2) + (DataPair[DataPair.columns[j]])

    # To rename pair columns to their mode 11 values
    DataPair.rename(
        columns={10: '13', 11: '14', 12: '15', 13: '16', 14: '17', 15: '18', 16: '19', 17: '20', 18: '21', 19: '25',
                 20: '26', 21: '27', 22: '28', 23: '29', 24: '30', 25: '31', 26: '32', 27: '37', 28: '38', 29: '39',
                 30: '40', 31: '41',
                 32: '42', 33: '43', 34: '49', 35: '50', 36: '51', 37: '52', 38: '53', 39: '54', 40: '61', 41: '62',
                 42: '63', 43: '64', 44: '65', 45: '73', 46: '74', 47: '75', 48: '76', 49: '85', 50: '86', 51: '87',
                 52: '97', 53: '98', 54: '109'}, inplace=True)
    # print(dat)
    # print(dat.columns)
    # print(DataPair)
    print("DataPair.columns",DataPair.columns)
    print("Datapair=\n", DataPair)

    #To create the dataframe with pairs columns which are not the combinations of user-selected diseases
    # DataPair = pd.read_csv("pairsForChord_10Ds.csv")
    #pairs: d12,d13,d14,d15,d16,d17, d18,d19,d110,d23,d24,d25,d26,d27,d28,d29,d210,d34,d35,d36,d37,d38,d39,d310
    #mode11:13, 14, 15, 16, 17, 18,  19,  20, 21, 25 , 26, 27, 28, 29,30, 31, 32,  37, 38, 39, 40, 41, 42, 43
    # pairs: d45,d46,d47,d48,d49,d410,d56,d57,d58,d59,d510,d67,d68,d69,d610,d78,d79,d710,d89,d810,d910
    #mode11: 49, 50, 51, 52, 53, 54,  61, 62, 63, 64, 65,  73, 74, 75, 76 , 85, 86, 87,  97, 98, 109
    DataPair1 = DataPair.iloc[:, 10:55]
    print("DataPair1=\n", DataPair1)
    new_data = pd.DataFrame()
    resetData = DataPair1
    n=11 #number of diseases+1
    new_list = []
    #Removing string variables from the selected list by user (shricol)
    for e in shricol:
        if e not in ('sex', 'SocioeconomicStatus', 'age_2'):
            new_list.append(int(e))
    shricolwithoutChar = new_list
    # To create the dataframe with pairs columns which are not the combinations of user-selected diseases
    for j in range(len(shricolwithoutChar)):
        for i in range(len(DataPair1.columns)):
            a = int(int(DataPair1.columns[i]) / n)
            b = (int(DataPair1.columns[i])) % n
            if (shricolwithoutChar[j] == a) or (shricolwithoutChar[j] == b):
                # print("shricolwithoutChar[j]", shricolwithoutChar[j])
                for k in range(len(resetData.columns)):
                    if (resetData.columns[k] != DataPair1.columns[i]):
                        new_data.loc[:, resetData.columns[k]] = resetData[resetData.columns[k]]
                resetData = new_data
                new_data = pd.DataFrame()

            # print("i", i)
            # print("j", j)
            # print("a=", a)
            # print("b=", b)
    print("selected Pairs=\n", resetData) #the final pairs dataset
    print("reset data columns= ",resetData.columns )
    corr = [None] * len(resetData.columns)

    matrix1 = [] #making a matrix with 1's at the main diagonal and 3's for pairs which are not selected in resetData!
    for i in range(10):  #number of rows
        row = []
        for j in range(10): #number of columns
            if i==j:
                row.append(1)#if the row and the column are equal
            else: row.append(3)#for pairs which are selected
        matrix1.append(row)  # add fully defined column into the row

    if int(matrixtype_val) ==2: #Multinomial or softmax logistic regression for every cell (every pair) in correlation matrix
        ProbPair= []
        logoddPair=[]
        intercept_array=[]
        withoutintercept=[]
        interceptarray=[]
        logoddPair00=logoddPair01=logoddPair10=P1_=P_1=0
        for k in range(len(resetData.columns)):
            Y_Pair = resetData[resetData.columns[k]]
            X_Pair = shrinkdat
            xx=shrinkdat.copy()
            xx['intercept'] = 1.0
            # print("xx=\n",xx)
            # print("x=\n", X_Pair)
            # print("Y_Pair=\n", Y_Pair)
            modelPair = sm.MNLogit(Y_Pair, xx)
            resultPair = modelPair.fit()
            print("resultPair.params=",resultPair.params)
            # BetaPair = np.array(resultPair.params.drop('intercept'))
            BetaPair = np.array(resultPair.params)
            print("BetaPair=", BetaPair)

            print("resultPair.params_matrix=\n", resultPair.params)
            BetaPair_without_intercept = np.delete(BetaPair, (-1), axis=0)
            print("BetaPair_without_intercept", BetaPair_without_intercept)

            for f in range(0, 3):
                # print("BetaPair[f]\n", BetaPair[:, f])
                logoddPair= varval.dot(BetaPair_without_intercept[:, f])
                print("logoddPair=", logoddPair)

                if f==0:
                    logoddPair00=logoddPair+BetaPair[-1,0]
                elif f==1:
                    logoddPair01=logoddPair+BetaPair[-1,1]
                else:
                    logoddPair10=logoddPair+BetaPair[-1,2]
                print("BetaPair[-1,2]", BetaPair[-1,2])
                print("logoddPair=\n", logoddPair)
            print("logoddPair00=", logoddPair00)
            print("logoddPair01=", logoddPair01)
            print("logoddPair10=", logoddPair10)
            print("type_logoddPair10=", type(logoddPair10))
            ProbPair10= math.exp(logoddPair00)/(1+math.exp(logoddPair00)+math.exp(logoddPair01)+math.exp(logoddPair10))
            ProbPair01 = math.exp(logoddPair01) / (1 + math.exp(logoddPair00) + math.exp(logoddPair01) + math.exp(logoddPair10))
            ProbPair00 = math.exp(logoddPair10) / (1 + math.exp(logoddPair00) + math.exp(logoddPair01) + math.exp(logoddPair10))
            ProbPair11 = 1 / (1 + math.exp(logoddPair00) + math.exp(logoddPair01) + math.exp(logoddPair10))
            #
            print("ProbPair00=", ProbPair00)
            print("ProbPair01=", ProbPair01)
            print("ProbPair10=", ProbPair10)
            print("ProbPair11=", ProbPair11)

            sum_ProbPair = ProbPair00 + ProbPair01 + ProbPair10 + ProbPair11
            print("sum_ProbPair=", sum_ProbPair)

            #To calculate the corr for each pair:
            P1_=ProbPair10 + ProbPair11
            P_1 = ProbPair01 + ProbPair11
            corr[k]=(ProbPair11- (P1_*P_1))/(math.sqrt(P1_*(1-P1_))*math.sqrt(P_1*(1-P_1)))
            print("CorrelationForEachPair=\n", corr[k])
        print("ListofCorrelations softmax for matrix=",corr)

        # for k in range(len(resetData.columns)): #first method for creating the 10*10 matrix dataset
        #     for i in range(len(matrix1)):
        #         for j in range(len(matrix1[i])):
        #             c = int(int(resetData.columns[k]) / n)
        #             d = (int(resetData.columns[k])) % n
        #             if ((i+1)==c) and ((j+1)==d):
        #                 matrix1[i][j]=corr[k]
        #                 # matrix1[j][i]=corr[k]
        for k in range(len(resetData.columns)): #second method
            c = int(int(resetData.columns[k]) / n)
            d = (int(resetData.columns[k])) % n
            matrix1[c-1][d-1]=corr[k]
            # matrix1[d-1][c-1] = corr[k]

        # print("\nOur Desired matrix1=",matrix1) #### Our desired matrix

    elif int(matrixtype_val) ==1: #decision tree model for every cell (every pair) in correlation matrix
        x_train = shrinkdat.copy()
        if "age_2" in x_train.columns:
            x_train = x_train.drop(["age_2", "age_3"], axis=1)
            x_train['age'] = data1.age
            x_train['age']= x_train.age +1 #values of age categories should be matched with the drop down labels for age in frontend
        for k in range(len(resetData.columns)):
            y_train_tree_matrix= resetData[resetData.columns[k]]
            x_train_tree_matrix=x_train
            dt = DecisionTreeClassifier(max_depth=3, min_samples_leaf=200)
            dt.fit(x_train_tree_matrix, y_train_tree_matrix)
            print("x_train_tree=\n", x_train_tree_matrix)
            varvaloriginal = np.array(varvaloriginal)
            varvaloriginal = varvaloriginal.reshape(1, -1)
            ProbPair00 = dt.predict_proba(varvaloriginal)[:, 0]
            ProbPair01 = dt.predict_proba(varvaloriginal)[:, 1]
            ProbPair10 = dt.predict_proba(varvaloriginal)[:, 2]
            ProbPair11 = dt.predict_proba(varvaloriginal)[:, 3]

            sum_ProbPair = ProbPair00 + ProbPair01 + ProbPair10 + ProbPair11
            print("sum_ProbPair=", sum_ProbPair)

            # To calculate the corr for each pair:
            P1_ = ProbPair10 + ProbPair11
            P_1 = ProbPair01 + ProbPair11
            corr[k] = (ProbPair11 - (P1_ * P_1)) / (math.sqrt(P1_ * (1 - P1_)) * math.sqrt(P_1 * (1 - P_1)))
            # print("CorrelationForEachPair=\n", corr[k])
        corr=np.array(corr)
        corr=corr.flatten()
        print("ListofCorrelations_decision tree=", corr)
        for k in range(len(resetData.columns)): #To fill up the cells with predictions
            c = int(int(resetData.columns[k]) / n)
            d = (int(resetData.columns[k])) % n
            matrix1[c-1][d-1]=corr[k]
            # matrix1[d-1][c-1] = corr[k]


    array_list=[] #a 45 array list (half of matrix)
    for i in range(0, 9):
        for j in range(i+1, 10):
            array_list.append(matrix1[i][j])
    # print("array_list=",array_list)

    import json
    with open('datdat_dat.json', 'r') as file: #datdat_dat is a json dataset for matrix without "data" at the beginning
        matrix_datdat = json.load(file)
        for i in range(0, 45):
            matrix_datdat["links"][i]['value'] = array_list[i]
    # print(matrix_datdat)

    ##########################################################################################
    # resres=json.dumps(output)
    # response = app.response_class(
    #     response=json.dumps(output),
    #     status=200,
    #     mimetype='application/json'
    # )
   # return (response)

    payload = {
        "First_response": matrix_datdat,
        "Second_response": output+ samplesize,
        # "Third_response": Prob+TotallNumofCases
    }
    return payload

if __name__ == "__main__":
    app.run()

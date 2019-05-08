import pyodbc
import csv
import os
from decimal import *

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=dc-bir-cdb01;"
                      "Database=InsightWarehouse;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()
business_date = '2019-01-31'
exchange_rate = {'USD_KHR': 4018.00000, 'USD_THB': 32.27309}
product_type_cbc = {
    'GRPCVB': 'RVL',
    'GRPEVB': 'CMT',
    'GRPIVB': 'CMT',
    'INDAEL': 'AGL',
    'INDBSL': 'WCL',
    'INDEDL': 'EDU',
    'INDEML': 'EML',
    'INDESL': 'WCL',
    'INDFEL': 'EML',
    'INDGLC': 'RVL',
    'INDGLE': 'WCL',
    'INDGLI': 'WCL',
    'INDHIL': 'HIL',
    'INDMKL': 'WCL',
    'INDMTL': 'MTL',
    'INDSCL': 'RVL',
    'INDSSL': 'AGL',
    'INDULE': 'WCL',
    'INDULI': 'WCL',
    'SMEIVL': 'WCL',
    'SMEIVLC': 'WCL',
    'SMEIVLI': 'WCL',
    'SMEWCL': 'WCL',
    'STFAAL': 'STL',
    'STFGSL': 'STL',
    'STFSEL': 'STL',
    'STFSHL': 'SHL'
}
query = """
    SELECT  '202' AS 'Creditor ID'
            ,FORMAT(A.BusinessDate,'yyyyMM') AS 'Period(YYYYMM)'
           ,A.AccountNum AS 'Active Account Number'
           ,C.CustomerNum
           ,A.DisburseDate AS 'Open Date (YYYY-MM-DD)'
           ,A.ProductCode AS 'Proudct Type'	
           ,CASE 
                WHEN A.Auto_Class ='DOUBTFUL' THEN 'D'
                WHEN A.Auto_Class ='LOSS' THEN 'L'
                WHEN A.Auto_Class ='SPL-MENTION' THEN 'S'
                WHEN A.Auto_Class ='STANDARD' THEN 'N'
                WHEN A.Auto_Class ='SUB-STANDARD' THEN 'U'
                END 'Account Status'
        
            ,A.Currency
           ,A.Overdue_PR AS 'OutStanding Balance'
           ,A.DelinquentAmount AS 'Delinquent Balance'
         ,CASE 
                WHEN A.DelinquentDays IS Null THEN 'current'
                WHEN A.DelinquentDays BETWEEN 1 AND 29 THEN '1'
                WHEN A.DelinquentDays BETWEEN 30 AND 59 THEN '2'
                WHEN A.DelinquentDays BETWEEN 60 AND 89 THEN '3'
                WHEN A.DelinquentDays BETWEEN 90 AND 119 THEN '4'
                WHEN A.DelinquentDays BETWEEN 120 AND 149 THEN '5'
                WHEN A.DelinquentDays BETWEEN 150 AND 179 THEN '6'
                WHEN A.DelinquentDays BETWEEN 180 AND 209 THEN '7'
                WHEN A.DelinquentDays BETWEEN 210 AND 239 THEN '8'
                WHEN A.DelinquentDays BETWEEN 240 AND 269 THEN '9'
    
                WHEN A.DelinquentDays BETWEEN 270 AND 299 THEN 'T'
                WHEN A.DelinquentDays BETWEEN 300 AND 329 THEN 'E'
                WHEN A.DelinquentDays BETWEEN 330 AND 359 THEN 'Y'
                
                ELSE 'L'
                END  AS 'Last Payment Status Code'
              FROM [InsightWarehouse].[dbo].[v_Account] AS A 
              LEFT JOIN [InsightWarehouse].[dbo].[v_Customer] AS C ON C.CustomerId=A.CustomerId AND C.BusinessDate=A.BusinessDate
             
             WHERE  A.Category='Loan' AND A.IsActive='Yes'
              AND A.BusinessDate = '2019-01-31'
              AND A.Auto_Class IS NOT NULL
        """
cursor.execute(query)

filename1 = 'detail.csv'
filename2 = 'summary.csv'
# Delete file first
try:
    os.remove(filename1)
    os.remove(filename2)
except OSError:
    pass
total_outstanding_balance = []
total_active_accounts = []
total_active_clients = []
total_delinquent_balances = []

with open(filename1, 'w+', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'Creditor ID',
        'Period(YYYYMM)',
        'Active Account Number',
        'Customer Number',
        'Open Date (YYYY-MM-DD)',
        'Product Type',
        'Account Status',
        'Currency',
        'Outstanding Balance',
        'Delinquent Balance',
        'Last Payment Status Code'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    i = 0
    for row in cursor:
        # print('row = %r' % (row,))
        total_active_accounts.append(row[2])
        total_active_clients.append(row[3])

        if row[7] == "KHR":
            if row[8] is not None:
                total_outstanding_balance.append(float(row[8]) / exchange_rate['USD_KHR'])
                total_delinquent_balances.append(float(row[9]) / exchange_rate['USD_KHR'])
            else:
                total_outstanding_balance.append(0.0)
                total_delinquent_balances.append(0.0)
        elif row[7] == "THB":
            if row[8] is not None:
                total_outstanding_balance.append(float(row[8]) / exchange_rate['USD_THB'])
                total_delinquent_balances.append(float(row[9]) / exchange_rate['USD_THB'])
            else:
                total_outstanding_balance.append(0.0)
                total_delinquent_balances.append(0.0)
        else:
            if row[8] is not None:
                total_outstanding_balance.append(float(row[8]))
                total_delinquent_balances.append(float(row[9]))
            else:
                total_outstanding_balance.append(0.0)
                total_delinquent_balances.append(0.0)
        writer.writerow({
            'Creditor ID': row[0],
            'Period(YYYYMM)': row[1],
            'Active Account Number': row[2],
            # 'Customer Number': row[3],
            'Open Date (YYYY-MM-DD)': row[4],
            'Product Type': product_type_cbc[row[5]],
            'Account Status': row[6],
            'Currency': row[7],
            'Outstanding Balance': row[8],
            # 'Delinquent Balance': row[9],
            'Last Payment Status Code': row[10]
        })

writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
data = {
    'Total outstanding balance (USD)': '{:,.2f}'.format(sum(total_outstanding_balance)),
    'Total active accounts': len(set(total_active_accounts)),
    'Total active clients': len(set(total_active_clients)),
    'Total Delinquent balance (USD)': '{:,.2f}'.format(sum(total_delinquent_balances))
}
with open(filename2, 'w+',newline='') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, data.keys())
    w.writeheader()
    w.writerow(data)

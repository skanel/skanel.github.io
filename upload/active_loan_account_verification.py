import pyodbc
import csv
import os

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=dc-bir-cdb01;"
                      "Database=InsightWarehouse;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()
cursor.execute(
    """
        SELECT 
		 '202' AS 'Creditor ID'
		 ,FORMAT(AA.MIS_DATE,'yyyyMM') AS 'Period(YYYYMM)',
		 LN.DISB_DATE AS 'Open Date (YYYY-MM-DD)',
		 AA.ACCOUNT_REFERENCE AS 'Active Account Number',
		 --AGING_STATUS,
		CASE 
			WHEN AGING_STATUS ='DBT' THEN 'D'
			WHEN AGING_STATUS ='LOS' THEN 'L'
			WHEN AGING_STATUS ='SMP' THEN 'S'
			WHEN AGING_STATUS ='STD' THEN 'N'
			WHEN AGING_STATUS ='SUB' THEN 'U'
			END 'Account Status',
		 B.OS_PR_AMT AS 'Outstanding Balance',
		 AAP.Product AS 'Product Type',
		 B.CURRENCY AS 'Currency',
		 --LN.ARREAR_DAYS,

		 CASE 
			WHEN LN.ARREAR_DAYS = 0 THEN 'current'
			WHEN LN.ARREAR_DAYS BETWEEN 1 AND 29 THEN '1'
			WHEN LN.ARREAR_DAYS BETWEEN 30 AND 59 THEN '2'
			WHEN LN.ARREAR_DAYS BETWEEN 60 AND 89 THEN '3'
			WHEN LN.ARREAR_DAYS BETWEEN 90 AND 119 THEN '4'
			WHEN LN.ARREAR_DAYS BETWEEN 120 AND 149 THEN '5'
			WHEN LN.ARREAR_DAYS BETWEEN 150 AND 179 THEN '6'
			WHEN LN.ARREAR_DAYS BETWEEN 180 AND 209 THEN '7'
			WHEN LN.ARREAR_DAYS BETWEEN 210 AND 239 THEN '8'
			WHEN LN.ARREAR_DAYS BETWEEN 240 AND 269 THEN '9'

			WHEN LN.ARREAR_DAYS BETWEEN 270 AND 299 THEN 'T'
			WHEN LN.ARREAR_DAYS BETWEEN 300 AND 329 THEN 'E'
			WHEN LN.ARREAR_DAYS BETWEEN 330 AND 359 THEN 'Y'
			
			ELSE 'L'
			END  AS 'Last Payment Status Code'
		 
        FROM  [InsightLanding].[dbo].[v_AA_BILL_DETAILS] AS B 
        LEFT JOIN  [InsightLanding].[dbo].[v_AA_ARR_ACCOUNT] AS AA ON AA.[ID_COMP_1] = B.[ARRANGEMENT_ID] AND AA.MIS_DATE = B.MIS_DATE
        
        LEFT JOIN [InsightLanding].[dbo].[v_AA_ARRANGEMENT_Product] AS AAP ON AAP.[@ID] =  B.[ARRANGEMENT_ID] AND AAP.MIS_DATE = B.MIS_DATE
        
        LEFT JOIN [InsightLanding].[dbo].[v_AMK_L_LN_COLL_OD_DETS] AS LN ON LN.[@ID] = AA.ACCOUNT_REFERENCE AND LN.MIS_DATE = B.MIS_DATE
        
        WHERE B.MIS_DATE='2019-01-29' AND  B.PAYMENT_TYPE='PRINCIPAL' AND  B.PROPERTY='ACCOUNT'
        AND B.AGING_STATUS IN ('DBT', 'LOS','SMP','STD','SUB')
        --AND LN.ARREAR_DAYS IS NOT NULL

    """
)
filename = 'active_loan_account_verification.csv'

# Delete file first
try:
    os.remove(filename)
except OSError:
    pass
total_accounts = []

with open(filename, 'w+', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'Creditor ID',
        'Period(YYYYMM)',
        'Open Date (YYYY-MM-DD)',
        'Active Account Number',
        'Account Status',
        'Outstanding Balance',
        'Product Type',
        'Currency',
        'Last Payment Status Code'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    i=0
    for row in cursor:
        # print('row = %r' % (row,))
        total_accounts.append(row[3])
        writer.writerow({
            'Creditor ID': row[0],
            'Period(YYYYMM)': row[1],
            'Open Date (YYYY-MM-DD)': row[2],
            'Active Account Number': row[3],
            'Account Status': row[4],
            'Outstanding Balance': row[5],
            'Product Type': row[6],
            'Currency': row[7],
            'Last Payment Status Code': row[8]
        })

print(len(total_accounts))

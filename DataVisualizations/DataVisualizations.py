"""
1. You are given a dataset, which is present in the LMS, containing the number of
hurricanes occurring in the United States along the coast of the Atlantic. Load the
data from the dataset into your program and plot a Bar Graph of the data, taking
the Year as the x-axis and the number of hurricanes occurring as the Y-axis.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data into a pandas dataframe
df = pd.read_csv('/Users/benjaminadams/Downloads/777_m5_datasets_v1.0/Hurricanes.csv')

# Group the data by year and calculate the number of hurricanes occurring each year
hurricanes_by_year = df.groupby('Year')['Hurricanes'].sum()

# Plot the number of hurricanes occurring each year as a bar chart
plt.bar(hurricanes_by_year.index, hurricanes_by_year.values)
plt.xlabel('Year')
plt.ylabel('Number of Hurricanes')
plt.title('Number of Hurricanes Occurring Along the Coast of the Atlantic')
plt.show()

'''
2. The dataset given, records data of city temperatures over the years 2014 and
2015. Plot the histogram of the temperatures over this period for the cities of
San Francisco and Moscow.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Read the data into a dataframe
df = pd.read_csv('/Users/benjaminadams/Downloads/777_m5_datasets_v1.0 2/CityTemps.csv')

# Select the rows for San Francisco and Moscow
sf = df[df['Year'] == 'San Francisco']
moscow = df[df['Year'] == 'Moscow']

# Plot the histogram of temperatures for each city
sf['San Francisco'].plot.hist(bins=20, range=(0, 40), alpha=0.5, color='blue')
moscow['Moscow'].plot.hist(bins=20, range=(0, 40), alpha=0.5, color='red')

# Add a title and label the axes
plt.title('Temperatures in San Francisco and Moscow')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

# Show the plot
plt.show()

'''
3. Plot a pie-chart of the number of models released by every manufacturer,
recorded in the data provide. Also mention the name of the manufacture with
the largest releases.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Load data into a pandas dataframe
df = pd.read_csv('/Users/benjaminadams/Downloads/777_m5_datasets_v1.0 2/Cars2015.csv')

# Group the data by manufacturer and calculate the number of models released by each manufacturer
make_by_manufacturer = df.groupby('Make')['Type'].sum()

# Create a list of values and a list of labels for the pie chart
values = make_by_manufacturer.values
labels = make_by_manufacturer.index

import pandas as pd

# Convert a column in a dataframe from a string to a float
df = pd.DataFrame({
    'value': ['Hatchback', 'SUV', '7Pass', 'Sporty', 'Wagon', 'SUV', 'Sedan']
})

# Replace invalid values with a sentinel value
df['value'].replace('invalid', 'Hatchback ', inplace=True)

df['value'].replace('invalid', 'Sedan', inplace=True)

df['value'].replace('invalid', "7Pass", inplace=True)

df['value'] = pd.to_numeric(df['value'], errors='coerce')
print(df)


# Plot the number of models released by each manufacturer as a pie chart
plt.pie(values, labels=labels)
plt.title('Number of Models Released by Manufacturers')
plt.show()

# Find the manufacturer with the largest number of model releases
max_manufacturer = make_by_manufacturer.idxmax()
print(f'The manufacturer with the largest number of model releases is {max_manufacturer}.')

'''
4. Create csv file from the data below and read in pandas data frame

Phase 1 -Reading Data

Phase 2 –Describe the data
Describe the data on the unit price

Phase 3 –filter the data
Create new dataframe having columns 'name','net_price','date' and group all the
records according to name

Phase 4 –Plotting graph
Plot the graph after calculating total sales by each customer. Customer name should be
on x axis and total sales in y axis.

account_number,name,item_code,category,quantity,unit price,net_price,date
296809,Carroll PLC,QN-82852,Belt,13,44.48,578.24,2014-09-27 07:13:03
098022,Heidenreich-Bosco,MJ-21460,Shoes,19,53.62,1018.78,2014-07-29 02:10:44
563905,"Kerluke, Reilly and Bechtelar",AS-93055,Shirt,12,24.16,289.92,2014-03-01 10:51:24
093356,Waters-Walker,AS-93055,Shirt,5,82.68,413.40,2013-11-17 20:41:11
659366,Waelchi-Fahey,AS-93055,Shirt,18,99.64,1793.52,2014-01-03 08:14:27
563905,"Kerluke, Reilly and Bechtelar",AS-93055,Shirt,17,52.82,897.94,2013-12-04 02:07:05
995267,Cole-Eichmann,GS-86623,Shoes,18,15.28,275.04,2014-04-09 16:15:03
524021,Hegmann and Sons,LL-46261,Shoes,7,78.78,551.46,2014-06-18 19:25:10
929400,"Senger, Upton and Breitenberg",LW-86841,Shoes,17,38.19,649.23,2014-02-10 05:55:56
563905,"Kerluke, Reilly and Bechtelar",KV-99194,Shirt,12,26.98,323.76,2014-05-20 00:21:28
995267,Cole-Eichmann,KV-99194,Shirt,19,60.22,1144.18,2014-03-10 06:23:31
524021,Hegmann and Sons,QN-82852,Belt,6,13.12,78.72,2013-11-03 18:38:16
758133,"Kihn, McClure and Denesik",LL-46261,Shoes,4,59.69,238.76,2014-01-11 21:48:28
555594,"Ernser, Cruickshank and Lind",FK-71853,Shirt,12,97.25,1167.00,2014-09-19 13:20:00
201259,Koelpin PLC,GS-86623,Shoes,9,81.44,732.96,2014-08-12 08:05:27
093356,Waters-Walker,LL-46261,Shoes,18,53.33,959.94,2014-07-15 23:21:11
563905,"Kerluke, Reilly and Bechtelar",KV-99194,Shirt,4,35.62,142.48,2014-10-05 23:38:16
201259,Koelpin PLC,KV-99194,Shirt,17,98.23,1669.91,2014-01-26 01:52:36
758133,"Kihn, McClure and Denesik",WJ-02096,Belt,15,69.52,1042.80,2013-11-13 21:38:46
296809,Carroll PLC,VG-32047,Shirt,12,80.12,961.44,2014-05-24 16:03:28
750461,"Volkman, Goyette and Lemke",WJ-02096,Belt,13,81.19,1055.47,2014-01-08 02:45:07
929400,"Senger, Upton and Breitenberg",LL-46261,Shoes,2,48.15,96.30,2014-04-28 07:01:04
563905,"Kerluke, Reilly and Bechtelar",MJ-21460,Shoes,1,54.94,54.94,2014-08-09 11:22:15
734922,Berge LLC,QN-82852,Belt,4,57.75,231.00,2013-11-04 09:48:26
296809,Carroll PLC,AS-93055,Shirt,14,47.68,667.52,2014-01-12 00:28:09
304860,Huel-Haag,QN-82852,Belt,2,41.40,82.80,2014-09-23 02:36:55
563905,"Kerluke, Reilly and Bechtelar",VG-32047,Shirt,6,58.52,351.12,2014-03-14 02:28:57
750461,"Volkman, Goyette and Lemke",LL-46261,Shoes,12,96.62,1159.44,2013-12-13 03:19:19
850140,Kunze Inc,KV-99194,Shirt,12,93.67,1124.04,2014-02-19 06:03:09
115138,Gorczany-Hahn,VG-32047,Shirt,12,72.63,871.56,2014-02-07 03:30:14
711951,Kilback-Gerlach,AS-93055,Shirt,2,90.80,181.60,2014-03-26 20:56:14
676847,Hamill-Hackett,AS-93055,Shirt,6,42.96,257.76,2013-11-14 22:16:18
711951,Kilback-Gerlach,AS-93055,Shirt,1,71.50,71.50,2014-04-14 16:58:07
305803,"Davis, Kshlerin and Reilly",AS-93055,Shirt,1,74.43,74.43,2014-09-20 09:49:19
201259,Koelpin PLC,GS-86623,Shoes,8,35.38,283.04,2013-12-12 02:37:57
115138,Gorczany-Hahn,QN-82852,Belt,16,24.87,397.92,2014-02-20 07:42:49
296809,Carroll PLC,WJ-02096,Belt,14,15.33,214.62,2013-12-03 01:25:07
093356,Waters-Walker,AS-93055,Shirt,12,94.34,1132.08,2014-09-04 13:39:04
850140,Kunze Inc,MJ-21460,Shoes,18,12.78,230.04,2014-02-20 13:18:47
676847,Hamill-Hackett,LL-46261,Shoes,3,28.71,86.13,2014-01-02 12:49:41
115138,Gorczany-Hahn,VG-32047,Shirt,11,11.21,123.31,2013-12-10 20:13:01
201259,Koelpin PLC,KV-99194,Shirt,4,29.79,119.16,2013-11-07 17:43:31
201259,Koelpin PLC,LW-86841,Shoes,11,35.82,394.02,2014-06-21 19:49:30
676847,Hamill-Hackett,WJ-02096,Belt,6,55.43,332.58,2014-08-08 13:50:43
304860,Huel-Haag,GS-86623,Shoes,4,95.75,383.00,2014-03-15 12:50:59
304860,Huel-Haag,MJ-21460,Shoes,10,12.63,126.30,2014-06-05 22:34:03
850140,Kunze Inc,MJ-21460,Shoes,10,26.21,262.10,2014-04-21 02:14:10
758133,"Kihn, McClure and Denesik",LW-86841,Shoes,11,92.10,1013.10,2014-03-21 14:26:03
750461,"Volkman, Goyette and Lemke",MJ-21460,Shoes,10,98.27,982.70,2014-10-02 04:41:10
555594,"Ernser, Cruickshank and Lind",FK-71853,Shirt,6,65.40,392.40,2014-09-17 19:15:27
995267,Cole-Eichmann,KV-99194,Shirt,10,23.79,237.90,2013-11-17 23:56:36
201259,Koelpin PLC,MJ-21460,Shoes,7,52.01,364.07,2014-05-23 17:49:08
758133,"Kihn, McClure and Denesik",FK-71853,Shirt,11,13.06,143.66,2014-03-01 08:58:41
850140,Kunze Inc,GS-86623,Shoes,14,92.43,1294.02,2014-08-03 21:22:07
201259,Koelpin PLC,FK-71853,Shirt,14,57.69,807.66,2014-05-26 16:29:02
555594,"Ernser, Cruickshank and Lind",KV-99194,Shirt,10,83.05,830.50,2014-01-05 10:16:57
098022,Heidenreich-Bosco,GS-86623,Shoes,10,26.49,264.90,2014-02-12 07:27:39
929400,"Senger, Upton and Breitenberg",GS-86623,Shoes,15,88.24,1323.60,2014-07-09 19:31:43
305803,"Davis, Kshlerin and Reilly",LL-46261,Shoes,13,75.38,979.94,2014-03-05 09:26:56
850140,Kunze Inc,LW-86841,Shoes,16,66.61,1065.76,2014-07-25 22:56:12
734922,Berge LLC,GS-86623,Shoes,3,99.88,299.64,2014-08-04 23:08:09
995267,Cole-Eichmann,AS-93055,Shirt,7,41.75,292.25,2014-07-08 15:01:53
115138,Gorczany-Hahn,AS-93055,Shirt,13,22.23,288.99,2014-01-13 18:31:57
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,18,71.38,1284.84,2014-09-24 04:14:12
098022,Heidenreich-Bosco,LW-86841,Shoes,9,89.82,808.38,2013-11-30 23:19:44
115138,Gorczany-Hahn,KV-99194,Shirt,10,85.12,851.20,2014-05-17 03:23:30
555594,"Ernser, Cruickshank and Lind",VG-32047,Shirt,17,75.04,1275.68,2014-02-09 16:56:59
750461,"Volkman, Goyette and Lemke",KV-99194,Shirt,3,45.05,135.15,2014-02-17 04:26:57
563905,"Kerluke, Reilly and Bechtelar",GS-86623,Shoes,16,76.77,1228.32,2014-01-05 02:40:58
659366,Waelchi-Fahey,VG-32047,Shirt,11,99.09,1089.99,2014-07-15 21:09:33
555594,"Ernser, Cruickshank and Lind",AS-93055,Shirt,3,71.25,213.75,2014-09-29 06:24:24
563905,"Kerluke, Reilly and Bechtelar",QN-82852,Belt,14,40.30,564.20,2014-01-15 18:10:47
659366,Waelchi-Fahey,AS-93055,Shirt,1,10.38,10.38,2014-09-12 21:26:08
304860,Huel-Haag,GS-86623,Shoes,8,69.32,554.56,2014-08-05 15:34:59
758133,"Kihn, McClure and Denesik",QN-82852,Belt,12,82.74,992.88,2014-07-28 00:55:13
524021,Hegmann and Sons,QN-82852,Belt,17,81.64,1387.88,2014-05-29 05:51:07
676847,Hamill-Hackett,LL-46261,Shoes,5,50.63,253.15,2014-10-22 11:43:28
850140,Kunze Inc,LW-86841,Shoes,6,81.41,488.46,2014-09-11 08:41:22
115138,Gorczany-Hahn,QN-82852,Belt,13,18.45,239.85,2014-01-19 21:22:08
563905,"Kerluke, Reilly and Bechtelar",AS-93055,Shirt,17,17.36,295.12,2014-01-29 14:09:39
304860,Huel-Haag,AS-93055,Shirt,9,55.09,495.81,2014-06-28 22:39:25
995267,Cole-Eichmann,LL-46261,Shoes,3,17.54,52.62,2014-01-17 19:11:41
758133,"Kihn, McClure and Denesik",AS-93055,Shirt,7,82.51,577.57,2014-01-13 08:06:03
304860,Huel-Haag,WJ-02096,Belt,3,14.90,44.70,2013-11-21 14:28:29
659366,Waelchi-Fahey,FK-71853,Shirt,6,89.05,534.30,2014-05-15 02:19:37
563905,"Kerluke, Reilly and Bechtelar",QN-82852,Belt,18,57.99,1043.82,2014-09-25 06:23:20
201259,Koelpin PLC,VG-32047,Shirt,1,35.82,35.82,2014-04-01 11:12:52
734922,Berge LLC,LW-86841,Shoes,5,56.00,280.00,2013-11-22 17:45:35
555594,"Ernser, Cruickshank and Lind",WJ-02096,Belt,7,77.52,542.64,2014-02-01 09:30:21
555594,"Ernser, Cruickshank and Lind",LL-46261,Shoes,12,47.07,564.84,2014-08-08 11:08:24
758133,"Kihn, McClure and Denesik",KV-99194,Shirt,18,70.12,1262.16,2013-10-25 03:43:33
563905,"Kerluke, Reilly and Bechtelar",VG-32047,Shirt,20,28.61,572.20,2014-09-30 19:16:05
115138,Gorczany-Hahn,FK-71853,Shirt,12,73.92,887.04,2014-05-15 13:22:25
201259,Koelpin PLC,FK-71853,Shirt,2,38.82,77.64,2013-12-10 17:54:51
299771,"Kuphal, Zieme and Kub",KV-99194,Shirt,14,69.26,969.64,2014-01-20 20:34:55
734922,Berge LLC,GS-86623,Shoes,19,28.54,542.26,2013-10-26 17:03:00
296809,Carroll PLC,LL-46261,Shoes,7,79.15,554.05,2014-03-07 09:38:37
299771,"Kuphal, Zieme and Kub",GS-86623,Shoes,20,36.19,723.80,2014-07-02 08:35:43
750461,"Volkman, Goyette and Lemke",LL-46261,Shoes,19,93.21,1770.99,2014-04-20 18:58:11
201259,Koelpin PLC,MJ-21460,Shoes,5,23.76,118.80,2014-08-17 11:00:49
115138,Gorczany-Hahn,FK-71853,Shirt,2,44.10,88.20,2014-08-09 18:31:40
115138,Gorczany-Hahn,LL-46261,Shoes,20,41.05,821.00,2014-02-20 07:29:02
305803,"Davis, Kshlerin and Reilly",LW-86841,Shoes,19,47.78,907.82,2014-02-22 13:15:38
711951,Kilback-Gerlach,LW-86841,Shoes,9,95.92,863.28,2014-05-29 22:08:13
093356,Waters-Walker,GS-86623,Shoes,4,50.10,200.40,2014-08-11 02:09:32
098022,Heidenreich-Bosco,WJ-02096,Belt,10,75.51,755.10,2013-10-22 23:19:39
555594,"Ernser, Cruickshank and Lind",VG-32047,Shirt,19,64.38,1223.22,2014-09-02 21:51:04
524021,Hegmann and Sons,FK-71853,Shirt,12,17.42,209.04,2014-01-22 14:25:19
115138,Gorczany-Hahn,MJ-21460,Shoes,11,81.67,898.37,2014-09-06 11:50:34
555594,"Ernser, Cruickshank and Lind",VG-32047,Shirt,6,74.08,444.48,2014-02-28 18:37:43
299771,"Kuphal, Zieme and Kub",MJ-21460,Shoes,18,25.91,466.38,2014-08-12 22:48:01
524021,Hegmann and Sons,LL-46261,Shoes,6,57.32,343.92,2013-12-20 12:38:08
750461,"Volkman, Goyette and Lemke",QN-82852,Belt,6,78.61,471.66,2013-12-18 12:13:25
563905,"Kerluke, Reilly and Bechtelar",MJ-21460,Shoes,5,50.85,254.25,2014-08-02 05:30:13
750461,"Volkman, Goyette and Lemke",FK-71853,Shirt,13,72.12,937.56,2014-03-09 14:23:35
299771,"Kuphal, Zieme and Kub",MJ-21460,Shoes,14,24.91,348.74,2014-04-06 19:20:34
555594,"Ernser, Cruickshank and Lind",MJ-21460,Shoes,9,43.25,389.25,2014-04-26 16:22:46
299771,"Kuphal, Zieme and Kub",QN-82852,Belt,12,66.32,795.84,2013-11-19 04:47:16
659366,Waelchi-Fahey,AS-93055,Shirt,2,24.30,48.60,2013-11-10 13:25:32
734922,Berge LLC,MJ-21460,Shoes,12,53.70,644.40,2014-09-27 02:51:01
201259,Koelpin PLC,LL-46261,Shoes,16,80.82,1293.12,2014-08-19 00:53:50
555594,"Ernser, Cruickshank and Lind",QN-82852,Belt,10,91.71,917.10,2014-06-25 19:11:32
563905,"Kerluke, Reilly and Bechtelar",KV-99194,Shirt,11,16.05,176.55,2014-09-26 03:52:52
093356,Waters-Walker,VG-32047,Shirt,17,86.18,1465.06,2014-08-13 15:42:49
758133,"Kihn, McClure and Denesik",LW-86841,Shoes,14,87.56,1225.84,2014-04-27 07:55:06
676847,Hamill-Hackett,GS-86623,Shoes,20,27.49,549.80,2014-07-02 12:51:29
093356,Waters-Walker,GS-86623,Shoes,4,73.11,292.44,2014-08-21 19:29:11
758133,"Kihn, McClure and Denesik",FK-71853,Shirt,11,90.64,997.04,2014-05-11 06:10:17
555594,"Ernser, Cruickshank and Lind",KV-99194,Shirt,12,72.17,866.04,2014-09-15 20:49:18
659366,Waelchi-Fahey,LL-46261,Shoes,9,50.76,456.84,2014-08-29 11:32:00
093356,Waters-Walker,FK-71853,Shirt,16,21.43,342.88,2014-05-25 00:38:58
093356,Waters-Walker,LL-46261,Shoes,20,21.09,421.80,2013-12-23 04:50:54
524021,Hegmann and Sons,VG-32047,Shirt,20,25.37,507.40,2014-07-19 17:18:19
676847,Hamill-Hackett,KV-99194,Shirt,20,29.59,591.80,2014-01-01 19:55:03
995267,Cole-Eichmann,KV-99194,Shirt,17,20.24,344.08,2014-10-01 21:20:26
850140,Kunze Inc,WJ-02096,Belt,13,71.35,927.55,2014-06-09 20:22:22
524021,Hegmann and Sons,KV-99194,Shirt,16,79.67,1274.72,2013-10-25 07:31:02
711951,Kilback-Gerlach,LW-86841,Shoes,2,60.75,121.50,2014-05-17 13:10:42
299771,"Kuphal, Zieme and Kub",KV-99194,Shirt,5,44.47,222.35,2014-04-11 05:00:15
093356,Waters-Walker,GS-86623,Shoes,2,86.17,172.34,2014-03-12 14:25:12
555594,"Ernser, Cruickshank and Lind",LW-86841,Shoes,14,54.50,763.00,2014-10-06 09:47:02
299771,"Kuphal, Zieme and Kub",AS-93055,Shirt,18,37.75,679.50,2014-04-05 20:02:30
299771,"Kuphal, Zieme and Kub",FK-71853,Shirt,20,32.70,654.00,2014-04-26 05:18:02
296809,Carroll PLC,MJ-21460,Shoes,15,93.06,1395.90,2014-08-17 18:39:56
750461,"Volkman, Goyette and Lemke",LL-46261,Shoes,17,49.59,843.03,2013-10-29 12:57:27
750461,"Volkman, Goyette and Lemke",WJ-02096,Belt,17,45.43,772.31,2014-05-09 06:44:04
711951,Kilback-Gerlach,AS-93055,Shirt,2,31.54,63.08,2014-01-26 05:15:19
304860,Huel-Haag,LW-86841,Shoes,6,93.02,558.12,2013-11-23 08:51:18
750461,"Volkman, Goyette and Lemke",FK-71853,Shirt,16,57.02,912.32,2014-10-14 14:07:31
711951,Kilback-Gerlach,FK-71853,Shirt,11,53.17,584.87,2014-06-10 15:11:01
305803,"Davis, Kshlerin and Reilly",LL-46261,Shoes,12,52.51,630.12,2014-08-03 03:39:52
115138,Gorczany-Hahn,MJ-21460,Shoes,13,96.31,1252.03,2013-12-03 04:04:40
201259,Koelpin PLC,LW-86841,Shoes,16,90.97,1455.52,2014-08-29 07:41:36
734922,Berge LLC,KV-99194,Shirt,7,64.02,448.14,2013-11-05 03:55:12
563905,"Kerluke, Reilly and Bechtelar",GS-86623,Shoes,15,18.41,276.15,2014-03-02 17:47:13
305803,"Davis, Kshlerin and Reilly",MJ-21460,Shoes,2,29.63,59.26,2014-03-27 23:48:17
750461,"Volkman, Goyette and Lemke",FK-71853,Shirt,4,46.82,187.28,2014-02-15 06:51:19
850140,Kunze Inc,VG-32047,Shirt,9,93.69,843.21,2014-03-20 15:25:39
093356,Waters-Walker,GS-86623,Shoes,15,64.11,961.65,2013-10-23 08:28:53
304860,Huel-Haag,LL-46261,Shoes,3,48.87,146.61,2014-04-03 22:36:22
929400,"Senger, Upton and Breitenberg",MJ-21460,Shoes,14,87.01,1218.14,2013-12-14 16:40:16
929400,"Senger, Upton and Breitenberg",KV-99194,Shirt,4,17.98,71.92,2014-07-22 19:10:27
734922,Berge LLC,AS-93055,Shirt,10,93.77,937.70,2014-08-17 09:21:15
734922,Berge LLC,MJ-21460,Shoes,6,84.73,508.38,2014-07-20 18:27:59
711951,Kilback-Gerlach,QN-82852,Belt,11,45.49,500.39,2013-11-12 10:13:25
299771,"Kuphal, Zieme and Kub",LL-46261,Shoes,17,70.23,1193.91,2014-08-14 13:57:01
995267,Cole-Eichmann,FK-71853,Shirt,10,51.29,512.90,2014-09-16 05:26:10
093356,Waters-Walker,AS-93055,Shirt,16,75.48,1207.68,2014-08-23 04:04:11
676847,Hamill-Hackett,MJ-21460,Shoes,19,56.90,1081.10,2014-10-21 08:46:48
524021,Hegmann and Sons,FK-71853,Shirt,10,71.89,718.90,2014-09-11 00:45:37
929400,"Senger, Upton and Breitenberg",MJ-21460,Shoes,10,13.02,130.20,2014-06-30 10:31:23
304860,Huel-Haag,MJ-21460,Shoes,3,79.49,238.47,2014-06-02 13:06:24
734922,Berge LLC,AS-93055,Shirt,11,81.53,896.83,2014-09-01 17:46:10
659366,Waelchi-Fahey,LL-46261,Shoes,1,18.68,18.68,2014-05-19 18:10:49
201259,Koelpin PLC,MJ-21460,Shoes,20,45.32,906.40,2014-07-06 22:06:23
711951,Kilback-Gerlach,AS-93055,Shirt,10,68.74,687.40,2014-03-27 12:14:12
750461,"Volkman, Goyette and Lemke",AS-93055,Shirt,10,90.00,900.00,2014-07-10 22:17:15
995267,Cole-Eichmann,WJ-02096,Belt,6,20.30,121.80,2014-05-23 10:24:32
563905,"Kerluke, Reilly and Bechtelar",VG-32047,Shirt,17,58.67,997.39,2013-12-08 13:43:29
659366,Waelchi-Fahey,FK-71853,Shirt,2,12.68,25.36,2014-04-27 03:38:16
676847,Hamill-Hackett,GS-86623,Shoes,17,49.68,844.56,2014-01-28 15:37:10
524021,Hegmann and Sons,MJ-21460,Shoes,2,95.37,190.74,2014-03-30 08:27:54
524021,Hegmann and Sons,AS-93055,Shirt,20,96.98,1939.60,2014-06-13 18:23:55
296809,Carroll PLC,VG-32047,Shirt,16,23.79,380.64,2014-02-26 18:22:57
995267,Cole-Eichmann,KV-99194,Shirt,2,37.86,75.72,2014-04-04 19:30:50
304860,Huel-Haag,KV-99194,Shirt,9,66.18,595.62,2014-01-15 11:55:40
524021,Hegmann and Sons,KV-99194,Shirt,6,98.89,593.34,2014-04-22 00:24:15
758133,"Kihn, McClure and Denesik",VG-32047,Shirt,4,25.02,100.08,2014-05-26 06:54:22
563905,"Kerluke, Reilly and Bechtelar",WJ-02096,Belt,16,64.58,1033.28,2013-12-17 23:35:15
305803,"Davis, Kshlerin and Reilly",FK-71853,Shirt,18,48.70,876.60,2014-02-10 08:43:23
734922,Berge LLC,QN-82852,Belt,16,24.66,394.56,2013-12-12 00:57:07
563905,"Kerluke, Reilly and Bechtelar",LW-86841,Shoes,5,43.15,215.75,2014-04-06 06:24:33
296809,Carroll PLC,QN-82852,Belt,2,54.52,109.04,2014-08-24 09:43:19
929400,"Senger, Upton and Breitenberg",WJ-02096,Belt,8,91.14,729.12,2014-06-11 10:12:04
098022,Heidenreich-Bosco,LW-86841,Shoes,13,65.79,855.27,2014-06-28 04:47:33
750461,"Volkman, Goyette and Lemke",AS-93055,Shirt,8,14.73,117.84,2014-03-19 05:18:21
758133,"Kihn, McClure and Denesik",VG-32047,Shirt,14,96.18,1346.52,2014-10-04 09:49:10
524021,Hegmann and Sons,MJ-21460,Shoes,6,81.10,486.60,2014-02-15 15:29:46
098022,Heidenreich-Bosco,FK-71853,Shirt,12,38.32,459.84,2014-06-25 09:29:53
929400,"Senger, Upton and Breitenberg",FK-71853,Shirt,3,51.80,155.40,2014-03-31 04:17:46
850140,Kunze Inc,FK-71853,Shirt,13,40.29,523.77,2014-09-01 23:53:15
098022,Heidenreich-Bosco,KV-99194,Shirt,10,22.17,221.70,2014-02-26 06:59:32
711951,Kilback-Gerlach,MJ-21460,Shoes,15,43.41,651.15,2014-03-09 00:29:06
115138,Gorczany-Hahn,KV-99194,Shirt,11,67.32,740.52,2014-02-28 18:44:43
524021,Hegmann and Sons,FK-71853,Shirt,3,17.90,53.70,2014-10-14 19:22:12
563905,"Kerluke, Reilly and Bechtelar",LW-86841,Shoes,7,44.27,309.89,2014-10-08 13:05:13
524021,Hegmann and Sons,FK-71853,Shirt,18,51.72,930.96,2014-02-14 00:05:05
305803,"Davis, Kshlerin and Reilly",AS-93055,Shirt,9,22.01,198.09,2014-04-08 03:17:21
563905,"Kerluke, Reilly and Bechtelar",KV-99194,Shirt,10,36.38,363.80,2014-01-02 13:43:36
304860,Huel-Haag,FK-71853,Shirt,11,63.78,701.58,2014-07-15 23:58:16
201259,Koelpin PLC,MJ-21460,Shoes,10,56.51,565.10,2014-09-22 16:34:24
555594,"Ernser, Cruickshank and Lind",AS-93055,Shirt,2,10.47,20.94,2014-04-23 15:24:21
734922,Berge LLC,GS-86623,Shoes,8,21.39,171.12,2014-03-12 11:43:23
201259,Koelpin PLC,LL-46261,Shoes,13,26.49,344.37,2014-09-09 14:59:01
758133,"Kihn, McClure and Denesik",VG-32047,Shirt,20,95.60,1912.00,2014-10-12 20:10:43
995267,Cole-Eichmann,LL-46261,Shoes,17,72.91,1239.47,2014-02-26 16:19:25
659366,Waelchi-Fahey,FK-71853,Shirt,15,89.45,1341.75,2014-09-09 09:21:01
305803,"Davis, Kshlerin and Reilly",KV-99194,Shirt,4,63.39,253.56,2014-09-15 18:49:05
305803,"Davis, Kshlerin and Reilly",QN-82852,Belt,15,51.64,774.60,2014-09-07 02:44:53
115138,Gorczany-Hahn,LW-86841,Shoes,6,72.98,437.88,2014-06-15 03:34:22
850140,Kunze Inc,MJ-21460,Shoes,8,63.28,506.24,2014-06-21 21:09:50
555594,"Ernser, Cruickshank and Lind",WJ-02096,Belt,15,63.31,949.65,2014-04-23 06:25:35
734922,Berge LLC,MJ-21460,Shoes,10,44.59,445.90,2014-05-04 18:52:20
563905,"Kerluke, Reilly and Bechtelar",LW-86841,Shoes,7,41.87,293.09,2013-12-09 01:15:23
299771,"Kuphal, Zieme and Kub",LW-86841,Shoes,4,35.00,140.00,2014-04-13 20:37:05
659366,Waelchi-Fahey,WJ-02096,Belt,13,68.39,889.07,2013-11-27 12:45:23
555594,"Ernser, Cruickshank and Lind",LL-46261,Shoes,8,82.19,657.52,2014-07-19 13:51:23
296809,Carroll PLC,AS-93055,Shirt,1,58.80,58.80,2014-09-06 13:00:55
296809,Carroll PLC,QN-82852,Belt,16,27.44,439.04,2014-07-06 13:23:48
296809,Carroll PLC,MJ-21460,Shoes,14,99.50,1393.00,2014-06-07 23:28:22
929400,"Senger, Upton and Breitenberg",MJ-21460,Shoes,3,56.34,169.02,2014-07-13 09:41:43
995267,Cole-Eichmann,LW-86841,Shoes,9,83.87,754.83,2014-07-28 01:53:47
296809,Carroll PLC,MJ-21460,Shoes,19,56.63,1075.97,2013-12-08 02:40:53
711951,Kilback-Gerlach,WJ-02096,Belt,1,56.95,56.95,2014-03-08 15:50:55
524021,Hegmann and Sons,GS-86623,Shoes,10,31.81,318.10,2013-11-18 23:11:16
995267,Cole-Eichmann,QN-82852,Belt,13,40.34,524.42,2014-09-08 14:00:39
758133,"Kihn, McClure and Denesik",GS-86623,Shoes,10,91.59,915.90,2014-03-19 14:06:11
758133,"Kihn, McClure and Denesik",GS-86623,Shoes,7,95.78,670.46,2014-05-16 23:44:14
296809,Carroll PLC,LL-46261,Shoes,9,90.91,818.19,2014-10-11 20:37:05
758133,"Kihn, McClure and Denesik",AS-93055,Shirt,12,24.09,289.08,2013-12-08 06:53:09
711951,Kilback-Gerlach,LL-46261,Shoes,9,10.81,97.29,2013-12-06 00:59:43
093356,Waters-Walker,QN-82852,Belt,3,59.61,178.83,2014-08-02 13:29:11
201259,Koelpin PLC,WJ-02096,Belt,16,16.30,260.80,2014-04-05 02:00:02
929400,"Senger, Upton and Breitenberg",LL-46261,Shoes,4,23.08,92.32,2014-09-13 11:34:24
524021,Hegmann and Sons,MJ-21460,Shoes,18,42.01,756.18,2013-11-27 03:18:14
676847,Hamill-Hackett,LL-46261,Shoes,5,74.02,370.10,2013-11-10 07:30:39
093356,Waters-Walker,QN-82852,Belt,11,77.66,854.26,2014-03-15 17:01:26
098022,Heidenreich-Bosco,LL-46261,Shoes,7,14.75,103.25,2014-09-14 23:53:52
659366,Waelchi-Fahey,LW-86841,Shoes,16,38.75,620.00,2014-03-20 05:48:40
929400,"Senger, Upton and Breitenberg",LL-46261,Shoes,13,53.39,694.07,2014-02-26 15:03:04
676847,Hamill-Hackett,KV-99194,Shirt,1,55.51,55.51,2014-07-15 17:41:23
305803,"Davis, Kshlerin and Reilly",KV-99194,Shirt,7,16.00,112.00,2014-05-05 21:05:51
850140,Kunze Inc,AS-93055,Shirt,20,63.75,1275.00,2014-02-09 10:28:34
201259,Koelpin PLC,GS-86623,Shoes,15,66.78,1001.70,2014-04-29 20:36:59
093356,Waters-Walker,VG-32047,Shirt,2,75.16,150.32,2013-11-26 12:30:16
098022,Heidenreich-Bosco,MJ-21460,Shoes,14,34.80,487.20,2014-03-08 06:35:20
296809,Carroll PLC,QN-82852,Belt,14,14.82,207.48,2014-04-06 19:17:38
676847,Hamill-Hackett,VG-32047,Shirt,4,88.99,355.96,2013-12-16 01:09:18
711951,Kilback-Gerlach,LW-86841,Shoes,13,71.43,928.59,2014-04-26 03:39:28
304860,Huel-Haag,LL-46261,Shoes,6,23.37,140.22,2013-10-22 22:50:47
711951,Kilback-Gerlach,LL-46261,Shoes,19,30.06,571.14,2014-06-28 01:20:04
555594,"Ernser, Cruickshank and Lind",QN-82852,Belt,2,74.42,148.84,2013-12-09 09:10:44
659366,Waelchi-Fahey,QN-82852,Belt,4,38.69,154.76,2014-02-14 02:42:30
201259,Koelpin PLC,AS-93055,Shirt,3,16.22,48.66,2014-07-11 08:17:44
296809,Carroll PLC,VG-32047,Shirt,15,63.45,951.75,2014-10-12 09:08:07
563905,"Kerluke, Reilly and Bechtelar",KV-99194,Shirt,19,78.34,1488.46,2014-09-28 19:20:15
299771,"Kuphal, Zieme and Kub",KV-99194,Shirt,9,79.63,716.67,2014-02-16 01:11:09
750461,"Volkman, Goyette and Lemke",LW-86841,Shoes,3,96.59,289.77,2014-01-11 05:10:44
524021,Hegmann and Sons,WJ-02096,Belt,20,66.27,1325.40,2014-10-05 01:36:59
115138,Gorczany-Hahn,AS-93055,Shirt,8,16.11,128.88,2014-08-06 01:09:28
850140,Kunze Inc,FK-71853,Shirt,7,76.23,533.61,2013-11-06 02:36:22
524021,Hegmann and Sons,LL-46261,Shoes,15,20.61,309.15,2014-05-26 03:15:30
995267,Cole-Eichmann,GS-86623,Shoes,6,55.05,330.30,2013-12-27 08:33:09
299771,"Kuphal, Zieme and Kub",LW-86841,Shoes,9,60.33,542.97,2014-09-16 13:47:08
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,12,96.02,1152.24,2014-04-06 03:35:41
555594,"Ernser, Cruickshank and Lind",KV-99194,Shirt,16,94.05,1504.80,2014-03-13 22:14:32
734922,Berge LLC,MJ-21460,Shoes,19,88.62,1683.78,2014-01-29 06:44:37
850140,Kunze Inc,FK-71853,Shirt,6,38.76,232.56,2014-09-18 05:56:57
995267,Cole-Eichmann,QN-82852,Belt,10,12.35,123.50,2014-07-05 01:51:03
299771,"Kuphal, Zieme and Kub",LW-86841,Shoes,3,30.77,92.31,2014-03-01 02:12:31
659366,Waelchi-Fahey,FK-71853,Shirt,14,23.86,334.04,2014-09-30 12:37:58
659366,Waelchi-Fahey,WJ-02096,Belt,3,72.43,217.29,2014-10-03 23:46:12
296809,Carroll PLC,VG-32047,Shirt,10,91.46,914.60,2013-11-24 08:11:02
850140,Kunze Inc,QN-82852,Belt,19,75.70,1438.30,2014-02-15 14:11:02
563905,"Kerluke, Reilly and Bechtelar",KV-99194,Shirt,9,95.53,859.77,2014-03-18 14:35:55
305803,"Davis, Kshlerin and Reilly",AS-93055,Shirt,15,67.57,1013.55,2014-08-02 12:03:04
093356,Waters-Walker,GS-86623,Shoes,3,99.42,298.26,2014-01-27 11:30:33
304860,Huel-Haag,MJ-21460,Shoes,9,75.62,680.58,2013-12-18 14:27:30
305803,"Davis, Kshlerin and Reilly",LL-46261,Shoes,9,84.10,756.90,2014-10-06 21:13:27
093356,Waters-Walker,LL-46261,Shoes,11,78.54,863.94,2013-12-28 22:14:49
758133,"Kihn, McClure and Denesik",VG-32047,Shirt,3,67.37,202.11,2014-09-01 18:40:25
563905,"Kerluke, Reilly and Bechtelar",MJ-21460,Shoes,15,42.96,644.40,2014-04-06 13:20:57
734922,Berge LLC,LL-46261,Shoes,2,62.32,124.64,2014-03-12 11:38:47
711951,Kilback-Gerlach,AS-93055,Shirt,7,82.95,580.65,2014-08-05 11:34:16
201259,Koelpin PLC,WJ-02096,Belt,14,40.79,571.06,2014-01-16 02:43:35
304860,Huel-Haag,QN-82852,Belt,7,38.58,270.06,2014-08-29 23:41:16
676847,Hamill-Hackett,FK-71853,Shirt,1,99.97,99.97,2014-05-10 12:10:10
711951,Kilback-Gerlach,GS-86623,Shoes,11,96.66,1063.26,2014-02-13 11:43:17
563905,"Kerluke, Reilly and Bechtelar",FK-71853,Shirt,17,75.69,1286.73,2013-11-25 02:35:28
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,18,42.02,756.36,2014-03-19 23:24:01
115138,Gorczany-Hahn,WJ-02096,Belt,12,80.25,963.00,2013-11-06 05:25:34
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,4,70.28,281.12,2014-01-25 23:43:12
305803,"Davis, Kshlerin and Reilly",LW-86841,Shoes,5,49.68,248.40,2014-09-20 17:40:46
299771,"Kuphal, Zieme and Kub",GS-86623,Shoes,14,73.92,1034.88,2013-11-23 17:48:24
296809,Carroll PLC,WJ-02096,Belt,17,69.41,1179.97,2014-09-11 02:20:46
850140,Kunze Inc,AS-93055,Shirt,18,87.42,1573.56,2014-05-31 04:28:20
850140,Kunze Inc,KV-99194,Shirt,20,74.34,1486.80,2014-01-27 19:42:12
305803,"Davis, Kshlerin and Reilly",VG-32047,Shirt,17,59.12,1005.04,2014-05-11 06:38:13
850140,Kunze Inc,AS-93055,Shirt,14,77.40,1083.60,2014-08-16 21:03:22
734922,Berge LLC,LL-46261,Shoes,15,58.85,882.75,2014-08-22 04:35:06
305803,"Davis, Kshlerin and Reilly",QN-82852,Belt,1,44.77,44.77,2014-02-25 11:20:59
201259,Koelpin PLC,VG-32047,Shirt,15,26.93,403.95,2014-01-24 10:23:39
093356,Waters-Walker,MJ-21460,Shoes,12,95.96,1151.52,2014-06-12 00:58:43
299771,"Kuphal, Zieme and Kub",AS-93055,Shirt,8,31.12,248.96,2013-12-03 14:12:26
563905,"Kerluke, Reilly and Bechtelar",GS-86623,Shoes,7,83.84,586.88,2014-10-20 05:47:49
563905,"Kerluke, Reilly and Bechtelar",LW-86841,Shoes,4,19.86,79.44,2013-11-30 16:47:24
299771,"Kuphal, Zieme and Kub",FK-71853,Shirt,3,77.07,231.21,2014-06-14 17:54:02
734922,Berge LLC,LW-86841,Shoes,15,46.94,704.10,2014-05-23 13:09:21
711951,Kilback-Gerlach,FK-71853,Shirt,11,39.02,429.22,2013-12-08 14:04:38
734922,Berge LLC,VG-32047,Shirt,2,33.92,67.84,2014-06-27 15:53:05
299771,"Kuphal, Zieme and Kub",FK-71853,Shirt,11,81.22,893.42,2013-12-01 05:10:26
201259,Koelpin PLC,QN-82852,Belt,2,25.42,50.84,2014-03-21 17:57:32
563905,"Kerluke, Reilly and Bechtelar",LW-86841,Shoes,4,59.07,236.28,2014-04-07 08:54:29
304860,Huel-Haag,KV-99194,Shirt,15,50.20,753.00,2013-12-29 14:24:05
305803,"Davis, Kshlerin and Reilly",LW-86841,Shoes,3,24.83,74.49,2014-05-20 15:22:35
201259,Koelpin PLC,MJ-21460,Shoes,12,89.95,1079.40,2013-12-28 16:19:22
758133,"Kihn, McClure and Denesik",LW-86841,Shoes,4,67.14,268.56,2014-01-30 10:21:27
524021,Hegmann and Sons,FK-71853,Shirt,8,22.67,181.36,2013-12-30 14:16:13
758133,"Kihn, McClure and Denesik",AS-93055,Shirt,6,50.19,301.14,2014-04-26 22:58:25
734922,Berge LLC,KV-99194,Shirt,7,46.71,326.97,2014-06-15 15:52:58
659366,Waelchi-Fahey,FK-71853,Shirt,17,75.46,1282.82,2013-11-17 15:36:57
750461,"Volkman, Goyette and Lemke",FK-71853,Shirt,13,23.73,308.49,2014-01-11 12:21:50
711951,Kilback-Gerlach,QN-82852,Belt,11,71.02,781.22,2014-01-14 18:43:44
734922,Berge LLC,MJ-21460,Shoes,15,77.10,1156.50,2013-12-07 11:53:40
758133,"Kihn, McClure and Denesik",LW-86841,Shoes,3,39.99,119.97,2013-11-13 02:00:22
201259,Koelpin PLC,QN-82852,Belt,14,95.77,1340.78,2014-05-04 10:45:11
850140,Kunze Inc,GS-86623,Shoes,14,13.93,195.02,2014-01-23 17:49:03
555594,"Ernser, Cruickshank and Lind",MJ-21460,Shoes,15,42.09,631.35,2014-10-17 03:56:02
201259,Koelpin PLC,VG-32047,Shirt,5,60.51,302.55,2014-10-22 07:16:46
296809,Carroll PLC,GS-86623,Shoes,5,41.58,207.90,2014-03-29 08:13:19
734922,Berge LLC,QN-82852,Belt,12,89.48,1073.76,2014-05-23 06:43:54
850140,Kunze Inc,MJ-21460,Shoes,2,18.29,36.58,2014-01-16 20:23:03
304860,Huel-Haag,WJ-02096,Belt,1,23.12,23.12,2014-10-17 20:09:53
659366,Waelchi-Fahey,MJ-21460,Shoes,14,53.60,750.40,2014-09-14 11:01:14
750461,"Volkman, Goyette and Lemke",MJ-21460,Shoes,16,72.41,1158.56,2014-09-19 21:41:12
201259,Koelpin PLC,MJ-21460,Shoes,5,33.20,166.00,2014-09-04 23:45:59
563905,"Kerluke, Reilly and Bechtelar",VG-32047,Shirt,20,14.99,299.80,2014-06-01 20:29:08
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,3,45.60,136.80,2013-12-21 04:01:40
750461,"Volkman, Goyette and Lemke",AS-93055,Shirt,18,80.70,1452.60,2014-05-09 23:51:49
734922,Berge LLC,MJ-21460,Shoes,4,15.22,60.88,2013-11-15 07:17:16
734922,Berge LLC,LL-46261,Shoes,13,53.11,690.43,2014-08-29 16:34:09
115138,Gorczany-Hahn,QN-82852,Belt,1,90.21,90.21,2014-01-30 17:16:08
676847,Hamill-Hackett,VG-32047,Shirt,4,76.81,307.24,2014-09-06 20:28:27
098022,Heidenreich-Bosco,AS-93055,Shirt,17,61.31,1042.27,2014-03-19 02:46:57
524021,Hegmann and Sons,FK-71853,Shirt,7,33.00,231.00,2014-02-04 19:29:41
995267,Cole-Eichmann,QN-82852,Belt,4,36.62,146.48,2014-08-11 23:29:08
758133,"Kihn, McClure and Denesik",LW-86841,Shoes,10,72.10,721.00,2014-07-19 16:40:01
524021,Hegmann and Sons,AS-93055,Shirt,18,23.74,427.32,2014-06-18 06:31:15
750461,"Volkman, Goyette and Lemke",LL-46261,Shoes,6,51.13,306.78,2014-06-13 21:32:57
093356,Waters-Walker,FK-71853,Shirt,17,58.55,995.35,2014-05-04 23:02:26
299771,"Kuphal, Zieme and Kub",MJ-21460,Shoes,6,54.27,325.62,2014-05-15 19:28:27
305803,"Davis, Kshlerin and Reilly",LL-46261,Shoes,13,77.78,1011.14,2013-11-30 17:23:21
201259,Koelpin PLC,QN-82852,Belt,8,69.58,556.64,2014-04-03 01:34:49
676847,Hamill-Hackett,LW-86841,Shoes,10,67.36,673.60,2014-07-15 04:34:11
299771,"Kuphal, Zieme and Kub",LL-46261,Shoes,15,16.55,248.25,2014-01-09 17:51:49
929400,"Senger, Upton and Breitenberg",MJ-21460,Shoes,16,99.13,1586.08,2014-09-26 10:54:06
995267,Cole-Eichmann,QN-82852,Belt,17,69.11,1174.87,2014-09-23 05:58:41
563905,"Kerluke, Reilly and Bechtelar",AS-93055,Shirt,12,81.57,978.84,2014-09-25 14:09:16
563905,"Kerluke, Reilly and Bechtelar",FK-71853,Shirt,20,62.12,1242.40,2014-07-01 22:14:25
734922,Berge LLC,VG-32047,Shirt,4,96.25,385.00,2014-07-09 19:18:49
098022,Heidenreich-Bosco,LL-46261,Shoes,18,71.34,1284.12,2013-11-17 00:18:08
711951,Kilback-Gerlach,QN-82852,Belt,19,33.10,628.90,2014-03-04 07:23:35
296809,Carroll PLC,WJ-02096,Belt,15,38.73,580.95,2014-02-03 03:57:26
929400,"Senger, Upton and Breitenberg",VG-32047,Shirt,17,43.10,732.70,2014-08-19 11:22:06
296809,Carroll PLC,WJ-02096,Belt,16,91.09,1457.44,2014-03-18 23:14:03
524021,Hegmann and Sons,LW-86841,Shoes,13,60.72,789.36,2014-01-18 22:40:14
201259,Koelpin PLC,QN-82852,Belt,3,64.13,192.39,2014-08-07 15:28:03
758133,"Kihn, McClure and Denesik",GS-86623,Shoes,14,40.86,572.04,2014-08-21 08:07:56
676847,Hamill-Hackett,LW-86841,Shoes,1,73.74,73.74,2014-09-04 10:46:25
305803,"Davis, Kshlerin and Reilly",VG-32047,Shirt,6,26.40,158.40,2014-09-04 09:18:54
850140,Kunze Inc,MJ-21460,Shoes,19,36.32,690.08,2014-08-10 20:15:29
676847,Hamill-Hackett,LL-46261,Shoes,17,10.96,186.32,2014-01-19 22:01:00
115138,Gorczany-Hahn,FK-71853,Shirt,17,88.39,1502.63,2014-07-31 12:28:26
098022,Heidenreich-Bosco,VG-32047,Shirt,20,94.00,1880.00,2014-05-31 22:53:56
555594,"Ernser, Cruickshank and Lind",LW-86841,Shoes,4,34.42,137.68,2014-10-10 18:54:24
299771,"Kuphal, Zieme and Kub",GS-86623,Shoes,14,68.25,955.50,2014-03-16 21:35:20
299771,"Kuphal, Zieme and Kub",LW-86841,Shoes,5,89.36,446.80,2014-06-08 14:33:12
758133,"Kihn, McClure and Denesik",KV-99194,Shirt,3,44.37,133.11,2014-04-23 12:05:25
850140,Kunze Inc,VG-32047,Shirt,11,69.20,761.20,2014-03-14 03:16:51
555594,"Ernser, Cruickshank and Lind",QN-82852,Belt,12,92.94,1115.28,2014-10-10 18:02:37
995267,Cole-Eichmann,VG-32047,Shirt,4,54.20,216.80,2014-08-28 06:28:19
676847,Hamill-Hackett,QN-82852,Belt,3,42.71,128.13,2014-06-09 12:21:47
929400,"Senger, Upton and Breitenberg",KV-99194,Shirt,4,81.46,325.84,2013-10-25 16:52:01
098022,Heidenreich-Bosco,MJ-21460,Shoes,9,22.08,198.72,2014-01-21 05:08:12
305803,"Davis, Kshlerin and Reilly",AS-93055,Shirt,8,98.01,784.08,2014-04-11 08:23:07
750461,"Volkman, Goyette and Lemke",WJ-02096,Belt,13,83.60,1086.80,2014-08-19 20:42:22
098022,Heidenreich-Bosco,MJ-21460,Shoes,1,82.28,82.28,2014-10-05 08:28:30
676847,Hamill-Hackett,AS-93055,Shirt,16,44.38,710.08,2014-09-16 05:22:44
093356,Waters-Walker,MJ-21460,Shoes,5,54.96,274.80,2013-11-18 19:41:31
299771,"Kuphal, Zieme and Kub",VG-32047,Shirt,7,97.85,684.95,2014-03-02 21:47:35
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,11,12.27,134.97,2014-01-15 07:26:27
563905,"Kerluke, Reilly and Bechtelar",LL-46261,Shoes,8,83.88,671.04,2014-07-03 13:24:21
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,2,31.18,62.36,2014-09-21 03:36:32
524021,Hegmann and Sons,WJ-02096,Belt,13,15.28,198.64,2014-07-26 14:07:00
711951,Kilback-Gerlach,QN-82852,Belt,14,40.48,566.72,2014-07-10 06:12:22
563905,"Kerluke, Reilly and Bechtelar",LW-86841,Shoes,5,38.73,193.65,2014-04-26 11:51:54
201259,Koelpin PLC,GS-86623,Shoes,5,23.38,116.90,2014-07-26 09:33:15
711951,Kilback-Gerlach,LL-46261,Shoes,1,54.04,54.04,2014-06-09 20:05:03
734922,Berge LLC,WJ-02096,Belt,17,25.26,429.42,2014-06-16 10:03:35
850140,Kunze Inc,GS-86623,Shoes,3,46.00,138.00,2013-10-25 11:42:04
676847,Hamill-Hackett,GS-86623,Shoes,8,34.76,278.08,2013-11-19 02:20:09
734922,Berge LLC,VG-32047,Shirt,1,93.10,93.10,2013-12-25 10:00:14
555594,"Ernser, Cruickshank and Lind",KV-99194,Shirt,10,23.43,234.30,2014-08-20 16:25:05
305803,"Davis, Kshlerin and Reilly",WJ-02096,Belt,7,41.77,292.39,2014-10-21 05:51:47
676847,Hamill-Hackett,QN-82852,Belt,11,53.13,584.43,2014-09-24 02:05:24
711951,Kilback-Gerlach,LW-86841,Shoes,9,90.02,810.18,2014-08-22 13:18:26
676847,Hamill-Hackett,KV-99194,Shirt,14,37.64,526.96,2014-02-15 06:51:00
299771,"Kuphal, Zieme and Kub",KV-99194,Shirt,18,50.99,917.82,2014-02-20 05:55:31
296809,Carroll PLC,VG-32047,Shirt,9,67.68,609.12,2014-05-22 05:51:16
299771,"Kuphal, Zieme and Kub",AS-93055,Shirt,18,19.01,342.18,2013-11-14 11:33:02
659366,Waelchi-Fahey,MJ-21460,Shoes,15,19.62,294.30,2013-11-24 23:33:56
659366,Waelchi-Fahey,WJ-02096,Belt,14,75.49,1056.86,2014-02-18 02:07:31
305803,"Davis, Kshlerin and Reilly",WJ-02096,Belt,1,69.57,69.57,2013-12-21 16:04:44
115138,Gorczany-Hahn,WJ-02096,Belt,6,95.08,570.48,2014-02-01 01:28:20
305803,"Davis, Kshlerin and Reilly",GS-86623,Shoes,17,20.45,347.65,2014-08-30 03:56:20
305803,"Davis, Kshlerin and Reilly",QN-82852,Belt,4,85.30,341.20,2014-10-17 13:18:21
304860,Huel-Haag,VG-32047,Shirt,16,63.97,1023.52,2014-02-06 19:14:35
299771,"Kuphal, Zieme and Kub",GS-86623,Shoes,1,93.72,93.72,2014-09-30 09:16:18
758133,"Kihn, McClure and Denesik",AS-93055,Shirt,12,64.09,769.08,2014-04-22 14:36:05
093356,Waters-Walker,LW-86841,Shoes,16,16.59,265.44,2014-09-07 02:26:24
115138,Gorczany-Hahn,WJ-02096,Belt,3,52.57,157.71,2014-08-15 13:23:42
929400,"Senger, Upton and Breitenberg",VG-32047,Shirt,1,34.40,34.40,2014-05-19 20:50:19
093356,Waters-Walker,VG-32047,Shirt,13,45.97,597.61,2014-07-05 08:56:46
296809,Carroll PLC,LL-46261,Shoes,10,37.40,374.00,2014-05-05 05:17:28
750461,"Volkman, Goyette and Lemke",LW-86841,Shoes,14,15.58,218.12,2013-12-23 21:32:05
995267,Cole-Eichmann,AS-93055,Shirt,11,45.24,497.64,2014-08-06 01:25:27
734922,Berge LLC,GS-86623,Shoes,9,30.49,274.41,2014-03-02 13:04:07
758133,"Kihn, McClure and Denesik",KV-99194,Shirt,18,90.84,1635.12,2014-02-01 21:38:06
659366,Waelchi-Fahey,GS-86623,Shoes,1,38.20,38.20,2013-11-23 15:45:41
850140,Kunze Inc,QN-82852,Belt,8,72.29,578.32,2014-02-15 21:05:44
850140,Kunze Inc,MJ-21460,Shoes,20,61.03,1220.60,2013-12-23 23:07:45
299771,"Kuphal, Zieme and Kub",KV-99194,Shirt,18,77.66,1397.88,2014-10-18 18:07:37
929400,"Senger, Upton and Breitenberg",VG-32047,Shirt,10,16.01,160.10,2014-05-07 20:02:28
676847,Hamill-Hackett,LW-86841,Shoes,9,61.42,552.78,2014-10-16 12:50:55
304860,Huel-Haag,VG-32047,Shirt,17,64.75,1100.75,2014-09-13 02:51:49
296809,Carroll PLC,KV-99194,Shirt,16,50.36,805.76,2014-01-03 07:56:48
305803,"Davis, Kshlerin and Reilly",VG-32047,Shirt,4,64.91,259.64,2014-02-20 20:48:46
758133,"Kihn, McClure and Denesik",KV-99194,Shirt,16,65.00,1040.00,2014-05-14 17:57:45
305803,"Davis, Kshlerin and Reilly",GS-86623,Shoes,6,57.28,343.68,2014-04-09 15:32:28
676847,Hamill-Hackett,VG-32047,Shirt,3,71.55,214.65,2014-02-16 04:42:01
995267,Cole-Eichmann,VG-32047,Shirt,4,37.74,150.96,2014-03-21 08:21:18
201259,Koelpin PLC,QN-82852,Belt,12,41.57,498.84,2014-05-22 08:56:14
659366,Waelchi-Fahey,QN-82852,Belt,13,59.59,774.67,2013-12-04 04:11:33
524021,Hegmann and Sons,FK-71853,Shirt,20,62.71,1254.20,2014-03-06 22:55:08
115138,Gorczany-Hahn,GS-86623,Shoes,16,37.88,606.08,2013-12-05 07:33:43
750461,"Volkman, Goyette and Lemke",LW-86841,Shoes,20,83.10,1662.00,2014-09-14 18:26:11
555594,"Ernser, Cruickshank and Lind",WJ-02096,Belt,10,11.81,118.10,2014-03-13 00:31:33
929400,"Senger, Upton and Breitenberg",MJ-21460,Shoes,20,59.10,1182.00,2014-10-02 05:30:08
563905,"Kerluke, Reilly and Bechtelar",QN-82852,Belt,8,60.70,485.60,2014-04-01 13:03:54
659366,Waelchi-Fahey,WJ-02096,Belt,1,42.83,42.83,2013-11-05 05:06:14
734922,Berge LLC,QN-82852,Belt,17,76.13,1294.21,2013-11-25 14:33:27
201259,Koelpin PLC,FK-71853,Shirt,4,41.09,164.36,2014-08-24 20:22:11
659366,Waelchi-Fahey,GS-86623,Shoes,12,32.84,394.08,2014-09-13 15:23:40
296809,Carroll PLC,VG-32047,Shirt,5,10.81,54.05,2014-08-28 00:56:58
115138,Gorczany-Hahn,LL-46261,Shoes,1,26.19,26.19,2014-01-10 05:09:07
115138,Gorczany-Hahn,LL-46261,Shoes,12,48.63,583.56,2014-09-17 06:25:26
305803,"Davis, Kshlerin and Reilly",LL-46261,Shoes,5,51.82,259.10,2014-01-08 02:36:38
750461,"Volkman, Goyette and Lemke",LW-86841,Shoes,7,53.36,373.52,2014-06-02 19:58:55
711951,Kilback-Gerlach,KV-99194,Shirt,5,56.33,281.65,2014-09-06 01:57:32
304860,Huel-Haag,AS-93055,Shirt,11,79.58,875.38,2013-11-21 04:46:33
734922,Berge LLC,FK-71853,Shirt,7,58.95,412.65,2014-03-14 04:16:55
850140,Kunze Inc,MJ-21460,Shoes,9,78.44,705.96,2013-12-18 17:23:54
995267,Cole-Eichmann,WJ-02096,Belt,15,54.77,821.55,2013-11-14 11:15:21
098022,Heidenreich-Bosco,GS-86623,Shoes,15,73.45,1101.75,2014-01-03 12:09:44
929400,"Senger, Upton and Breitenberg",LL-46261,Shoes,14,21.01,294.14,2014-01-01 00:15:37
524021,Hegmann and Sons,FK-71853,Shirt,15,45.99,689.85,2014-01-21 14:40:49
524021,Hegmann and Sons,LW-86841,Shoes,11,89.80,987.80,2014-03-14 06:17:28
734922,Berge LLC,FK-71853,Shirt,4,63.74,254.96,2014-08-31 19:57:31
296809,Carroll PLC,KV-99194,Shirt,9,36.35,327.15,2014-01-17 22:03:57
299771,"Kuphal, Zieme and Kub",MJ-21460,Shoes,13,55.99,727.87,2013-12-27 08:36:12
296809,Carroll PLC,FK-71853,Shirt,4,12.28,49.12,2014-04-03 06:43:35
659366,Waelchi-Fahey,WJ-02096,Belt,10,64.42,644.20,2014-09-05 03:46:20
563905,"Kerluke, Reilly and Bechtelar",LL-46261,Shoes,5,29.87,149.35,2014-08-02 00:25:56
305803,"Davis, Kshlerin and Reilly",GS-86623,Shoes,13,66.85,869.05,2013-11-19 07:26:52
299771,"Kuphal, Zieme and Kub",LL-46261,Shoes,5,13.07,65.35,2014-08-30 04:09:41
563905,"Kerluke, Reilly and Bechtelar",QN-82852,Belt,5,56.63,283.15,2014-10-13 02:27:35
750461,"Volkman, Goyette and Lemke",FK-71853,Shirt,19,89.14,1693.66,2013-11-14 18:25:50
524021,Hegmann and Sons,LW-86841,Shoes,5,67.31,336.55,2013-12-16 09:59:38
555594,"Ernser, Cruickshank and Lind",KV-99194,Shirt,17,11.24,191.08,2014-04-25 15:37:03
524021,Hegmann and Sons,AS-93055,Shirt,10,73.82,738.20,2014-10-22 04:43:23
850140,Kunze Inc,QN-82852,Belt,15,11.74,176.10,2014-01-09 04:36:36
524021,Hegmann and Sons,LL-46261,Shoes,5,83.98,419.90,2014-05-24 20:18:52
555594,"Ernser, Cruickshank and Lind",KV-99194,Shirt,6,63.40,380.40,2013-12-09 19:01:44
758133,"Kihn, McClure and Denesik",VG-32047,Shirt,15,80.59,1208.85,2014-10-05 18:13:24
758133,"Kihn, McClure and Denesik",AS-93055,Shirt,19,31.41,596.79,2014-05-09 11:00:05
296809,Carroll PLC,WJ-02096,Belt,9,61.39,552.51,2014-07-15 13:04:50
750461,"Volkman, Goyette and Lemke",LL-46261,Shoes,15,96.00,1440.00,2014-10-21 15:04:18
929400,"Senger, Upton and Breitenberg",WJ-02096,Belt,12,94.51,1134.12,2014-07-26 07:44:53
305803,"Davis, Kshlerin and Reilly",KV-99194,Shirt,15,18.07,271.05,2014-05-24 05:33:35
659366,Waelchi-Fahey,MJ-21460,Shoes,13,74.07,962.91,2014-01-13 12:18:04
995267,Cole-Eichmann,FK-71853,Shirt,16,88.32,1413.12,2014-06-17 22:27:38
929400,"Senger, Upton and Breitenberg",WJ-02096,Belt,4,77.19,308.76,2014-04-03 19:08:57
098022,Heidenreich-Bosco,GS-86623,Shoes,18,58.56,1054.08,2014-08-25 17:52:34
305803,"Davis, Kshlerin and Reilly",MJ-21460,Shoes,12,81.42,977.04,2014-07-09 13:58:55
850140,Kunze Inc,AS-93055,Shirt,3,68.90,206.70,2014-09-13 01:40:40
995267,Cole-Eichmann,QN-82852,Belt,19,39.75,755.25,2014-05-23 15:58:55
093356,Waters-Walker,KV-99194,Shirt,11,83.22,915.42,2014-01-03 19:04:02
750461,"Volkman, Goyette and Lemke",QN-82852,Belt,19,17.25,327.75,2014-02-08 14:06:56
659366,Waelchi-Fahey,QN-82852,Belt,7,41.70,291.90,2014-01-14 22:56:55
524021,Hegmann and Sons,MJ-21460,Shoes,20,44.56,891.20,2014-02-11 11:05:35
201259,Koelpin PLC,WJ-02096,Belt,4,15.24,60.96,2014-09-12 06:29:42
115138,Gorczany-Hahn,KV-99194,Shirt,1,66.03,66.03,2014-03-06 19:04:47
995267,Cole-Eichmann,LL-46261,Shoes,8,95.99,767.92,2014-02-28 06:46:39
711951,Kilback-Gerlach,WJ-02096,Belt,18,18.29,329.22,2014-05-28 10:39:07
929400,"Senger, Upton and Breitenberg",WJ-02096,Belt,1,50.58,50.58,2014-01-10 01:35:58
995267,Cole-Eichmann,WJ-02096,Belt,6,47.21,283.26,2014-01-27 15:50:35
750461,"Volkman, Goyette and Lemke",VG-32047,Shirt,3,82.06,246.18,2014-03-14 17:54:57
563905,"Kerluke, Reilly and Bechtelar",LW-86841,Shoes,18,36.32,653.76,2014-03-25 15:08:27
850140,Kunze Inc,QN-82852,Belt,10,45.33,453.30,2013-10-23 00:45:16
296809,Carroll PLC,VG-32047,Shirt,18,30.34,546.12,2014-06-21 11:50:51
995267,Cole-Eichmann,WJ-02096,Belt,14,23.57,329.98,2014-04-11 23:10:59
929400,"Senger, Upton and Breitenberg",GS-86623,Shoes,14,16.78,234.92,2014-04-15 00:55:47
929400,"Senger, Upton and Breitenberg",VG-32047,Shirt,4,92.05,368.20,2013-11-20 17:39:53
563905,"Kerluke, Reilly and Bechtelar",MJ-21460,Shoes,6,25.35,152.10,2014-02-21 00:43:26
850140,Kunze Inc,VG-32047,Shirt,13,28.29,367.77,2014-05-14 11:34:59
750461,"Volkman, Goyette and Lemke",LL-46261,Shoes,6,70.64,423.84,2014-04-13 10:46:26
304860,Huel-Haag,KV-99194,Shirt,7,32.91,230.37,2014-03-21 02:07:18
201259,Koelpin PLC,WJ-02096,Belt,10,31.82,318.20,2014-05-10 12:48:18
676847,Hamill-Hackett,FK-71853,Shirt,12,74.47,893.64,2014-03-22 00:45:00
676847,Hamill-Hackett,LW-86841,Shoes,6,72.92,437.52,2014-04-30 13:50:54
995267,Cole-Eichmann,AS-93055,Shirt,14,70.03,980.42,2013-12-31 09:37:47
093356,Waters-Walker,KV-99194,Shirt,19,47.53,903.07,2014-03-10 16:34:16
929400,"Senger, Upton and Breitenberg",AS-93055,Shirt,5,82.05,410.25,2013-12-03 12:28:55
711951,Kilback-Gerlach,LW-86841,Shoes,16,99.65,1594.40,2014-10-06 23:33:32
734922,Berge LLC,FK-71853,Shirt,17,49.12,835.04,2014-02-24 20:49:28
676847,Hamill-Hackett,LL-46261,Shoes,6,52.06,312.36,2014-02-04 19:46:55
305803,"Davis, Kshlerin and Reilly",KV-99194,Shirt,13,71.70,932.10,2014-07-08 01:00:22
305803,"Davis, Kshlerin and Reilly",MJ-21460,Shoes,3,37.34,112.02,2013-11-12 01:13:29
304860,Huel-Haag,WJ-02096,Belt,20,58.52,1170.40,2013-11-21 18:37:52
299771,"Kuphal, Zieme and Kub",LL-46261,Shoes,16,18.08,289.28,2013-12-12 00:31:40
098022,Heidenreich-Bosco,GS-86623,Shoes,6,81.70,490.20,2014-10-04 16:06:25
929400,"Senger, Upton and Breitenberg",FK-71853,Shirt,13,89.53,1163.89,2014-08-11 16:47:07
299771,"Kuphal, Zieme and Kub",AS-93055,Shirt,7,24.63,172.41,2014-01-28 18:58:01
305803,"Davis, Kshlerin and Reilly",GS-86623,Shoes,10,73.08,730.80,2013-10-29 17:00:22
929400,"Senger, Upton and Breitenberg",WJ-02096,Belt,12,52.24,626.88,2014-02-22 00:09:48
524021,Hegmann and Sons,QN-82852,Belt,4,84.72,338.88,2013-10-22 13:54:50
299771,"Kuphal, Zieme and Kub",VG-32047,Shirt,13,37.56,488.28,2013-11-10 06:24:28
929400,"Senger, Upton and Breitenberg",AS-93055,Shirt,18,22.98,413.64,2014-06-02 14:24:05
995267,Cole-Eichmann,MJ-21460,Shoes,2,79.87,159.74,2014-08-15 04:36:37
093356,Waters-Walker,KV-99194,Shirt,7,59.50,416.50,2014-04-29 12:04:58
659366,Waelchi-Fahey,WJ-02096,Belt,14,67.01,938.14,2013-12-13 15:04:13
201259,Koelpin PLC,MJ-21460,Shoes,5,61.76,308.80,2013-10-30 04:16:24
750461,"Volkman, Goyette and Lemke",MJ-21460,Shoes,7,33.16,232.12,2014-08-25 05:45:04
299771,"Kuphal, Zieme and Kub",GS-86623,Shoes,1,77.22,77.22,2014-01-21 12:40:40
296809,Carroll PLC,WJ-02096,Belt,8,55.69,445.52,2014-01-02 21:35:10
304860,Huel-Haag,AS-93055,Shirt,13,72.75,945.75,2013-11-02 06:09:13
304860,Huel-Haag,GS-86623,Shoes,20,71.91,1438.20,2014-02-14 02:11:56
758133,"Kihn, McClure and Denesik",KV-99194,Shirt,2,58.02,116.04,2014-05-28 00:51:31
296809,Carroll PLC,AS-93055,Shirt,19,78.72,1495.68,2014-08-01 13:54:15
850140,Kunze Inc,FK-71853,Shirt,8,44.56,356.48,2014-10-01 13:21:06
711951,Kilback-Gerlach,LW-86841,Shoes,19,92.34,1754.46,2014-05-13 03:41:20
758133,"Kihn, McClure and Denesik",GS-86623,Shoes,12,19.81,237.72,2014-10-12 12:33:27
563905,"Kerluke, Reilly and Bechtelar",QN-82852,Belt,2,29.15,58.30,2013-12-29 06:05:11
758133,"Kihn, McClure and Denesik",VG-32047,Shirt,8,71.71,573.68,2014-06-15 23:49:22
093356,Waters-Walker,GS-86623,Shoes,13,52.61,683.93,2014-01-31 10:14:51
711951,Kilback-Gerlach,MJ-21460,Shoes,4,90.75,363.00,2013-10-27 22:03:05
659366,Waelchi-Fahey,MJ-21460,Shoes,3,50.33,150.99,2014-02-25 05:11:55
098022,Heidenreich-Bosco,VG-32047,Shirt,6,96.02,576.12,2013-12-25 18:02:41
201259,Koelpin PLC,KV-99194,Shirt,14,66.37,929.18,2013-11-05 13:34:42
676847,Hamill-Hackett,LL-46261,Shoes,3,59.85,179.55,2013-10-26 04:33:08
524021,Hegmann and Sons,FK-71853,Shirt,2,66.63,133.26,2013-12-07 04:15:11
734922,Berge LLC,AS-93055,Shirt,8,94.37,754.96,2013-12-31 01:14:11
734922,Berge LLC,MJ-21460,Shoes,2,37.10,74.20,2014-10-04 18:30:12
659366,Waelchi-Fahey,QN-82852,Belt,1,78.95,78.95,2014-09-01 04:34:57
659366,Waelchi-Fahey,FK-71853,Shirt,7,76.57,535.99,2014-09-01 21:04:49
201259,Koelpin PLC,AS-93055,Shirt,10,43.97,439.70,2014-10-03 17:04:10
676847,Hamill-Hackett,VG-32047,Shirt,6,59.00,354.00,2014-08-26 02:03:17
850140,Kunze Inc,GS-86623,Shoes,4,17.63,70.52,2013-11-06 15:35:14
555594,"Ernser, Cruickshank and Lind",AS-93055,Shirt,12,40.03,480.36,2014-09-18 02:54:50
115138,Gorczany-Hahn,VG-32047,Shirt,1,61.73,61.73,2013-12-19 05:37:56
563905,"Kerluke, Reilly and Bechtelar",VG-32047,Shirt,9,38.76,348.84,2013-11-18 18:59:05
750461,"Volkman, Goyette and Lemke",AS-93055,Shirt,15,35.73,535.95,2014-07-29 13:03:54
299771,"Kuphal, Zieme and Kub",KV-99194,Shirt,7,80.19,561.33,2014-05-22 07:55:43
929400,"Senger, Upton and Breitenberg",LL-46261,Shoes,14,12.35,172.90,2014-02-28 10:45:43
098022,Heidenreich-Bosco,QN-82852,Belt,20,38.39,767.80,2013-11-18 22:22:57
734922,Berge LLC,QN-82852,Belt,11,60.05,660.55,2014-09-28 12:19:39
758133,"Kihn, McClure and Denesik",LW-86841,Shoes,15,17.57,263.55,2014-03-09 21:17:26
659366,Waelchi-Fahey,GS-86623,Shoes,9,43.69,393.21,2014-03-12 02:19:35
676847,Hamill-Hackett,GS-86623,Shoes,18,69.13,1244.34,2014-02-11 23:45:29
304860,Huel-Haag,QN-82852,Belt,3,94.18,282.54,2014-09-09 20:05:35
524021,Hegmann and Sons,VG-32047,Shirt,17,80.42,1367.14,2014-05-13 03:46:45
850140,Kunze Inc,AS-93055,Shirt,13,31.53,409.89,2014-06-12 12:09:39
750461,"Volkman, Goyette and Lemke",FK-71853,Shirt,6,18.33,109.98,2014-01-16 01:38:16
850140,Kunze Inc,KV-99194,Shirt,1,73.79,73.79,2013-11-07 19:52:06
296809,Carroll PLC,LW-86841,Shoes,3,10.67,32.01,2014-05-30 21:32:51
093356,Waters-Walker,GS-86623,Shoes,19,53.33,1013.27,2014-05-31 08:48:28
296809,Carroll PLC,AS-93055,Shirt,18,55.23,994.14,2013-12-02 17:42:51
296809,Carroll PLC,WJ-02096,Belt,7,77.91,545.37,2014-10-17 14:13:45
995267,Cole-Eichmann,VG-32047,Shirt,20,28.81,576.20,2014-03-19 16:59:03
299771,"Kuphal, Zieme and Kub",VG-32047,Shirt,16,31.86,509.76,2014-09-04 05:27:45
296809,Carroll PLC,GS-86623,Shoes,8,28.32,226.56,2014-10-01 04:15:37
659366,Waelchi-Fahey,GS-86623,Shoes,2,88.57,177.14,2014-06-16 02:35:22
524021,Hegmann and Sons,VG-32047,Shirt,11,52.58,578.38,2014-01-22 08:06:36
201259,Koelpin PLC,WJ-02096,Belt,14,20.87,292.18,2014-02-09 05:27:27
758133,"Kihn, McClure and Denesik",AS-93055,Shirt,7,54.95,384.65,2013-12-31 04:32:30
734922,Berge LLC,AS-93055,Shirt,11,36.86,405.46,2014-01-01 08:13:10
995267,Cole-Eichmann,KV-99194,Shirt,5,52.07,260.35,2014-09-17 06:06:34
750461,"Volkman, Goyette and Lemke",AS-93055,Shirt,19,71.71,1362.49,2013-12-29 04:27:13
750461,"Volkman, Goyette and Lemke",KV-99194,Shirt,3,71.09,213.27,2013-11-16 02:18:39
555594,"Ernser, Cruickshank and Lind",KV-99194,Shirt,7,60.04,420.28,2013-12-14 15:26:14
711951,Kilback-Gerlach,KV-99194,Shirt,5,55.82,279.10,2014-05-24 05:01:20
734922,Berge LLC,KV-99194,Shirt,16,24.13,386.08,2013-12-20 01:56:23
093356,Waters-Walker,WJ-02096,Belt,20,62.39,1247.80,2014-04-19 16:00:54
201259,Koelpin PLC,FK-71853,Shirt,2,83.01,166.02,2014-01-05 22:32:10
555594,"Ernser, Cruickshank and Lind",GS-86623,Shoes,2,58.61,117.22,2014-04-25 18:15:52
524021,Hegmann and Sons,LW-86841,Shoes,15,98.54,1478.10,2014-09-04 06:01:32
659366,Waelchi-Fahey,WJ-02096,Belt,15,20.03,300.45,2014-09-06 09:47:38
093356,Waters-Walker,VG-32047,Shirt,17,71.32,1212.44,2014-09-16 10:45:19
711951,Kilback-Gerlach,VG-32047,Shirt,10,55.04,550.40,2014-08-19 17:39:10
093356,Waters-Walker,QN-82852,Belt,19,95.37,1812.03,2014-05-20 09:39:21
750461,"Volkman, Goyette and Lemke",LW-86841,Shoes,16,19.83,317.28,2014-09-03 12:10:24
995267,Cole-Eichmann,WJ-02096,Belt,5,50.88,254.40,2014-02-15 03:16:45
929400,"Senger, Upton and Breitenberg",MJ-21460,Shoes,17,36.81,625.77,2013-12-05 23:10:45
524021,Hegmann and Sons,VG-32047,Shirt,4,42.78,171.12,2014-03-07 04:28:42
995267,Cole-Eichmann,VG-32047,Shirt,6,87.35,524.10,2013-12-12 21:41:39
299771,"Kuphal, Zieme and Kub",QN-82852,Belt,10,59.42,594.20,2014-06-11 12:10:16
750461,"Volkman, Goyette and Lemke",LL-46261,Shoes,3,30.80,92.40,2014-01-29 11:47:43
734922,Berge LLC,MJ-21460,Shoes,14,74.75,1046.50,2014-02-06 23:35:03
201259,Koelpin PLC,LW-86841,Shoes,12,73.70,884.40,2014-03-12 01:27:20
563905,"Kerluke, Reilly and Bechtelar",LW-86841,Shoes,10,36.30,363.00,2014-04-14 22:51:06
093356,Waters-Walker,GS-86623,Shoes,10,75.72,757.20,2014-01-31 09:09:36
758133,"Kihn, McClure and Denesik",AS-93055,Shirt,14,73.07,1022.98,2013-11-29 18:17:10
201259,Koelpin PLC,VG-32047,Shirt,19,76.09,1445.71,2014-08-04 04:24:32
093356,Waters-Walker,VG-32047,Shirt,13,45.42,590.46,2013-12-29 21:47:14
201259,Koelpin PLC,WJ-02096,Belt,10,65.97,659.70,2014-03-19 04:16:23
201259,Koelpin PLC,WJ-02096,Belt,2,20.06,40.12,2014-05-31 02:07:45
296809,Carroll PLC,GS-86623,Shoes,3,62.25,186.75,2014-03-26 00:33:22
659366,Waelchi-Fahey,KV-99194,Shirt,6,86.20,517.20,2013-11-14 19:38:21
758133,"Kihn, McClure and Denesik",GS-86623,Shoes,14,23.97,335.58,2013-12-01 12:17:58
115138,Gorczany-Hahn,QN-82852,Belt,10,10.06,100.60,2014-03-08 10:50:44
299771,"Kuphal, Zieme and Kub",GS-86623,Shoes,7,34.71,242.97,2014-04-29 04:10:38
929400,"Senger, Upton and Breitenberg",AS-93055,Shirt,14,31.36,439.04,2014-01-12 16:01:32
555594,"Ernser, Cruickshank and Lind",LW-86841,Shoes,1,96.74,96.74,2014-04-30 16:25:44
524021,Hegmann and Sons,QN-82852,Belt,1,93.93,93.93,2014-03-18 14:44:49
676847,Hamill-Hackett,AS-93055,Shirt,9,58.32,524.88,2013-12-16 15:10:41
296809,Carroll PLC,LL-46261,Shoes,8,58.48,467.84,2014-05-31 00:30:56
758133,"Kihn, McClure and Denesik",WJ-02096,Belt,6,68.70,412.20,2013-12-07 08:40:13
758133,"Kihn, McClure and Denesik",LW-86841,Shoes,4,65.73,262.92,2014-06-04 13:29:57
555594,"Ernser, Cruickshank and Lind",VG-32047,Shirt,8,60.40,483.20,2013-12-26 04:26:05
093356,Waters-Walker,KV-99194,Shirt,20,49.97,999.40,2014-04-28 20:35:33
711951,Kilback-Gerlach,KV-99194,Shirt,19,38.38,729.22,2014-05-25 09:18:43
734922,Berge LLC,LW-86841,Shoes,11,72.20,794.20,2013-11-13 21:15:53
659366,Waelchi-Fahey,KV-99194,Shirt,13,32.24,419.12,2013-12-22 05:25:56
750461,"Volkman, Goyette and Lemke",LL-46261,Shoes,8,95.39,763.12,2014-01-12 00:59:09
659366,Waelchi-Fahey,WJ-02096,Belt,5,73.03,365.15,2014-01-23 12:48:34
296809,Carroll PLC,VG-32047,Shirt,11,33.31,366.41,2014-07-29 15:09:19
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,3,65.52,196.56,2014-04-02 22:23:07
304860,Huel-Haag,GS-86623,Shoes,5,45.24,226.20,2013-12-12 03:58:09
304860,Huel-Haag,FK-71853,Shirt,20,81.79,1635.80,2014-09-23 04:52:44
524021,Hegmann and Sons,AS-93055,Shirt,7,91.68,641.76,2013-11-10 14:15:25
299771,"Kuphal, Zieme and Kub",GS-86623,Shoes,16,68.37,1093.92,2014-01-25 17:14:26
296809,Carroll PLC,GS-86623,Shoes,20,66.43,1328.60,2013-12-30 09:47:58
929400,"Senger, Upton and Breitenberg",FK-71853,Shirt,3,97.08,291.24,2014-01-28 10:18:57
659366,Waelchi-Fahey,LW-86841,Shoes,11,99.58,1095.38,2014-08-16 12:51:50
850140,Kunze Inc,FK-71853,Shirt,6,63.84,383.04,2014-01-06 17:32:46
758133,"Kihn, McClure and Denesik",FK-71853,Shirt,11,75.07,825.77,2014-06-23 22:07:37
734922,Berge LLC,FK-71853,Shirt,6,17.54,105.24,2014-08-19 04:51:46
115138,Gorczany-Hahn,KV-99194,Shirt,19,71.61,1360.59,2014-06-11 12:52:36
995267,Cole-Eichmann,QN-82852,Belt,17,92.49,1572.33,2013-12-30 08:52:54
995267,Cole-Eichmann,LW-86841,Shoes,1,40.04,40.04,2014-05-04 08:13:07
758133,"Kihn, McClure and Denesik",KV-99194,Shirt,6,92.02,552.12,2014-06-20 23:33:17
093356,Waters-Walker,KV-99194,Shirt,12,66.41,796.92,2014-04-02 00:13:13
995267,Cole-Eichmann,GS-86623,Shoes,13,53.32,693.16,2013-11-09 01:35:47
299771,"Kuphal, Zieme and Kub",LL-46261,Shoes,7,48.69,340.83,2014-07-29 18:34:42
734922,Berge LLC,WJ-02096,Belt,18,75.81,1364.58,2013-12-08 08:54:42
995267,Cole-Eichmann,MJ-21460,Shoes,4,89.88,359.52,2014-06-28 09:15:38
524021,Hegmann and Sons,LW-86841,Shoes,10,73.73,737.30,2014-10-08 20:26:26
296809,Carroll PLC,AS-93055,Shirt,19,67.10,1274.90,2014-06-20 16:14:34
659366,Waelchi-Fahey,WJ-02096,Belt,17,62.47,1061.99,2014-06-16 14:44:12
758133,"Kihn, McClure and Denesik",QN-82852,Belt,12,29.83,357.96,2014-01-27 07:20:04
758133,"Kihn, McClure and Denesik",QN-82852,Belt,18,24.57,442.26,2014-04-03 13:47:21
299771,"Kuphal, Zieme and Kub",KV-99194,Shirt,1,27.41,27.41,2014-08-10 21:23:09
098022,Heidenreich-Bosco,GS-86623,Shoes,9,92.90,836.10,2014-05-16 07:08:48
093356,Waters-Walker,AS-93055,Shirt,9,95.16,856.44,2013-12-03 07:38:11
929400,"Senger, Upton and Breitenberg",FK-71853,Shirt,7,77.52,542.64,2014-08-26 18:28:56
711951,Kilback-Gerlach,MJ-21460,Shoes,14,40.64,568.96,2014-10-21 15:55:43
995267,Cole-Eichmann,GS-86623,Shoes,5,54.09,270.45,2014-10-19 21:08:59
115138,Gorczany-Hahn,FK-71853,Shirt,17,62.60,1064.20,2013-12-15 18:40:06
758133,"Kihn, McClure and Denesik",WJ-02096,Belt,18,93.91,1690.38,2014-08-11 18:42:50
711951,Kilback-Gerlach,LW-86841,Shoes,11,29.20,321.20,2013-12-26 04:44:50
304860,Huel-Haag,AS-93055,Shirt,9,23.99,215.91,2014-08-04 09:20:38
929400,"Senger, Upton and Breitenberg",LW-86841,Shoes,16,92.41,1478.56,2014-05-25 15:09:33
555594,"Ernser, Cruickshank and Lind",LW-86841,Shoes,2,17.89,35.78,2014-08-30 15:52:20
676847,Hamill-Hackett,LL-46261,Shoes,19,47.71,906.49,2013-12-16 00:12:31
850140,Kunze Inc,WJ-02096,Belt,9,76.78,691.02,2013-12-29 01:08:35
750461,"Volkman, Goyette and Lemke",GS-86623,Shoes,18,76.54,1377.72,2014-01-21 02:04:48
304860,Huel-Haag,AS-93055,Shirt,5,63.59,317.95,2014-02-08 20:17:34
995267,Cole-Eichmann,LL-46261,Shoes,20,53.25,1065.00,2013-12-10 12:10:01
201259,Koelpin PLC,LL-46261,Shoes,7,91.20,638.40,2014-02-28 18:14:54
296809,Carroll PLC,LW-86841,Shoes,8,95.17,761.36,2014-07-18 09:26:00
524021,Hegmann and Sons,WJ-02096,Belt,11,54.79,602.69,2014-05-20 14:10:47
201259,Koelpin PLC,LL-46261,Shoes,3,62.68,188.04,2014-01-14 23:34:45
676847,Hamill-Hackett,GS-86623,Shoes,10,72.15,721.50,2014-04-07 09:45:23
305803,"Davis, Kshlerin and Reilly",VG-32047,Shirt,1,78.93,78.93,2014-02-24 00:46:07
563905,"Kerluke, Reilly and Bechtelar",LL-46261,Shoes,20,37.75,755.00,2013-12-24 08:34:32
563905,"Kerluke, Reilly and Bechtelar",LL-46261,Shoes,6,41.95,251.70,2013-12-09 23:19:11
676847,Hamill-Hackett,LW-86841,Shoes,11,91.04,1001.44,2014-05-30 04:37:34
201259,Koelpin PLC,MJ-21460,Shoes,18,29.75,535.50,2014-10-10 12:44:46
929400,"Senger, Upton and Breitenberg",LW-86841,Shoes,4,46.09,184.36,2014-07-23 09:02:37
929400,"Senger, Upton and Breitenberg",KV-99194,Shirt,17,94.19,1601.23,2014-01-17 12:05:59
524021,Hegmann and Sons,AS-93055,Shirt,9,76.23,686.07,2014-03-22 11:25:47
296809,Carroll PLC,LL-46261,Shoes,12,39.49,473.88,2014-05-22 17:50:01
734922,Berge LLC,KV-99194,Shirt,6,88.31,529.86,2013-12-23 16:08:03
734922,Berge LLC,VG-32047,Shirt,11,58.29,641.19,2014-04-23 09:49:39
850140,Kunze Inc,KV-99194,Shirt,17,80.50,1368.50,2014-08-21 15:51:34
659366,Waelchi-Fahey,VG-32047,Shirt,4,40.80,163.20,2014-04-26 23:38:33
524021,Hegmann and Sons,AS-93055,Shirt,7,73.69,515.83,2014-09-11 02:00:52
750461,"Volkman, Goyette and Lemke",FK-71853,Shirt,3,63.58,190.74,2014-04-20 20:45:20
563905,"Kerluke, Reilly and Bechtelar",FK-71853,Shirt,1,65.61,65.61,2013-10-30 09:34:40
758133,"Kihn, McClure and Denesik",GS-86623,Shoes,13,72.07,936.91,2014-02-22 13:36:56
524021,Hegmann and Sons,MJ-21460,Shoes,14,36.60,512.40,2014-07-01 22:27:00
555594,"Ernser, Cruickshank and Lind",VG-32047,Shirt,14,38.93,545.02,2013-12-23 14:57:03
734922,Berge LLC,FK-71853,Shirt,7,51.72,362.04,2013-12-07 09:43:31
304860,Huel-Haag,FK-71853,Shirt,14,51.11,715.54,2013-12-18 06:44:56
555594,"Ernser, Cruickshank and Lind",LW-86841,Shoes,4,93.90,375.60,2013-11-16 08:42:24
995267,Cole-Eichmann,LW-86841,Shoes,15,17.68,265.20,2013-11-04 20:12:32
850140,Kunze Inc,FK-71853,Shirt,11,85.24,937.64,2014-07-15 19:12:33
995267,Cole-Eichmann,QN-82852,Belt,2,53.38,106.76,2014-09-12 09:29:52
750461,"Volkman, Goyette and Lemke",FK-71853,Shirt,12,39.64,475.68,2014-10-15 01:53:52
563905,"Kerluke, Reilly and Bechtelar",LW-86841,Shoes,6,83.60,501.60,2013-11-27 21:04:11
304860,Huel-Haag,FK-71853,Shirt,8,74.64,597.12,2014-03-06 03:36:31
299771,"Kuphal, Zieme and Kub",AS-93055,Shirt,18,13.67,246.06,2014-05-11 20:21:19
850140,Kunze Inc,LL-46261,Shoes,11,72.69,799.59,2013-10-23 15:54:16
750461,"Volkman, Goyette and Lemke",WJ-02096,Belt,7,23.04,161.28,2014-09-01 01:15:01
676847,Hamill-Hackett,AS-93055,Shirt,3,50.86,152.58,2014-10-04 23:43:05
676847,Hamill-Hackett,MJ-21460,Shoes,6,17.46,104.76,2014-05-22 06:36:25
093356,Waters-Walker,QN-82852,Belt,11,44.93,494.23,2014-06-19 04:21:18
850140,Kunze Inc,LW-86841,Shoes,18,44.87,807.66,2014-07-12 18:59:33
750461,"Volkman, Goyette and Lemke",WJ-02096,Belt,6,54.49,326.94,2014-04-14 11:01:03
995267,Cole-Eichmann,VG-32047,Shirt,9,41.58,374.22,2014-06-21 21:58:56
850140,Kunze Inc,LL-46261,Shoes,8,80.60,644.80,2013-12-05 20:18:00
524021,Hegmann and Sons,MJ-21460,Shoes,19,67.55,1283.45,2014-06-21 20:12:03
305803,"Davis, Kshlerin and Reilly",WJ-02096,Belt,5,16.32,81.60,2013-11-17 08:52:44
299771,"Kuphal, Zieme and Kub",VG-32047,Shirt,15,21.39,320.85,2013-12-07 12:59:30
995267,Cole-Eichmann,QN-82852,Belt,19,99.90,1898.10,2014-04-23 22:30:58
758133,"Kihn, McClure and Denesik",AS-93055,Shirt,7,48.05,336.35,2014-02-04 09:34:00
758133,"Kihn, McClure and Denesik",QN-82852,Belt,18,94.04,1692.72,2014-07-25 18:30:19
555594,"Ernser, Cruickshank and Lind",AS-93055,Shirt,15,94.00,1410.00,2014-07-22 11:45:36
201259,Koelpin PLC,GS-86623,Shoes,5,26.55,132.75,2013-11-22 05:59:05
563905,"Kerluke, Reilly and Bechtelar",VG-32047,Shirt,5,64.85,324.25,2014-05-13 16:03:58
734922,Berge LLC,QN-82852,Belt,5,16.73,83.65,2014-03-01 13:41:40
555594,"Ernser, Cruickshank and Lind",LL-46261,Shoes,7,46.60,326.20,2014-09-06 15:20:19
098022,Heidenreich-Bosco,QN-82852,Belt,6,48.13,288.78,2013-11-04 03:41:41
296809,Carroll PLC,FK-71853,Shirt,3,55.60,166.80,2013-11-27 18:35:28
296809,Carroll PLC,LL-46261,Shoes,19,78.56,1492.64,2014-07-19 20:45:37
201259,Koelpin PLC,QN-82852,Belt,5,25.46,127.30,2013-10-23 07:39:47
563905,"Kerluke, Reilly and Bechtelar",WJ-02096,Belt,9,43.28,389.52,2014-08-24 22:30:54
563905,"Kerluke, Reilly and Bechtelar",VG-32047,Shirt,15,41.15,617.25,2014-02-12 05:07:04
750461,"Volkman, Goyette and Lemke",FK-71853,Shirt,19,39.29,746.51,2014-03-21 14:27:33
758133,"Kihn, McClure and Denesik",QN-82852,Belt,9,46.44,417.96,2014-07-02 06:59:14
659366,Waelchi-Fahey,QN-82852,Belt,1,95.03,95.03,2014-03-31 10:31:43
098022,Heidenreich-Bosco,FK-71853,Shirt,16,82.77,1324.32,2014-07-21 08:11:22
676847,Hamill-Hackett,LL-46261,Shoes,6,72.06,432.36,2014-08-10 14:34:54
659366,Waelchi-Fahey,MJ-21460,Shoes,5,43.64,218.20,2014-01-30 19:04:33
299771,"Kuphal, Zieme and Kub",LW-86841,Shoes,2,76.42,152.84,2014-09-09 14:28:18
659366,Waelchi-Fahey,VG-32047,Shirt,11,25.74,283.14,2014-02-06 22:09:58
929400,"Senger, Upton and Breitenberg",WJ-02096,Belt,2,40.68,81.36,2014-06-20 03:39:40
659366,Waelchi-Fahey,WJ-02096,Belt,4,12.66,50.64,2014-06-01 03:07:50
929400,"Senger, Upton and Breitenberg",VG-32047,Shirt,3,21.25,63.75,2014-03-08 05:49:21
758133,"Kihn, McClure and Denesik",FK-71853,Shirt,16,96.47,1543.52,2014-03-17 15:44:50
750461,"Volkman, Goyette and Lemke",GS-86623,Shoes,9,34.83,313.47,2014-01-28 15:52:04
524021,Hegmann and Sons,KV-99194,Shirt,1,24.90,24.90,2014-07-05 14:02:45
929400,"Senger, Upton and Breitenberg",KV-99194,Shirt,11,19.26,211.86,2013-12-01 21:23:11
555594,"Ernser, Cruickshank and Lind",VG-32047,Shirt,7,84.46,591.22,2013-11-15 23:56:38
850140,Kunze Inc,LW-86841,Shoes,14,62.03,868.42,2014-03-29 03:29:59
299771,"Kuphal, Zieme and Kub",KV-99194,Shirt,3,79.00,237.00,2013-11-26 08:15:06
711951,Kilback-Gerlach,KV-99194,Shirt,12,31.44,377.28,2013-12-15 21:44:27
524021,Hegmann and Sons,WJ-02096,Belt,2,73.96,147.92,2013-12-08 04:33:54
115138,Gorczany-Hahn,QN-82852,Belt,18,18.41,331.38,2014-05-07 04:59:51
555594,"Ernser, Cruickshank and Lind",QN-82852,Belt,18,39.11,703.98,2014-01-19 06:06:01
115138,Gorczany-Hahn,FK-71853,Shirt,5,94.62,473.10,2014-02-14 22:33:04
929400,"Senger, Upton and Breitenberg",WJ-02096,Belt,7,50.85,355.95,2014-07-25 14:33:33
115138,Gorczany-Hahn,AS-93055,Shirt,7,45.14,315.98,2014-04-13 09:02:34
296809,Carroll PLC,FK-71853,Shirt,6,15.69,94.14,2014-05-09 02:08:03
098022,Heidenreich-Bosco,QN-82852,Belt,10,76.76,767.60,2013-12-08 18:53:38
850140,Kunze Inc,LW-86841,Shoes,20,53.03,1060.60,2014-08-20 20:57:38
304860,Huel-Haag,GS-86623,Shoes,2,78.64,157.28,2014-04-24 06:13:24
093356,Waters-Walker,QN-82852,Belt,19,72.11,1370.09,2014-02-22 07:22:10
563905,"Kerluke, Reilly and Bechtelar",GS-86623,Shoes,16,33.21,531.36,2014-09-05 17:43:19
850140,Kunze Inc,AS-93055,Shirt,8,59.23,473.84,2014-04-15 02:11:56
093356,Waters-Walker,LL-46261,Shoes,13,81.45,1058.85,2013-11-02 14:31:09
115138,Gorczany-Hahn,AS-93055,Shirt,3,61.04,183.12,2014-05-26 22:06:38
850140,Kunze Inc,AS-93055,Shirt,2,39.31,78.62,2014-03-05 15:04:43
524021,Hegmann and Sons,FK-71853,Shirt,7,60.29,422.03,2014-08-15 15:41:54
299771,"Kuphal, Zieme and Kub",MJ-21460,Shoes,14,46.43,650.02,2014-05-17 10:02:32
750461,"Volkman, Goyette and Lemke",WJ-02096,Belt,15,15.12,226.80,2014-03-16 15:37:39
296809,Carroll PLC,LL-46261,Shoes,8,51.47,411.76,2014-01-09 11:37:20
734922,Berge LLC,MJ-21460,Shoes,15,91.88,1378.20,2013-12-10 12:02:09
296809,Carroll PLC,VG-32047,Shirt,16,82.36,1317.76,2014-03-24 12:29:30
098022,Heidenreich-Bosco,LL-46261,Shoes,8,84.24,673.92,2014-04-18 19:19:35
659366,Waelchi-Fahey,GS-86623,Shoes,10,88.36,883.60,2014-08-24 23:09:27
676847,Hamill-Hackett,LW-86841,Shoes,10,47.20,472.00,2014-05-05 18:51:45
929400,"Senger, Upton and Breitenberg",WJ-02096,Belt,20,51.16,1023.20,2013-10-31 15:48:14
304860,Huel-Haag,KV-99194,Shirt,3,55.75,167.25,2013-11-22 04:34:56
201259,Koelpin PLC,MJ-21460,Shoes,13,81.58,1060.54,2014-02-10 01:33:21
758133,"Kihn, McClure and Denesik",VG-32047,Shirt,1,13.47,13.47,2014-08-07 04:18:29
676847,Hamill-Hackett,VG-32047,Shirt,11,23.33,256.63,2013-12-29 02:31:41
098022,Heidenreich-Bosco,WJ-02096,Belt,12,84.23,1010.76,2014-01-28 00:34:31
659366,Waelchi-Fahey,LL-46261,Shoes,17,98.86,1680.62,2014-05-10 02:37:09
850140,Kunze Inc,KV-99194,Shirt,5,12.07,60.35,2013-10-24 08:39:48
676847,Hamill-Hackett,AS-93055,Shirt,8,87.50,700.00,2014-01-26 12:58:22
659366,Waelchi-Fahey,VG-32047,Shirt,8,63.37,506.96,2014-05-02 01:13:09
524021,Hegmann and Sons,FK-71853,Shirt,9,87.07,783.63,2014-09-10 21:37:02
098022,Heidenreich-Bosco,KV-99194,Shirt,2,88.57,177.14,2013-12-31 08:53:19
299771,"Kuphal, Zieme and Kub",MJ-21460,Shoes,1,16.29,16.29,2014-04-25 04:33:22
201259,Koelpin PLC,GS-86623,Shoes,8,55.16,441.28,2014-08-14 03:02:46
995267,Cole-Eichmann,MJ-21460,Shoes,20,25.66,513.20,2014-03-24 03:39:51
098022,Heidenreich-Bosco,LL-46261,Shoes,13,19.69,255.97,2014-01-28 23:58:09
305803,"Davis, Kshlerin and Reilly",MJ-21460,Shoes,3,71.28,213.84,2014-08-07 10:01:03
524021,Hegmann and Sons,QN-82852,Belt,6,57.14,342.84,2014-08-24 06:07:33
659366,Waelchi-Fahey,MJ-21460,Shoes,3,97.92,293.76,2014-08-03 14:44:21
555594,"Ernser, Cruickshank and Lind",VG-32047,Shirt,9,60.94,548.46,2014-09-14 01:36:31
093356,Waters-Walker,LL-46261,Shoes,6,51.18,307.08,2014-07-31 17:50:40
659366,Waelchi-Fahey,FK-71853,Shirt,18,62.58,1126.44,2014-03-31 08:44:34
750461,"Volkman, Goyette and Lemke",FK-71853,Shirt,13,77.42,1006.46,2014-07-16 00:38:04
093356,Waters-Walker,LL-46261,Shoes,11,36.49,401.39,2013-12-26 18:47:55
305803,"Davis, Kshlerin and Reilly",KV-99194,Shirt,17,57.50,977.50,2014-02-25 14:46:40
296809,Carroll PLC,WJ-02096,Belt,17,76.08,1293.36,2013-11-14 23:35:37
659366,Waelchi-Fahey,FK-71853,Shirt,14,11.91,166.74,2014-03-09 23:23:06
850140,Kunze Inc,LW-86841,Shoes,17,82.86,1408.62,2014-10-02 16:34:54
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,16,51.93,830.88,2014-01-17 08:36:29
299771,"Kuphal, Zieme and Kub",LL-46261,Shoes,17,96.71,1644.07,2014-09-04 18:21:15
115138,Gorczany-Hahn,QN-82852,Belt,15,25.75,386.25,2013-11-30 12:14:42
850140,Kunze Inc,AS-93055,Shirt,6,38.77,232.62,2014-06-19 22:24:10
304860,Huel-Haag,LW-86841,Shoes,6,52.93,317.58,2013-12-03 02:57:43
711951,Kilback-Gerlach,MJ-21460,Shoes,17,97.99,1665.83,2014-01-15 22:54:28
659366,Waelchi-Fahey,QN-82852,Belt,10,36.72,367.20,2014-06-18 14:02:05
734922,Berge LLC,MJ-21460,Shoes,9,84.43,759.87,2014-06-23 09:12:45
750461,"Volkman, Goyette and Lemke",GS-86623,Shoes,11,68.13,749.43,2014-05-09 09:32:44
299771,"Kuphal, Zieme and Kub",VG-32047,Shirt,6,92.62,555.72,2014-06-19 12:30:22
995267,Cole-Eichmann,KV-99194,Shirt,8,51.86,414.88,2013-11-23 02:03:48
750461,"Volkman, Goyette and Lemke",AS-93055,Shirt,19,52.45,996.55,2014-08-08 03:00:19
304860,Huel-Haag,KV-99194,Shirt,19,32.23,612.37,2014-10-02 01:11:44
563905,"Kerluke, Reilly and Bechtelar",QN-82852,Belt,4,61.06,244.24,2014-05-09 03:27:55
711951,Kilback-Gerlach,AS-93055,Shirt,11,44.56,490.16,2014-02-23 05:35:58
115138,Gorczany-Hahn,WJ-02096,Belt,1,58.03,58.03,2013-12-11 14:01:46
758133,"Kihn, McClure and Denesik",QN-82852,Belt,11,39.89,438.79,2014-05-18 15:53:12
524021,Hegmann and Sons,MJ-21460,Shoes,18,51.46,926.28,2014-07-08 18:37:36
676847,Hamill-Hackett,AS-93055,Shirt,12,92.28,1107.36,2014-04-28 21:34:27
115138,Gorczany-Hahn,FK-71853,Shirt,20,32.53,650.60,2014-10-22 10:04:21
304860,Huel-Haag,VG-32047,Shirt,6,67.49,404.94,2014-09-17 12:35:31
296809,Carroll PLC,VG-32047,Shirt,11,14.92,164.12,2014-01-14 05:53:11
299771,"Kuphal, Zieme and Kub",MJ-21460,Shoes,3,16.50,49.50,2014-08-09 14:56:26
734922,Berge LLC,WJ-02096,Belt,20,25.09,501.80,2014-02-15 00:17:15
711951,Kilback-Gerlach,KV-99194,Shirt,20,72.86,1457.20,2013-12-27 03:41:18
304860,Huel-Haag,WJ-02096,Belt,4,60.95,243.80,2014-01-20 10:14:17
676847,Hamill-Hackett,QN-82852,Belt,12,47.05,564.60,2013-10-24 07:27:44
850140,Kunze Inc,VG-32047,Shirt,20,36.00,720.00,2013-11-19 04:49:59
555594,"Ernser, Cruickshank and Lind",LW-86841,Shoes,3,25.52,76.56,2013-12-15 23:23:29
098022,Heidenreich-Bosco,QN-82852,Belt,3,43.89,131.67,2014-02-06 22:02:39
098022,Heidenreich-Bosco,LL-46261,Shoes,6,55.68,334.08,2014-02-25 02:43:31
734922,Berge LLC,KV-99194,Shirt,13,21.76,282.88,2014-09-16 19:43:28
659366,Waelchi-Fahey,VG-32047,Shirt,14,85.44,1196.16,2014-06-04 14:34:07
711951,Kilback-Gerlach,AS-93055,Shirt,20,88.71,1774.20,2014-08-14 19:08:27
929400,"Senger, Upton and Breitenberg",LW-86841,Shoes,1,32.44,32.44,2014-06-21 04:34:22
758133,"Kihn, McClure and Denesik",FK-71853,Shirt,12,40.53,486.36,2014-03-06 03:01:26
711951,Kilback-Gerlach,LL-46261,Shoes,8,41.95,335.60,2014-05-18 00:50:58
098022,Heidenreich-Bosco,KV-99194,Shirt,3,41.04,123.12,2014-10-09 15:27:45
750461,"Volkman, Goyette and Lemke",AS-93055,Shirt,4,65.64,262.56,2014-02-15 17:07:56
734922,Berge LLC,FK-71853,Shirt,4,59.00,236.00,2014-08-15 07:13:09
296809,Carroll PLC,GS-86623,Shoes,19,20.01,380.19,2013-11-20 14:26:00
711951,Kilback-Gerlach,LL-46261,Shoes,18,37.06,667.08,2014-07-09 17:04:57
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,8,13.41,107.28,2013-12-21 04:32:13
115138,Gorczany-Hahn,AS-93055,Shirt,19,36.84,699.96,2014-09-13 06:33:24
659366,Waelchi-Fahey,KV-99194,Shirt,18,13.47,242.46,2014-03-25 04:34:58
299771,"Kuphal, Zieme and Kub",LW-86841,Shoes,11,87.09,957.99,2013-10-22 16:08:40
201259,Koelpin PLC,QN-82852,Belt,19,18.85,358.15,2014-07-02 12:21:25
850140,Kunze Inc,LW-86841,Shoes,7,56.99,398.93,2014-06-25 22:06:27
115138,Gorczany-Hahn,AS-93055,Shirt,20,31.99,639.80,2014-09-15 19:14:27
304860,Huel-Haag,GS-86623,Shoes,14,27.24,381.36,2014-03-14 04:16:47
758133,"Kihn, McClure and Denesik",LW-86841,Shoes,11,51.07,561.77,2014-03-06 09:21:00
524021,Hegmann and Sons,GS-86623,Shoes,11,40.32,443.52,2014-02-07 07:39:54
758133,"Kihn, McClure and Denesik",WJ-02096,Belt,19,62.80,1193.20,2014-08-27 15:48:09
115138,Gorczany-Hahn,LW-86841,Shoes,5,33.56,167.80,2014-09-20 07:43:39
299771,"Kuphal, Zieme and Kub",FK-71853,Shirt,17,60.22,1023.74,2014-09-26 18:44:51
296809,Carroll PLC,GS-86623,Shoes,8,21.41,171.28,2014-09-11 18:45:17
296809,Carroll PLC,KV-99194,Shirt,13,43.03,559.39,2014-01-20 19:43:09
093356,Waters-Walker,LL-46261,Shoes,11,76.80,844.80,2014-02-23 18:36:40
850140,Kunze Inc,MJ-21460,Shoes,12,81.66,979.92,2014-09-04 03:23:22
995267,Cole-Eichmann,FK-71853,Shirt,16,63.20,1011.20,2014-06-22 09:34:54
711951,Kilback-Gerlach,LW-86841,Shoes,1,95.18,95.18,2013-11-16 10:27:30
201259,Koelpin PLC,VG-32047,Shirt,10,20.20,202.00,2014-10-02 18:38:33
305803,"Davis, Kshlerin and Reilly",LL-46261,Shoes,15,59.34,890.10,2013-12-04 02:43:20
296809,Carroll PLC,WJ-02096,Belt,16,91.77,1468.32,2014-02-23 18:10:13
734922,Berge LLC,MJ-21460,Shoes,4,87.65,350.60,2014-04-26 20:59:35
711951,Kilback-Gerlach,LL-46261,Shoes,13,34.40,447.20,2014-04-27 02:17:28
734922,Berge LLC,LL-46261,Shoes,18,44.89,808.02,2014-05-28 15:41:26
929400,"Senger, Upton and Breitenberg",LL-46261,Shoes,15,75.00,1125.00,2014-09-25 18:00:19
929400,"Senger, Upton and Breitenberg",MJ-21460,Shoes,8,19.05,152.40,2014-01-08 00:39:35
115138,Gorczany-Hahn,WJ-02096,Belt,5,13.31,66.55,2014-06-02 11:41:36
304860,Huel-Haag,KV-99194,Shirt,5,58.12,290.60,2014-08-02 12:08:32
676847,Hamill-Hackett,LL-46261,Shoes,19,58.95,1120.05,2014-03-12 06:27:02
758133,"Kihn, McClure and Denesik",GS-86623,Shoes,16,51.28,820.48,2013-12-19 05:40:26
659366,Waelchi-Fahey,KV-99194,Shirt,2,35.44,70.88,2013-10-25 14:47:00
555594,"Ernser, Cruickshank and Lind",KV-99194,Shirt,16,79.23,1267.68,2014-09-20 09:36:03
524021,Hegmann and Sons,LW-86841,Shoes,2,19.42,38.84,2014-08-23 03:19:29
093356,Waters-Walker,KV-99194,Shirt,9,70.81,637.29,2014-01-30 11:06:55
555594,"Ernser, Cruickshank and Lind",WJ-02096,Belt,10,27.65,276.50,2014-08-05 02:49:13
555594,"Ernser, Cruickshank and Lind",KV-99194,Shirt,18,53.57,964.26,2013-11-09 07:53:05
098022,Heidenreich-Bosco,GS-86623,Shoes,19,87.08,1654.52,2014-09-20 22:36:07
304860,Huel-Haag,AS-93055,Shirt,3,88.25,264.75,2013-11-22 02:08:50
115138,Gorczany-Hahn,MJ-21460,Shoes,16,74.73,1195.68,2014-10-08 07:30:19
758133,"Kihn, McClure and Denesik",VG-32047,Shirt,15,39.14,587.10,2014-08-02 17:24:19
850140,Kunze Inc,LW-86841,Shoes,5,63.32,316.60,2014-02-13 19:42:05
305803,"Davis, Kshlerin and Reilly",LW-86841,Shoes,7,18.99,132.93,2014-04-17 16:31:36
093356,Waters-Walker,FK-71853,Shirt,6,48.34,290.04,2014-10-07 11:12:45
093356,Waters-Walker,MJ-21460,Shoes,1,76.61,76.61,2014-05-07 10:17:28
929400,"Senger, Upton and Breitenberg",MJ-21460,Shoes,11,10.12,111.32,2014-03-29 05:53:03
995267,Cole-Eichmann,AS-93055,Shirt,20,96.14,1922.80,2014-08-02 19:08:15
304860,Huel-Haag,MJ-21460,Shoes,10,69.19,691.90,2014-01-07 14:36:19
563905,"Kerluke, Reilly and Bechtelar",VG-32047,Shirt,16,64.75,1036.00,2014-02-11 09:04:11
201259,Koelpin PLC,LW-86841,Shoes,1,62.87,62.87,2014-01-01 22:40:22
299771,"Kuphal, Zieme and Kub",QN-82852,Belt,13,13.05,169.65,2014-09-04 16:33:40
093356,Waters-Walker,KV-99194,Shirt,2,96.80,193.60,2014-07-13 09:44:29
098022,Heidenreich-Bosco,LL-46261,Shoes,6,23.04,138.24,2014-03-02 03:45:46
850140,Kunze Inc,KV-99194,Shirt,8,35.98,287.84,2014-05-20 14:38:17
115138,Gorczany-Hahn,AS-93055,Shirt,9,14.71,132.39,2014-03-01 13:31:22
995267,Cole-Eichmann,GS-86623,Shoes,2,43.85,87.70,2014-06-09 21:31:11
563905,"Kerluke, Reilly and Bechtelar",LW-86841,Shoes,9,52.42,471.78,2014-05-22 11:49:32
098022,Heidenreich-Bosco,QN-82852,Belt,15,20.07,301.05,2014-06-27 12:15:09
659366,Waelchi-Fahey,QN-82852,Belt,17,56.27,956.59,2014-02-09 14:52:49
098022,Heidenreich-Bosco,QN-82852,Belt,8,79.20,633.60,2014-06-07 18:59:21
555594,"Ernser, Cruickshank and Lind",MJ-21460,Shoes,7,97.93,685.51,2014-04-05 00:29:44
524021,Hegmann and Sons,QN-82852,Belt,8,49.06,392.48,2014-05-03 20:50:41
750461,"Volkman, Goyette and Lemke",GS-86623,Shoes,5,62.46,312.30,2014-05-13 14:52:47
305803,"Davis, Kshlerin and Reilly",FK-71853,Shirt,20,11.96,239.20,2014-09-04 18:27:56
201259,Koelpin PLC,KV-99194,Shirt,12,91.33,1095.96,2014-03-01 09:46:48
115138,Gorczany-Hahn,WJ-02096,Belt,3,93.50,280.50,2014-08-25 21:36:41
098022,Heidenreich-Bosco,GS-86623,Shoes,19,26.88,510.72,2014-04-07 07:12:29
555594,"Ernser, Cruickshank and Lind",MJ-21460,Shoes,8,49.15,393.20,2014-10-12 21:49:47
098022,Heidenreich-Bosco,WJ-02096,Belt,7,52.04,364.28,2013-11-07 19:58:39
995267,Cole-Eichmann,KV-99194,Shirt,13,97.04,1261.52,2014-06-17 08:28:31
555594,"Ernser, Cruickshank and Lind",AS-93055,Shirt,6,29.88,179.28,2014-09-04 14:54:23
524021,Hegmann and Sons,KV-99194,Shirt,6,62.36,374.16,2014-01-07 03:14:00
524021,Hegmann and Sons,AS-93055,Shirt,15,88.44,1326.60,2014-10-15 01:54:05
711951,Kilback-Gerlach,KV-99194,Shirt,16,79.71,1275.36,2014-08-30 06:23:27
676847,Hamill-Hackett,LW-86841,Shoes,11,96.57,1062.27,2014-01-09 13:36:39
296809,Carroll PLC,VG-32047,Shirt,12,79.85,958.20,2014-01-16 11:38:27
093356,Waters-Walker,AS-93055,Shirt,2,47.74,95.48,2014-03-22 02:00:16
995267,Cole-Eichmann,KV-99194,Shirt,18,97.33,1751.94,2014-01-16 12:27:14
676847,Hamill-Hackett,FK-71853,Shirt,18,98.39,1771.02,2014-01-06 08:14:31
995267,Cole-Eichmann,LL-46261,Shoes,2,94.06,188.12,2013-12-16 21:29:38
929400,"Senger, Upton and Breitenberg",LL-46261,Shoes,11,19.17,210.87,2013-10-26 13:17:07
305803,"Davis, Kshlerin and Reilly",GS-86623,Shoes,18,20.74,373.32,2013-10-22 20:01:38
995267,Cole-Eichmann,AS-93055,Shirt,7,80.69,564.83,2014-01-10 21:42:10
093356,Waters-Walker,AS-93055,Shirt,15,84.23,1263.45,2014-07-18 04:09:08
524021,Hegmann and Sons,GS-86623,Shoes,9,39.14,352.26,2013-11-17 23:11:28
929400,"Senger, Upton and Breitenberg",VG-32047,Shirt,10,67.36,673.60,2013-11-02 03:09:24
734922,Berge LLC,VG-32047,Shirt,14,93.45,1308.30,2014-02-10 07:13:32
201259,Koelpin PLC,LL-46261,Shoes,8,62.68,501.44,2013-11-10 16:34:17
555594,"Ernser, Cruickshank and Lind",QN-82852,Belt,13,86.33,1122.29,2013-10-23 02:35:36
711951,Kilback-Gerlach,GS-86623,Shoes,1,25.23,25.23,2014-02-15 18:56:38
555594,"Ernser, Cruickshank and Lind",KV-99194,Shirt,14,93.56,1309.84,2014-10-21 14:14:21
296809,Carroll PLC,LW-86841,Shoes,19,22.36,424.84,2014-07-08 00:03:47
711951,Kilback-Gerlach,LW-86841,Shoes,13,72.82,946.66,2014-02-10 18:44:09
098022,Heidenreich-Bosco,AS-93055,Shirt,4,22.33,89.32,2014-05-22 10:55:51
929400,"Senger, Upton and Breitenberg",MJ-21460,Shoes,5,41.67,208.35,2013-12-04 08:24:01
296809,Carroll PLC,MJ-21460,Shoes,13,29.69,385.97,2014-03-25 09:03:04
758133,"Kihn, McClure and Denesik",GS-86623,Shoes,20,20.83,416.60,2014-09-07 19:59:58
524021,Hegmann and Sons,LW-86841,Shoes,12,96.49,1157.88,2014-08-24 02:46:41
758133,"Kihn, McClure and Denesik",WJ-02096,Belt,15,51.35,770.25,2014-05-13 12:39:44
563905,"Kerluke, Reilly and Bechtelar",GS-86623,Shoes,16,90.96,1455.36,2013-11-02 09:19:40
711951,Kilback-Gerlach,LW-86841,Shoes,12,22.81,273.72,2014-09-17 02:46:57
093356,Waters-Walker,AS-93055,Shirt,19,28.76,546.44,2013-12-19 19:43:07
098022,Heidenreich-Bosco,VG-32047,Shirt,2,35.71,71.42,2014-07-03 03:16:33
296809,Carroll PLC,LL-46261,Shoes,9,32.75,294.75,2014-02-08 10:48:21
758133,"Kihn, McClure and Denesik",LW-86841,Shoes,2,92.23,184.46,2014-02-18 03:57:38
524021,Hegmann and Sons,MJ-21460,Shoes,12,18.24,218.88,2014-05-01 16:46:03
305803,"Davis, Kshlerin and Reilly",AS-93055,Shirt,6,49.81,298.86,2013-11-01 16:31:25
304860,Huel-Haag,QN-82852,Belt,2,22.38,44.76,2014-01-23 23:47:01
929400,"Senger, Upton and Breitenberg",QN-82852,Belt,10,25.65,256.50,2013-12-20 14:10:18
299771,"Kuphal, Zieme and Kub",QN-82852,Belt,12,37.50,450.00,2013-12-30 04:04:50
115138,Gorczany-Hahn,VG-32047,Shirt,20,72.35,1447.00,2014-08-11 19:02:14
758133,"Kihn, McClure and Denesik",LL-46261,Shoes,2,48.21,96.42,2014-09-16 16:12:02
711951,Kilback-Gerlach,VG-32047,Shirt,1,91.96,91.96,2013-10-23 15:08:31
929400,"Senger, Upton and Breitenberg",GS-86623,Shoes,7,62.27,435.89,2013-12-30 01:55:14
093356,Waters-Walker,KV-99194,Shirt,20,99.74,1994.80,2014-04-18 15:39:12
098022,Heidenreich-Bosco,QN-82852,Belt,15,82.82,1242.30,2014-03-27 04:42:40
734922,Berge LLC,GS-86623,Shoes,8,85.04,680.32,2014-02-26 14:43:51
995267,Cole-Eichmann,LW-86841,Shoes,10,73.24,732.40,2014-06-07 10:04:53
093356,Waters-Walker,AS-93055,Shirt,9,68.62,617.58,2014-08-12 08:06:21
304860,Huel-Haag,QN-82852,Belt,1,57.33,57.33,2014-08-27 11:27:28
850140,Kunze Inc,KV-99194,Shirt,9,27.16,244.44,2014-02-08 06:22:34
659366,Waelchi-Fahey,LW-86841,Shoes,10,56.56,565.60,2014-10-01 11:38:04
296809,Carroll PLC,WJ-02096,Belt,20,14.37,287.40,2014-07-20 17:22:03
758133,"Kihn, McClure and Denesik",WJ-02096,Belt,11,60.50,665.50,2014-08-03 10:39:51
850140,Kunze Inc,GS-86623,Shoes,16,19.66,314.56,2014-05-03 21:18:15
093356,Waters-Walker,GS-86623,Shoes,13,90.95,1182.35,2014-06-14 12:43:51
304860,Huel-Haag,LL-46261,Shoes,9,98.22,883.98,2014-07-26 01:10:57
098022,Heidenreich-Bosco,LW-86841,Shoes,14,74.83,1047.62,2014-06-27 05:58:33
'''

import pandas as pd

# Read the CSV file into a dataframe
df = pd.read_csv("/Users/benjaminadams/Downloads/777_m5_datasets_v1.0 2/sample-salesv2.csv")

# Get the number of rows and columns
print(df.shape)

# Get the data types of each column
print(df.dtypes)

# Calculate basic statistics for numeric columns
print(df.describe())

# Count the number of missing values in each column
print(df.isnull().sum())

# Select only certain columns
df = df[['name', 'net_price', 'date']]

# Group the data by name
df = df.groupby('name').sum()

# Filter rows based on a condition
df = df[df['net_price'] > 100]

import matplotlib.pyplot as plt

# Calculate the total sales by each customer
sales = df.groupby('name')['net_price'].sum()

# Plot the data
plt.bar(sales.index, sales.values)

# Label the axes
plt.xlabel('Customer Name')
plt.ylabel('Total Sales')

# Add a title
plt.title('Total Sales by Customer')

# Show the plot
plt.show()

'''
5. Let the x axis data points and y axis data points are
    X = [1,2,3,4]
    y = [20, 21, 20.5, 20.8]
    5.1: Draw a Simple plot
    5.2: Configure the line and markers in simple plot
    5.3: configure the axes
    5.4: Give title of Graph & labels of x axis and y axis
    5.5: Give error bar if y_error = [0.12, 0.13, 0.2, 0.1]
    5.6: define width, height as figsize=(4,5) DPI and adjust plot dpi=100
    5.7: Give a font size of 14
    5.8: Draw a scatter graph of any 50 random values of x and y axis
    5.9: Create a dataframe from following data
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
    Draw a Scatterplot of preTestScore and postTestScore, with the size of each point
    determined by age
    5.10: Draw a Scatterplot from the data in question 9 of preTestScore and
    postTestScore with the size = 300 and the color determined by sex
'''
import matplotlib.pyplot as plt

X = [1, 2, 3, 4]
y = [20, 21, 20.5, 20.8]

plt.plot(X, y)

plt.plot(X, y, linestyle='dashed', marker='^', color='red')

plt.xlabel('X axis')
plt.ylabel('Y axis')


plt.title('My Plot')

y_error = [0.12, 0.13, 0.2, 0.1]

plt.errorbar(X, y, yerr=y_error)

plt.figure(figsize=(4, 5), dpi=100)

plt.rc('font', size=14)

import random

X = [random.random() for _ in range(50)]
y = [random.random() for _ in range(50)]
plt.scatter(X, y)


import pandas as pd

data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
}



df = pd.DataFrame(data)

plt.scatter(df['preTestScore'], df['postTestScore'], s=df['age'])

plt.scatter(df['preTestScore'], df['postTestScore'], s=300, c=df['female'])

plt.colorbar()

plt.show()

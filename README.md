


To Create a list of indicators that can be used to predict the chances of a ticket gettting confirmed after train chart preparation
===================================================================================================================================

Dataset was collected from Kaggle:
======================
Dataset URL:  https://www.kaggle.com/competitions/railofy-challenge/data
======================
Feature	Description:
======================

GRCA: General Reservation Current Availability	Indicates the number of currently available seats in the general reservation category.

CCA: Current Charted Availability  	The number of seats available after the chart has been prepared 

JD: Journey Date   	The date of the journey for which the ticket is booked 

ODD: Origin-Destination Distance	The distance between the boarding station and the destination station 

JS: Journey Start 	The time when the journey begins 

ODS: Origin-Destination Station 	Code or indicator of the stations involved in the journey 

SL: Sleeper Class 	Indicates the number of seats or bookings in the Sleeper Class. 

NDTD: Number of Days to Travel Date	The number of days left until the journey date from the date of booking

CURP: Current Upgraded Reservation Percentage 	The percentage of reservations that have been upgraded (e.g., from RAC to confirmed) 

GROP: General Reservation Occupancy Percentage	The percentage of general reservation seats occupied

CANP: Cancellation Percentage	The percentage of tickets that have been canceled 

SBRA: Sleeper Berth Reservation Availability 	Availability of sleeper berths at the time of query 

SCRA: Sleeper Class Reservation Availability	Number of available seats in the Sleeper Class 

GRA: General Reservation Availability 	Indicates the availability of seats in the general category 

CURA: Current Upgraded Reservation Availability 	Number of available upgraded reservations 

RPW: Reservation Probability Weight	A calculated weight indicating the likelihood of reservation confirmation.

CUCA: Current Unreserved Seat Availability  	Number of unreserved seats available currently. 

CAR: Confirmed Against RAC   	Number of RAC tickets that have been confirmed 

BKT_2: Bucket 2	Could represent a specific category or quota bucket used in allocation. 

CL_1: Class 1	Number of bookings or availability in the highest travel class (could be AC First Class).

CL_2: Class 2 	Number of bookings or availability in the second-highest travel class (could be AC 2-Tier) 

CL_3: Class 3 	Number of bookings or availability in the third-highest travel class (could be AC 3-Tier)

Best Model:    K - Nearest Neighbors Classifier 
===============================================

F1 score:  .872

Matthews Correlation Coefficient:  .815

Key Indicators:
================

CURP: Current Upgraded Reservation Percentage

GROP: General Reservation Occupancy Percentage

CUCA: Current Unreserved Seat Availability

NDTD: Number of Days to Travel Date

GRCA: General Reservation Current Availability

ODD: Origin-Destination Distance

CANP: Cancellation Percentage

JD: Journey Date

CCA: Current Charted Availability

RPW: Reservation Probability Weight

ODS: Origin-Destination Station

JS: Journey Start

Model Deployment strategy:
==========================

Model was deployed using Flask in the file app.py

Endpoint was defined as ‘/predict’

Test file was read and stored in variable input_data

All preprocessing steps such as dropping columns, removing outliers and label encoding were applied within a function before predicting the model

Also, feature selection has been implemented to select the top 12 most influential columns that help in predicting the model

Code was executed using python app.py

Predictions were returned to the user as a file named predictions.csv



                                              

                      

# Auto-garbage-disposal
# Group members (Satya Bhanu Khichi, Gajula Rohan, Siddharth L Hasanabadi)

# Abstract
Garbage collection continues to be a large problem in towns and metropolitan areas. We intend to utilize the Internet of Things to come up with a solution to this problem. We are proposing a method to collect garbage at the most optimum times of the day so as to make sure excess garbage is not left in the open any longer than necessary or dumped in the streets instead. 

# Proposed technique
The current method we intend to use is as follows:-<br>
1.	Use a smart dustbin to send garbage level to the cloud.<br>
2.	Do a time analysis of the data.<br>
3.	Apply a K Means classifier to group data in to N distinct temporal groups where N is the number of trips a truck can make in a day.<br>
4.	Accordingly, schedule timings when garbage truck should collect garbage and locations where they will be collected from.<br>

# File descriptions

**doctored_2_visual_only.csv** - contains information of posinsion of garbage bins, serial number and when they got filled in a day.<br>
**doctored_2.csv** - Same as previous except, it is used in code.<br>
**clustering.py** - provides a K means temporal clustering to cluster data in the **doctored_2.csv**. The number of clusters correspond to number of trips a truck ca make in a day.<br>
**path optimization.py** - Plots cluster paths accoding to output from **clustering.py** . ( **Please note:-** (0,0) is assumed to be location of the main landfill/dump .)<br>

# Results

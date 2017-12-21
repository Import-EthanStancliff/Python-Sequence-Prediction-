import statistics
Class Predict():
	def init(self, dataset):
		self.data = dataset
   
	def Geometric(self, pValue): #The geometric sequence predictor
		data = self.data
		data_value_differences = []
		for i in range(len(data)-1):
			data_value_differences.append(data[i+1]/data[i]) #Gathers the amount you multiply from one to get the next
		mean = statistics.mean(data_value_differences) #Calculates the mean of that value
		sDev = statistics.pstdev(data_value_differences) #Gets the standard deviation from the data_value_differences

		if sDev <= pValue: #Only gives you the value if it's more accurate than what you asked for
			return mean
		else:
			return 0

# Tableau-Boat-Sales

As an IT Technician at the Catamaran Company trying to break into the Data Science Industry, I decided to expand my skills with visualization tools, and the most popular by far seems to be Tableau. After this project, the appeal is clear as many different representation are create quickly and easily. 

The data was collected from the company's sales portal website which has been tabulating every boat sale through the comapany since about 2011. The data is far from being perfect, but it is clean enough to pull useful insights. Ten views were created, which will be posted and discussed below.

# Revenue Over Time

The first graph is the sum revenue each quarter since data started being collected in 2011, as well as the average price of the boat, and then the number of boats sold each quarter

![Price Boats are sold at Over the Years](https://github.com/alexretana/Tableau-Boat-Sales/blob/master/Images/Price%20Boats%20are%20sold%20at%20Over%20the%20Years.png?raw=true)

From here, the best quarter was the summer of 2013 and fall of 2014, seperated by a short dip in sales. This increase in revenue was caused by an increase in the number boats sold, which is evident from the high correlation between the graphs at that time. Then early 2018 was very strong and stays strong until 2020 (which dips down due to Covid-19 affecting the world economy, as well as the final quarter not being complete. These peaks near the end are highly correlated with the price of boats. Interesting enough, high revenues were achievable either through more boat sales, or by selling bigger deal. It would likely cost less to implement the second strategy because if you focus on better deals instead of more deals, the company will have to contract less brokers.

Although brokers come and go at this company, there are a handful of brokers who have stuck for a while due to their success. It'd be good to see how these brokers compare to each other accross certain metrics. Please note that names legend have been censor to conserve the privacy of the brokers' preformance to the public.

![Revenue by Top Brokers Over Time](https://github.com/alexretana/Tableau-Boat-Sales/blob/master/Images/Revenue%20by%20Top%20Brokers%20over%20time.png?raw=true)

It should be noted that the data was cleaned a bit before this was produced. Most noteably, there were many null values at the beginning, as well as sales marked down with no selling broker, but instead just the company name. It appears that either the code or the procedures were impoved to store and conserve data better. 

Likely one of the first things to notice is the enourmous peak in 2017 from the green colored broker. This broker has an really strong year in 2017 where he sold a large volume of boats. The company had deal with a certain boat manufacture and was able to sell various boats at reduced prices, which our green broker took good advantage. Perhaps he was so financially satisfied from that year that he decided to kick back and reduce his workload, and maybe pass over his leads to other brokers. Mr. DarkGrey had a good year too, but then appears to has more sales spread accrosss different broker. This could be explain by the hiring of more highly dedicated brokers. Entering 2019, Ms. Pink, and Mr. LightGrey took a strong lead with Mr. DarkGrey in clos third place. Personally knowing Ms.Pink, I know last year she really put in significantly more time into working with clients, and it seems to pay off. The big drop by all brokers at the end of 2019  into 2020 is explain by loosing the deal with the boat manufactuary, giving us a smaller listing of boats.

![Number of Boats Sold by Brokers(Sail vs Power)](https://github.com/alexretana/Tableau-Boat-Sales/blob/master/Images/Number%20of%20Boats%20Sold%20By%20Brokers(Sail%20vs%20Power).png)
![Number of Boats Sold by Brokers(Used vs New)](https://github.com/alexretana/Tableau-Boat-Sales/blob/master/Images/Number%20of%20Boats%20Sold%20By%20Brokers(Used%20vs%20New).png)
![Number of Boats Sold by Brokers(Price Cut)](https://github.com/alexretana/Tableau-Boat-Sales/blob/master/Images/Number%20of%20Boats%20Sold%20By%20Brokers(Price%20Cut).png)

Looking at the count of boats sold by the top selling brokers, there are various ways to split up their counts by categories. First, spliting up by Sail boats vs Powered boats, the majority of boats sold by our company are sail boats. Broker 2 has the most success with power boat sales. Next,...

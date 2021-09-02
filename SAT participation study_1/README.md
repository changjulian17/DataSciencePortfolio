# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Standardized Test Analysis


#### Julian Chang - Group 1

### Problem Statement

Observe the relationship of SAT participation in the US against the different regions and divisions. Then substantiate strategies related to the uncovered geographic relationship. 

### Executive Summary

The SAT test administered by ColleagueBoard is a standardized assessment to allow prospective students to evaluate their writing, reading and mathematical skills and use this information as part of their colleague application process. Being widely established and acknowledged, the SAT has supported large numbers of students and universities in the admission process. While being widely used, critique on the test has become more vocal, with main concerns challenging the adequateness of standardized tests to predict success of prospective students, methodological critic on recent test structure revisions and the accusation of it facilitating social injustices.

For the course of this project, DSIF2-Group1 has decided to support the ColleagueBoard with an analytical consulting project tackling three major concerns:
(1) How can SAT acceptance be strengthened?
(2) How can the ColleagueBoard tap into auxiliary revenue streams to support proactive tackling of big challenges
(3) Which measures can be taken to support its long-term license to operate?

This subset of the overarching project focuses on (1), investigating where and how to support its acceptance. Since there is a high degree of bias in grades related to inequality and inaccessibility it is preferrable to increase the participation within the united states. Given a limited resource of an expansion project for the college board a multiple strategies are offered to with different objectives and resource allocation based on the expansiveness and resources available.

There are three that are recommended with recommendations with varying cost such as building to smaller marketing and campaigning. 

### Conclusions and Recommendations

There are 3 Strategies highlighted
Strategy 1 targets DIVISIONS with Non-mandatory testing with low participation
Strategy 2 targets STATES with Non-mandatory testing with low participation in divisions and regions with moderate to high participation
Strategy 3 targets STATES with Mandatory testing with low participation and neighbour states with high participation

|Strategy|Opportunity|Geographic Leverage|Opportunistic States|Strategy|Implementation|
|---|---|---|---|---|---|
|Strategy 1|DIVISIONS with Non-mandatory testing with low participation|Division 8 - utilise Colorado as a base. Division 9 - untapped regions with a hub of resources being able to effectively serve many states|Division 8 - Arizona, New Mexico. Division 9 - Alaska, California, Oregon, Washington, Hawaii|Increase lowest SAT participation in a geographic Division with a regional hub| **Building offices and schools** Convince states' school boards of mandatory SAT tests - lobbying, campaigns in school or school boards. Create SAT schools to teaching SAT teachers|
|Strategy 2|STATES with Non-mandatory testing with low participation|Use adjacent states within the region to springboard adoption of SAT as a standard test|Division 1 - Vermont. Division 2 - all states. Division 3 - Indiana. Division 5 - Virginia. Most are in the North-East|Utilise states in the Region with expertise to expand SAT influence based on transfer of knowledge and advantages of SAT network| **Brand campaign and advertising focused**1. (pull) increase recognition of SAT to Regional colleges and univeristies. 2. (pull) Advertise campaign in successful SAT grads 3. (push) increase subsidised tution and learning resources (Youtube, Khan acad etc). 4. Collaborate with Schools on teaching programs. 5. (push) make partnerships with academic institutions to provide scholarships for SAT takers|
|Strategy 3|STATES with Mandatory testing with low participation|Encourage SAT as a preferred test compared to other tests|Division 5 - North and South Carolina. Division 9 - Hawaii. Division 7 - Oklahoma (not preferred)|Propose to schools / school boards on the advantage of SAT over ACT or other tests|Similar to Strategy 2. **Institution/School board focused** a. School roadshows of SAT advantages and registration process. b. Reduce particulars required and sign up time. c. update process for bulk applications, digitise individual and school applications. d. allow for just-in-time sign ups and simplify validation for student or class submissions|

Finally, given the skewness of lower participating states it should be noted that as the majority of SAT takers decrease there is also a correlated decrease of scoring. Besides the disproportionate fall in grades it is notable how this can affect the intrinsic value of SAT as a benchmarking system which may reinforce inequality. Where participation is low there are higher mean scores implying bias in the SAT takers there. As the SAT scores are normalised, this system of grading may not effectively account for skew in the testing population. Whereas a fair distribution may be closer to a normal distribution for example. Therefore it would be preferential to continue to increase moderate to high SAT participation states over very low participating states.

### Data

There are 10 datasets included in the [`data`](./data/) folder for this project. You are required to pick **at least two** of these to complete your analysis. Feel free to use more than two if you would like, or add other relevant datasets you find online.

* [`sat_2017.csv`](../data/sat_2017.csv): 2017 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/))
* [`sat_2018.csv`](../data/sat_2018.csv): 2018 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/))
* [`sat_2019.csv`](../data/sat_2019.csv): 2019 SAT Scores by State ([source](https://blog.prepscholar.com/average-sat-scores-by-state-most-recent))
#### Additional Data
* [`2017_19_SAT_Participation_Numbers.csv`](../data/2017_19_SAT_Participation_Numbers.csv): 2017 to 2019 number of SAT participants and High School Graduates ([source](SEE IN .csv))
* mandated_states: 2019 list of states with mandated SAT or ACT testing ([source] SAT https://blog.prepscholar.com/which-states-require-the-sat ACT https://blog.prepscholar.com/which-states-require-the-act-full-list-and-advice)
* [`US_Regions.csv`]('../data/US_Regions.csv'): List of US states by Region and Division ([source] https://simple.wikipedia.org/wiki/List_of_regions_of_the_United_States)


Updated data dictionary.

|Feature|Type|Dataset|Description|
|---|---|---|---|
|column name|int/float/object|ACT/SAT|This is an example| 
|'state'|object| US State|Virginia
|'part_sat_2017'|float64|2017 SAT participation calculated as SAT taker over high school graduations| 5%|
|'erw_sat_2017'|int64|2017 Average Evidence-Based Read and Writing Scores for a state (between 200-800)| 500|
|'math_sat_2017'|int64|2017 Average Math Scores for a state (between 200-800)| 500|
|'total_sat_2017'|int64|2017 Average Total Scores for a state (between 400-1600)| 1000|
|'part_sat_2018'|float64|2018 SAT participation calculated as SAT taker over high school graduations| 5%|
|'erw_sat_2018'|int64|2018 Average Evidence-Based Read and Writing Scores for a state (between 200-800)| 500|
|'math_sat_2018'|int64|2018 Average Math Scores for a state (between 200-800)| 500|
|'total_sat_2018'|int64|2018 Average Total Scores for a state (between 400-1600)| 1000|
|'part_sat_2019'|float64|2019 SAT participation calculated as SAT taker over high school graduations| 5%|
|'erw_sat_2019'|int64|2019 Average Evidence-Based Read and Writing Scores for a state (between 200-800)| 500|
|'math_sat_2019'|int64|2019 Average Math Scores for a state (between 200-800)| 500|
|'total_sat_2019'|int64|2019 Average Total Scores for a state (between 400-1600)| 1000|
|'sat_takers_2017'|int64|2017 no. of SAT participants|60000|
|'sat_takers_2018'|int64|2018 no. of SAT participants|66396|
|'sat_takers_2019'|int64|2019 no. of SAT participants|60000|
|'high_school_graduates_2017'|int64|2017 no. of SAT participants|100000|
|'high_school_graduates_2018'|int64|2018 no. of SAT participants|100000|
|'high_school_graduates_2019'|int64|2019 no. of SAT participants|100000|
|'mandated'|int64|states with mandatory SAT or ACT in 2017-2019 (1 or 0 for yes or no)|1|
|'region'|int64|broad region in US|1|
|'division'|int64|division in US state|2|
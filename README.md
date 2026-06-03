# Summer-Project---Quant-Research-

As of 03/06/26, the first thing I am doing is researching a stock and also reading some academic papers around abnormal stock returns based on the results of clinical trials. So far, I am reading a paper titled: 'Stock Market Returns and Clinical Trial Results of Investigational Compounds: An Event Study Analysis of Large Biopharmaceutical Companies'. This paper is written by Thomas J. Hwang, and was published 7th August 2013. It looks at seven large American biopharmaceutical companies, namely Amgen (AMGN), Biogen Idec (BIIB), Bristol-Myers Squibb (BMY), Eli Lilly & Co. (LLY), Gilead Sciences (GILD), Merck (MRK) and Pfixer (PFE).


// Problems ran into so far //

- Noise that makes the percentage changes incorrect. For example a split event currently tells my function that a stock has an incredible percentage return for one day compared to the previous days close, which is of course a false positive. The stock has not had a rapid price increase due to an announcement being made about a clinical trial for example.

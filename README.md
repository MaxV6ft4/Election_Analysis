# Election_Analysis

## Project Overview
This project is an audit of a local congressional election in Colorado.

In all, there were seven tasks to complete:

1. Calculate the total number of votes cast.
2. Calculate the voter turnout for each county.
3. Calculate the percentages of votes from each county (out of the total vote count).
4. Determine county with the highest voter turnout.
5. Calculate the total number of votes each candidate received.
6. Calculate the percentage of votes each candidate won.
7. Determine the winner of the election based on popular vote.

## Resources
- Data source: [Election Results](https://github.com/MaxV6ft4/Election_Analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code 1.61.2

## Results

[Election Analysis Python File](https://github.com/MaxV6ft4/Election_Analysis/blob/main/PyPoll_Challenge.py)

The analytics of the election show that:

- The total number of votes cast in the election was 369,711.
            
            # Add to the total vote count.
            total_votes += 1
        
- The voter turnout per county was as follows:
    - Jefferson County contained 10.5% of the total votes with 38,855 votes.
    - Denver County contained 82.8% of the total votes with 306,055 votes.
    - Arapahoe County contained 6.7% of the total votes with 24,801 votes.

            # For each county in the county dictionary,
            for county_name in county_votes:

            # retrieve the county vote count,
            votes_for_each_county = county_votes[county_name]

            # calculate the percentage of votes for the county.
            county_vote_percentage = float(votes_for_each_county) / float(total_votes) * 100
            
- The county with the largest turnout was Denver.

            # Determine the winning county by getting its vote count.
            if votes_for_each_county > winning_county_count:

                   winning_county_count = votes_for_each_county
                   winning_county = county_name
                   
- The election results were as follows:
    - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
    - Diana DeGette received 73.8% of the vote with 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.

            # Retrieve vote count and percentage.
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
        
- Therefore, the winner of the election was:
    - Diana DeGette, who received 73.8% of the vote with 272,892 votes.

            # Determine winning vote count, winning percentage and winning candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                   winning_count = votes
                   winning_candidate = candidate_name
                   winning_percentage = vote_percentage

[Election Analysis Text](https://github.com/MaxV6ft4/Election_Analysis/blob/main/Analysis/election_analysis.txt)

## Summary


HEADLINE HUSTLE
===============

A command-line quiz game that challenges players to identify whether a news headline is real or fake. Headlines are randomly sampled from a MongoDB database containing both real and fake news entries.

------------------------------------------------------------
HOW TO PLAY
------------------------------------------------------------
When you run the game, you'll be prompted to enter how many rounds you want to play. In each round, a headline will be displayed, and you must guess whether it's "Real" or "Fake" by entering `r` or `f`.

At the end of the game, your score and accuracy percentage will be displayed.

------------------------------------------------------------
REQUIREMENTS
------------------------------------------------------------
- Python 3.x
- `pymongo` library
- A local MongoDB server running
- A MongoDB database named `News` with two collections:
  - `Real`: contains documents with at least a `title` field (real headlines)
  - `Fake`: contains documents with at least a `title` field (fake headlines)
  - CSV files to populate MongoDB found [here](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

Install the required Python package using pip:

    pip install pymongo

------------------------------------------------------------
USAGE
------------------------------------------------------------

Make sure your MongoDB server is running and the database is properly populated. Then run the script:

    python headline_hustle.py

------------------------------------------------------------
EXAMPLE DATABASE STRUCTURE
------------------------------------------------------------
Database: News

Collection: Real
Document example:
{
    "title": "NASA Confirms Water on the Sunlit Surface of the Moon"
}

Collection: Fake
Document example:
{
    "title": "Aliens Land in Central Park to Demand Equal Voting Rights"
}

------------------------------------------------------------
NOTES
------------------------------------------------------------
- Headlines are chosen at random using MongoDB's `$sample` aggregation operator.
- This is a local game and does not require any external API or internet access.
- Perfect for quick quizzes or classroom demonstrations on media literacy.

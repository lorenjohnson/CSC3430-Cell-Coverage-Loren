# CSC3430-Cell-Coverage

## Problem being solved

From Kleinberg and Tardos's *Algorithm Design* on page 190 in the exercise at the end of the *Greed Algorithms* chapter:

  5. Let’s consider a long, quiet country road with houses scattered very sparsely along it. (We can picture the road as a long line segment, with an eastern endpoint and a western endpoint.) Further, let’s suppose that despite the bucolic setting, the residents of all these houses are avid cell phone users. You want to place cell phone base stations at certain points along the road, so that every house is within four miles of one of the base stations.
  Give an efficient algorithm that achieves this goal, using as few base stations as possible.

## Requirements to run the code

* Python 3.x

## Instructions for running the code

1) Clone this repository (https://github.com/lorenjohnson/CSC3430-Cell-Coverage-Loren)
2) Assuming you have Python 3 installed and in your path, run `python cell-coverage.py` from the root directory of the cloned repository

## General Reflections on this problem and my solution

The resulting solution to this problem eximplifies greedy well. What is optimal for one turns out to be optimal for the next one, and that relatively easy to arrive at in this example. Much like Interval vs Weighted Interval scheduling problems adding a real world factor to complicate this problem, such as optimizing around the cost of placing a tower in any given location, would break the simple greedy solution and quickly turn this into a problem for dynamic programming.



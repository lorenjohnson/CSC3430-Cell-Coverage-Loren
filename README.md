# CSC3430-Cell-Coverage

## Problem being solved

From Kleinberg and Tardos's *Algorithm Design* on page 190 in exercise 5 at the end of the *Greed Algorithms* chapter:
> "Let’s consider a long, quiet country road with houses scattered very sparsely along it. (We can picture the road as a long line segment, with an eastern endpoint and a western endpoint.) Further, let’s suppose that despite the bucolic setting, the residents of all these houses are avid cell phone users. You want to place cell phone base stations at certain points along the road, so that every house is within four miles of one of the base stations.
> Give an efficient algorithm that achieves this goal, using as few base stations as possible."

## Requirements to run the code

* Python 3.x

## Instructions for running the code

1) Clone this repository (https://github.com/lorenjohnson/CSC3430-Cell-Coverage-Loren)
2) Assuming you have Python 3 installed and in your path, run `python optimal_cell_tower_locations.py` from the root directory of the cloned repository

> 🦉  **If you'd like to try with your own numbers you can modify the `SAMPLE_HOUSES` and `DEFAULT_TOWER_RANGE` values at the top of `python optimal_cell_tower_locations.py`**

## General Reflections on this problem and my solution

The resulting solution to this problem eximplifies greedy well. What is optimal for one turns out to be optimal for the next one, and that is relatively easy to see in this example. 

Much like Interval vs Weighted Interval scheduling problems adding a real world factor to complicate this problem, such as the cost of placing a tower in any given location or the ability for towers to repeat signals, could break down this simple greedy solution quickly into a problem for dynamic programming.

The time complexity of this algorithm is *O(n)* where *n* is the number of houses. 

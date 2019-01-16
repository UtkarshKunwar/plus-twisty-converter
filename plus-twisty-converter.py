#! /usr/bin/env python3

import os, sys
import json
import argparse

# Argument Parser initialisation.
parser = argparse.ArgumentParser(description="A utility to convert plusTimer .json data to importable Twisty Timer format.")
parser.add_argument("input_file", help="Path to the plusTimer .json file.")
parser.add_argument("output_file", help="Path to the output Twisty Timer file.")
parser.add_argument("-p", "--puzzle", help="Select the type of puzzle of the input_file.", choices=["2x2", "3x3", "4x4", "5x5", "6x6", "7x7", "clock", "mega", "pyra", "skewb", "sq1"], default="3x3")
parser.add_argument("-c", "--category", help="Select the category of the puzzle.", choices=["Normal", "OH", "BLD", "Feet"], default="Normal")
args = parser.parse_args()

in_file = args.input_file
out_file = args.output_file
category = args.category

# How Twisty Timer sees these puzzles
puzzle_types = {
    "2x2" : "222",
    "3x3" : "333",
    "4x4" : "444",
    "5x5" : "555",
    "6x6" : "666",
    "7x7" : "777"
}
puzzle = puzzle_types.get(args.puzzle, args.puzzle)

# Opening output file for writing.
outf = open(out_file, "a+")
if not os.path.getsize(out_file):
    outf.write("Puzzle,Category,Time(millis),Date(millis),Scramble,Penalty,Comment\n")

# To remove duplicates.
with open(out_file, "r") as outf_r:
    lines_seen = set()
    for line in outf_r:
        lines_seen.add(line)

# Processes and writes the .json input to the output file.
with open(in_file, "r") as inf:
    json_data = json.load(inf)
    number_session = len(json_data)

    for i, session in enumerate(json_data):
        number_solves = len(session["mSolves"])
        for i, solve in enumerate(session["mSolves"]):
            penalty = solve["mPenalty"]
            raw_time = solve["mRawTime"]
            scramble = solve["mScrambleAndSvg"]["mScramble"]
            timestamp = solve["mTimestamp"]

            # Penalty Codes according to Twisty Timer
            add_penalty = 0
            if penalty == "PLUSTWO":
                penalty = "1"
                add_penalty = 2000
            elif penalty == "DNF":
                penalty = "2"
            else:
                penalty = "0"

            # Twisty Timer takes millis, plusTimer takes nano.
            time = int(raw_time / 10**6) + add_penalty
            line = '"{}"; "{}"; "{}"; "{}"; "{}"; "{}"; ""\n'.format(puzzle, category, time, timestamp, scramble, penalty)
            if line not in lines_seen:
                outf.write(line)
                lines_seen.add(line)
outf.close()

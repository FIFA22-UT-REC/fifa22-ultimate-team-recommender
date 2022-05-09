# This driver script completes all preliminary data processing and results
# from data scraped from web to further use it to train for model
# Author: Tony Liang
# Date: May, 2022

all : data/raw/player_raw_data.csv data/processed/ST.csv data/processed/CF.csv data/processed/CAM.csv data/processed/CM.csv data/processed/CDM.csv data/processed/CB.csv data/processed/GK.csv data/processed/LB.csv data/processed/RB.csv data/processed/LWB.csv data/processed/RWB.csv data/processed/LM.csv data/processed/RM.csv data/processed/LW.csv data/processed/RW.csv

# scrap the data
data/raw/player_raw_data.csv :
	python main.py

# process data and divide according to positions
data/processed/ST.csv data/processed/CF.csv data/processed/CAM.csv data/processed/CM.csv data/processed/CDM.csv data/processed/CB.csv data/processed/GK.csv data/processed/LB.csv data/processed/RB.csv data/processed/LWB.csv data/processed/RWB.csv data/processed/LM.csv data/processed/RM.csv data/processed/LW.csv data/processed/RW.csv: main.py data/raw/player_raw_data.csv
	Rscript	src/process_data.R --file_path=data/raw/player_raw_data.csv --out_path=data/processed

# clean 
clean:
	rm -rf data/raw data/processed

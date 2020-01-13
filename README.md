# GlobalDef

<img src="https://upload.wikimedia.org/wikipedia/commons/d/db/Nasa_blue_marble.jpg" align="right" width="300" height="300"/>

Data, figures, and python source code associated with the quantitative study of global scale as well as hemispheric scale, global aquatic scale, and global terrestrial scale.

All software, data, and figures in this repository are original and/or free from licensed (re)use other than that of the license associated with this repository (GNU v3.0).

## Author
Kenneth J. Locey, Ph.D.

## Software used
* Anaconda navigator 1.9.7
* Anaconda client 1.7.2
* Anaconda project 0.8.3
* python 3.7.4
* Spyder 3.3.6
* numpy 1.17.2
* geopy 1.20.0
* Cartopy 0.17.0
* matplotlib 3.1.1
* pandas 0.25.1
* scipy 1.3.1
* Shapely 1.6.4.post1

## Contents

**DataSets**: A directory to contain empirical datasets obtained from the Global Biodiversity Information Facility (GBIF), the Global Prokaryotic Census (GPC), the Earth Microbiome Project (EMP), the Mammal Community Database (MCDB), and the Global Biotic Interactions (GloBI) service. Those datasets are not provided in this repository, for redistribution reasons that varied among datasets. Directions for obtaining and using those datasets are given in the `DataSets.pdf` file inside the directory.

* **DataSets.pdf**: A file providing descriptions and important information for each dataset used in the associated study and provided here.
* **Distances**: A directory containing files used by fig3.py to generate Fig3.png. Each file contains measures of distance randomly sampled from each dataset.
		* DataSets-AMNH-B.txt
		* DataSets-EMP.txt
		* DataSets-GBI.txt
		* DataSets-GPC.txt
		* DataSets-MCDB.txt
		* DataSets.txt
* **EMP**: Contains data used from the Earth Microbiome Project (EMP).
		* emp\_qiime\_mapping\_release1\_20170912_LatLon.tsv: A tab separated file containing latitudes and longitudes in decimal degrees for each site in the EMP dataset. 
* **GBI**: Contains data used from the Global Biotic Interactions (GloBI) service.
		* **citations.tsv.gz**: A compressed file containing citations to open source studies used by GloBI
		* **GetLatLons.py**: A python file used to extract geographical coordinates from the 7.6GB main GloBI file
		* **interactions_latlons.txt.zip**: A compressed file containing geographical coordinates for GloBI sites, used by DataSets-GLoBI.py
		
* **GBIF**: Contains directories for each dataset obtained from the Global Biodiversity Information Facility (GBIF). Each directory contains a markdown file title 'GetDataHere.md', that gives explicit step-by-step directions for obtaining data needed to reproduce files in the 'Distances' directory. 
* **GPC**: Contains one files on the Global Prokaryotic Census (GPC) obtained from the primary source (see GPC citation).
		* GPC.tsv: Used to produce DataSets-GPC.txt using the Scripts/DataSets/DataSets-GPC.py file.	 
* **MCDB**: Contains one file on the Mammal Community Database (obtained from http://esapubs.org/archive/ecol/E092/201/; see MCDB citation).
		*  MCDB_latlon.csv: Contains latitudes and longitudes for cites in the MCDB. Used to produce DataSets-MCDB.txt using the Scripts/DataSets/DataSets-MCDB.py file.

**figures**: A directory containing figures used in the associated manuscript. The figures are labeled in accordance with the manuscript. 


**Modeling**: A directory containing two directories related to the simulation-based probabilistic modeling of local-to-global scale ecological communities

* **Modeling.pdf**: A file providing descriptions of the simulation-based probabilistic communities models used in the associated study.

* **Sims**: Contains data and code for running community simulations
	* EnvData: Contains geotiffs used by ModelSims.py
	* ModelSims.py: A well-commented python script for simulating iterations of 12 models that vary in 7 community assembly characteristics, as described in the associated manuscript and online supplement.  
* **SimData**: Contains one data file:
	* Data4Figs.txt: A tab-separated file containing the output of ModelSims.py. The data in this file is used by the following python scripts to generated corresponding figures: 
		* Fig5.py
		* FigS1.py
		* FigS2.py  
	


**scripts**: A directory of python scripts containing four subdirectories and one script of central functions (fxns.py). 

* **Datasets**: Contains six .py files for processing empirical data files from GBIF, GPC, MCDB, EMP, GloBI, and data from the American Museum of Natural History's bird collection.
	* DataSets-GLoBI.py: Produces DataSets/Distances/DataSets-GloBI.txt
	* DataSets-EMP.py: Produces DataSets/Distances/DataSets-EMP.txt
	* DataSets-GBIF.py: Produces DataSets/Distances/DataSets-GBIF.txt
	* DataSets-MCDB.py: Produces DataSets/Distances/DataSets-MCDB.txt
	* DataSets-GPC.py: Produces DataSets/Distances/DataSets-GPC.txt
	* DataSets-AMNH-B.py: Produces DataSets/Distances/DataSets-AMNH-B.txt
	
* **Figs**: Contains seven .py files for producing figures of the associated manuscript and supplement.
	* Fig1.py: Uses
	* Fig2.py: Uses SimData/Moments.txt
	* Fig3.py: Uses
	* Fig4.py: Uses
	* Fig5.py: Uses
	* FigS1.py: Uses
	* FigS2.py: Uses
	
* **Moments**: Contains three files associated with deriving moments for global scale, hemispheric scale, global aquatic scale, and global terrestrial scale.

	* EstimatedMoments.py: Uses SimData/Moments.txt to print out the following for each of global scale, hemispheric scale, global aquatic scale, and global terrestrial scale:
		* Estimated mean distance and assocated standard deviation from 1,000 simulated distributions.
		* Estimated variance in distance and assocated standard deviation from 1,000 simulated distributions.
		* Estimated skewness distance and assocated standard deviation from 1,000 simulated distributions.
		
	* Moments.py: Simulates 19,000 distributions for each of global scale, hemispheric scale, global aquatic scale, and global terrestrial scale, using numbers of randomly chosen sites ranging from 10 to 1,000. Estimates the mean distance, variance in distance, and skewness of distance for each simulated distribution. Writes the results to SimData/Moments.txt.
	 
* **Test**: Contains one file:
	* PermTest.py: Simulates 10,000 global scale distributions of sample locations and compares each to discrete uniform distributions and tests each against Pearson's chi-square. Generates SimData/PermTest-great_circle.txt' or SimData/PermTest-geodesic.txt' depending on user preference.
	
* fxns.py: A script of central importance. Contains functions for the following, which are used throughout other scripts of this repository:
	*  antipodal(): finds the antipodal point of a given point
	*  is_land(): determines whether a given point occurs on land or in water
	*  get_pts(): The most important function of this repository. Generates an unbiased random set of locations for global scale, hemispheric scale, global aquatic scale, and global terrestrial scale. Accepts Great Circle and geopy's geodesic models. 
	*  haversine(): a function to compute distances on a Great Circle model of Earth. Operates faster than equivalent functions in geopy, cartopy, and basemap.


**SimData**: Contains simulated data.

* Moments.txt: Contains output from Moments.py (described above). Data columns are:
	* sites: Number of simulated sites
	* sim: Simulation number
	* method: Whether Great Circle or Geodesic
	* type: global, hemispheric, global aquatic, or global terrestrial
	* mean: Mean distance among all unique pairs of sites
	* var: Variance in distance among all unique pairs of sites
	* skew: Skewness of distance among all unique pairs of sites

* PermTest-great_circle.txt: Contains output from PermTest.py (described above). Data columns are:
	* sim: Simulation number
	* iteration: iteration of the particular simulation
	* num\_ref\_sites: Number of sites (k) used to form non-overlapping circular areas of equal size, used in testing.
	* dist_ref: Radius of each of the above mentioned non-overlapping sites.
	* x2: Pearson's chi-square value resulting from testing the resulting geographical distribution of sites among k areas.
	* pval: p-value associated with x2
	* x22: Pearson's chi-square value resulting from testing a discrete uniform distribution of sites among k areas. 
	* pval2: p-value associated with x22 
	* var1: Variance in numbers of locations resulting from the geographical distribution of sites among k areas.
	* skew1: Skewnness in numbers of locations resulting from the geographical distribution of sites among k areas. 
	* kur1: Kurtosis in numbers of locations resulting from the geographical distribution of sites among k areas.
	* var2: Variance in numbers of locations resulting from a discrete uniform distribution of sites among k areas.
	* skew2: Skewness in numbers of locations resulting from a discrete uniform distribution of sites among k areas. 
	* kur2: Kurtosis in numbers of locations resulting from a discrete uniform distribution of sites among k areas.






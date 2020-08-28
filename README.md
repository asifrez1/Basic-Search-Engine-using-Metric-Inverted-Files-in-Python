# Basic-Search-Engine-using-Metric-Inverted-Files-in-Python
### A Basic Search Engine using Python to Perform ‘Similarity Search’ using Metric Inverted Files (MIF)

This project is about developing a software that does “similarity search” using the MIF data. The software will ask for a data object (that may not exist in the input file) and 
will display the similar objects from your input files using the MIF data file.

Methodology:
- Example Data: https://drive.google.com/file/d/1_3crfwSa3pMomVenE0I4ZyGmd6tSn6r0/view?usp=sharing
- This will also generate a file named "RefIndices.json", which stores the indices of the Reference Objects
- Use the "MIF_Generator.py" to generate MIF from the data
- Example MIF: https://drive.google.com/file/d/1e-mmiQ2rTpQgRs9k3AcO3aXh7_bjGLf7/view?usp=sharing
- Enter your queries in the "Enter-Query-Here.csv" file and save it.
- Run "Query-Search.py" to perform similarity search and get the outputs

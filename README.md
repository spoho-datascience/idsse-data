# An integrated dataset of synchronized spatiotemporal and event data in elite soccer

This is the official repository for the paper: 
>Bassek, M., Rein, R., Weber, H., Memmert, D. (2024). An integrated dataset of
> synchronized spatiotemporal and event data in elite soccer. In submission.

## Project Structure

- `data_processing.py`: Functions for loading and processing met data, event data, and position data.
- `visualization.py`: Functions for visualizing the processed data.
- `data_summary.ipynb`: Jupyter notebook to replicate the descriptive statistics and visualizations presented in the paper.

## Data Source and Characteristics

- Soccer matches from the [German Bundesliga](https://www.dfl.de/de/) 1st and 2nd division 
- Size: 7 full matches
  - Official meta data (match information)
  - Official event data.
  - Official position data captured by [TRACAB](https://tracab.com/products/tracab-technologies/)
  
## License
The data are provided with authorization auf the [Deutsche Fussball Liga (DFL)](https://www.dfl.de/de/). The dataset
is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). You must therefore give appropriate credit
when using this dataset by
1) naming the *Deutsche Fußball Liga (DFL)*
2) [citing this publication](##citation)

## Usage

### Data Processing and visualzaion

1. Download the raw data [here](LINKTOREPO)
2. Open the `data_summary.ipynb` notebook.
3. Define the path to your dataset directory in the `path` variable.
4. Run the cells to load and process the data.
5. The processed data summary will be displayed.

## Citation
```BibTeX
@article{BassekDataset,
author = {Bassek, Manuel and Rein, Robert and Weber, Henrik and Memmert,
Daniel},
journal = {In Submission},
title = {An integrated dataset of synchronized spatiotemporal and event data in elite soccer},
year = {2024}
}
```
---

## Funding
This project has been kindly supported by the [Institute of Exercise Training and Sport
Informatics](https://www.dshs-koeln.de/en/institut-fuer-trainingswissenschaft-und-sportinformatik/) at the German Sport
University Cologne under supervision of Prof. Daniel Memmert. Funding was provided by the 
[German Research Foundation](https://www.dfg.de/en) 
([floodlight](https://gepris.dfg.de/gepris/projekt/522904388?context=projekt&task=showDetail&id=522904388&)).

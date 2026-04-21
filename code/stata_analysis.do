* stata_analysis.do
* Rwanda Firm Activity Analysis
* Created: April 2026

clear all
set more off

* Load panel data
import delimited using "data/processed/firm_nightlights_panel.csv", clear

* Summary statistics by cluster and year
tabstat nightlights, by(cluster) stats(mean sd min max n)

* Regression: Nightlights trend by cluster (simple demonstration)
encode type, gen(type_num)
reg nightlights i.cluster i.year i.type_num, robust

* Export results
outreg2 using "outputs/regression_results.doc", replace word
# Azure DE learning - Architecture notes

## Stack
- Storage : Azure Delta Lake Storage Gen2
- Compute : Azure Databricks (Spark/Python)
- Orchestration : Azure Data Factory
- Format : Delta Lake
- Architecture : Medallion (Bronze/Silver/Gold)

## My Medallion Understanding
We build the bronze/silver/gold layers for enabling long term scalability for the cheap while also ensuring that we are confind to a specific structured or unstructured format and the raw data can be used in future in precisely the source intended structure for any of our changing reporting or analysis needs.

## Resource created this weel
- Resource group : de-learning-rg
- Storage account : pndelearningstorage
- Containter : bronze, silver, gold
- Databrince free edition workspace

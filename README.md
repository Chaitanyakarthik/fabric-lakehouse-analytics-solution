Microsoft Fabric Lakehouse Analytics Solution
Project Overview

This project demonstrates an end-to-end analytics solution built using Microsoft Fabric, leveraging a modern Lakehouse architecture to ingest, transform, and analyze retail sales data.

The solution integrates API-driven data ingestion, scalable Lakehouse storage, PySpark transformations, and interactive Power BI dashboards to enable business intelligence and KPI analysis.

Solution Architecture

HTTP JSON API → Fabric Data Pipeline → Lakehouse (Bronze → Silver → Gold) → Power BI Dashboard

Technologies Used

• Microsoft Fabric
• OneLake / Lakehouse
• Fabric Data Pipeline
• PySpark
• Parquet / Delta Lake Storage
• Power BI

 Key Components
 Data Ingestion Pipeline

Designed a Microsoft Fabric Data Pipeline to automate ingestion of retail sales data from an HTTP JSON source into the Lakehouse Bronze layer.

Pipeline capabilities:

• API-driven ingestion
• JSON dataset processing
• Schema translation & flattening
• Parquet storage with Snappy compression
• Scalable OneLake storage

Lakehouse Architecture 

Implemented a multi-layer Lakehouse processing framework to structure data for analytics workloads.

The Lakehouse serves as the centralized data platform supporting scalable storage, transformation, and analytical processing.

Bronze Layer (Raw Data Storage)

• Stores raw ingested API data
• Preserves original schema

 Silver Layer (Data Standardization & Cleansing)

Applied PySpark transformations to prepare clean and structured datasets.

Transformation steps:

• Schema normalization
• Column standardization
• Data type casting
• Data validation & cleaning

Gold Layer (Analytics & Reporting Layer)

Constructed analytics-optimized tables designed for business intelligence workloads.

The Gold layer organizes curated datasets into fact-style analytical structures, enabling efficient dimensional analysis.

Key characteristics:

• Aggregated revenue & order metrics
• Business-oriented analytical tables
• Delta Lake table storage

 Power BI Dashboard & KPIs

Developed an executive-style dashboard enabling interactive analytics.

Key KPIs:

• Total Sales
• Total Orders
• Average Transaction Value
• Unit Cost
• Revenue Distribution by Channel
• Regional Performance
• Product Category Contribution

Interactive Features:

• Channel Filter
• Region Filter
• Dynamic KPI updates

Business Impact

This Lakehouse-based analytics solution enables stakeholders to monitor revenue performance, evaluate channel effectiveness, analyze purchasing behavior, and track regional trends through interactive dashboards.

Dashboard & Pipeline Preview

## Executive Sales Dashboard

This dashboard provides an interactive analytical view of revenue performance, order volume, regional trends, and customer segmentation.

[Dashboard Overview](snapshots/dashboard.png)

Key Learnings

• End-to-end Lakehouse pipeline design
• API-based data ingestion
• PySpark transformation workflows
• Lakehouse data modeling principles
• Analytical aggregation strategies
• Business intelligence dashboard design

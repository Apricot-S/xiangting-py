#!/usr/bin/env bash

source .venv/bin/activate
pytest --benchmark-only --benchmark-columns='min,max,mean,stddev,median,iqr,outliers' --benchmark-sort=mean
deactivate

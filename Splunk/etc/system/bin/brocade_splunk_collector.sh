#!/bin/bash

#Setup run-time environment 
# this should be the directory containing python files related to slx-collector
export WORK_DIR=python-slx-collector
export LOG_CFG=log.yaml

cd $WORK_DIR
#chose python according to protobuf and Splunk ;
#At the time of this POC, it was Python27
#Below port is the one which is registered as a collector on SLX
python collector_main.py server --port 54321 --json $WORK_DIR
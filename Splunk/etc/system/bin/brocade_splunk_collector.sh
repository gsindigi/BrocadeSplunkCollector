#!/bin/bash

#Setup run-time environment 
DIRNAME=`dirname $0`
export LOG_CFG=log.yaml
PROGNAME=`basename $0`
CURRENTDIR=`cd $DIRNAME/..; pwd`
export CURRENTDIR=$CURRENTDIR

cd $CURRENTDIR
#chose python according to protobuf and Splunk ;
#At the time of this POC, it was Python27
#Below port is the one which is registered as a collector on SLX
python collector_main.py server --port 54321 --json $CURRENTDIR
@echo off
REM Sample bat file to set things right and launch collector
set LOG_CFG=log.yaml
set WORK_DIR = C:\CCSplunk\
cd "%WORK_DIR%"
REM chose python according to protobuf and Splunk ;
REM At the time of this POC, it was Python27
REM Below port is the one which is registered as a collector on SLX
python.exe collector_main.py server --port 54321 --json "%WORK_DIR%"
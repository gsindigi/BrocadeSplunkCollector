# BrocadeSplunkCollector
A streaming based collector example to integrate with Splunk.

This example helps integrate SLX's telemetry streaming support with Splunk and 
configure Splunk to receive and interpret the telemetry response of various supported types. 

This is an attempt to demonstrate how to use the SLX's telemetry streaming support 
and integrate with Splunk. 


## Pre-Requisites
1. Requires Google's Protocol Buffer support (protobuf==3.1.0.post1); If not present 
   install the same
   >python -m pip install protobuf
2. Requires Python YAML support (PyYAML==3.12)
   >python -m pip install pyyaml
3. The files under "python-slx-collector/protos/" are generated using `protoc` for the 
   protobuf files SLX supporting. Make sure to have these files are indeed of the right
   version that SLX supporting. 

## Setup Details

### Splunk - Data Inputs
- Splunk provides different data inputs. These can be used out-of-box, when 
  there is no custom interpretation involved
- For this example, SLX's Collector model support is leveraged
- Copy files under Splunk\etc\system\bin\brocade_splunk_collector\* to respective 
  folders under Splunk installation according to platform.
- Update WORK_DIR in *brocade_splunk_collector\** files to reflect correct path to 
  the python files related to slx-collector
- Set up a custom data-input on the Splunk instance "Settings\Data Input\", 
  under "Local Inputs", choose "Scripts".
- Choose the script path "$SPLUNK_HOME\etc\system\bin" script-name as 
  "*brocade_splunk_collector\**" and set the requisite values for Interval etc
  
  | Field | Value (e.g.) |
  | --- | --- |
  | Interval | 60 |
  | Source name override | BrocadeSplunkCollector |
  | Source Type | manual, \_json |

### SLX Configuration
On the SLX box, configure a collector with ipv4 and port of the Splunk instance
inline with details "*brocade_splunk_collector*\*" 
```
telemetry collector SplunkCollector
  ip <ipv4> port <portNum> ! ipv4 & portNum should be actual values
  profile system-profile default_system_utilization_statistics
  profile interface-profile default_interface_statistics
  activate ! this token controls the collector behavior
!  
```

## In Action
- SLX-OS box (switch/router) needs to be configured with Splunk as a collector
- Make sure the Script data-input *BrocadeSplunkCollector* is enabled and active in Splunk
- Custom collector receives the data, does necessary conversions (json, in this case) 
so that Splunk can interpret it
- Pumps converted payload into Splunk
- Use Splunk’s Search App to view the data in raw (json) form 
- Use Splunk's reports/dashboard widget capabilities to plot these values received real-time



# Edge Insights Platform

The edge insights platform from Intel is a framework for rapidly deploying video analytics solutions. It provides a microservice architecture that distributes the tasks of video intake, filtering, analyzing with deep learning and computer vision, and performing automated actions, alerts, and intelligent monitoring.

The edge insights platform provides triggers/filters and classifiers that can be customized by an organization to fit their custom needs. 

The edge insights platform supports both a developer mode and a production mode. The developer mode disables certificate security and allows the developer to concentrate on the functionality of their application without deploying cryptographic certificates.

Let's go through a description of the components of this microarchitecture


## Components of the Edge Insights Platform

Multiple microservices coordinate to provide the overall service of the edge insights platform. a number of these are open source projects such as telegraf, influxdb, chronograf, Kapacitor (collectively called the TICK stack) and Vault, a service that keeps cryptographic secrets in a secure manner. 

Here's a list of the microservices:



*   The data agent
*   Data analytics
*   Data bus abstraction
*   Data ingestion library
*   The factory control application
*   The image store
*   The stream manager
*   Stream sub library
*   Telegraph
*   Video ingestion
*   Secret storage
*   Algorithms including triggers / filters and classifiers

Let's go over each of these and describe their role in the system as well as how they connect to other parts of the system.


### The Data Agent


#### Technologies and Components Used

The data agent uses a number of technologies directly and it also bundles several projects as sidecars into its docker image.



1. Toml - Tom's obvious, minimal language is a specification that is often used for configuration files. This language is used for the configuration files in the TICK stack.
2. GRPC - a high-performance, open source universal RPC framework


#### Execution


##### Security



*   When the data agent begins it starts by reading the command-line arguments and checking if the program is running on a genuine Intel system.
*   if it is running on a genuine Intel system it checks to see if the trusted platform module can be enabled
*   If then checks to see if it is running in developer mode or production mode.
*   Next it checks to make sure that vault is running and if it is not running the data agent will exit.
*   It then reads the certificates for influxdb from vault and writes out the SSL secrets that the grpc internal client will use.
*   The certificate authority certificate is written to /etc/ssl/ca/ca_certificate.pem


##### Service Initialization



*   After the security initialization is performed the data agent then launches influxdb and the stream manager.
*   The data agent and then takes UDP data from influxdb and forward it to the stream manager
*   The key for each stream is used as the topic to publish to the stream server.


### Data Analytics

the job of the data analytics microservice is to evaluate video and time series data and classify that data according to the users custom algorithm.

The edge insights platform can process two types of data for analytics the first type is video data and the second type is point or time series data. At this point in the development of the edge insights platform the focus of current activity is on video data and integration with openvino. Video data is analyzed on a frame-by-frame basis.

There is a sample analytics application included in the repository they can serve as a guide to creating your own classifiers and deploying them.


#### Dependencies

The data analytics microservice depends upon the openvino libraries to perform deep learning and computer vision analytics. 

Python 3.6 is dependency of the data analytics microservice.

Data analytics also uses the stream sub library which is part of the edge analytics platform.


#### Execution

The data handler is responsible for subscribing to influxdb for point data and to the image store for video data. Once the data is received then running classifier algorithms on that data. 


### Factory Control App

the factory control application controls the alarm light and reset buttons for a demo that was created using the edge insights platform. 

It subscribes to the stream sub library. If defects are detected then it writes data to a modbus controller which controls the lights and alarms.


### The Image Store Service

This service uses Redis for metadata storage and MinIO for object storage.


#### Execution



*   The image storage process starts by parsing the command line options and then launching a grpc server. 
*   Next it checks that it is running on genuine Intel hardware.
*   Next it checks that the data agent is running if it's not running then it exits
*   Event gets the configuration files for Redis and Minio 


### Stream Manager

The stream manager subscribes to influxdb and posts topics to the data bus in OPC-UA format.

cryptographic certificates are used in all connections in order to ensure data security.


#### Execution



*   as the screen manager is initializing it first creates an HTTP client connection to Influxdb and creates a subscription to the data.


### Data bus abstraction


#### There are three different libraries that are written for data bus abstraction 1 written in C language, one written in Python, and another written in Go lang.

the date of bus abstraction implements the following command interface:



*   Create context
*   Start topic
*   Send
*   Receive
*   Stop topic
*   Destroy context

the create context function creates the OPC UA server client pubsub context-based on a configuration file.


### Algorithms

the algorithms folder contains mainly two different types of hooks in the edge insights platform: the trigger, ingestor and the classifier. It also defines a number of primitive utility classes that convey the information needed for triggers in classifiers such as a display info object and defect object.


#### Ingestor

the ingester opens a number of video ingestion streams that are captured inside objects called video capture objects. The Ingestor also has a polling_interval that specifies how frequently to take frames from the video stream.

VideoCapture objects open up any number of opencv video streams based on the number of streams set up in the configuration file. 

frames that are selected according to the polling interval are put onto a queue and the call_on_data callback is executed on the frame.

On_data is it called back which is passed into the constructor of the video ingestor.


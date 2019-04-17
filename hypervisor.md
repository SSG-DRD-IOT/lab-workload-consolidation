# Workload consolidation at different levels of the competing stack


## Hypervisors

Workload consolidation is a generalized statement that can encompass many ideas about interacting computer systems. 
Even though the implementation of a system that has multiple consolidated workloads can vary, the goal of workload consolidation is to achieve a higher overall return on investment in computer equipment, as well as the people in systems needed to manage them.

In this workshop we're going to look at four different levels of workload consolidation:
* Type 1 hypervisors - hardware-based virtualization
* Type 2 hypervisors - operating system level virtualization
* Containerization - application level virtualization
* Networking level application sharing

## What is a Hypervisor?
Computer virtualization is changing IT/OT from a job using physical devices to a profession using logical devices. A hypervisor is a lightweight piece of software that maps physical devices to logical devices. It allows multiple logical devices to share a single physical or logical device.

### Type 1 Hypervisors - hardware-based virtualization
These hypervisors run directly on the bare metal hardware and coordinate access to that hardware two operating systems which run on top of it. The term hypervisor is an alternative to the word supervisor which in the early days of computing was a common term for the operating system.

### Type 2 Hypervisors - operating system level virtualization
These hypervisor is run on top of a operating system and manage control of host operating system resources to virtualized operating system resources. Examples of this include VMware Workstation™, Virtualbox™, Parallels Desktop for Mac™ and QEMU.

Virtualizing all of the resources of an operating system can be an extremely expensive task and in the initial days of type 2 hypervisor they were known for their inefficient performance. 

**Intel® Virtualization Technology (Intel® VT)** builds virtualization technology that allows type 2 hypervisor to directly access type one level hardware resources.

Intel® Virtualization Technology (Intel® VT) are hardware and software specific extensions that enabled the virtualization of CPU resources, GPU resources, memory virtualization and IO resources.

#### CPU virtualization
CPU virtualization features enable faithful abstraction of the full prowess of Intel® CPU to a virtual machine (VM). All software in the VM can run without any performance or compatibility hit, as if it was running natively on a dedicated CPU. Live migration from one Intel® CPU generation to another, as well as nested virtualization, is possible.

#### Memory virtualization 
Memory virtualization features allow abstraction isolation and monitoring of memory on a per virtual machine (VM) basis. These features may also make live migration of VMs possible, add to fault tolerance, and enhance security. Example features include direct memory access (DMA) remapping and extended page tables (EPT), including their extensions: accessed and dirty bits, and fast switching of EPT contexts.


#### I/O virtualization
I/O virtualization features facilitate offloading of multi-core packet processing to network adapters as well as direct assignment of virtual machines to virtual functions, including disk I/O. Examples include Intel® Virtualization Technology for Directed I/O (VT-d), Virtual Machine Device Queues (VMDQ), Single Root I/O Virtualization (SR-IOV, a PCI-SIG standard), and Intel® Data Direct I/O Technology (Intel® DDIO) enhancements.
Intel® Graphics Virtualization Technology (Intel® GVT) allows VMs to have full and/or shared assignment of the graphics processing units (GPU) as well as the video transcode accelerator engines integrated in Intel system-on-chip products. It enables usages such as workstation remoting, desktop-as-a-service, media streaming, and online gaming.


#### Virtualization of Security and Network functions
Virtualization of Security and Network functions enables transformation of traditional network and security workloads into compute. Virtual functions can be deployed on standard high volume servers anywhere in the data center, network nodes, or cloud, and smartly co-located with business workloads. Examples of technologies making it happen include Intel® QuickAssist Technology (Intel® QAT) and the Data Plane Development Kit (DPDK).

#### Containerization
Containerization is rapidly becoming an adopted it custom thanks to Docker, Kibernetes and other containerization technologies. It allows your organization the freedom to build, manage and secure applications without fear that their environment will change. It allows the applications to be tested in a known state and environment and deployed in the same conditions.

Containerization technologies will reduce testing and deployment expenses because testing and deployment are done in the same containerized environment.

Containers share the resources of the host operating system but they allow the application to run with limited virtualized access to the underlying operating system. 

Containers also allow workloads to be migrated to new hardware and for the technicians to know that it will run exactly the same on the new hardware.

Intel support the number of containerization projects including Clear Linux(R).

In the next Lab we will use Docker containers to deploy The Foundry Edge X services and create. 

#### Network level resource sharing
There are many ways of partitioning applications across networked architectures. Some of the more popular patterns include the micro-service architecture, fog enabled applications and the client/server model. All cloud providers have APIs to scale applications across their enterprise. 

In this lab, we will take a look at Edge X Foundry which is a vendor-neutral, open source, loosely-coupled microservices framework providing the choice to plug and play from a growing ecosystem of available 3rd party offerings or augment with your own proprietary innovations. EdgeX focuses on Industrial and business IoT solutions.
 
# What is Next?
Next we will install the EdgeX Foundry service architecture and begin using it to connect devices on our network.

Please, continue to this link and begin working on the lab.

https://docs.edgexfoundry.org/Ch-GettingStartedUsers.html

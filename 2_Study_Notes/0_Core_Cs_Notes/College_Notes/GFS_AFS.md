---
created:
topics: []
tags: []
aliases: []
purpose: ""
---

# Introduction

Distributed File Systems (DFS) play a critical role in providing transparent, reliable, and scalable access to files across multiple machines in a networked environment. This assignment presents a detailed examination of two significant distributed file systems: the Andrew File System (AFS) and the Google File System (GFS), based entirely on the concepts covered in Module 5. Every aspect described in the lecture notes is included without omission. The study covers the background, architecture, components, file handling mechanisms, operations, key features, and design philosophies of both systems.

# Section 1: The Andrew File System (AFS)

## 1.1 Background and Development

The Andrew File System (AFS) was developed by Carnegie Mellon University as part of the Andrew distributed computing environments in 1986. It was a research project aimed at creating a campus-wide file system. Like the Network File System (NFS), AFS provides transparent access to remote shared files for UNIX programs running on workstations.

## 1.2 Implementation Architecture

AFS is implemented as two software components that exist as UNIX processes:

- Vice - acts as the flat file service.
- Venus - acts as the directory service.

These two processes (Vice and Venus) work together to provide the complete file service.

## 1.3 Overall System Architecture

The architecture of AFS distributes processes across workstations and servers. Workstations run the Venus process, while file servers run the Vice process. The distribution of processes in the Andrew File System is illustrated in Figure 11 of the notes, which shows multiple workstations connected via a network to multiple servers.

Each workstation contains:

- User programs
- Venus process
- UNIX kernel

The servers contain the Vice process. The network connects all Venus processes on workstations to the Vice processes on servers.

## 1.4 File Handling in AFS

The files available to user processes running on workstations are either local or shared.

- Local files are handled as normal UNIX files. They are stored on the workstation's disk and are available only to local user processes.
- Shared files are stored on servers, and copies of them are cached on the local disks of workstations.

## 1.5 Operations Supported by AFS

AFS supports the following operations:

- `Fetch(fid) -> attr, data`: Returns the attributes (status) and, optionally, the contents of the file.
- `Store(fid, attr, data)`: Updates the attributes and (optionally) the contents of a specified file.
- `Create() -> fid`: Creates a new file and records it.
- `Remove(fid)`: Deletes the specified file.
- `SetLock(fid, mode)`: Sets a lock on the specified file or directory.
- `ReleaseLock(fid)`: Unlocks the specified file or directory.

These operations are provided by the combination of Vice (flat file service) and Venus (directory service) processes.

# Section 2: The Google File System (GFS)

## 2.1 Background and Objectives

Google Inc. developed the Google File System (GFS), a scalable distributed file system (DFS), to meet the company's growing data processing needs. GFS offers fault tolerance, dependability, scalability, availability, and performance to big networks and connected nodes. It reduced hardware flaws while making gains from commercially available servers. GFS manages two types of data: File metadata and File Data.

## 2.2 Core Design Features

- Large (64 MB) pieces of the stored data are split up and replicated at least three times around the network.
- Reduced network overhead results from the greater chunk size.
- Without hindering applications, GFS is made to meet Google's huge cluster requirements.
- Hierarchical directories with path names are used to store files.
- The master is in charge of managing metadata, including namespace, access control, and mapping data.
- The master communicates with each chunk server by timed heartbeat messages and keeps track of its status updates.
- More than 1,000 nodes with 300 TB of disk storage capacity make up the largest GFS clusters.
- This system is available for constant access by hundreds of clients.

## 2.3 Architecture and Components

GFS consists of three main components:

### GFS Clients

These are computer programs or applications that may be used to request files. Requests may be made to access and modify already-existing files or add new files to the system.

### GFS Master Server

- It serves as the cluster's coordinator.
- It preserves a record of the cluster's actions in an operation log.
- Additionally, it keeps track of the data that describes chunks (metadata).

### GFS Chunk Servers

- They are the GFS's workhorses.
- They keep 64 MB-sized file chunks.
- The master server does not receive any chunks from the chunk servers.
- Instead, they directly deliver the desired chunks to the client.
- The GFS makes numerous copies of each chunk and stores them on various chunk servers in order to assure stability; the default is three copies.

## 2.4 Features of GFS

The key features of Google File System are:

- Fault tolerance.
- Reduced client and master interaction.
- High availability.
- Critical data replication.
- Automatic and efficient data recovery.
- High aggregate throughput.

## 2.5 Architectural Diagram Description

The architecture of GFS (as shown in the notes) depicts:

- Multiple GFS Clients interacting with the GFS Master Server for metadata operations.
- Clients communicating directly with multiple GFS Chunk Servers for actual data read/write operations.
- The Master Server maintaining heartbeat communication with all Chunk Servers.
- Files are divided into 64 MB chunks, each replicated across three (or more) Chunk Servers for fault tolerance.

# Conclusion

The Andrew File System (AFS) and the Google File System (GFS) represent two important milestones in the evolution of distributed file systems. AFS, developed in 1986 at Carnegie Mellon University, focused on providing a transparent campus-wide file system using Vice (flat file service) and Venus (directory service) processes, with clear distinction between local and shared files and support for operations such as Fetch, Store, Create, Remove, SetLock, and ReleaseLock.

In contrast, GFS, designed by Google Inc. to handle massive data processing requirements, introduced a highly scalable architecture based on large 64 MB chunks with triple replication, a single Master Server for metadata management, multiple Chunk Servers as the primary data stores, and direct client-to-chunk-server data transfer. Its design emphasizes fault tolerance, reduced client-master interaction, high availability, critical data replication, automatic recovery, and high aggregate throughput, making it suitable for Google's enormous cluster environments with over 1,000 nodes and 300 TB storage.

Both systems achieve transparency and scalability but differ significantly in scale, fault-tolerance mechanisms, and design philosophy - AFS for campus environments and GFS for planet-scale data-intensive applications.

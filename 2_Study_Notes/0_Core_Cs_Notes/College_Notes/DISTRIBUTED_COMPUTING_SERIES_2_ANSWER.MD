**CST 402 - DISTRIBUTED COMPUTING**  
**MODEL ANSWERS – PAPER 2 (Modules 3, 4 & 5)**  
**(All questions answered – Detailed as per marks)**

---

### **PART – A (3 Marks each)**

**1. Describe any three requirements of mutual exclusion algorithms.**  
Mutual exclusion algorithms in distributed systems must satisfy three fundamental requirements (Module 3):

1. **Safety Property**: At any instant, only one process is allowed to execute its critical section (CS). No two processes should be in the CS simultaneously.

2. **Liveness Property**: The algorithm must be free from deadlock and starvation. Every requesting process must eventually get a chance to enter the CS in finite time. No process should wait indefinitely while others repeatedly enter the CS.

3. **Fairness Property**: Requests for the CS should be granted in the order of their arrival in the system (FIFO fairness). Each process should get a fair chance to execute the CS.

These properties ensure correct, deadlock-free, and equitable access to shared resources.

**2. Outline coteries and quorums in quorum-based mutual exclusion algorithms.**  
In quorum-based mutual exclusion (Module 3), a site does not request permission from all other sites but only from a subset called a **quorum**.

- A **coterie** C is a set of sets (quorums). Each set g ∈ C is called a **quorum**.
- **Intersection Property**: Any two quorums in the coterie must have at least one common site. This ensures that when two sites request the CS concurrently, at least one site receives both requests and can serialize them.
- **Minimality Property**: No quorum is a proper subset of another quorum. This avoids unnecessary messages and improves efficiency.

Quorum-based algorithms significantly reduce message complexity compared to Lamport or Ricart-Agrawala algorithms.

**3. Explain any three models of deadlock.**  
(Module 3 – Models of Deadlocks)

1. **Single-Resource Model**: A process can have at most one outstanding request for a single resource unit. The wait-for graph (WFG) has out-degree at most 1. Presence of a cycle in WFG indicates deadlock.

2. **AND Model**: A process can request multiple resources simultaneously. The request is granted only when **all** requested resources are available. Out-degree can be > 1. A cycle in WFG means deadlock.

3. **OR Model**: A process requests multiple resources and the request is satisfied if **any one** of them is granted. Presence of a cycle in WFG does **not** necessarily mean deadlock (because a process may proceed if any resource is available).

Other models include AND-OR model and Unrestricted model.

**4. Explain domino effect in checkpointing and rollback recovery.**  
(Module 4)

In uncoordinated (independent) checkpointing, each process takes checkpoints independently. When a process fails and rolls back, it may create an **orphan message** (a message whose receive is recorded but send is undone). To maintain consistency, the receiver must also roll back, which may create new orphan messages, forcing further rollbacks.

This cascading rollback can continue until the initial state, resulting in the **domino effect** — a large amount of useful computation is lost. The domino effect makes independent checkpointing impractical.

**5. List any three assumptions in consensus and agreement algorithms.**  
(Module 5)

1. **Failure Model**: At most _f_ processes can be faulty (fail-stop, omission, or Byzantine).
2. **Synchronous / Asynchronous Communication**: In synchronous systems, message delay is bounded; in asynchronous systems, there is no upper bound.
3. **Channel Reliability & Sender Identification**: Channels are reliable; a receiver always knows the identity of the sender.

---

### **PART – B**

**6(a) Explain Maekawa’s algorithm for mutual exclusion with an example.** (14 Marks)

**Maekawa’s Algorithm** (Quorum-based Mutual Exclusion – Module 3)

Maekawa’s algorithm was the first quorum-based mutual exclusion algorithm. It reduces message complexity by requesting permission from only a subset (quorum) of sites instead of all sites.

**Key Ideas**:

- Each site Si has a quorum Ri (a subset of sites).
- Quorums satisfy **intersection property** (any two quorums intersect) and **minimality property**.
- A site can send only **one REPLY** message at a time. It locks the sites in its quorum in exclusive mode before entering CS.
- Messages must be delivered in the order they are sent between every pair of sites.

**Algorithm Steps**:

1. **Requesting the CS**:
   - Site Si sends **REQUEST** messages to all sites in its quorum Ri.
   - Si waits until it receives **REPLY** from **every** site in Ri.

2. **Executing the CS**:
   - After getting REPLY from all sites in Ri, Si enters the CS.
   - Only one site can lock a particular site at a time.

3. **Releasing the CS**:
   - After exiting CS, Si sends **RELEASE** messages to all sites in Ri.

4. **Receiving REQUEST**:
   - When a site Sj receives a REQUEST from Si:
     - If Sj has not yet sent a REPLY to any other site, it sends REPLY to Si and locks itself for Si.
     - Otherwise, it defers the REPLY until it receives RELEASE from the current holder.

**Example**:
Suppose 7 sites with quorums of size 3 (e.g., using projective plane).

- Site S1’s quorum = {S1, S2, S3}
- Site S4’s quorum = {S1, S4, S5}  
  They intersect at S1. When both request simultaneously, S1 will serialize the requests.

**Performance**:

- Message complexity per CS execution = **3√N** (approximately)
- Much better than Lamport’s O(N) or Ricart-Agrawala’s 2(N-1)

**Advantages**: Lower message complexity.  
**Disadvantages**: Deadlock possible if quorums are not chosen carefully; requires careful quorum construction.

---

**6(b) Explain Lamport’s algorithm for mutual exclusion with an example.** (14 Marks)

**Lamport’s Algorithm** (Module 3 – Non-token based)

Lamport’s algorithm is one of the earliest distributed mutual exclusion algorithms. It is based on Lamport’s logical clocks and ensures fairness using timestamps.

**Data Structure**:

- Each site Si maintains a **request_queuei** (priority queue ordered by timestamp).

**Algorithm**:

1. **Requesting CS**:
   - Site Si increments its logical clock and assigns timestamp **TSi** to the request.
   - Sends **REQUEST(TSi, i)** to **all other sites**.
   - Enters its own request into request_queuei.

2. **Receiving REQUEST**:
   - On receiving REQUEST(TSj, j) from Sj:
     - Update local clock.
     - Add the request to request_queuei.
     - Send **REPLY** to Sj.

3. **Executing CS**:
   - Si can enter CS only when:
     - Its own request is at the **top** of request_queuei, **and**
     - It has received **REPLY** from **all other sites**.

4. **Releasing CS**:
   - Remove its request from request_queuei.
   - Send **RELEASE** to all sites that have not yet received REPLY for this request.

**Example**:
Three sites S1, S2, S3.

- S1 requests with TS=5 → sends REQUEST to S2 and S3.
- S2 requests with TS=3 → sends REQUEST to S1 and S3.  
  Because TS2 (3) < TS1 (5), S2’s request has higher priority. S1 will defer entering CS until S2 finishes.

**Properties**:

- Satisfies safety, liveness, and fairness (requests served in timestamp order).
- Message complexity: **3(N-1)** per CS execution.
- Requires FIFO channels.

**Advantages**: Simple, fair.  
**Disadvantages**: High message overhead, single point of failure not tolerated well.

---

**7(a) Explain the advantages, disadvantages and issues in distributed shared memory.** (14 Marks)

**Distributed Shared Memory (DSM)** (Module 4)

**DSM Abstraction**:  
DSM provides the illusion of a single shared address space to programmers in a distributed system. Programmers use only **read/write** primitives instead of send/receive.

**Advantages** (7 points from notes):

1. Simplifies programming (read/write instead of message passing).
2. Single address space → easier passing of complex data structures with pointers.
3. Exploits locality of reference to reduce communication.
4. Cheaper than dedicated multiprocessors (uses off-the-shelf hardware).
5. No single memory bus bottleneck.
6. Provides large virtual main memory.
7. High portability (common programming interface).

**Disadvantages**:

1. Programmers must understand and handle different **replica consistency models**.
2. Implemented using message passing underneath → overhead is at least as high as message-passing systems.
3. General DSM layer may be less efficient than application-specific message-passing code.
4. Programmer loses fine-grained control over communication.

**Main Issues in Designing DSM**:

1. **Semantics for concurrent access**: What consistency model to support (strict, sequential, causal, etc.)?
2. **Replication strategy**: Full vs partial replication? Read-replication or write-replication?
3. **Location management**: How to find remote data if not fully replicated?
4. **Minimizing communication**: Reduce number of messages and delays while maintaining consistency.

DSM trades ease of programming for some performance overhead.

---

**7(b) With a diagram, explain the different types of messages in checkpointing and rollback recovery.** (14 Marks)

**Types of Messages in Checkpointing & Rollback Recovery** (Module 4)

When a process fails and rolls back, messages can be left in inconsistent states. Five important types are:

1. **In-transit Messages**  
   Messages that have been sent but not yet received at the time of checkpoint.  
   Shown in global state as “sent but not received”.  
   Must be delivered if channels are reliable.

2. **Lost Messages**  
   Send event is recorded in the restored state, but receive event is undone due to rollback.  
   Example: Sender does not roll back beyond send, but receiver rolls back before receive.  
   Solution: Message logging and replay.

3. **Delayed Messages**  
   Messages that arrive after rollback or while the process is recovering.  
   Example: Messages m2 and m5 in the diagram.

4. **Orphan Messages**  
   Receive event is recorded, but send event is undone by rollback.  
   These are impossible in a consistent global state. They force further rollback (domino effect).

5. **Duplicate Messages**  
   Arise due to message logging and replay during recovery.

**Diagram Description** (as in Module 4 notes – Figure 13.3):

- Process lines with checkpoints (vertical bars).
- Messages labelled as normal, vanished, lost, delayed, orphan.
- Orphan message H forces Pj to roll back, creating another orphan I, forcing Pk to roll back.

Proper handling of these message types is essential for correct rollback recovery.

---

**8(a) With a diagram, explain the architecture of Google File System.** (7 Marks)

**Google File System (GFS) Architecture** (Module 5)

GFS is a scalable, fault-tolerant distributed file system designed by Google for large-scale data processing.

**Main Components**:

1. **GFS Master (Metadata Server)**:
   - Single master coordinates the cluster.
   - Maintains metadata (namespace, access control, chunk mapping).
   - Keeps operation log for recovery.
   - Communicates with chunk servers via heartbeat messages.

2. **GFS Chunk Servers**:
   - Store actual file data in fixed-size **64 MB chunks**.
   - Each chunk is replicated (default 3 replicas) on different chunk servers.
   - Serve read/write requests directly from clients.

3. **GFS Clients**:
   - Applications that read/write files.
   - Ask master for chunk locations, then communicate directly with chunk servers.

**Diagram Description** (as in notes):

- Clients → Master (for metadata)
- Clients ↔ Chunk Servers (for actual data transfer)
- Master ↔ Chunk Servers (heartbeats & metadata updates)
- Files divided into 64 MB chunks with multiple replicas.

**Key Features**: Fault tolerance through replication, reduced client-master interaction, high throughput.

---

**8(b) With a diagram, explain the architecture of Andrew File System.** (7 Marks)

**Andrew File System (AFS) Architecture** (Module 5)

AFS was developed at Carnegie Mellon University for campus-wide file sharing.

**Main Components**:

- **Vice**: Server-side component (flat file service). Runs on file servers. Stores and manages shared files.
- **Venus**: Client-side process (directory service + cache manager). Runs on every workstation.

**Architecture**:

- Workstations run **Venus** process.
- File servers run **Vice** process.
- Shared files are cached on local disks of workstations.
- Local files are handled normally by UNIX kernel.

**Diagram Description** (Figure 11 in notes):

- Multiple Workstations with Venus + User programs + UNIX kernel.
- Network connecting to multiple Servers running Vice.
- Venus communicates with Vice for shared files.
- Local files stay on workstation disk.

**Key Features**:

- Whole-file caching (fetch entire file on open).
- Callback mechanism for cache consistency.
- Provides location transparency and high scalability for campus environment.

---

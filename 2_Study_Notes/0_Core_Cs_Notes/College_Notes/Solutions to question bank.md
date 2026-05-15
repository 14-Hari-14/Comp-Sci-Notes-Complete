---
created:
topics: []
tags: []
aliases: []
purpose: ""
---

### Module 1 

**1. What do you mean by a distributed System?**

A distributed system is a collection of independent computers (or processors) that appear to the users as a single coherent computer. These computers do not share common memory or a global physical clock and communicate with each other by passing messages over a communication network. Each computer has its own local memory and runs its own operating system. The key characteristic is that the crash of a single machine does not prevent the rest of the system from continuing to work.

**2. List the characteristics of a Distributed System.**

The main characteristics of a distributed system are:
- No common physical clock
- No shared memory
- Geographical separation of nodes
- Autonomy and heterogeneity (nodes may have different speeds and run different operating systems)
- Communication through message passing
- Collection of independent entities that cooperate to solve a common problem

**3. What are the various features of distributed System?**

The important features of a distributed system are:
- No common physical clock
- No shared memory
- Geographical separation
- Autonomy and heterogeneity of processors
- Processes communicate solely by message passing
- The system continues to function even if one machine crashes
- It appears to users as a single coherent system

**4. What are the motivation / advantages of a distributed system?**

The main motivations/advantages of distributed systems are:
- Inherently distributed computations (e.g., banking transactions)
- Resource sharing
- Access to geographically remote data and resources
- Enhanced reliability (availability, fault-tolerance)
- Improved performance/cost ratio
- Scalability
- Modularity and incremental expandability

**5. Discuss about the transparency requirements of distributed system.**

Transparency hides the complexity of distribution from users. Important transparency requirements are:
- **Access transparency**: Hides differences in data representation and provides uniform access operations.
- **Location transparency**: Users need not know the physical location of resources.
- **Migration transparency**: Resources can be moved without changing their names.
- **Replication transparency**: Users are unaware of data replication.
- **Concurrency transparency**: Masks concurrent access to shared resources.
- **Failure transparency**: The system appears reliable despite failures.

**6. List the algorithmic challenges in designing a distributed system.**

Major algorithmic challenges include:
- Designing useful execution models and frameworks
- Dynamic distributed graph algorithms and routing algorithms
- Time and global state in a distributed system
- Synchronization and coordination mechanisms
- Group communication, multicast, and ordered message delivery
- Monitoring distributed events and predicates
- Distributed program design, verification, and debugging
- Data replication, consistency models, and caching

**7. List out few applications of distributed computing.**

Important applications of distributed computing are:
- Mobile systems
- Sensor networks
- Ubiquitous/Pervasive computing
- Peer-to-peer (P2P) computing
- Publish-subscribe systems and content distribution
- Distributed agents
- Distributed data mining
- Grid computing
- Distributed file systems

**8. What do you mean by a distributed program?**

A distributed program is composed of a set of *n* asynchronous processes *p₁, p₂, ..., pₙ* that run on different processors and communicate solely by passing messages over a communication network. These processes do not share a global memory and cooperate to achieve a common goal.

**9. Define causal precedence relation.**

Causal precedence relation (also called happened-before relation, denoted by →) is a partial order defined on the set of events in a distributed computation. It is defined as:
- If events *a* and *b* occur in the same process and *a* happened before *b*, then *a → b*.
- If *a* is the send event of a message and *b* is the corresponding receive event, then *a → b*.
- If *a → b* and *b → c*, then *a → c* (transitivity).

Two events are concurrent if neither *a → b* nor *b → a* holds.

**10. Compare and contrast physical & logical concurrency.**

- **Physical Concurrency**: Refers to actual simultaneous execution of processes on different processors at the same wall-clock time.
- **Logical Concurrency**: Refers to the interleaving of events from different processes in a distributed computation, even if they do not execute at exactly the same physical time.

**Contrast**: Physical concurrency depends on real-time clocks and hardware parallelism, while logical concurrency is defined using the happened-before relation and is independent of physical clocks. In distributed systems, we mostly deal with logical concurrency because there is no global physical clock.

**11. What do you mean by load balancing in a distributed environment?**

Load balancing is the process of distributing workload (tasks or data) across multiple nodes in a distributed system so that no single node becomes overloaded while others remain idle. The goal is to improve throughput and reduce user-perceived latency. It can be achieved through data migration, computation migration, or distributed scheduling.

---

### Answers from Model Question Paper (3 marks each)

**1. Identify any three distributed applications and for each application, determine which all motivating factors are important for building an application over a distributed system.**

- **Banking System (Money Transfer)**: Inherently distributed computations + Resource sharing + Enhanced reliability.
- **Sensor Networks**: Geographical separation + Scalability + Access to remote data.
- **Peer-to-Peer File Sharing**: Resource sharing + Scalability + Fault tolerance.

**2. Assume that the surface of the past cone forms a consistent cut. Does it mean that all events on the surface of the past cone are always concurrent? Demonstrate with the help of an example.**

No. Even if the surface of the past cone forms a consistent cut, events on that surface are **not necessarily concurrent**.  

**Example**: Consider two events *e1* and *e2* on the surface of the past cone. If there is a causal path from *e1* to *e2* through some other events (even if not directly visible on the surface), then *e1 → e2*, so they are **not concurrent**. A consistent cut only guarantees that no message crosses backward; it does not guarantee that all events on the cut are incomparable.

**3. Specify the issues in recording global state.**

The two main issues in recording a global state are:
1. **How to distinguish messages** that should be included in the snapshot from those that should not (i.e., separating past and future messages).
2. **Determining the exact instant** when each process should record its local state, because there is no global clock and processes run asynchronously.

---

### Module 2 

**1. Define Logical Clock.**

A logical clock is a mechanism used in distributed systems to assign timestamps to events so that the causal precedence (happened-before) relation can be captured. It provides an ordering among events without using a common physical clock. If event *a* causally precedes event *b* (denoted *a → b*), then the logical timestamp of *a* is less than that of *b*.

**2. Define scalar time. Explain the rules to update scalar clock.**

Scalar time is a simple logical clock system proposed by Lamport in which each process maintains a single integer variable called the scalar clock.  

**Update Rules:**
- **Rule R1**: Before executing an internal event or sending a message, increment the scalar clock by 1.
- **Rule R2**: On receiving a message with timestamp *Tm*, set the scalar clock to *max(current clock, Tm) + 1*.

**3. What are the basic properties of scalar time?**

The basic properties of scalar time are:
1. **Consistency**: If event *a → b*, then scalar timestamp of *a* is less than that of *b*.
2. **Total Ordering**: Events can be totally ordered by using the pair *(timestamp, process ID)* as a tie-breaker.
3. **Event Counting**: The scalar clock value represents the number of events executed so far.
4. **Not Strongly Consistent**: Two concurrent events may receive the same timestamp.

**4. Define Vector Time.**

Vector time is a logical clock system in which each process *pᵢ* maintains an *n*-dimensional vector *Vᵢ* (where *n* is the number of processes). Each component of the vector represents the number of events known to have occurred at a particular process. Vector time provides strong consistency and can exactly capture the causal precedence relation.

**5. What are the basic properties of Vector time?**

The important properties of vector time are:
1. **Isomorphism**: The partial order defined by vector timestamps is isomorphic to the happened-before relation.
2. **Strong Consistency**: For any two events *e* and *f*, *e → f* if and only if *V(e) ≤ V(f)* component-wise and *V(e) ≠ V(f)*.
3. **Event Counting**: The *k*-th component of the vector counts the exact number of events that occurred at process *pₖ*.

**6. What are the applications of vector time?**

Vector time is used in:
- Distributed debugging
- Causal message ordering
- Causal distributed shared memory
- Establishing global breakpoints
- Checking consistency of checkpoints in optimistic recovery

**7. What do you mean by a leader election algorithm?**

A leader election algorithm is a distributed algorithm that enables a group of processes to collectively select a unique process as the coordinator (leader) to perform a special role. The algorithm must satisfy **safety** (exactly one leader is elected) and **liveness** (election eventually terminates). It is required when the current coordinator fails or a new coordinator is needed.

**8. What do you mean by a consistent Global State?**

A consistent global state is a collection of local states of all processes and the states of communication channels such that for every message, if the receive event is included in the global state, then the corresponding send event must also be included. Graphically, it corresponds to a consistent cut in the space-time diagram where no message arrow crosses the cut from the future to the past.

**9. What do you mean by Termination Detection?**

Termination detection is the problem of determining whether a distributed computation has terminated, i.e., all processes have become idle and there are no messages in transit anywhere in the system. It is important because results can be used only after the computation has truly ended.

**10. In bully algorithm if the highest node is assigned as coordinator and that site is unreachable then an election is conducted and a new coordinator is assigned. What happens when that highest node comes back online?**

When the highest ID node (original coordinator) comes back online, it initiates a new election by sending Election messages to all processes with higher IDs (there are none). Since no one responds, it declares itself as the new coordinator and sends Coordinator messages to all other processes, thereby taking over the leadership again.

---

### Answers from Model Question Paper

**1. Define logical clock and explain the implementation of the logical clock.**

A logical clock is a software mechanism that assigns timestamps to events in a distributed system to capture the causal precedence (happened-before) relation without using a shared physical clock.

**Implementation**:
- Each process maintains a local data structure (scalar or vector) representing logical time.
- Two issues are addressed:
  1. Local data structure to represent time.
  2. Protocol (set of rules) to update the data structure on internal events, send events, and receive events so that the consistency condition (*if a → b then C(a) < C(b)*) is satisfied.

**2. Specify the issues in recording a global state?**

The two main issues in recording a global state are:
1. How to distinguish messages that belong to the snapshot (past) from those that do not (future).
2. Determining the exact instant at which each process should record its local state, since there is no global clock and processes execute asynchronously.

**3. Explain the rules used to update clocks in scalar time representation.**

In scalar time representation:
- **Rule R1**: Before executing an internal event or a send event, the process increments its scalar clock by 1.
- **Rule R2**: When a process receives a message with timestamp *Tm*, it sets its scalar clock to *max(own clock, Tm) + 1*.

These rules ensure the consistency property of scalar time.


---

### Module 3 – 3 Mark Answers

**1. What do you mean by mutual exclusion in a distributed environment?**

Mutual exclusion in a distributed environment is a mechanism that ensures only one process executes its critical section (CS) at any given time, even though the processes are running on different sites with no shared memory. It serializes concurrent access to a shared resource or data so that the execution appears atomic.

**2. Discuss about various approaches for implementing distributed mutual exclusion.**

There are three basic approaches for implementing distributed mutual exclusion:

- **Token-based Approach**: A unique token circulates among the sites. Only the site holding the token is allowed to enter the critical section.
- **Non-token-based Approach**: Processes exchange multiple rounds of REQUEST and REPLY messages. A site enters the CS when a local assertion (usually based on timestamps) becomes true.
- **Quorum-based Approach**: A site requests permission from only a subset of sites (called a quorum) instead of all sites. Quorums are designed such that any two quorums intersect, ensuring mutual exclusion.

**3. What are the requirements of mutual exclusion algorithms?**

A good mutual exclusion algorithm must satisfy three requirements:
1. **Safety**: At any instant, only one process is allowed to execute the critical section.
2. **Liveness**: There should be no deadlock or starvation. Every requesting process must eventually get a chance to enter the CS.
3. **Fairness**: Requests should be granted in the order of their arrival in the system (usually based on timestamps).

**4. What are the performance evaluation metrics of a mutual exclusion algorithm?**

The performance of a mutual exclusion algorithm is measured using these four metrics:
- **Message Complexity**: Number of messages exchanged per critical section execution.
- **Synchronization Delay**: Time taken between one process leaving the CS and the next process entering the CS.
- **Response Time**: Time interval from when a process sends its request until it finishes executing the CS.
- **Throughput**: Rate at which the system can execute critical section requests.

**5. List out the strategies for handling deadlocks in a distributed environment.**

The three main strategies for handling deadlocks in distributed systems are:
1. **Deadlock Prevention**: Design the system so that deadlock can never occur (e.g., acquire all resources at once).
2. **Deadlock Avoidance**: Grant a resource only if the resulting global state is safe.
3. **Deadlock Detection and Resolution**: Allow deadlocks to occur, detect them using Wait-For Graph, and resolve by aborting one or more processes.

**6. Discuss the issues in deadlock detection.**

The main issues in deadlock detection in distributed systems are:
1. **Maintenance of Wait-For Graph (WFG)**: Since there is no shared memory, maintaining a consistent and up-to-date global WFG is difficult.
2. **Searching for Cycles**: Detecting cycles or knots in the distributed WFG is complex due to message delays and lack of global view.
3. **Correctness**: The algorithm must satisfy **Progress** (detect all real deadlocks) and **Safety** (no false/phantom deadlocks).

**7. Describe how quorum-based mutual exclusion algorithms differ from the other categories of mutual exclusion algorithms.**

Quorum-based algorithms differ in two major ways:
- A site requests permission from only a **subset** of sites (its quorum) instead of all sites (as in Lamport and Ricart-Agrawala).
- Each site can send only **one REPLY** at a time and must receive a RELEASE before sending another REPLY (it locks itself for one requester).

This significantly reduces message complexity compared to non-token-based algorithms that require O(N) messages.

**8. Calculate the rate at which a system can execute the critical section requests if the synchronization delay and average critical section execution times are 3 and 1 second respectively.**

Given:  
Synchronization delay = 3 seconds  
Average CS execution time = 1 second  

Rate of CS execution (System throughput) = 1 / (Synchronization Delay + Avg. CS execution time)  
= 1 / (3 + 1)  
= **1/4** = **0.25** requests per second.

---

### Answers from Model Question Paper

**1. What are the requirements of mutual exclusion algorithms?**

A mutual exclusion algorithm must satisfy the following three requirements:  
1. **Safety**: Only one process executes the critical section at any time.  
2. **Liveness**: No deadlock and no starvation; every requesting process eventually enters the CS.  
3. **Fairness**: Requests are served in the order of their arrival (timestamp order).

**2. Describe how quorum-based mutual exclusion algorithms differ from the other categories of mutual exclusion algorithms.**

Quorum-based algorithms differ from token-based and non-token-based algorithms in two important ways:  
- Instead of requesting permission from **all** sites, a process requests permission only from a **subset** of sites called its quorum.  
- A site can grant only **one REPLY** at a time and must receive a RELEASE message before granting permission to another process (exclusive locking).  

Due to the intersection property of quorums, mutual exclusion is guaranteed with significantly fewer messages.

**3. Explain with example, how wait-for-graphs can be used in deadlock detection.**

In distributed systems, the Wait-For Graph (WFG) is a directed graph where nodes represent processes and a directed edge from Pi to Pj means “Pi is blocked waiting for a resource held by Pj”.  

A system is in deadlock if and only if there exists a **cycle** in the WFG.  

**Example**:  
If P1 waits for resource held by P2, P2 waits for resource held by P3, and P3 waits for resource held by P1, then the WFG has a cycle P1 → P2 → P3 → P1, indicating a deadlock.

---

### Module 4 

**1. Explain the advantages of shared memory.**  
*(Note: This refers to Distributed Shared Memory – DSM)*

The main advantages of Distributed Shared Memory (DSM) are:
- It provides a simple read/write interface, making programming easier compared to explicit message passing.
- It offers a single address space, which simplifies passing complex data structures and pointers.
- It exploits locality of reference, reducing communication overhead.
- It is cheaper than dedicated multiprocessor systems as it uses commodity hardware.
- It provides a large virtual shared memory and improves program portability.

**2. Explain the disadvantages of shared memory.**

The disadvantages of Distributed Shared Memory (DSM) are:
- Programmers must understand and handle different replica consistency models.
- The implementation overhead is at least as high as message-passing systems, and sometimes higher due to generality.
- Programmers lose fine-grained control over communication because the DSM layer handles everything.
- DSM may be less efficient than a carefully hand-tuned message-passing implementation for specific applications.

**3. What is a checkpoint?**

A checkpoint is a snapshot of the state of a process (or the entire system) saved on stable storage during failure-free execution. It contains the current values of variables, program counter, and other necessary information. In case of a failure, the process can rollback to this saved state and resume execution, thereby reducing the amount of lost work.

**4. What is roll back propagation?**

Rollback propagation is the phenomenon in which the rollback of one failed process forces other non-failed processes to also roll back. This happens due to inter-process dependencies created by message passing. If a process rolls back to a state before sending a message, the receiver of that message may also need to roll back, potentially causing a chain of rollbacks.

**5. Explain domino effect with an example.**

The domino effect is an uncontrolled cascading rollback in which the failure of one process causes a chain reaction of rollbacks across multiple processes, possibly forcing the entire system to roll back to the initial state.

**Example**:  
Suppose P1 sends message m to P2, and P2 sends message n to P3. If P1 fails and rolls back to a state before sending m, then P2 must roll back (to undo receipt of m), which in turn forces P3 to roll back (to undo receipt of n). This cascading rollback is called the domino effect.

**6. What is global checkpoint and consistent system state?**

A **global checkpoint** is a set of local checkpoints, one taken from each process in the system.  

A **consistent system state** (or consistent global state) is a global checkpoint in which, for every message, if the receive event is recorded in a process’s state, then the corresponding send event must also be recorded. In other words, there should be no orphan messages. It represents a state that could have occurred in a failure-free execution.

---

### Answers from Model Question Paper

**1. Illustrate the detailed abstraction of distributed shared memory and interaction with application processes.**

Distributed Shared Memory (DSM) provides the abstraction of a single monolithic shared memory to the programmer, even though the memory is physically distributed across multiple nodes.  

A part of each computer’s local memory is earmarked as shared space, while the rest remains private. The DSM layer (memory mapping management) handles all read and write operations. When an application process performs a read or write on a shared variable, the DSM system transparently manages data location, replication, consistency, and communication over the network. The programmer uses only normal read/write primitives and does not deal with send/receive messages or explicit synchronization.

**2. List any three advantages of using distributed shared memory.**

Three advantages of Distributed Shared Memory (DSM) are:
1. It simplifies programming by providing a familiar read/write interface instead of complex message passing.
2. It provides a single address space, making it easy to pass complex data structures and pointers.
3. It is cheaper than dedicated multiprocessor systems and offers a large virtual shared memory.

**3. Define the no-orphans consistency condition.**

The no-orphans consistency condition states that no process should depend on a non-deterministic event (such as message receipt) whose determinant has not been logged on stable storage or made available locally to that process. In other words, if a process’s state depends on an event *e* (according to the happened-before relation), then the determinant of *e* must either be stable or available in the volatile memory of that process.

**4. Differentiate consistent and inconsistent states with examples.**

- **Consistent State**: A global state is consistent if, for every message, the receive event is recorded only if the corresponding send event is also recorded.  
  **Example**: In a space-time diagram, if message m is shown as received by P2, then P1 must also show that it has sent m.

- **Inconsistent State**: A state is inconsistent if a message receive is recorded but the corresponding send is not.  
  **Example**: P2 has recorded the receipt of message m, but P1’s state shows that it never sent m (e.g., P1 rolled back before sending m). This is called an orphan message and cannot occur in any correct failure-free execution.

---
### Module 5 – 3 Mark Answers

**1. Explain the different types of failure models.**

There are two main failure models in distributed systems:

- **Crash Failure (Crash-Stop Model)**: A process stops executing permanently after failure. It does not send any more messages and does not behave maliciously. This is the simpler and most commonly assumed model.

- **Byzantine Failure (Arbitrary Failure)**: A faulty process can behave arbitrarily — it may send wrong messages, lie, or collude with other faulty processes. This is the most severe failure model and is much harder to handle.

**2. Explain Byzantine agreement problem.**

The Byzantine agreement problem is a consensus problem in the presence of **Byzantine failures**. In this problem, a set of processes (some of which may be faulty and behave maliciously) must agree on a common value. The faulty processes can send conflicting or arbitrary messages to different processes. The goal is to ensure that all **correct (non-faulty)** processes agree on the same value, even if up to *f* processes are Byzantine faulty (typically requiring *n > 3f* processes).

**3. Explain consensus problem.**

The consensus problem requires a group of processes to agree on a single common value (decision) proposed by one or more processes. It must satisfy three properties:
- **Agreement**: All correct processes decide on the same value.
- **Validity**: The decided value must be one of the values proposed by some process.
- **Termination**: Every correct process eventually decides.

Consensus is fundamental for leader election, atomic commit, and replicated state machines.

**4. Explain interactive consistency problem.**

The interactive consistency problem (also called the Byzantine Generals Problem with multiple values) requires that every correct process obtains the **same vector** of values, where the *i*-th entry of the vector is the value proposed by process *pᵢ*. Even if some processes are Byzantine faulty, all correct processes must agree on the entire vector. It is a stronger form of agreement than simple consensus.

---

### Answers from Model Question Paper

**1. Explain how consensus problem differs from the Byzantine agreement problem.**

- **Consensus Problem**: Assumes only **crash failures** (processes may stop but do not lie). The goal is to agree on a single value.
- **Byzantine Agreement Problem**: Assumes **Byzantine (arbitrary) failures**, where faulty processes can send conflicting or malicious messages. It is much harder because faulty processes can actively try to prevent agreement or cause different correct processes to decide differently.

In short, Byzantine agreement is a more difficult version of consensus that tolerates malicious behavior.

**2. Define Byzantine agreement problem.**

The Byzantine agreement problem is a variant of the consensus problem in which some processes may be **Byzantine faulty** (they can behave arbitrarily and send conflicting messages). The requirement is that all **correct (non-faulty)** processes must agree on the same common value, despite the presence of up to *f* faulty processes (typically requiring *n > 3f* total processes).

**3. Differentiate between whole file serving and whole file caching in Andrew file system.**

| Feature                    | Whole File Serving                          | Whole File Caching (AFS)                       |
|---------------------------|---------------------------------------------|------------------------------------------------|
| Transfer Mechanism        | Server sends the entire file on every request | Client caches the entire file locally after first access |
| Subsequent Access         | Requires network transfer every time        | Served from local cache (fast)                 |
| Consistency               | Server validates on every open              | Uses callback mechanism from server            |
| Performance               | Moderate                                    | Excellent for read-heavy workloads             |
| Scalability               | Lower                                       | Higher                                         |

In AFS, whole file caching significantly improves performance for files that are read frequently after initial access.




---

### Module 1 – 7 Mark Answers

**1. Relate a computer system with a distributed system with the aid of neat sketches.**

A single computer system has a **centralized architecture** with one processor, shared memory, and a common clock. All components are tightly coupled.

In contrast, a **distributed system** consists of multiple independent computers (nodes) connected by a network. Each node has its own processor, local memory, and local clock. There is **no shared memory** and **no global physical clock**. Nodes communicate only by passing messages.

**Sketch Description** (Draw in exam):

- **Single Computer System**: One box with CPU + Memory + I/O, all connected internally.
- **Distributed System**: Multiple boxes (nodes) connected through a network cloud. Each box has its own CPU and Memory. Arrows between boxes labeled “Message Passing”.

**Key Difference**: In a distributed system, the crash of one node does not stop the entire system, whereas in a single computer, failure of the CPU halts everything.

**2. Discuss about various Primitives for distributed communication.**

Distributed communication primitives are of two types: **Message Passing** and **Shared Memory** (though shared memory is emulated in DSM).

**Main Message Passing Primitives**:
- **Send** and **Receive**

**Classification**:
- **Synchronous vs Asynchronous**:
  - Synchronous: Sender and receiver synchronize (handshake). Sender waits until receiver receives the message.
  - Asynchronous: Sender continues after sending (data copied to buffer).

- **Blocking vs Non-blocking**:
  - Blocking Send: Sender waits until message is received and acknowledged.
  - Non-blocking Send: Sender continues immediately after initiating send.
  - Blocking Receive: Receiver waits until a message arrives.
  - Non-blocking Receive: Receiver checks or continues even if no message.

**Buffered vs Unbuffered**:
- Buffered: Data is copied to a system buffer.
- Unbuffered: Sender waits for receiver to be ready.

These primitives are implemented using **RPC** or **Message-Oriented Communication** in practice.

**3. Explain in detail about the design issues of a distributed System.**

The major design issues in distributed systems are:

1. **Communication**: Choosing between RPC, message passing, or stream-oriented communication.
2. **Processes**: Management of processes/threads, code migration, and mobile agents.
3. **Naming**: Designing scalable naming schemes for resources and processes (location transparency).
4. **Synchronization**: Handling mutual exclusion, clock synchronization, and logical clocks.
5. **Data Storage and Access**: Efficient distributed file systems and data placement.
6. **Consistency and Replication**: Maintaining consistency among replicas while improving performance.
7. **Fault Tolerance**: Handling node/link failures, checkpointing, and recovery.
8. **Security**: Authentication, authorization, cryptography, and secure group management.
9. **Transparency**: Hiding distribution details (access, location, failure, replication, etc.).
10. **Scalability and Modularity**: Designing algorithms that scale with system size.

**4. Explain the algorithmic challenges of designing a distributed system.**

Algorithmic challenges in distributed systems include:

- Designing proper execution models (interleaving vs partial order model).
- Dynamic distributed graph algorithms and routing in changing topologies.
- Handling time and global state (logical clocks, snapshot algorithms).
- Synchronization and coordination mechanisms (mutual exclusion, leader election).
- Group communication, multicast, and ordered message delivery.
- Monitoring distributed events and predicates for debugging.
- Distributed program design, verification, and debugging tools.
- Data replication, consistency models, and caching strategies.

These challenges arise due to lack of global clock, no shared memory, and unpredictable message delays.

**5. Explain the applications of distributed computing.**

Distributed computing is used in many modern systems:

- **Mobile Systems**: Wireless communication, routing, location management.
- **Sensor Networks**: Monitoring physical parameters (temperature, humidity) using many small nodes.
- **Ubiquitous/Pervasive Computing**: Smart homes, smart offices.
- **Peer-to-Peer (P2P) Computing**: Decentralized file sharing (e.g., BitTorrent).
- **Publish-Subscribe Systems**: Content distribution and multimedia streaming.
- **Distributed Agents**: Autonomous agents that collaborate.
- **Distributed Data Mining**: Mining data spread across multiple sites.
- **Grid Computing**: Utilizing idle CPU cycles across networked machines.
- **Distributed File Systems**: NFS, AFS, GFS.

**6. Explain in detail about the models of distributed execution.**

A distributed execution consists of events at different processes. There are two main models:

1. **Interleaving Model**: Assumes a global total order of all events. All events are serialized as if executed on a single processor. Useful for reasoning but does not reflect true concurrency.

2. **Partial Order Model**: Based on Lamport’s **happened-before** relation (→). Events are partially ordered:
   - Events in same process are ordered.
   - Send event precedes corresponding receive event.
   - Transitivity applies.

This model better captures true concurrency and causality in distributed systems. It is widely used for designing algorithms and debugging.

**7. Explain the models of communication networks.**

The common models of communication networks in distributed systems are:

1. **FIFO Channels**: Messages between two processes are delivered in the order they were sent.

2. **Non-FIFO Channels**: Messages may be delivered out of order.

3. **Reliable vs Unreliable Channels**:
   - Reliable: Messages are eventually delivered (no loss).
   - Unreliable: Messages may be lost, duplicated, or corrupted.

Most algorithms assume **reliable FIFO channels** for simplicity, while some (like Chandy-Lamport) explicitly use FIFO property for marker separation.

**8. Discuss about the global state of distributed system.**

The **global state** of a distributed system is the collection of:
- Local states of all processes, and
- States of all communication channels (messages in transit).

Recording a global state is non-trivial because:
- There is no global clock.
- Message delays are unpredictable.

A **consistent global state** is one in which, for every message, if the receive is recorded, the send must also be recorded (no orphan messages). It corresponds to a **consistent cut** in the space-time diagram.

Global states are used for checkpointing, deadlock detection, and termination detection.

**9. Explain past cone and future cone of events in cuts of distributed computations.**

In a space-time diagram of a distributed computation:

- **Past Cone of an Event**: All events that causally precede (can affect) the given event. It includes all ancestors in the happened-before relation.

- **Future Cone of an Event**: All events that are causally affected by the given event (descendants).

A **cut** is a line dividing the diagram into past and future. A **consistent cut** has no message crossing from future to past. The past cone helps in reasoning about what could have influenced an event, while the future cone shows its impact.

---

### Model QP Answers

**1. Explain the three different models of the service provided by communication networks.**

The three models are:
1. **Message-Oriented Communication**: Discrete messages are sent (used in most distributed algorithms).
2. **Stream-Oriented Communication**: Continuous flow of data (used in multimedia, video streaming).
3. **Remote Procedure Call (RPC)**: Makes remote calls appear like local procedure calls (hides distribution).

**2. Explain how the causal dependency between events in distributed execution is defined using Lamport’s happened before relationship.**

Lamport’s happened-before (→) defines causal dependency as:
- If *a* and *b* are in the same process and *a* occurred before *b*, then *a → b*.
- If *a* is send of message *m* and *b* is receive of *m*, then *a → b*.
- Transitivity: If *a → b* and *b → c*, then *a → c*.

Two events are concurrent if neither *a → b* nor *b → a* holds. This relation captures true causality without physical clocks.

**3. Address the various strategies that can be adopted to satisfy the requirements of a reliable and fault tolerant distributed system.**

Strategies include:
- **Replication**: Data and services replicated across nodes.
- **Checkpointing and Rollback Recovery**: Periodic state saving and recovery.
- **Redundancy**: Multiple paths, backup servers.
- **Failure Detection and Masking**: Heartbeats, timeouts, and graceful degradation.
- **Consensus Algorithms**: Paxos/Raft for agreement despite failures.
- **Fault-Tolerant Design**: Byzantine fault tolerance for malicious failures.

**4. Which are the different versions of send and receive primitives for distributed communication? Explain.**

The primitives are classified as:

- **Synchronous vs Asynchronous**: Synchronous waits for handshake; asynchronous returns immediately.
- **Blocking vs Non-blocking**: Blocking waits for completion; non-blocking returns control immediately.
- **Buffered vs Unbuffered**: Buffered copies data to system buffer; unbuffered requires receiver readiness.

These variations trade off simplicity, performance, and reliability.

---

### MODULE 2 – 7/14 Mark Answers

**1. Discuss the implementation of logical Clock. Discuss about various Primitives for distributed communication.**

**Implementation of Logical Clock**:
A logical clock is implemented by maintaining a local data structure at each process and a set of rules to update it.  
- **Data Structure**: Scalar clock (single integer) or Vector clock (n-dimensional vector).  
- **Rules**: On internal/send events, increment the clock. On receive events, update the clock based on the incoming timestamp so that if *a → b*, then C(a) < C(b).  

This ensures the consistency condition for causal precedence.

**Primitives for Distributed Communication**:
There are two basic communication primitives:

- **Send** and **Receive**.
- **Synchronous vs Asynchronous**: Synchronous primitives block until the corresponding operation completes (handshake). Asynchronous primitives return control immediately after copying data.
- **Blocking vs Non-blocking**: Blocking primitives wait until the operation finishes. Non-blocking primitives return immediately.

**Buffered vs Unbuffered**: In buffered send, data is copied to a system buffer. In unbuffered, the sender waits until the receiver is ready.

**2. Explain Ring based election Algorithms in detail.**

**Ring-Based Election Algorithm**:

- Processes are arranged in a logical ring.
- Any process can initiate election by sending an **Election** message containing its ID to its clockwise neighbor.
- On receiving an Election message with ID *j*:
  - If *j > own ID*, forward it.
  - If *j < own ID* and not yet a participant, replace *j* with own ID and forward.
  - If the message returns with its own ID, the process becomes the **coordinator** and sends an **Elected** message around the ring.

**Properties**: It satisfies safety (exactly one coordinator) and liveness (election terminates).  
**Message Complexity**: 2N messages in the worst case.

**3. Explain Bully Algorithm in detail.**

**Bully Algorithm** (Highest ID wins):

- Three message types: **Election**, **Answer (OK)**, **Coordinator**.
- When a process notices the coordinator is down, it sends **Election** messages to all processes with higher IDs.
- If no Answer is received within timeout, it declares itself coordinator and sends **Coordinator** messages to all lower ID processes.
- If a higher ID process receives Election, it sends Answer and starts its own election.
- The process with the highest ID eventually becomes the coordinator.

**Properties**: Simple but has O(N²) message complexity in worst case.

**4. In a ring topology 7 processes... Calculate total number of election messages and coordinator messages.**

**Given Ring**: P20 → P5 → P10 → P18 → P3 → P16 → P9  
P10 initiates election.

**Step-by-step**:
- Election message starts with 10, travels around the ring, and gets updated to the highest ID seen (20).
- It takes **12 election messages** to complete one full circulation and elect the coordinator (P20).
- Then **6 coordinator (Elected) messages** are sent to inform all processes.

**Total**:  
- Election messages = **12**  
- Coordinator messages = **6**

**5. Pid’s 0,4,2,1,5,6,3,7, P7 was the initial coordinator... Illustrate Bully algorithm...**

P7 (highest ID) crashed. P4 initiates election.

**Steps**:
- P4 sends Election to higher IDs: 5,6,7 (but 7 is down).
- P5 and P6 reply with Answer and start their own elections.
- Eventually, P6 (highest alive) becomes coordinator.

**Message Count**:
- Election messages = **6**
- Coordinator messages = **6**

**6. Explain in detail about Global state and snapshot recording algorithms.**

A global state is the collection of local states of all processes and the states of all communication channels.  

**Snapshot Recording** is difficult because:
- No global clock.
- Messages have unpredictable delays.

**Consistent Global State**: No orphan messages (if receive is recorded, send must also be recorded). It corresponds to a consistent cut in the space-time diagram.

**Issues**:
1. Distinguishing past and future messages.
2. Deciding when each process should take its local snapshot.

**7. Discuss in detail about Chandy Lamport algorithm.**

**Chandy-Lamport Snapshot Algorithm** (for FIFO channels):

- Uses a special **Marker** message.
- Initiator records its local state and sends Marker on all outgoing channels.
- On receiving first Marker: Record local state, record incoming channel as empty, send Markers on all outgoing channels.
- On receiving subsequent Markers: Record the state of that channel (messages received after local snapshot but before Marker).

**Termination**: When a process has received Markers on all incoming channels.  
The collected local snapshots form a **consistent global snapshot**.

**8. Explain Termination detection using distributed snapshots.**

Termination detection using snapshots works because termination is a **stable property**.  

When a process becomes idle, it initiates a snapshot request. If the collected consistent snapshot shows:
- All processes are idle, and  
- No messages are in transit,  

then the computation has terminated. The algorithm uses logical ordering of idle events so that only the request from the **last** process to become idle succeeds.

**9. Discuss the method of Termination detection by weight throwing in detail.**

In **Weight Throwing** method:
- A controlling agent starts with weight = 1.
- Every active process and every message in transit carries a positive fraction of weight (total weight always = 1).
- When a process sends a message, it splits its weight and attaches part to the message.
- When a process becomes idle, it sends its entire current weight back to the controlling agent.
- When the controlling agent’s weight becomes **1** again, it declares termination (all processes idle + no messages in transit).

**10. Discuss in Detail about spanning-tree-based termination detection algorithm.**

**Spanning-Tree-based Termination Detection**:
- A fixed spanning tree with root P0 is used.
- Leaf nodes start with tokens.
- A leaf sends its token to parent only after it becomes idle.
- An internal node sends token to its parent only after it is idle **and** has received tokens from all children.
- Root declares termination when it is idle and has received tokens from all children.

**With Black/White Coloring** (to avoid false termination):
- Process turns **Black** when it sends a message.
- Sends **Black token** if it was black when terminating, then turns white again.
- Root declares termination only on receiving all **White tokens**.

---

### Model QP Answers (7 marks)

**1. Apply ring-based leader election algorithm with 10 processes in the worst-performing case. Count the number of messages needed.**

In the worst case (lowest ID process initiates), the election message travels the full ring once, getting updated at each step.  
For 10 processes, it takes **2 × 10 = 20 messages** (10 for election circulation + 10 for elected message circulation).

**2. Apply spanning tree-based termination detection algorithm... (with diagram description)**

(Describe the tree with root 0, children 1 and 2, etc., tokens moving upward from leaves. Mention black/white coloring if needed. Root declares termination only after receiving tokens from all children and itself being idle.)

**3. Illustrate bully algorithm... Does it meet liveness and safety?**

(Refer to earlier Bully explanation).  
Yes, it satisfies **Safety** (exactly one coordinator – the highest ID) and **Liveness** (election eventually terminates).

**4. Clearly mentioning assumptions, explain the rules of termination detection using distributed snapshots.**

Assumptions: Reliable channels, asynchronous communication.  
Rules: When a process becomes idle, it sends snapshot requests with logical timestamps. A process grants a request only if it is the most recent one seen and the process is idle. Only the request from the **last** idle process gets granted by everyone, forming a consistent snapshot. If the snapshot shows all idle + no messages, termination is declared.

**5. In Chandy-Lamport algorithm... Can multiple processes initiate concurrently?**

Yes, multiple processes can initiate concurrently. Each initiator starts its own marker wave. The algorithm still produces consistent snapshots because markers cleanly separate past and future messages on FIFO channels. The recorded local snapshots from each wave can be combined to form consistent global snapshots.

**6. Illustrate the working of spanning tree-based termination detection algorithm.**

(Describe token propagation from leaves to root. Mention that root declares termination only when idle and all children have sent tokens. Use black/white coloring to handle late messages.)


---

### Module 3 – 7 Mark Answers

**1. Explain Lamport’s algorithm for mutual exclusion.**

Lamport’s algorithm is a non-token-based mutual exclusion algorithm that uses logical clocks to ensure fairness.

**Algorithm:**

Each site maintains:
- A logical clock.
- A priority queue `request_queue` ordered by timestamp (lower timestamp = higher priority).

**When a process wants to enter CS:**
- Increment its logical clock.
- Broadcast `REQUEST(ts, i)` to all other sites.
- Add its own request to its `request_queue`.
- Wait until two conditions are satisfied:
  1. It has received REPLY from **all** other sites.
  2. Its own request is at the **top** of its `request_queue`.

**When a site receives REQUEST(ts, k):**
- Update its logical clock: `C = max(C, ts) + 1`
- Insert the request into its queue.
- Send REPLY immediately to the sender.

**When a process exits CS:**
- Remove its request from the queue.

**Correctness:**
- **Safety**: Only the process with the highest priority (lowest timestamp) can enter CS.
- **Fairness**: Requests are served in timestamp order.
- **Message Complexity**: 3(N-1) messages per CS execution.

**2. Explain Ricart–Agrawala algorithm.**

Ricart-Agrawala algorithm is an optimized non-token-based mutual exclusion algorithm that improves upon Lamport’s algorithm by reducing message overhead.

**Algorithm:**

Each process maintains a logical clock and a request-deferred array `RD[1..N]`.

**To enter CS:**
- Increment logical clock and broadcast `REQUEST(ts, i)` to all other processes.
- Wait until it receives REPLY from **all** other processes.

**On receiving REQUEST(ts, k) from process k:**
- Update logical clock.
- If the receiver is **not** requesting or executing CS, or if its own request has **higher priority** (lower timestamp) than the incoming request → send REPLY immediately.
- Otherwise, defer the reply by setting `RD[k] = 1`.

**On exiting CS:**
- For every process k where `RD[k] == 1`, send REPLY and reset `RD[k] = 0`.

**Advantages**: Message complexity is reduced to **2(N-1)** messages per CS execution.  
**Correctness**: Safety and liveness are guaranteed by timestamp-based priority.

**3. Explain Quorum-based mutual exclusion algorithms. / Explain Maekawa’s algorithm for mutual exclusion.**

**Quorum-based Mutual Exclusion**:  
In quorum-based algorithms, a process does not request permission from all sites but only from a **subset** of sites called its **quorum**. Quorums are constructed such that any two quorums have at least one common site (intersection property). This significantly reduces message complexity.

**Maekawa’s Algorithm (First Quorum-based Algorithm):**

- Each site Si has its own quorum Ri.
- To enter CS, Si sends REQUEST to all sites in its quorum Ri.
- It waits for REPLY from **every** site in Ri.
- A site can send only **one REPLY** at a time. It must receive a RELEASE from the previous requester before sending REPLY to another.

**Message Types**:
- REQUEST
- REPLY
- RELEASE

**How it handles deadlocks**:  
Because of the intersection property, at most one quorum can be granted permission at any time, preventing deadlock. If two sites request simultaneously, the common site in both quorums will grant permission to only one, forcing the other to wait.

**Message Complexity**: Approximately 3√N to 5√N messages (much better than O(N)).

**4. Illustrate Suzuki–Kasami’s broadcast algorithm.**

Suzuki-Kasami is a token-based mutual exclusion algorithm.

**Algorithm**:

- There is only **one unique token** in the system.
- The token contains:
  - `token_array[1..N]`: sequence numbers of the latest requests served for each site.
  - A queue of pending requests.

**When a site wants to enter CS:**
- If it has the token → enter CS.
- Else → broadcast `REQUEST(i, seq_i)` to **all** sites (seq_i is its sequence number).

**When a site holding the token receives a REQUEST:**
- If it is not in CS, it sends the token to the highest priority pending requester.
- If it is in CS, it queues the request and sends the token only after finishing CS.

**After exiting CS:**
- Update its entry in `token_array`.
- Send the token to the next pending requester (if any).

**Correctness**: Mutual exclusion is guaranteed because only the token holder can enter CS.  
**Message Complexity**: In worst case N messages (broadcast), but usually much lower.

**5. Explain with example, how wait-for-graphs can be used in deadlock detection.**

In distributed systems, the **Wait-For Graph (WFG)** is used for deadlock detection.

- **Nodes** represent processes.
- A directed edge **Pi → Pj** means “Pi is blocked waiting for a resource currently held by Pj”.

**Rule**: A deadlock exists if and only if there is a **cycle** in the WFG.

**Example**:
- P1 holds R1 and waits for R2 (held by P2) → edge P1 → P2
- P2 holds R2 and waits for R3 (held by P3) → edge P2 → P3
- P3 holds R3 and waits for R1 (held by P1) → edge P3 → P1

This forms a cycle P1 → P2 → P3 → P1 → indicating a deadlock.

**6. Explain / compare various models of deadlocks.**

Distributed systems support different resource request models:

1. **Single-Resource Model**: A process requests only one resource at a time. Out-degree = 1. Cycle in WFG ⇒ Deadlock.

2. **AND Model**: A process waits until **all** requested resources are granted. Cycle in WFG ⇒ Deadlock.

3. **OR Model**: A process waits until **any one** of the requested resources is granted. Cycle in WFG does **not** necessarily mean deadlock.

4. **AND-OR Model**: Requests can be arbitrary combinations of AND and OR conditions.

5. **P-out-of-Q Model**: A process needs any P resources out of Q available resources.

6. **Unrestricted Model**: No restrictions on request patterns (most general).

**Comparison**: Single-resource and AND models are easier to detect (cycle = deadlock). OR and AND-OR models are more complex because a cycle does not always imply deadlock.

**7. Explain in detail about deadlock handling strategies in a distributed environment.**

There are three strategies:

1. **Deadlock Prevention**:  
   Make deadlock impossible by design (e.g., acquire all required resources at once or impose a total ordering on resource requests). It is highly inefficient in distributed systems.

2. **Deadlock Avoidance**:  
   Before granting a resource, check whether the resulting global state is safe. Due to lack of global view and communication delays, avoidance is impractical in distributed systems.

3. **Deadlock Detection and Resolution** (Most Practical):  
   Allow deadlocks to occur. Periodically construct the Wait-For Graph and search for cycles. Once a deadlock is detected, resolve it by aborting one or more processes (victim selection) and releasing their resources.

**8. Site S1, S2, S3 … Evaluate whether the resultant is in a deadlocked condition.**

**Given**:
- S1: P17, P32, P61, P72
- S2: P33, P44, P7   (all demanding R7)
- S3: P91, P6, P23, P28  (R7 assigned to first process i.e., P91)

**Analysis**:
- All processes in S2 are waiting for R7 held by P91 in S3.
- Second process in S2 (P44) is demanding a resource held by third process in S1 (P61).

**Wait-For Graph**:
- Processes in S2 → P91 (for R7)
- P44 (S2) → P61 (S1)

There is **no cycle** in the Wait-For Graph.

**Conclusion**: The system is **NOT in a deadlocked condition**.

---

### Answers from Model Question Paper

**1. Illustrate Suzuki-Kasami’s broadcast algorithm.**  
(Refer to answer 4 above)

**2. Compare different models of deadlocks.**  
(Refer to answer 6 above)

**3. Explain and illustrate Lamport’s mutual exclusion algorithm.**  
(Refer to answer 1 above)

**4. Discuss the three types of messages required for deadlock handling in Maekawa’s algorithm. Explain how Maekawa’s algorithm handles deadlocks.**  

Maekawa’s algorithm uses three types of messages:
- **REQUEST**: Sent to all sites in the quorum to ask for permission.
- **REPLY**: Sent by a site to grant permission (a site can send only one REPLY at a time).
- **RELEASE**: Sent after exiting CS to release the lock so other requesters can get REPLY.

**How it handles deadlocks**: Due to the **intersection property** of quorums, at most one quorum can be fully granted permission at any time. The common site in overlapping quorums ensures that conflicting requests are serialized.

**5. Explain and illustrate Ricart-Agrawala algorithm for achieving mutual exclusion.**  
(Refer to answer 2 above)

**6. Explain any three different models of deadlock.**  
(Refer to answer 6 above – Single Resource, AND, and OR models)

---

### Module 4 – 7 Mark Answers

**1. Explain the different ways to avoid domino effect.**

The domino effect is an uncontrolled cascading rollback caused by inter-process message dependencies. The following techniques are used to avoid it:

1. **Coordinated Checkpointing**:  
   All processes coordinate their checkpointing activity so that the set of local checkpoints forms a globally consistent state. Since the checkpoint is consistent, there are no orphan messages, and rollback propagation is completely avoided. All processes restart from the most recent consistent checkpoint.

2. **Communication-Induced Checkpointing**:  
   Processes take checkpoints independently, but they are occasionally forced to take additional checkpoints based on information piggybacked on received messages. This ensures that a consistent global state always exists on stable storage, preventing the domino effect while preserving some autonomy.

3. **Log-based Rollback Recovery**:  
   In addition to checkpoints, non-deterministic events (especially message receipts) are logged. During recovery, the logged determinants are replayed in the original order. This allows processes to recover beyond the last checkpoint without causing cascading rollbacks, effectively avoiding the domino effect.

**2. Explain the different types of messages that occur during failure recovery.**

During rollback recovery, messages can be left in abnormal states. The different types are:

1. **In-transit Messages**: Messages that have been sent but not yet received at the time of failure. They do not cause inconsistency if included in the global state.

2. **Lost Messages**: The send event is recorded in the restored state, but the receive event has been undone due to rollback. The receiver will not get the message again unless special mechanisms (like message logging) are used.

3. **Delayed Messages**: Messages that arrive after the receiving process has rolled back. These may arrive during or after recovery.

4. **Orphan Messages**: The receive event is recorded in the restored state, but the corresponding send event has been undone. These are the most dangerous and must be avoided by ensuring consistent global states.

5. **Duplicate Messages**: These arise when logged messages are replayed during recovery, causing the same message to be delivered again.

---

### Answers from Model Question Paper

**1. Classify different log-based rollback recovery techniques.**

Log-based rollback recovery techniques are classified into three categories based on when and how determinants (information about non-deterministic events) are logged:

1. **Pessimistic Logging**:  
   The determinant of every non-deterministic event is logged to stable storage **before** the event is allowed to affect the computation. It guarantees the “always-no-orphans” condition and never creates orphan processes. It is very safe but has high runtime overhead.

2. **Optimistic Logging**:  
   Determinants are logged asynchronously to stable storage. It allows temporary creation of orphan processes during failure-free execution. These orphans are resolved during recovery using dependency information. It has lower runtime overhead but more complex recovery.

3. **Causal Logging**:  
   It combines the advantages of both pessimistic and optimistic logging. It guarantees the no-orphans condition without requiring synchronous logging to stable storage (except during output commit). It limits rollback to the most recent checkpoint and isolates processes from failures of others.

**2. What are the issues in failure recovery? Illustrate with suitable examples.**

The main issues in failure recovery are:

1. **Restoring a Consistent Global State**:  
   After a failure, the system must be restored to a consistent state (no orphan messages).  
   *Example*: If P1 rolls back before sending message m to P2, but P2 has already received m, then an orphan message is created.

2. **Handling Messages in Abnormal States**:  
   Messages can become lost, delayed, orphan, or duplicate after rollback.  
   *Example*: Message D is a **lost message** (send recorded, receive undone). Messages E and F are **delayed orphan messages** that must be discarded when they arrive.

3. **Output Commit Problem**:  
   Outputs sent to the external world before failure cannot be undone easily. The system must ensure that once an output is committed, the state from which it was sent is never rolled back.

4. **Domino Effect**: Uncontrolled cascading rollback due to message dependencies.

**3. Show that Lamport’s Bakery algorithm for shared memory mutual exclusion satisfies the three requirements of critical section problem.**

Lamport’s Bakery algorithm satisfies the three requirements as follows:

- **Mutual Exclusion (Safety)**: Processes enter the CS in increasing order of the pair `<number, pid>`. Since the comparison is done for all processes and only the process with the smallest pair proceeds, no two processes can be in the CS simultaneously.

- **Progress**: If no process is in the CS, then at least one process will have the smallest `<number, pid>` pair and will eventually enter the CS (no deadlock).

- **Bounded Waiting**: A process waits for at most (n-1) other processes to finish their CS. Once a process has chosen its number, any new process choosing a number later will have a higher number or same number but higher ID, so the waiting process will eventually enter.

Thus, the algorithm satisfies safety, progress, and bounded waiting.

**4. What is checkpoint-based rollback-recovery? Explain the three classifications of checkpoint-based rollback recovery.**

Checkpoint-based rollback recovery is a fault-tolerance technique in which processes periodically save their local states (checkpoints) on stable storage. Upon failure, processes roll back to a previous checkpoint and resume execution.

It is classified into three types:

1. **Uncoordinated Checkpointing**:  
   Each process takes checkpoints independently at its own convenience. It has low runtime overhead but suffers from the domino effect and useless checkpoints.

2. **Coordinated Checkpointing**:  
   Processes coordinate their checkpointing so that the set of local checkpoints forms a globally consistent state. It avoids the domino effect and simplifies recovery, but has higher synchronization overhead.

3. **Communication-Induced Checkpointing**:  
   Processes take checkpoints independently but are forced to take additional checkpoints based on information received in messages. It tries to avoid the domino effect while preserving some autonomy and reducing useless checkpoints.

---

### Module 5 – 7 Mark Answers

**1. Explain the two variations of Byzantine agreement problem.**

There are two important variations of the Byzantine agreement problem:

**a) Byzantine Agreement (BA) / Single Value Agreement**  
In this variation, all correct processes must agree on a **single common value**. Even if up to *f* processes are Byzantine faulty (malicious), all non-faulty processes must decide on the same value. The decided value must be valid (i.e., proposed by at least one correct process).

**b) Interactive Consistency (IC) / Vector Agreement**  
In this stronger variation, every correct process must obtain the **same vector** of values. The *i*-th entry of the vector is the value proposed by process *pᵢ*. Even if some processes are faulty and propose different values to different processes, all correct processes must agree on the **entire vector**. This is harder than simple Byzantine agreement.

Both variations require *n > 3f* processes to tolerate *f* Byzantine failures.

**2. Explain the challenges of designing distributed file system.**

Designing a distributed file system is challenging due to the following reasons:

- **Transparency**: Providing access, location, migration, replication, and failure transparency while hiding distribution details.
- **Consistency**: Maintaining consistent views of data when files are replicated and cached across multiple nodes.
- **Performance**: Achieving high throughput and low latency despite network delays and communication overhead.
- **Fault Tolerance**: Handling server crashes, network partitions, and ensuring availability.
- **Scalability**: Supporting a large number of clients and files without performance degradation.
- **Security**: Providing authentication, authorization, and protection against unauthorized access.
- **Heterogeneity**: Supporting different hardware, operating systems, and file formats.

**3. Explain the characteristics of distributed file system.**

The main characteristics of a Distributed File System are:

- **Transparency**: Users should not be aware of the distribution (access, location, replication, failure transparency).
- **Performance**: High speed for file operations and good scalability.
- **Fault Tolerance**: The system should continue working despite failures of servers or links.
- **Consistency**: Proper handling of concurrent updates and cache coherence.
- **Security**: Strong authentication and access control mechanisms.
- **Concurrent Access**: Support for multiple users accessing the same file simultaneously with proper synchronization.
- **Heterogeneity**: Ability to work across different operating systems and hardware platforms.

**4. Explain distributed file system requirements.**

The key requirements of a Distributed File System are:

- **Transparency Requirements**: Access, location, migration, replication, concurrency, and failure transparency.
- **Performance**: Low latency and high throughput for file operations.
- **Scalability**: Ability to handle increasing number of clients and data volume.
- **Fault Tolerance**: Recovery from server and network failures.
- **Consistency**: Maintaining consistent view of shared files.
- **Security**: Authentication, authorization, and data protection.
- **Concurrent File Updates**: Proper synchronization for simultaneous writes.
- **Efficiency**: Minimizing network traffic and communication overhead.

**5. Explain file service architecture in detail.**

File service architecture consists of three main components:

1. **Flat File Service**:  
   This component manages the actual contents of files. It provides operations like read, write, create, delete, and get/set attributes on files identified by unique File Identifiers (UFIDs). It deals with raw data blocks.

2. **Directory Service**:  
   This manages the naming hierarchy. It maps human-readable file names and directory paths to UFIDs. It supports operations like lookup, add name, remove name, and rename.

3. **Client Module**:  
   This runs on the client side and provides a transparent interface to applications. It hides the distribution details and interacts with flat file service and directory service using RPCs.

This layered architecture helps achieve transparency and modularity in DFS design.

**6. Explain flat file service and its interface.**

The Flat File Service is the lowest layer in file service architecture. It is responsible for managing the actual data content of files.

**Main Operations (Interface)**:
- `Read(fileID, position, length)` → returns data
- `Write(fileID, position, data)` → writes data
- `Create()` → creates a new file and returns its UFID
- `Delete(fileID)`
- `GetAttributes(fileID)` and `SetAttributes(fileID, attributes)`

It deals only with raw file content using unique File Identifiers (UFIDs) and does not handle naming or directories.

**7. Explain the architecture of Google File System (GFS).**

Google File System (GFS) is designed for large-scale data processing. Its architecture consists of:

- **Single Master Server**: Maintains all metadata (file to chunk mapping, chunk locations, access control). It does not store actual data.
- **Multiple Chunk Servers**: Store the actual file data in fixed-size chunks (usually 64 MB). Each chunk is replicated (default 3 replicas) on different chunk servers for fault tolerance.
- **Clients**: Interact with the master only for metadata. They read/write data directly from chunk servers.

GFS is optimized for sequential reads and append-heavy workloads. It uses relaxed consistency and is highly fault-tolerant using commodity hardware.

**8. Explain the architecture of Andrew File System.**

Andrew File System (AFS) has two main components:

- **Vice**: The server-side file repository. It stores files and manages the file system on servers.
- **Venus**: The client-side cache manager. It runs on every client machine and handles caching.

**Key Feature**: AFS uses **whole-file caching**. When a client opens a file, Venus fetches the entire file from Vice and caches it locally. Subsequent reads are served from the cache. For consistency, Vice uses a **callback mechanism** — it notifies clients when a cached file is modified. AFS provides excellent performance for read-heavy workloads and good scalability.

**9. Explain the architecture of Sun Network File System (NFS).**

Sun NFS follows a simple **client-server architecture**:

- **NFS Server**: Stores files and provides remote access. It is **stateless** (does not maintain client-specific state).
- **NFS Client**: Uses Remote Procedure Call (RPC) to access files on the server.
- Clients maintain local caches and perform cache validation on file open.

NFS provides transparent access to remote files as if they were local. It is widely used in Unix/Linux environments due to its simplicity and robustness.

---

### Answers from Model Question Paper

**1. Explain the directory service and its interface operations in a file service architecture.**

The Directory Service manages the naming hierarchy in a Distributed File System. It maps human-readable names and paths to unique File Identifiers (UFIDs).

**Main Interface Operations**:
- `Lookup(dir, name)` → returns UFID of the file/directory
- `AddName(dir, name, fileID)` → adds a new name to directory
- `RemoveName(dir, name)` → removes a name from directory
- `Rename(dir, oldname, newname)`
- `ReadDir(dir)` → lists contents of directory

It works above the Flat File Service and provides location transparency.

**2. Describe the architecture of Google File System.**

(Refer to answer 7 above – same content)

**3. Explain consensus algorithm for crash failures under synchronous systems.**

(You had mentioned “if they repeat like the byzantine question no need to answer it again” — this is similar to earlier consensus questions. Let me know if you still want it.)

**4. Summarize distributed file system requirements.**

(Refer to answer 4 above)

**5. Differentiate Andrew file system and NFS.**

| Feature                  | Andrew File System (AFS)                  | Sun NFS                                      |
|-------------------------|-------------------------------------------|---------------------------------------------|
| Caching                 | Whole-file caching                        | Block-level caching with validation         |
| Consistency             | Callback mechanism                        | Validation on open                          |
| Server Design           | Stateful (Vice + Venus)                   | Stateless                                   |
| Performance             | Excellent for read-heavy workloads        | Moderate                                    |
| Scalability             | High                                      | Moderate                                    |
| Target Environment      | Large-scale distributed computing         | General Unix/Linux file sharing             |

**6. Explain Sun NFS architecture with diagram.**

Sun NFS uses a **client-server architecture**. The NFS server is stateless. Clients access remote files using RPC calls. The client maintains a local cache and validates it on file open. The architecture consists of:

- NFS Client → RPC → NFS Server

(The server stores files and directories. Clients see remote files as if they were local.)

---

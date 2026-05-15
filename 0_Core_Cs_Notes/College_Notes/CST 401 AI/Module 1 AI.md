Date: 2025-11-10
Topics: #ai #clg_notes
Link: 
Class: [[AI]]

---

# Module 1: AI Fundamentals

Introduction to artificial intelligence basics and concepts.

## Key topics

- What is Artificial Intelligence?
- Types of AI (Narrow vs General)
- Machine Learning basics
- AI applications in real world

## Learning objectives

- Understand what AI is and isn't
- Learn different branches of AI
- Know how AI differs from traditional programming
- Explore real-world AI examples

## Related notes

- [AI-ML Basics](../../AI-ML/AI-ML%20Basics.md) - Foundation concepts
- [Module 2 AI](Module%202%20AI.md) - Continuation of this module
- [Supervised Learning](../../AI-ML/Supervised%20Learning.md) - Main ML paradigm
- [AI-ML Basics](../../AI-ML/AI-ML%20Basics.md)

---
### What is AI and how to define it ?

Artificial intelligence refers to the field of computer science and math which aim to use machines / computers to solve problems typically solved by humans
We can define an AI by observing the following 4 criterion:
1. Thinking Humanly
2. Thinking Rationally
3. Acting Humanly 
4. Acting Rationally

❗**Thinking humanly (Cognitive Modelling)** human thinking can be classified by the following 3 actions
- Introspection
- Psychological inspection
- Brain wave imaging
if the input / output of a machine matches the thinking pattern of humans we can classify the machine as capable of thinking humanly

**Thinking rationally (Law of Thought)** is commonly defined by the availability of the following two capabilities
- **Syllogism**: Using two or more propositions to reach a conclusion
- **Logic**: Converting informal information to formal information, the problem faced is that not all information is certain and its hard to do perform the conversion

❗**Acting humanly** is commonly tested with the **Turing Test** where a judge is to decide whether the responses submitted are by a human or a machine. The turing tests requires
- **natural language processing** (communicate like and with a human)
- **knowledge representation** (storing knowledge and info)
- **automated reasoning** (drawing conclusions from stored knowledge)
- **machine learning** (to adapt to new problems and extrapolate patterns)

**Acting rationally (Rational Agent)** is classified by the following actions
- Operate autonomously 
- Perceive information
- Sustain itself
- Adapt to changes 
- create and pursue goals


### What is an agent ?

An agent is anything that can perceive its environment using **sensors** and then act on that input via **actuators**
ex: human, robot, software all 3 have different methods of taking input, processing it and providing an output

**precept**: this refers to the input perceived by the agent at any point of time

An intelligent agent will refer to any agent that can act autonomously and can gather input with sensors and act on them via actuators. They may also learn patterns while collecting the input


### ❗What are task environments and their properties and describe PEAS system

Task environments can be referred to as the problems that these AI agents are required to solve

The properties of task environments are:
- **Fully / Partially Observable:** if the state of the agent can be completely seen at any point of time -> fully observable(chess) else partially observable(driving)
- **Deterministic / Stochastic:** if future actions are predictable by current ones(chess) -> deterministic else stochastic (**a random element is present**) (driving car)
- **Sequential / Episodic:** if previous actions are influential to current and future actions(**dependency between current and previous actions**) -> sequential (chess) else episodic (part checker in assembly line)
- **Single / Multi Agent:** if a single agent works (path finding) else multiple agent work (tic tac toe)
- **Known / Unknown:** If all outputs from current state are known else unknown
- **Discrete / Continuous:** if we get to output with finite number of steps -> discrete else continuous 
- **Static / Dynamic:** if state constantly changing -> dynamic else static

The **PEAS** system can be defined as:
- **Performance Measure**: how we measure the quality of an agent
- **Environment**: what sort of environment the agent works in
- **Actuators**: tools with which the agent interacts with the env
- **Sensors**: tools with which the agent gathers information / precept from the env


University question describe the PEAS system for interactive English tutor

Performance measure: understanding of the student, quality of explanation, time taken to convey information, understanding of weak areas of a student

Environment: classroom / home of the student

Actuators: computer to interact with student, text-to-speech, interactive feedback mechanism

Sensors: input devices to gather student input like keyboard, mouse, microphone, etc; response data and accuracy of a student


### What are the applications of AI ?

The various applications of AI can be seen in numerous disciplines:

- Robotics
- Spam filters
- Image Recognition
- Speech recognition
- Game Engines

### History of AI (Expand on this if u have time)

1. Birth (52-56)
2. Golden Year (56-74)
3. Winter 1 (74-80)
4. Boom (80-87)
5. Winter 2 (87-93)
6. Emergence of Agent (1993-2011)
7. Deep Learning (2011-present)

### Types of Agent Programs (Learn diagrams)

- Simple Reflex (based on current state do some action)
- Modal Based (based on current state and some data on previous state and changes do some action)
- Goal Based (based on the goal, current state, previous state and changes do some action)
- Utility Based (based on all the above mentioned data and utility level optimize action)

**There are diagrams for each one of them learn those** 


### Learning Agent (Learn diagrams)

Components of a learning agent are
1. **Learning Element:** The performance review given by critic is used to improve the working of the performance element
2. **Performance Element:** Gets input and decides what kind of actions are required
3. **Critic:** Compares the performance of the agent with standard metrics and that data is sent to the learning element
4. **Problem Generator:** Decides on new actions to be performed by the agent which will allow the agent to gather more data

![[../../../2_Images/Learning Agent Architecture.png|Learning Agent Architecture.png]]

#### Representation
The following figure shows how states are represented inside with increasing complexity

![[../../../2_Images/State Representation.png|State Representation.png]]
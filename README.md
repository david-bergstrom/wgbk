# Description

There are three types of nodes in our network:

1. A single always on router-node
2. Publicly available nodes
3. Private nodes

Ideally the first node has near 100% uptime and a fast internet connection with low latency.

Private nodes can connect directly to the publically available nodes, and to other private nodes via the always on node. They keep a connection open to all public nodes, in case the public nodes wants to communicate with them. They keep a connection open to the publically available node, in case any other private node wants to communicate with them.

Public nodes can connect to each other directly and to the private nodes through direct connections established from the private nodes. 

Private nodes are typically behind NATs, such as home computers, office computers or are moving around, such as smartphones, tablets or laptops. Public nodes are computers with direct access to the internet, such as desktop computer. The advantage of public nodes is that they can communicate with private nodes during downtime of the always on router-node. Additionally the public nodes can communicate with private nodes without the latency and speed limitations of the always on router-node.

The always-on node is a agreed-upon elevated public node.

# Features

* [ ] Centralized list of all nodes in a network
* [ ] Generates configuration files for nodes, depending on specified node type
* [ ] Additional support to generate private keys for mobile devices
* [ ] Support for pre-shared keys
* [ ] Written in pure Python 3 without any dependencies
* [ ] Configuration limited to a directory which can be shared via e.g. git

# Commands

Create an empty network

```
<tool> init
```

Adding a private node with name node1 with a public keys returns the ip-address allocated to the node.

```
<tool> add node1 <public key of node1>
10.0.32.1
```

Delete the node using either a public key or an ip

```
<tool> delete 10.0.32.1
<tool> delete <public key of node1>
```

Designate a public node as the central always-on node.

```
<tool> set-router [ip or public key]
```

Upgrade a private node to a public node:

```
<tool> set-public [ip or public key] <external-ip>:<external port>
```

Downgrade a public node to a private node:

```
<tool> set-private [ip or public key]
```

Generate configuration file for a node:

```
<tool> config [ip or public key]
```

# Stockfish Cluster

## How to create a remote chess engine with Stockfish Cluster version

<img src="./coverpic.jpeg" alt="Getting started" />

> **_NOTE:_** Contributing:
This project welcomes contributions and suggestions.

 In this project, we will discuss how to create an MPI Cluster on several platforms including a cluster build with SBC (LePotato or Raspberry Pi or similar) and run a cluster Version of Stockfish to improve chess engine usage with ChessBase and other UCI software.

## Problem statement and goal ##

The journey started end of 2021. I wanted a remote server connected to ChessBase Software when analyzing chess games, tactical analysis etc. You might think why not just run stockfish or other engines on your laptop. Well true, but the heavy CPU usage of such engine on a laptop -let’s assume 8 cores- drain the battery fast if not connected to power. Also, a remote chess engine running on a cluster has much better performance.

<h2>Prerequesites</h2>
<ul>
 <li>Raspberry Pi 3 Model B or higher. As an alternative Libre Computer Board AML-S905X-CC (Le Potato) 2GB </li>
 <li>Reliable MicroSD Card (Samsung/SanDisk recommended)</li>
 <li>MicroUSB Power Supply</li>
 <li>Network switch such as NETGEAR 8-Port Gigabit Ethernet Plus Switch</li>
 <li>Internet Connection</li>
 <li>Azure account for Azure based Stockfish Cluster</li>
<li>Cluster Operating system:</li>
    <dd>Azure VM: Ubuntu OS</dd>
    <dd>Raspberry Pi: Armbian or Ubuntu</dd>
    <dd>LePotato: Armbian</dd>
</ul>
64 bit recommended to ensure highest performance. A mix of different SBC is not a problem. However, MPI tuning and/or network switch tuning might be necessary.

I will show how to build a raspberry Pi cluster (SBC) with a cluster version of Stockfish. Stockfish is a free and open-source chess engine, available for various desktop and mobile platforms. It can be used in chess software through the Universal Chess Interface (UCI).
Then we will connect to ChessBase and other UCI software. ChessBase is a personal, stand-alone chess database that has become the international standard for top players, from the World Champion to the amateur next door.
<h2>Message Passing Interface</h2>
To load balance an engine cluster version I use OpenMPI. OpenMPI is an open-source implementation of the Message Passing Interface concept. An MPI is a software that connects processes running across multiple computers and allows them to communicate as they run. This is what allows a single script to run a job spread across multiple cluster nodes.
And yes, there is a Stockfish Chess Enginge branch developed with MPI cluster implementation of Stockfish, allowing Stockfish to run on clusters of compute nodes connected with a high-speed network.

For details follow the links below.

# Setup Stockfish Cluster on SBC

In this part of the guide, we will walk you through the process of setting up a Stockfish cluster on a Single Board Computer (SBC). A Stockfish cluster allows you to run multiple instances of the Stockfish chess engine in parallel to speed up analysis and improve performance.

Follow the link [here](https://github.com/Egbert-Azure/stockfish-cluster/blob/main/setup-cluster/SetupStockfishCluster.md)

# Setting up a Basic MPI Cluster in Azure with Azure CLI

In this part of the guide, we will walk you through the process of setting up a basic MPI (Message Passing Interface) cluster in Azure using Azure CLI (Command Line Interface).
This cluster will consist of several virtual machines (VMs) that will communicate with each other using the MPI standard. We will also provide instructions on how to conduct a basic MPI latency test to verify the cluster's functionality.

### The documentation can be found [here](https://github.com/Egbert-Azure/stockfish-cluster/blob/main/setup-azure-cluster/SetupAzureBasicMPICluster.md) which includes a first MPI Latency Test too

<b>Additional Cluster test routines:</b>

[folder with sample code to test MPI cluster](MPI-Tests)

# Stockfish Cluster Installation

> **_NOTE:_**  Regardless of whether you are setting up a Stockfish cluster on a Single Board Computer or an Azure VM MPI cluster, the setup process is the same.

The first step in setting up a Stockfish cluster is to install the Stockfish engine on each node in the cluster.
Follow the link to
[Install Stockfish Engine](setup-cluster/Install%20the%20Stockfish%20Cluster%20Engine.md)

# ChessBase integration

`ChessBase` is a popular personal chess database that has become the standard for top players around the world, from the World Champion to the amateur next door. One of the benefits of ChessBase is its compatibility with UCI compliant chess engines, which allows users to analyze games and positions using powerful chess engines.

However, ChessBase only accepts executable (`exe`) files as engines, which can be a limitation for users who want to connect to non-exe engines, such as those running on Linux servers. In this guide, we will explore how to connect to ChessBase and other UCI software using a "middleman" to bridge the gap and enable communication between the two.

If you haven't read the first part of this guide, "Building a Remote Cluster with Stockfish Chess Engine," we recommend starting there to set up a remote chess engine cluster. With that in place, we can move on to connecting ChessBase to the remote cluster using the middleman tool.

* Option 1 with `InBetween`:

Follow the linke here
[inbetween.md](https://github.com/Egbert-Azure/stockfish-cluster/blob/main/inbetween.md)

* Option 2 with `SSH-Engine`:

Follow the link here
[ssh-engine.md](https://github.com/Egbert-Azure/stockfish-cluster/blob/main/sshengine.md)

* Option 3 with `DrawBridge`:

is with [drabwridge](https://github.com/Egbert-Azure/drawbridge),
an open source UCI engine bridging software developed by [Khadim Fall](https://www.linkedin.com/in/khad-im/). 
It will imitate a normal uci engine while bridging its traffic to a remote host. This will allow to use remote engine clusters to be used in traditional software.
Which is the most flexible bridging software with some advanced features such as middleware definition.

You might want and need to add this middleware to trick out `ChessBase` overruling the engine setup which cause the a connection failure

``` console
function message_in(line)
  return line;
end;

function message_out(line)
   --[[Example: Filter out Hash overwrites--]]
  filterPrefix = "setoption name Hash"
  if string.sub(line, 1, string.len(filterPrefix))==filterPrefix then
    return "";
  end

  --[[Example: Filter out Thread overwrites--]]
  filterPrefix = "setoption name Threads"
  if string.sub(line, 1, string.len(filterPrefix))==filterPrefix then
    return "";
  end

  return line;
end;

```

![image](https://user-images.githubusercontent.com/55332675/228965391-d2d522d2-0a79-4f13-837c-ebcc1bbed079.png)
![image](https://user-images.githubusercontent.com/55332675/228965510-806be23e-ec50-4b28-a902-729506158d73.png)



## Drop a Star ⭐ ##

If you like this project then drop a Github star by pressing the Star button ⭐

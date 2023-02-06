# Stockfish Cluster
<h2>How to create a remote chess engine</h2>
    <h3>with Stockfish Cluster version</h3>
<img src="./1666199543667.jpeg" alt="Getting started" />
 In this project, we will discuss how to create an MPI Cluster on several platforms including a cluster build with SBC (LePotato or Raspberry Pi or similar)
<h2>Problem statement and goal</h2>
The journey started end of 2021. I wanted a remote server connected to ChessBase Software when analyzing chess games, tactical analysis etc. You might think why not just run stockfish or other engines on your laptop. Well true, but the heavy CPU usage of such engine on a laptop -let’s assume 8 cores- drain the battery fast if not connected to power. Also, a remote chess engine running on a cluster has much better performance.

<h2>Prerequesites</h2>
<ul>
 <li>Raspberry Pi 3 Model B or higher. As an alternative Libre Computer Board AML-S905X-CC (Le Potato) 2GB </li>
 <li>Reliable MicroSD Card (Samsung/SanDisk recommended)</li>
 <li>MicroUSB Power Supply</li>
 <li>Network switch such as NETGEAR 8-Port Gigabit Ethernet Plus Switch</li>
 <li>Internet Connection</li>
<li>Cluster Operating system:</li>
    <dd>Azure VM: Ubuntu OS</dd>
    <dd>Raspberry Pi: Armbian or Ubuntu</dd>
    <dd>LePotato: Armbian</dd>
</ul>
64 bit recommended to ensure highest performance. A mix of different SBC is not a problem. However, MPI tuning and/or network switch tuning might be necessary.

I will show how to build a raspberry Pi cluster with a cluster version of Stockfish. Stockfish is a free and open-source chess engine, available for various desktop and mobile platforms. It can be used in chess software through the Universal Chess Interface (UCI).
Then we will connect to ChessBase and other UCI software. ChessBase is a personal, stand-alone chess database that has become the international standard for top players, from the World Champion to the amateur next door.
<h2>Message Passing Interface</h2>
To load balance an engine cluster version I use OpenMPI. OpenMPI is an open-source implementation of the Message Passing Interface concept. An MPI is a software that connects processes running across multiple computers and allows them to communicate as they run. This is what allows a single script to run a job spread across multiple cluster nodes.
And yes, there is a Stockfish Chess Enginge branch developed with MPI cluster implementation of Stockfish, allowing Stockfish to run on clusters of compute nodes connected with a high-speed network.

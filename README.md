# Stockfish Cluster
<h1>How to create a remote chess engine</h1>
    <h2>with Stockfish Cluster version</h2>
 In this article, we will discuss how to create an MPI Cluster on several platforms including a SBC cluster (LePotato or Raspberry Pi or similar)
<h2>Problem statement and goal</h2>
The journey started end of 2021. I wanted a remote server connected to ChessBase Software when analyzing chess games, tactical analysis etc. You might think why not just run stockfish or other engines on your laptop. Well true, but the heavy CPU usage of such engine on a laptop -let’s assume 8 cores- drain the battery fast if not connected to power. Also, a remote chess engine running on a cluster has much better performance.

<h2>Prerequesites</h2>
<ul>
 <li>Raspberry Pi 3 Model B or higher. As an alternative Libre Computer Board AML-S905X-CC (Le Potato) 2GB </li>
 <li>Reliable MicroSD Card (Samsung/SanDisk recommended)</li>
 <li>MicroUSB Power Supply</li>
 <li>Network switch such as NETGEAR 8-Port Gigabit Ethernet Plus Switch</li>
 <li>Internet Connection</li>
</ul>
<h2>Operating System</h2>
<li>Azure VM: Ubuntu OS</li>
<li>Raspberry Pi: Armbian or Ubuntu</li>
<li>LePotato: Armbian</li>
64 bit recommended to ensure highest performance. A mix of different SBC is not a problem. However, MPI tuning and/or network switch tuning might be necessary.

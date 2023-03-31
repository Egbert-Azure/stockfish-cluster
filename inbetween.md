# InBetween.exe (ver. 1.5) by O.Gunnar Malin

`InBetween.exe` is a command-line utility for Windows written by Odd Gunnar Malin that enables text commands between client and server to be translated or modified. It can be used to fix communication incompatibilities or glitches in protocol implementations, for example between a chess GUI (client) and CECP or UCI compliant chess engine (server).

With InBetween, you can log all communication between GUI and engine (client, server, or both), either as output to the console or as a log file. In addition, InBetween can be used in conjunction with PuTTY to connect a Windows GUI (such as ChessBase) to a chess engine on a Linux server via a Secure Shell.

InBetween is a powerful and flexible tool for resolving conflicts between chess GUI and engine commands. It has been in use in the chess community for over 20 years, and its longevity speaks to its value and effectiveness.

## Usage

To use InBetween, simply download the executable file and run it on your Windows machine. Then, set InBetween as your 'UCI engine' in Chessbase or your chess GUI of choice. When a command is sent from the GUI to the engine, InBetween will intercept it, modify it if necessary, and forward it on to the engine. Similarly, when a response is sent from the engine to the GUI, InBetween will intercept it, modify it if necessary, and forward it on to the GUI.

InBetween can be customized to suit your specific needs. For example, you can log all communication between GUI and engine to a file, or output it to the console. You can also modify specific commands to fix incompatibilities or glitches in the protocol implementation.

## Setup

To set up InBetween, create a separate directory such as "RaspberryCluster". In this directory, place InBetween.exe and the InBetween.ini file. You can rename the InBetween.exe to something else if you prefer, such as ClusterEngine.exe. In that case, make sure to rename the ini file as well, to ClusterEngine.ini.

Next, configure the ini file with the necessary settings. Here's a sample configuration:

``` ini
[InBetween]
Priority := high
CommandLine := C:\putty\plink.exe -ssh -C -i your.ppk userid@serverIP "./cluster14"

[Client2Server]
isready

[Server2Client]
readyok
```

The Priority parameter sets the priority of the process to high. The CommandLine parameter specifies the command line arguments to use when running the engine. In this example, we're using PuTTY's plink.exe to connect to a remote server via SSH and run the script cluster14.

Note that Windows adds a boost to foreground applications running with priority class set to normal. You may need to adjust this in the control panel/system if you try to get a foreground app and a background app to run with the same priority (engine match). You might want to start the GUI with the Boost=false setting.

For a Telnet connection, change the CommandLine parameter to:

``` console
CommandLine := PLINK.EXE -raw -P 3333 yourClusterMasterIP "./cluster14"
```

## Syntax

The syntax for the ini file is as follows:

``` ini
[InBetween]
Priority := priority_level
CommandLine := command_line_arguments

[Client2Server]
text_to_send

[Server2Client]
text_to_expect
```

Debug mode is useful to test things out where color coding is as follows:

* Blue: flow to the server
* Red: flow to the client
* Green: control signal

## History

InBetween was first released in 2001, and has been used by the chess community ever since. It is a testament to the tool's value and effectiveness that it has continued to be used for over 20 years. And one reason is that ChessBase integration is still hard to achieve.
While this is an outdated connector, it comes with some drawbacks, such as using another program `plink` to connect.

However, using InBetween can be a great solution for resolving incompatibilities or glitches in protocol implementations between a chess GUI and engine. By configuring the ini file with the appropriate settings, you can customize the connection to fit your needs.

>Disclaimer

InBetween is designed for use on Windows machines, and may not be compatible with other operating systems. Additionally, while InBetween is a powerful tool for resolving conflicts between chess GUI and engine commands, it should be used with caution, as modifying commands can lead to unexpected behavior. Use at your own risk.

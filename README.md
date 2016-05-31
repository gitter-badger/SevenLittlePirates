<html>
<div class="container">
<head>
<link rel="stylesheet" type="text/css" href="slpstyles.css">
</head>
<body>
<hr />
<h1>Seven Little Pirates</h1>
<hr />
<h2>Information about Seven Little Pirates</h2>
<p>Seven Little Pirates is a little game I made for my Spanish class. We had to do something creative, so I decided to write a small game and make it open source! Feel free to have a look at the source and modify it to your liking!</p>
<hr />
<h2>SLP on Android</h2>
<hr />
<h2>SLP on Termux (Android 5.0.x and above)</h2>
<p>So recently, I discovered an open source app for Android, called Termux. Now the special thing about this app is that it had the APT package manager from Debian and Ubuntu. This meant you could install a wide range of packages and use them on your Android device running Android 5.0.x or higher! The installation of packages is very easy. All you need is a stable internet connection and a bit of patience. The instructions below have been made for an Android device running Android 5.0.x or above and a stable version of Termux. If you do not have such a device I can only say that I'm working on a method to port this to older Android versions. You can get the Termux app on my App Store <a href="http://avasappstore.github.io/">here</a> or from the official project site of Termux <a href="http://termux.com/">here</a>.</p>

<p>Need help? Ask in the thread:</p>
<p><a href="https://gitter.im/al3xv3gas/Bave"><img src="https://badges.gitter.im/al3xv3gas/bave.svg"/></a></p>
<hr />
<h2>How do I get started?</h2>
<hr />
<p>So to get SLP up and running, we need to install some dependencies first. Before this we need to update the package lists. Do this by executing the command below in the Termux terminal!</p>
<div class="highlight-box">
<code>apt-get update</code>
</div>
<p>
Next, we need to install Git in order to get all the installation files onto our device. To do this execute the command below.</p>
<div class="highlight-box">
<code>apt-get install git</code>
</div>
<p>Now we need to change the working directory. Execute the command below to do this.</p>
<div class="highlight-box">
<code>cd $HOME</code>
</div>
<p>Congrats! You have successfully changed the working directory! Next, clone the files onto your device!</p>
<div class="highlight-box">
<code>git clone  https://github.com/<br />al3xv3gas/SevenLittlePirates.git</code>
</div>
<p>Congrats! You have successfully cloned the installation files onto the device. Now we need to change into the installer directory. To do this, execute the command below.</p>
<div class="highlight-box">
<code>cd bave/code</code>
</div>
<p>Next, we need to execute the installer script. To do this, type this command and hit "Enter".</p>
<div class="highlight-box">
<code>sh setup.sh</code>
</div>
<p>One step more! We need to change into the home directory. To do this, execute the command below.</p>
<div class="highlight-box">
<code>cd $HOME</code>
</div>
<p>Now you have successfully installed SLP. To start the console, execute this command:</p>
<div class="highlight-box">
<code>sh startSLP.sh</code>
</div>

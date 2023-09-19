# Kivymd_hotreload_demo
Implemented hot-reloading in KivyMD for smoother app development. Fixed multiple .kv file reload issue. #456

<p>
# KivyMD version 1.1.1
# GitHub: https://github.com/kivymd/KivyMD
# Kivy version 2.2.1
# Website: http://kivy.org

Author: Ramayan Mardi

About:
This demo showcases how to enable hot-reloading with KivyMD. It is intended to 
be a helpful resource for those who are struggling to set up hot-reload 
functionality in their apps.

<b>Why this demo?</b>
Setting up hot-reloading in my app was confusing for me, especially because 
there were no examples in the documentation. While there's a fork of KivyMD 
called Kaki that provides a demo, it wasn't as clear as I needed it to be. 
So, I created this demo to provide a straightforward example since I couldn't 
find much information on the topic online.

<b>Limitations:</b>
I have tested this script on a Windows 10 machine, and I cannot guarantee that 
it will work the same on other machines. According to KivyMD's documentation, 
this module may not be fully optimized for Windows yet. However, it works well 
with .kv files. It doesn't detect changes in .py files on Windows, except for 
the entry point .py file. (It seems to work better on Linux based on limited 
issue reports.)

I have not extensively tested this script with many .kv files simultaneously 
during hot-reloading. Make sure to test it with your own setup. I recommend 
organizing your .kv files in a structured way for easier access.

<b>Issues Solved:</b>
- Multiple reloads of .kv files during hot-reloading:
  To avoid this issue, if you are passing a directory or .kv files to a class 
  variable, refrain from loading your .kv files within other code. When you pass 
  your file to the class variable, it automatically loads those files for you, 
  making them ready for hot-reloading.
  
  Conclusion: If you're partially loading .kv files in your app, comment them 
  out when using hot-reloading and let the script handle everything. Don't 
  complicate things unnecessarily.

<b>Note:</b>
In Windows, I encountered a situation where the script sometimes couldn't load 
directory files at the start of the app. However, when you start editing and 
saving your .kv files in those directories, it usually gets fixed automatically.

<b>How to Use the Class:<b>
Using this class is relatively straightforward. You need to pay attention to 
minor details like not using the `build` method; instead, override `build_app`, 
which is a method of the `kivymd-hotreload` class.

If you don't want to hard-code the DEBUG variable and want to run it through 
cmd/powershell/linux, you can set the DEBUG variable before running the script:

- In cmd: `set DEBUG=1 && python hotreload_demo.py`
- In powershell: `($env: DEBUG=1) -and (python hotreload_demo.py)`
- In Linux: `DEBUG=1 python hotreload_demo.py`
'''
</p>

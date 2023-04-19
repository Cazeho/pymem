import subprocess
import tkinter as tk
from tkinter import filedialog


def create_local_dump():
    # Set the input and output file paths
    input_file = r"\\.\PhysicalDrive0"  # the physical drive to copy
    output_file = filedialog.asksaveasfilename(defaultextension=".dd")  # the output disk image file

    # Set the block size and number of blocks to copy
    block_size = 512  # bytes per block
    block_count = 100000  # number of blocks to copy

    # Run the dd command to create the disk image file
    dd_command = f"dd if={input_file} of={output_file} bs={block_size} count={block_count} conv=noerror,sync,ro"
    subprocess.run(dd_command, shell=True)


def send_remote_dump():
    # Set the input and output file paths
    input_file = r"\\.\PhysicalDrive0"  # the physical drive to copy
    output_file = filedialog.asksaveasfilename(defaultextension=".dd")  # the output disk image file

    # Set the block size and number of blocks to copy
    block_size = 512  # bytes per block
    block_count = 100000  # number of blocks to copy

    # Get the SSH connection information from the user
    ssh_host = host_entry.get()
    ssh_username = username_entry.get()
    ssh_password = password_entry.get()

    # Run the dd command to create the disk image file on the remote server
    dd_command = f"dd if={input_file} conv=noerror,sync,ro | sshpass -p {ssh_password} ssh {ssh_username}@{ssh_host} 'dd of={output_file} bs={block_size} count={block_count}'"
    subprocess.run(dd_command, shell=True)


# Create the GUI
root = tk.Tk()
root.title("Disk Dump Utility")

# Create the local dump button
local_button = tk.Button(root, text="Create Local Dump", command=create_local_dump)
local_button.pack()

# Create the remote dump button
remote_button = tk.Button(root, text="Send Remote Dump", command=send_remote_dump)
remote_button.pack()

# Create the remote server connection fields
host_label = tk.Label(root, text="Server Host:")
host_label.pack()
host_entry = tk.Entry(root)
host_entry.pack()

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

root.mainloop()

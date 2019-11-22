B
    *��]�a  �               @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ d dl	m
Z
 d dlmZ d dlmZ d dlmZ dZe� Zd Z Z Z Z ZZdd	� Zd
d� Zdd� Zedk�r�ed� ed� ed� ed� ed� ed� ed� ed�Zde d Zede d � ed�Zdek�r,ede � ned Zede � eed��Zed�Z ed k�r�ej!e ed!�Ze�"�  eeeeee� ed"� nJed#k�r�ej!e ed!�Ze�"�  eeeeee� ed"� ed$� ned%� dS )&�    N)�	webdriver)�Keys)�Options)�ExcelWriter)�	ExcelFile� c             C   sJ   d}x4t dd�D ]&}| j�|�dkr,d}P qt�d� qW |sFtd� | S )NF�   �   �����TzError. Timeout.)�rangeZpage_source�find�time�sleep�print)� b36d375bf6afe60d39a76745f781ab88�textZ!p5a7486c909fd18f4cd49d169b75e2d53�i� r   �obs_nessus config review.py�!w9d6b042ae634aa8159a9793988c6a7f7   s    r   c       
      C   s�   t �� }|d |  }t�d| d �}t�|�}t�|d �� |d |d �|d< |d }|d }|d }|d }xJtt	|��D ]:}	t
||	 � t
||	 � t
||	 � t
||	 � t
�  q�W tt||||� dS )N�/r   ZHostnameZIPZDescriptionZ
Credentialr   )�os�getcwd�pdZ
read_excelZ	DataFrame�np�whereZisnullr   �lenr   �!n1e1b20a4a7cfc16bc374338a263aec2dr   )
� d656c603994e747a4a39010356a737bb� e6603da1acdd6f636053fd30d4a653e3� e230450c7869f12283a9a784a6023a68� cb6462b1997e6e59ae9c0c40c41963c6�!c9bc48c8a0b0e1d60ae7b113617c864c7Z!p7c36de502f4aa5d7a5fb2292243a2aa9Z!p1dd8f006837f1230e42dc6e79e27215cZ a2571565ecf98e6d43f0536c7240880eZdfr   r   r   r   � a75b59e37ddaead95524079cb557a273   s"    
"
r#   c                s  t d�}t d�}| �t� t| d�} | �d��|� | �d��|� | �d���  t| d�} �x�tt|��D �]�}t	d� | �d	���  t| d
�} | �d���  t| d�} t	d||  � t	d||  � t	d||  � t	d||  � | �d��|| � | �d��|| � | �d��|| � | �d���  t| d�} | �d��
�  | �d��d� | �d���  t| d�} | �d��
�  | �d��d� | �d���  t| d�} | �d���  | �d��tjtj� | �d���  t| d�} | �d ���  | �d!���  | �d"���  | �d#���  | �d$���  t| d%�} | �d&���  | �d'���  | �d(���  | �d)���  | �d*���  | �d+���  | �d,���  t| d-�} || � d.}d/}	d0}
d.}d.}d.}d1|| k�r,t	d1� t�d2� | �d3���  t| d4�} | �d5��d6� | �d7��|| � t�d2� | �d8���  | �d9���  d:}t�d;� �}d.�|�}t�d<� �}d.�|�}d=� �� k�r�d>|k�r�d.}nd?}nt	d@� t� fdAdB�dCD ���r*t	dD� dE|k�r�dF}	dG}
dH}d>|k�r�d.}
dI}	dJ}dK|k�rdL� �� k�rdM}dN}	ndO}dI}	dP|k�r�dQ}dI}	n�t	dR� d>|k�rHd.}
dS}	dT}dU|k�rbdV}|}dW}	dG}
dX|k�r|dY}|}d.}	d.}
dP|k�r�dZ}dS}	n*dK|k�r�dL� �� k�r�d[}dS}	nd\}dS}	|| d] | |	 |
 }t	d^| � | �d_���  t| d`�} | �da��|� t�db� | �|���  t�d2� �n�t	dc� t�d2� | �dd���  t| d4�} t�d2� | �de���  | �de��tjtj� | �df��dg� | �dh��|| � | �di���  | �di��tjtjtjtjtjtjtjtj� | �dj��dg� | �dk��|| � | �dl��|| � dm� �� k�r~dm}t�dn� �}d.�|�}do}dU|k�r^dp| }dq}|d] | dr |
 }t	d^| � ds� �� k�r�ds}t�dn� �}d.�|�}dt}dU|k�r�du| }dv}|d] | dr |
 }t	d^| � dw� �� k�rvdw}t�dx� �}d.�|�}dy|k�r$|dz |
 }d{}n:d||k�r2d}}d~|k�r@d}d�|k�rNd�}d�| d� |
 }|d] | }t	d^| � d�� �� k�r�d�}|}d�}t	d^| � | �d_���  t| d`�} | �da��|� t�db� | �|���  t�d2� | �d����  t| d��} t�d�� qlW d�S )�NzEnter your nessus username:
$ zEnter your nessus password:
$ zSign Inz /html/body/div/form/div[1]/inputz /html/body/div/form/div[2]/inputz/html/body/div/form/buttonzMy Scansz.
##############  New Scanning  ##############
z%/html/body/section[3]/section[1]/a[1]zAdvanced ScanzB/html/body/section[3]/section[3]/section/div[1]/div[2]/div[2]/a[2]ZTargetszhost session : zdesc session : zip session : zpasswd session : zq/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div[1]/div[1]/div/inputzt/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div[1]/div[2]/div/textareazt/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div[1]/div[5]/div/textareazP/html/body/section[3]/section[3]/section/form/div[1]/div/div/aside/ul/li[2]/spanzDestination portsz�/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[4]/div[1]/div[1]/div[1]/div[6]/div[4]/div[2]/div/div[3]/div[1]/div/input�allzT/html/body/section[3]/section[3]/section/form/div[1]/div/div/aside/ul/li[2]/ul/li[2]Z	unscannedzq/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[5]/div[1]/div[1]/div[2]/div/inputzT/html/body/section[3]/section[3]/section/form/div[1]/div/div/aside/ul/li[2]/ul/li[3]ZProbez�/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[6]/div[1]/div[1]/div[2]/div[6]/div[1]/div/span/span[1]/spanzP/html/body/section[3]/section[3]/section/form/div[1]/div/div/aside/ul/li[4]/spanZOverridez|div.editor-view:nth-child(13) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)z|div.editor-view:nth-child(13) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)z|div.editor-view:nth-child(13) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)z|div.editor-view:nth-child(13) > div:nth-child(1) > div:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1)zP/html/body/section[3]/section[3]/section/form/div[1]/div/div/aside/ul/li[5]/spanzsafe checksz|div.editor-view:nth-child(14) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)z|div.editor-view:nth-child(14) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)z|div.editor-view:nth-child(14) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)zadiv.editor-settings-section:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)zadiv.editor-settings-section:nth-child(8) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)zadiv.editor-settings-section:nth-child(8) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1)z%/html/body/section[3]/section[2]/a[2]ZSNMPv3r   �dc�l1ZWindowsr   z|/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div/div[2]/ul[3]/li[3]/div/span[2]zAuthentication methodz�/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[6]/div[1]/div/inputZsysadminz�/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[6]/div[2]/div/inputz�div.component-inputs:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)z�div.component-inputs:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1)Zwindowsz20\d+z\d+ZserverZ2003z serverzNot windows serverc             3   s   | ]}|� � � kV  qd S )N)�lower)�.0�!t71d9de156a31eb8c06bb3bbf54d831d4)�!c103ee3639b6b08cfaa7b9afb18e4457dr   r   �	<genexpr>�   s    z4n1e1b20a4a7cfc16bc374338a263aec2d.<locals>.<genexpr>)r%   zdomain controllerzGot DC KeywordZ2008z domain controller zlevel 1zo/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[68]z dc zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[121]Z2012Zr2zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[134]z r2 dc zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[130]Z2016zs/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[76]/divzIt is not DCz ms zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[122]�7zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[126]z workstation �8zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[129]zo/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[77]zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[136]zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[132]� zsyntax is : z%/html/body/section[3]/section[2]/a[3]zAdd compliancezu/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[1]/div[2]/div[1]/input�   ZLinuxzt/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div/div[2]/ul[3]/li[2]/divzG//*[@id="active-credentials"]/li[2]/div[2]/div/div[1]/span/span[1]/spanz�/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[5]/div[1]/div/input�rootz�/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[5]/div[2]/div/inputzU//*[@id="active-credentials"]/li[2]/div[2]/div/div[5]/div[3]/div[1]/span/span[1]/spanz�/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[5]/div[3]/div[10]/div[1]/div/inputz�/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[5]/div[3]/div[10]/div[2]/div/inputz�/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[5]/div[4]/div/inputzred hatz([6|7])zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[140]Zelzp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[144]z server Zcentoszo/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[38]zel zo/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[42]Zubuntuz\d.+z12.04z lts benchmark zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[168]z14.04zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[170]z16.04zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[174]z18.04zp/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[178]zlinux z lts server zhp-uxzs/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[82]/divz9/html/body/section[3]/section[3]/section/form/div[2]/spanZSchedule�   r   )�input�get�!u2879959685cbf0727819759e44c6e715r   Zfind_element_by_xpathZ	send_keysZclickr   r   r   �clearr   ZDOWNZRETURNZfind_element_by_css_selectorr   r   �re�findall�joinr'   �anyZUP)r   r   r    r!   r"   Z!u57f4679269eb6506b6109bc966cd7157Z f366af137ab9cba47cf204ef452c82efr   Z d654a25a65caa5674e1c2a23ff24b939r%   r&   r)   Z!s87ed9fbf4288a3bebf159694b4b1ea5eZ f7a903a4359a35e02420a093fc769913�yZ!y476c00d2d8eacc5114658627e0bfe3bbZ e772d6a76b4710dcdf676392d3074a17�vZ!v7b429202f49c6f41db35b044af2b11f4r   )r*   r   r   1   s�   






























.












r   �__main__z6   _____       _ __                                   z6  / ___/____ _(_) /_____ _____ ___  ____ _____  ____ _z6  \__ \/ __ `/ / __/ __ `/ __ `__ \/ __ `/ __ \/ __ `/z6 ___/ / /_/ / / /_/ /_/ / / / / / / /_/ / / / / /_/ / z6/____/\__,_/_/\__/\__,_/_/ /_/ /_/\__,_/_/ /_/\__, /  z8                                             /____/   

z/Welcome to autoscan_nessus script by Saitamang
z-Kindly enter your Nessus IP ie:192.168.1.1
$ zhttps://z:8834z
URL entered is : �
z)Enter fullname of the excel filename :
$ z.xlsxzFile name is :zY
What is your os:-
1. Linux
2. Windows

Key in your number your number and press ENTER
$ z�
Give the full path of Google Chrome Driver and press ENTER
eg:
Linux: /usr/bin/chromedriver
Windows: D:\Desktop\chromedriver.exe

$ r   )Zexecutable_pathZoptionsz5
##############  Done Scanning Setup  ##############
r/   zS##############  Check out my github : https://github.com/saitamang  ##############
zOperating System don't exist)#r   r   ZseleniumZpandasr   Znumpyr   r6   r   Zselenium.webdriver.common.keysr   Z!selenium.webdriver.chrome.optionsr   r   r   r   Z!o41fbb39d7dc93ad07d8126d0d17139c3r4   r   r    r!   r"   r   r   r#   r   �__name__r   r2   �u�intZ e334d4bfdbe5614e4edd3f3111e80454Z!c030503c947bceca6be59816319a41cd2ZChromeZmaximize_windowr   r   r   r   �<module>   sT   0 O






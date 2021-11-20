
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [零、前言](#零-前言)
- [一、发行版](#一-发行版)
  - [Archlinux](#archlinux)
  - [Manjaro](#manjaro)
  - [Deepin](#deepin)
- [二、Linux 网站介绍](#二-linux-网站介绍)
  - [Linux中国（软件板块）](#linux中国软件板块)
  - [Arch wiki（应用列表）](#arch-wiki应用列表)
  - [超赞的 Linux 软件](#超赞的-linux-软件)
- [三、软件列表](#三-软件列表)
  - [浏览器](#浏览器)
  - [下载工具](#下载工具)
  - [效率](#效率)
  - [文件管理](#文件管理)
  - [安全](#安全)
  - [音乐](#音乐)
  - [视频](#视频)
  - [图片](#图片)
  - [文本编辑器](#文本编辑器)
  - [游戏](#游戏)
  - [美化](#美化)
  - [命令行](#命令行)
  - [其他](#其他)

<!-- /code_chunk_output -->

# 零、前言  

Linux 是我在生活中主要使用的系统。选择 Linux 作为主系统的体验其实相当的不错。我生活上的所有使用电脑的需求都能满足。  
而且比起 Windows 效率确实有明显的提高。而我一直使用 Linux 的原因里最关键的一点是，Linux 非常的好玩！  
这篇文章作为目录，会对我使用的所有软件进行汇总。并且像 Awesome 系列一样，进行一些简单的介绍。并且连接上我的配置；  

# 一、发行版  

首先要讲到的就是 Linux 的发行版。与 Windows 不同 Linux 拥有大量风格迥异的发行版，可以根据自己的喜好进行选择。下面简单介绍几个。  

## Archlinux

我一直使用的发行版，[Archlinux](https://www.archlinux.org/download/) 是一个简洁、现代、实用、以用户为中心的发行版。Arch采用滚动升级模式，尽全力提供最新的稳定版软件。初始安装的 Archlinux 只是一个基本系统，随后用户可以根据自己的喜好安装需要的软件并配置成符合自己理想的系统。Archlinux 的安装虽然略显困难，不过只要按照 [Arch wiki](https://wiki.archlinux.org/index.php/Installation_guide_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 的超详细的安装指南就能一步步地装好了。  
选择 Archlinux 的原因主要还是为了 Arch 用户软件仓库（Arch User Repository，AUR）；因为 AUR 的存在，Archlinux 里安装软件的效率是非常高的。比如说我想安装 Minecraft 的启动器 [HMCL](https://github.com/huanghongxun/hmcl) 。在其他的系统中需要打开官方网站下载安装包、配置 JRE 等；而在 Archlinux 中只需要一句命令 `yay -S hmcl` 等安装完成后就能自动帮你把所有的配置完成。使用体验非常爽！  

## Archcraft  

如果嫌弃 Archlinux 麻烦的安装步骤。还可以使用 Archlinux 的下游发行版 Archcraft。安装很无脑，基本可以做到开箱即用。  
安装方便。颜值优秀，在美化方面做了非常多的工作。可以免去配置的功夫。基本可以做到开箱即用。相比起 Manjaro，因为直接用的 ArchLinux 仓库，应该不会出现 cn 源的神奇 BUG。  
目前缺点是缺少中文化，并且因为字体原因中文是无法展示的。有人提过更换默认字体为 CJK 字体的 Issue，但是作者拒绝了。所以还是需要后续再配置。  

项目链接：<https://github.com/archcraft-os/archcraft>

## Deepin

[Deepin](https://www.deepin.org/download/) 是一个国产、相当傻瓜化、基于 Debian 的发行版。安装非常非常简单，将官方的 ISO 镜像文件解压后会有制作安装U盘的和直接硬盘安装的软件，直接无脑下一步就行。  
自带有一个能免费使用的 CrossOver。之前有段时间我的 Arch 被我玩坏了，而手上又刚好没有u盘，所以就试着换成了可以硬盘安装的 deepin。使用了一段时间感觉还挺不错的。非常的简单。  
默认的桌面环境是 DDE ，颜值挺不错的。也作了很多针对国内的优化，可以说是国内发行版里做的最良心的。  

# 二、Linux 网站介绍

接下来介绍一下我找软件的地方。Linux因为用户少，所以并不像win和Mac有各种博客，这方面还是挺糟糕的。  

## Linux中国（软件板块）

[https://linux.cn/share/](https://linux.cn/share/)  
 比较简洁地介绍软件的功能。其他的 Linux 新闻也挺不错的。

## Arch wiki（应用列表）

[https://wiki.archlinux.org/](https://wiki.archlinux.org/index.php/List_of_applications_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))  
 列举了大量Linux应用，并且可以快速到相应的Arch wiki条目，Arch wiki的介绍通常非常的详细。  

## 超赞的 Linux 软件  

[https://alim0x.gitbooks.io/awesome-linux-software-zh_cn/content/](https://alim0x.gitbooks.io/awesome-linux-software-zh_cn/content/)
 类似之前介绍过的 Windows 绝赞应用。  

# 三、软件列表

## 浏览器

- Firefox

我目前正在使用的浏览器。直接在浏览器搜索到的官网是中国特供版。注意辨别。  
项目链接：<https://www.mozilla.org/zh-CN/firefox/new/>  

## 下载工具

- Motrix

Motrix 是一款封装了 Aria2 作为内核，并为其套上图形界面的开源免费下载软件。（AUR 的 motrix-git 包有　BUG）  
项目链接：<https://motrix.app>  

- 坚果云

目前国内最好用的网盘应用，支持云桥、WebDAV;支持在线编辑部分文件  
项目链接：<https://www.jianguoyun.com/>  

- youtube-dl

下载常用视频网站视频的下载工具  
常用使用方式：  
1.自动下载最高画质视频

    youtube-dl -f best 

2.下载视频中的音频

    youtube-dl -x 

- Feem

同一内网中各设备间文件、信息传输工具  

## 效率

- UTools  

开源生产力提升工具，类似之前介绍过的Listary。可用于执行命令, 打开应用, 打开网页, 快捷翻译, 搜索. 支持插件。  
项目地址：<https://u.tools/>  

- ClipIt  

类似ditto的剪贴板管理软件，但仅仅能够存储文本。大部分情况下还是使用 Utools 插件  

- AngrySearch  

类似Everything的Linux 文件搜索，结果输入即得。  

## 文件管理

- Ranger  

一款使用 VI 快捷键的终端文件管理器。  

    Ctrl+H 显示隐藏文件夹

- PCManFM

发行版自带文件管理器，支持多标签  

## 安全

## 音乐

- MPD

极简的音乐播放器，可以与多种软件有很好的联动。  
项目链接：<https://www.musicpd.org/>

- Netease Music  

网易与 deepin 团队合作开发的Linux版，使用体验和其他平台的没什么差距。  
目前使用 VScode 插件代替。  

- REAPER

REAPER是一个完整的计算机数字音频制作应用程序，提供完整的多轨音频和MIDI录音、编辑、处理、混音和母带制作工具集。  
项目链接：<http://reaper.fm/>  

- Synthesizer V

使用人工智能技术和素片接续相结合而成的强力歌声合成引擎  
项目链接：<https://dreamtonics.com/synthesizerv/>

## 视频

- VLC  

VLC 是一个免费且开源的跨平台媒体播放器以及框架，可以播放大多数格式的多媒体文件以及 DVS，音频 CD，VCD，以及各种流媒体协议。  

- Open Broadcaster Software(OBS)  

OBS在屏幕录制软件里还是挺有名的，开源、免费、操作简单，录制效果也很不错，很棒。  

- Kdenlive  

还不错的视频编辑软件，虽然功能没有 Adobe 家的强大，但对我来说已经足够了。  

- 达芬奇  

跨平台视频编辑软件，支持特效、调色、音频编辑  
项目链接：<http://www.blackmagicdesign.com/cn/products/davinciresolve/>  

- Natron

Natron 是一个免费的开源（GPLv2许可证）视频合成器，其功能类似于 Adobe After Effects、Foundry 的 Nuke 或 Blackmagic Fusion。它是可移植的、跨平台的（GNU/Linux、macOS和Microsoft Windows）。

项目链接：<https://github.com/NatronGitHub/Natron>

- FFmpeg  

神器，FFmpeg 是一个多媒体编解码器库，并提供了命令行前端。许多软件都使用了 FFmpeg 来进行音频和视频的编解码，特别是像 MPlayer 这样的多媒体播放器
常用命令：  
1.压制ass字幕

    ffmpeg -i input.mp4 -vcodec libx264 -preset medium -crf 23 -vf "ass=input.ass" output.mp4

2.精确时间拆分视频

    ffmpeg -ss 01:08:43 -to 01:12:00 -accurate_seek -i input.mp4 -codec copy -avoid_negative_ts 1 output.mp4

## 图片

- GIMP  

GIMP 是一个免费的、分布式的图片润饰、图象制作和处理软件，内含几乎所有图象处理所需的功能，号称Linux下的PhotoShop。  

- Krita

偏向绘画而不是图片处理方面。对数位板兼容更好。  

## 文本编辑器

- VScode

微软出品的开源文本编辑器，用着是真的香。

- nvim

vim 的升级版，比起其他编辑器打开速度更快。  

## 游戏

- Minecraft  

简评我一直都在玩的游戏，详细介绍请看

## 工作

- 浩辰 CAD

优点：
1.各操作与 AutoCAD 相同无转换成本
2.设置像素级复制 AutoCAD 设置方便
3.打开大文件速度较快
4.支持 Linux
5.有网页版

缺点：
1.Linux 仅有 CAD 没有3D设计软件

项目链接：<https://www.gstarcad.com/>

## 美化

- GNOME  

GNOME 桌面环境是一个有吸引力且直观的的桌面，拥有大量的插件。
(虽然我现在并不是这个)

- I3WM

比起桌面环境我更喜欢使用窗口管理器。  

- Adapta Theme  

一款自适应的 Gtk+ 主题，遵循 Material 设计指南。

- Papirus Icon Theme  

简评这个也是质感设计的图标包，跟adapta搭配起来还挺好看的。Linux 系统 SVG 图标主题，基于 Paper 主题并有一些额外的特性（如硬编码托盘支持，kde 颜色方案支持，libreoffice 图标主题，filezilla 主题，smplayer 主题...）以及其它的修改。这个主题适用于 GTK 以及 KDE。

## 命令行

命令行对Linux来说依然非常重要，虽然这些桌面端的发行版可以完全离开命令行，但是使用命令行可以大幅提高使Linux系统的效率，而且……这是一件非常有趣而且逼格很高的事。

- Zsh  

 一款强大的命令行 shell。我在github写的文章里有过介绍。

进阶推荐《Zsh 开发指南》  

- Oh-my-zsh  

 一个由社区驱动，优雅的 zsh 配置管理框架。

我使用时主题是 gentoo  
扩展：  
git — 简化 git 命令  
sudo — 双击 ESC 键为当前命令  
zsh-autosuggestions — 类似 fish 的补全  
zsh-syntax-highlighting — 命令行的语法高亮  
zsh-completions — 应该是自动补全，不过我没试出来怎么用，网上也没找到具体介绍……

- Tmux  

它让你在一个终端中在多个程序间方便地切换，分离他们（保持在后台运行）并另一个终端中重新连接上去。  

- git  

Git 是一款免费和开源的分布式版本管理系统，被设计用来快速和高效地处理从小项目到大项目的一切内容。

- xdotool  

模拟按键的工具，可以做一些自动化。

- NeoFetch  

快速，高度定制化的系统信息获取脚本。

- The Fuck  

杰出的应用，它能纠正你的输入的错误命令。

## 社交

- telegram

可以说是在聊天体验方面做的最好一款软件。

- 钉钉

工作用联系工具，在国内算是比较好的。  


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [零、前言](#零-前言)
- [一、发行版](#一-发行版)
- [二、Linux 网站介绍](#二-linux-网站介绍)
- [三、软件列表](#三-软件列表)
  - [浏览器](#浏览器)
  - [下载工具](#下载工具)
  - [工具](#工具)
  - [文件管理](#文件管理)
  - [安全](#安全)
  - [音乐](#音乐)
  - [视频](#视频)
  - [图片](#图片)
  - [文本编辑器](#文本编辑器)
  - [游戏](#游戏)
  - [工作](#工作)
  - [美化](#美化)
  - [命令行](#命令行)
  - [社交](#社交)

<!-- /code_chunk_output -->

# 零、前言  

Linux 是我在生活中主要使用的系统。选择 Linux 作为主系统的体验其实相当的不错。我生活上的所有使用电脑的需求都能满足。  
而且比起 Windows 效率确实有明显的提高。而我一直使用 Linux 的原因里最关键的一点是，Linux 非常的好玩！  
这篇文章作为目录，会对我使用的所有软件进行汇总。并且像 Awesome 系列一样，进行一些简单的介绍。并且连接上我的配置；  

# 一、发行版  

首先要讲到的就是 Linux 的发行版。与 Windows 不同 Linux 拥有大量风格迥异的发行版，可以根据自己的喜好进行选择。下面简单介绍几个。  

- Archlinux

我一直使用的发行版，[Archlinux](https://www.archlinux.org/download/) 是一个简洁、现代、实用、以用户为中心的发行版。Arch采用滚动升级模式，尽全力提供最新的稳定版软件。初始安装的 Archlinux 只是一个基本系统，随后用户可以根据自己的喜好安装需要的软件并配置成符合自己理想的系统。Archlinux 的安装虽然略显困难，不过只要按照 [Arch wiki](https://wiki.archlinux.org/index.php/Installation_guide_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 的超详细的安装指南就能一步步地装好了。  
选择 Archlinux 的原因主要还是为了 Arch 用户软件仓库（Arch User Repository，AUR）；因为 AUR 的存在，Archlinux 里安装软件的效率是非常高的。比如说我想安装 Minecraft 的启动器 [HMCL](https://github.com/huanghongxun/hmcl) 。在其他的系统中需要打开官方网站下载安装包、配置 JRE 等；而在 Archlinux 中只需要一句命令 `yay -S hmcl` 等安装完成后就能自动帮你把所有的配置完成。使用体验非常爽！  

- Archcraft  

如果嫌弃 Archlinux 麻烦的安装步骤。还可以使用 Archlinux 的下游发行版 Archcraft。安装很无脑，基本可以做到开箱即用。  
安装方便。颜值优秀，在美化方面做了非常多的工作。可以免去配置的功夫。基本可以做到开箱即用。相比起 Manjaro，因为直接用的 ArchLinux 仓库，应该不会出现 cn 源的神奇 BUG。  
目前缺点是缺少中文化，并且因为字体原因中文是无法展示的。有人提过更换默认字体为 CJK 字体的 Issue，但是作者拒绝了。所以还是需要后续再配置。  

项目链接：<https://github.com/archcraft-os/archcraft>

- Deepin

[Deepin](https://www.deepin.org/download/) 是一个国产、相当傻瓜化、基于 Debian 的发行版。安装非常非常简单，将官方的 ISO 镜像文件解压后会有制作安装U盘的和直接硬盘安装的软件，直接无脑下一步就行。  
自带有一个能免费使用的 CrossOver。之前有段时间我的 Arch 被我玩坏了，而手上又刚好没有u盘，所以就试着换成了可以硬盘安装的 deepin。使用了一段时间感觉还挺不错的。非常的简单。  
默认的桌面环境是 DDE ，颜值挺不错的。也作了很多针对国内的优化，可以说是国内发行版里做的最良心的。  

# 二、Linux 网站介绍

接下来介绍一下我找软件的地方。Linux因为用户少，所以并不像win和Mac有各种博客，这方面还是挺糟糕的。  

- Linux中国（软件板块）

[https://linux.cn/share/](https://linux.cn/share/)  
 比较简洁地介绍软件的功能。其他的 Linux 新闻也挺不错的。

- Arch wiki（应用列表）

[https://wiki.archlinux.org/](https://wiki.archlinux.org/index.php/List_of_applications_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))  
 列举了大量Linux应用，并且可以快速到相应的Arch wiki条目，Arch wiki的介绍通常非常的详细。  

- 超赞的 Linux 软件  

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

## 工具

- UTools  

开源生产力提升工具，类似之前介绍过的Listary。可用于执行命令, 打开应用, 打开网页, 快捷翻译, 搜索. 支持插件。  
项目地址：<https://u.tools/>  

- Rubick - 基于 Electron 开源的插件化工具箱

UTool 准备将剪贴板功能收费。由于其付费方式为我个人很讨厌的订阅制，所以我虽然可以理解他的收费行为，但我并不打算接受。
我的解决方法是使用开源软件 Rubick 进行替换。Rubick 基本完整复刻了 Utool 的外观。使用方式也没有太大的差别。依然可以使用插件商城进行插件的查看、下载。不过与 Utool 不同，插件是直接托管到 npm 仓库，安装、使用、删除都还是挺方便的。

项目链接：<https://rubickcenter.github.io/rubick/>

- AngrySearch  

类似 Everything 的 Linux 文件搜索，结果输入即得。  

- Deskreen - 将任何设备转换为计算机的辅助屏幕

Deskreen 是一款桌面应用程序，可以通过 WiFi 将任何带有网络浏览器的设备变成电脑的辅助屏幕。Deskreen 可用于将整个计算机显示镜像到任何具有 Web 浏览器的设备屏幕上。您还可以限制 Deskreen 只选择一个要共享的应用程序窗口视图-这对于演示非常有用。Deskreen 的最大特点是可以使用任何设备作为辅助屏幕。要获得真正的扩展桌面体验，Deskreen 应与虚拟显示适配器配合使用。此外，不需要虚拟显示适配器，您可以使用平板电脑或智能手机拥有带有 Deskreen 的提示器，因为 Deskreen 具有翻转屏幕模式，可以在平板电脑的 Web 浏览器中镜像计算机屏幕 (又名：水平翻转屏幕)。

项目链接：<https://deskreen.com/lang-zh_CN>

- ​Warp - 基于 Rust 的终端
Warp 是一款速度极快的基于 Rust 的GPU加速终端，旨在让您和您的团队更加高效。
这款终端的功能非常有用且好玩。并且在其他的终端上还没有见过这么完善的。而且因为是基于 Rust 所以速度应该还不错。
具体的演示效果可以去项目主页查看。
目前缺点是仅支持 MacOS。当然这个项目还是有计划支持 Linux，Windows和Web（WASM）的，等待并心怀希望吧。
项目链接：<https://www.warp.dev/>

- paper2gui - 让每个人都简单方便的使用前沿人工智能技术

一款面向普通人的AI桌面APP工具箱，免安装即开即用，已支持18+AI模型，内容涵盖语音合成、视频补帧、视频超分、目标检测、图片风格化、OCR识别等领域。支持Windows、Mac、Linux系统，未来还将适配安卓和苹果设备，另外还有小程序。

项目链接：<https://github.com/Baiyuetribe/paper2gui>

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

- YesPlayMusic - 高颜值的第三方网易云播放器

之前我一直使用的是 VScode 的网易云插件来听歌。虽然这样用起来还挺有趣的。但是每次听歌都要开个文本编辑器还是比较奇怪的。
所以我还是再下载了一个单独的客户端 YesPlayMusic 。拥有多平台支持，还有网页版可以使用。并且支持 UnblockNeteaseMusic，自动使用各类音源替换变灰歌曲链接。
当然最关键的是颜值很不错，虽然并不是我最爱的质感设计（仅一代）。但是苹果风也还不错。

项目链接：<https://github.com/qier222/YesPlayMusic>

- musicn - 🎵 一个下载高品质音乐的命令行工具

命令行的音乐下载工具，来源是咪咕音乐。不过如果使用第三方的网易云的话这个其实不太必要。

项目链接：<https://github.com/zonemeen/musicn>

- REAPER

REAPER是一个完整的计算机数字音频制作应用程序，提供完整的多轨音频和MIDI录音、编辑、处理、混音和母带制作工具集。  
项目链接：<http://reaper.fm/>  

- Ultraschall - 播客制作工具

暂时不支持 Linux，据说是有支持的计划的。  
REAPER 的博客制作特化插件，将 REAPER 变成播客制作神器。  
不过没有相关资料，软件只有德语和英文。相关的介绍也大多是德语的。完全看不懂，需要再摸一下。  
目前中文资料只找到少数派的两篇文章，但是也介绍的不是很详细。  

项目链接：<https://ultraschall.fm/>
少数派文章：
<https://sspai.com/post/57334>
<https://sspai.com/post/59437>

- LABS — Free Virtual Instruments

非常优秀的免费音色库，出了很多特殊的声音。而且各音色的封面设计非常好看，UI也很现代。
项目链接：<https://labs.spitfireaudio.com>

- Synthesizer V

使用人工智能技术和素片接续相结合而成的强力歌声合成引擎  
项目链接：<https://dreamtonics.com/synthesizerv/>

- OpenUtau - 开源的UTAU继任者

OpenUtau 是一个为 UTAU 社区提供的具有现代用户体验的开源编辑环境。  
UTAU 的上次更新已经是 2013/9/5，整体UI设计都还留在 XP 时代。OpenUtau 是复刻了 UTAU 的功能，添加了 Win、Linux、Mac 系统的支持。并且将代码进行了开源。

项目链接：<https://github.com/stakira/OpenUtau>

- ​LSP (Linux Studio Plugins) - 专为 Linux 开发的音频插件套装

前几天在AUR闲逛时发现的一个不错的开源项目。看插件类型还算是比较齐全的。
该项目的基本思想是填补GNU/Linux平台下缺乏良好且有用的插件的不足。
在对其他开源项目做出一些贡献之后，决定实现独立的插件分发。
粗略看了一下UI确实还挺好看的，很好地弥补了 Linux 平台插件的缺少。我之前一直全用的 REAPER 自带插件。（理论上可以用Wine兼容Windows的插件，但我个人不太喜欢）
不过这个插件真的没有任何中文介绍。只能看油管的生肉+AI字幕瞎猜了。

项目链接：<https://lsp-plug.in/>

- ReEQ - 免费的 REAPER 专用参数均衡器

众所周知，在音频处理领域，FabFilter（肥波）Pro Q3 是最强的参数均衡插件。但是800+的价格，可以买隔壁的插件全家桶了。可以说是足以让非专业用户望而却步。而且作为 Linux 用户，通过 wine 来使用是非常麻烦的。
那么有没有这样一款免费插件，可以在实现 Q3 “部分”功能的同时还能支持 Linux 系统呢？那么就要看这次的主角 ReEQ 了。
基本操作和 Q3 非常类似。双击添加点，按住 shift 键监听当前频段，滚轮调整宽度。UI的结构也很相似，就是精致程度差了很多。下载安装很简单，除了直接在论坛里下载之外，可以通过 ReaPack 进行安装。由于是 JSFX 插件，在软件大小和CPU占用方面非常友好。
缺点是比起 Q3 除了基础的EQ功能之外，也缺少了很多细节功能，需要其他插件配合使用。

项目链接：<https://forum.cockos.com/showthread.php?t=213501>

- ‍FamiStudio - 8-bit 音乐制作软件

支持 Windows、MacOS、Linux、Android 的 8-bit 音乐制作软件 。具体使用方式这个视频介绍的挺详细的。挺推荐观看的。

视频链接：<https://www.bilibili.com/video/BV1aU4y117f6>
项目链接：<https://famistudio.org/>

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

- FFmpeg  

神器，FFmpeg 是一个多媒体编解码器库，并提供了命令行前端。许多软件都使用了 FFmpeg 来进行音频和视频的编解码，特别是像 MPlayer 这样的多媒体播放器
常用命令：  
1.压制ass字幕

    ffmpeg -i input.mp4 -vcodec libx264 -preset medium -crf 23 -vf "ass=input.ass" output.mp4

2.精确时间拆分视频

    ffmpeg -ss 01:08:43 -to 01:12:00 -accurate_seek -i input.mp4 -codec copy -avoid_negative_ts 1 output.mp4

- biliup-app - b站全平台投稿客户端，支持多p投稿，稿件编辑

众所周知，阿B取消了分P。要想上传带分P的视频只能通过投稿工具。然而尴尬的是，客户端是不支持 Linux 。那应该如何解决这个问题呢？
最近我在 AUR 闲逛的时候发现了这个项目。BiliUP -app 一个bilibili第三方投稿客户端，可以支持Windows，Linux，macOS。

支持多p上传，支持线路切换、并发数控制，上海腾讯云可使用内网线路上传免流+大幅提速。
支持稿件编辑追加多p，可编辑网页端不能编辑的"是否转载"、"投稿分区"等。
低电磁力等级也可上传大于16G视频，最大32G。
支持多种登录方式，账号密码，短信，扫码，浏览器登录。

项目链接：<https://github.com/ForgQi/biliup-app>

## 图片

- GIMP  

GIMP 是一个免费的、分布式的图片润饰、图象制作和处理软件，内含几乎所有图象处理所需的功能，号称Linux下的PhotoShop。  

- Krita

偏向绘画而不是图片处理方面。对数位板兼容更好。  

- ​Lorien - 适用于Windows、Linux和macOS的无限画布绘图/白板应用程序。

Lorien是一款无限画布绘图/笔记应用程序，专注于性能、小存储文件和简单性。它不是基于像Krita、Gimp或Photoshop这样的位图图像；而是将笔划保存为点的集合，并在运行时进行渲染（有点像SVG）。它的主要设计目的是用作数字笔记本和头脑风暴工具。虽然它完全可以用来制作小草图和图表，但它并不意味着取代传统的对位图图像进行操作的艺术程序。它完全是在Godot游戏引擎中编写的。
我非常喜欢的点是他是直接单文件运行。并且速度是真的超级快。在你需要随手记录一些什么的时候不用等软件打开。

项目链接：<https://github.com/mbrlabs/Lorien>

- Curtail - Linux 的批量图片压缩工具

通常在 Windows 系统我会使用图压这个软件来进行图片的批量压缩。这个软件的好处是非常简单的操作。设置好压缩比例，或者目标大小直接把图片拖进来就行。  
而在Linux下我之前经常使用的是压缩图片的网站，来进行在线压缩。要上传、下载非常麻烦。最近发现了这一款 Curtail 图片压缩工具可以说接近完美地解决了我的压图问题。  
可以在首页选择有损压缩，或者无损压缩。比起图压只能选择有损压缩要好一些。压缩的等级也可以在设置里调整。压缩的方式也和图压一样，直接拖进软件就能完成压缩，非常方便。压缩效果方面，即使是有损压缩出来的图片不放大肉眼也基本看不出差别。还是挺好的。  
缺点是缺少一个压缩到某个大小的功能。只能按等级来压缩。不过直接压出来的大小基本都能直接满足我的要求，所以也还好。还有一个问题是压缩WEBP格式的图片时，默认的无损压缩等级反而会加大图片的大小。需要用有损压缩的方式会比较合适。  

项目链接：<https://github.com/Huluti/Curtail>

## 文本编辑器

- VScode

微软出品的开源文本编辑器，用着是真的香。

- Markmap - 将 Markdown 目录转换为思维导图的插件

可即时生成直观可视化的思维导图。思维导图可以放大缩小，全屏显示。或者直接下载svg图片格式，或者HTML网页。
有 VScode 还有 VIM/NeoVIM 插件可以选择。

项目链接：<https://github.com/gera2ld/markmap>
VScode 链接：<https://marketplace.visualstudio.com/items?itemName=gera2ld.markmap-vscode>

- nvim

vim 的升级版，比起其他编辑器打开速度更快。  

- Notepadqq - Linux 轻量级文本编辑器

在改一些简单的文本内容时，我通常会使用轻量化的文本编辑器。在 Windows 上我使用的是 Windedit ，而在 Linux 上我试用的几个文本编辑器其实都有各种各样的问题，比如 VScode 打开速度慢、Kata 缺少一些功能、系统自带的 Geany 各方面都挺不错，但是缺少一个很关键的功能：在关闭最后一个标签时关闭软件。
Notepadqq 可以说是完美符合我的需要。在功能上跟 Notepad++ 很像，但是增加了一些新的功能。打开速度也很不错。而且外观可以说是薄纱 Notepad++ 那 XP 年代的 UI 了。目前唯一的问题可能是插件系统还是实验性。不过现在的功能已经足够了没什么需要增加的。

项目链接：<https://notepadqq.com/>

- ​Kate - KDE的具有众多功能的文本编辑器

Kate 和 KDE 开发的其他软件一样支持多平台。
Kate 的功能非常丰富，可以让你更轻松地查看和编辑所有的文本文件。Kate 可以让你同时编辑和查看多个文件，既可以在标签页中查看，也可以在分割视图中查看，并且还附带了多种插件，包括一个嵌入式终端，可以让你直接从 Kate 中启动控制台命令，强大的搜索和替换插件，以及一个预览插件，可以让你看到你的 MD、HTML 甚至 SVG 的样子。
虽然在功能上挺强大的，但是比起 VScode 是略逊一筹。但是 Kate 的开启速度比 VScode 快不少。（不过比起 Geany 之类的轻量编辑器还是稍微慢一点）
还有钛山老师画的吉祥物很可爱

项目链接：<https://kate-editor.org/zh-cn/>

## 游戏

- Minecraft  

简评我一直都在玩的游戏，详细介绍请看

- GDLauncher 一个简单但功能强大的Minecraft自定义启动器，非常注重用户体验。

简洁易用的 UI
可快速搜索安装及管理整合包、MOD
可快速安装 Java

项目链接：<https://gdevs.io/>

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

- I3WM

比起桌面环境我更喜欢使用窗口管理器。  

- Adapta Theme  

一款自适应的 Gtk+ 主题，遵循 Material 设计指南。

- Papirus Icon Theme  

简评这个也是质感设计的图标包，跟adapta搭配起来还挺好看的。Linux 系统 SVG 图标主题，基于 Paper 主题并有一些额外的特性（如硬编码托盘支持，kde 颜色方案支持，libreoffice 图标主题，filezilla 主题，smplayer 主题...）以及其它的修改。这个主题适用于 GTK 以及 KDE。

- Nord - 一个北极风的蓝色调主题。

为干净整洁的设计模式而创建，以实现代码语法高亮显示和UI组件的最佳焦点和可读性。

本质上是一整套非常详细的配色规范。并且提供有各设计软件的色板文件，可以快速将这套配色应用到你想要的地方。

在示例中提供了非常多款 Linux 常用软件的配色实例，可以统一各应用程序的外观。

项目链接：<https://www.nordtheme.com/>

- FluentDark-fcitx5 - Fluent 风格深色主题，具有模糊效果和阴影

Fcitx 5 输入法的皮肤主题。个人认为是挺好看的。不过有一个比较尴尬的地方是这个皮肤是使用Kwin提供的模糊效果，因此需要在 KDE 或其他使用 Kwin 作为后端的桌面环境下使用才能有完整的效果。个人使用下来我在 XFCE 使用会变成半透明。不过感觉效果意外的挺好。

项目链接：<https://github.com/Reverier-Xu/FluentDark-fcitx5>

- 小赖字体 - 一款衍生于「濑户字体」「内海字体」「cjkFonts 全濑体」的中文手写字型。

本字体是 濑户字体 / 内海字体 的简体中文化改良，利用濑户/内海字体里原有的部件，对原字体中缺少的汉字进行补足，主要为 GB2312 及《通用规范汉字表》里的汉字，其余的汉字、谚文、特殊符号用 cjkFonts 全濑体 补全。  
该字体可显示 GB18030-2000 范围内的全部汉字（共 27484 个），以及《通用规范汉字表》里的全部汉字（共 8105 个），满足中国大陆用户的使用需要。此外可显示日文假名、谚文 （韩文、朝鲜文） 音节和思源黑体可以显示的特殊符号，可直接用作手机字体。

项目链接：<https://github.com/lxgw/kose-font>

- 勿忘黑体 - Don't forgetWW 免费实验性标题装饰字库字体

以普玛彭古和一些古文明为灵感创作的一款基于英语的装饰性字体，
你可以通过修改字体的间距，改变字与字的连接以达到传达不同感受的目的；
还可以将残缺部分拼接成新的图形，字体还包含连字图形和部分符号，小写字体会减少部分细节。
勿忘黑体是一款装饰性字体，不推荐使用在正文排版设计当中。
推荐使用场景：风格化标题、点线面装饰。

根据作者的说法，这款字体是可以免费商用的。

项目链接：<https://www.zcool.com.cn/work/ZNTk2MDc3NTY=.html>

- 方舟像素字体 - 开源的泛中日韩像素字体

开源的泛中日韩像素字体。支持 10、12 和 16 像素。目标是为像素风格的游戏开发提供一套可用于正文的开箱即用的字体解决方案。

这个项目不仅提供了全部的字形设计源文件，也提供了构建字体所需要的完整程序。

项目链接:<https://github.com/TakWolf/ark-pixel-font>

- Activate-linux - 移植到 Linux 的“激活 Windows”水印

日常在 AUR 闲逛时发现的一个搞怪项目。能够实现的功能只是为屏幕添加一个 Windows 系统的未激活水印。
支持 Linux、MacOS，支持中文，可自定义字体、颜色等。可以说功能意外的齐全。甚至还让人有种“可能开发出实用用法”的错觉。
这种无厘头项目虽然没用，但是我意外的挺喜欢的。已经给电脑用上了，孩子很喜欢。

项目链接：<https://github.com/MrGlockenspiel/activate-linux>

## 命令行

命令行对Linux来说依然非常重要，虽然这些桌面端的发行版可以完全离开命令行，但是使用命令行可以大幅提高使Linux系统的效率，而且……这是一件非常有趣而且逼格很高的事。

- Zsh  

 一款强大的命令行 shell。我在github写的文章里有过介绍。

进阶推荐《Zsh 开发指南》  

- Oh-my-zsh  

一个由社区驱动，优雅的 zsh 配置管理框架。

我使用时主题是 gentoo  
扩展：
sudo — 双击 ESC 键为当前命令  
zsh-autosuggestions — 类似 fish 的补全  

- Tmux - 独立，漂亮和多功能.tmux.conf配置文件

它让你在一个终端中在多个程序间方便地切换，分离他们（保持在后台运行）并另一个终端中重新连接上去。  

- oh my tmux - 独立，漂亮和多功能.tmux.conf配置文件

类似 oh my zsh 的配置，可以快速地美化 tmux。但是其实不能开箱即用，还需要调整一下配置文件。

项目链接：<https://github.com/gpakosz/.tmux>

- ​Zellij - Rust 编写的终端复用器

终端复用器的作用大家应该都挺熟悉的。当我们与终端的连接断开之后，可以让正在进行的命令在后台运行。再次打开的时候可以回到关闭前的命令。在远程到服务器时可以不用担心用到一半网络波动让进行中的工作丢失。不过现在很多人使用终端复用器的目的是为了附带的分屏功能。也是挺有意思的。
相关的软件之前我一直使用的是 Tmux 加上 oh-my-tmux 配置项目。但是这个方案还是有两点问题。首先是配置还是不够“开箱即用”，还是需要下载配置和修改细节设置。还有一点是我的记忆力确实越来越不行了。没有提示始终还是有点问题。
然后我找到的符合我使用需求的就是这个软件。除了解决了我的痛点，还有速度快、积极更新等优点。我还是非常喜欢的。

项目链接：<https://zellij.dev/>

- git  

Git 是一款免费和开源的分布式版本管理系统，被设计用来快速和高效地处理从小项目到大项目的一切内容。

- xdotool  

模拟按键的工具，可以做一些自动化。

- NeoFetch  

快速，高度定制化的系统信息获取脚本。

- The Fuck  

杰出的应用，它能纠正你的输入的错误命令。

- Zoxide - 一个智能CD命令，灵感来自Z和AutoJump

众所周知，Linux 里非常常用的移动命令是 CD 。但是 CD 命令作为一个历史悠久的命令，其实用起来有点麻烦。Zoxide 就是在 CD 命令的基础上增加了一些方便移动的功能。
可以记得最常使用哪些目录，因此只需输入部分标题即可“跳到”需要的位置。
而且在安装 fzf 命令之后还能有一个联动，可以进行目录的搜索。非常方便。
这个命令主要是使用 Rust 编写的。对多平台的支持也非常不错。在 Linux、MacOS、Windows、BSD、Android 都可以安装。
具体可以参考官方提供的动图演示。

项目链接：<https://github.com/ajeetdsouza/zoxide>

## 社交

- telegram

可以说是在聊天体验方面做的最好一款软件。

- 钉钉 - 官方 Linux 版

我所在的公司使用钉钉作为交流工具，所以钉钉的客户端是不可缺少的。之前我一直使用的是网友制作的开源客户端。因为是基于 electron 和钉钉网页版开发。使用起来体验其实会有点难受。
最近在 AUR 闲逛时突然发现，钉钉居然有官方版的 Linux 客户端。下载试用了一下还挺不错。除了没有夜间模式以及没办法关闭更新检测之外就没有什么问题了。

项目链接：<https://aur.archlinux.org/packages/dingtalk-bin/>

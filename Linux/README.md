
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
    - [Firefox](#firefox)
    - [Chromium](#chromium)
  - [下载工具](#下载工具)
    - [Persepolis Download Manager](#persepolis-download-manager)
    - [Syncthing](#syncthing)
    - [You-Get](#you-get)
    - [Send Anywhere](#send-anywhere)
  - [效率](#效率)
    - [Cerebro](#cerebro)
    - [CopyQ](#copyq)
    - [Double Commander](#double-commander)
    - [AngrySearch](#angrysearch)
  - [安全](#安全)
  - [音乐](#音乐)
    - [Netease Music](#netease-music)
    - [vocal](#vocal)
    - [Audacious](#audacious)
    - [Let's make music](#lets-make-music)
  - [视频](#视频)
    - [VLC](#vlc)
    - [Open Broadcaster Software(OBS)](#open-broadcaster-softwareobs)
    - [Kdenlive](#kdenlive)
    - [FFmpeg](#ffmpeg)
  - [图片](#图片)
    - [GIMP](#gimp)
    - [LibreCAD](#librecad)
  - [文本](#文本)
    - [Atom](#atom)
    - [Emacs](#emacs)
    - [VIM](#vim)
    - [IntelliJ IDEA](#intellij-idea)
    - [Typora](#typora)
  - [游戏](#游戏)
    - [Minecraft](#minecraft)
    - [CMPDL](#cmpdl)
  - [美化](#美化)
    - [GNOME](#gnome)
    - [Adapta Theme](#adapta-theme)
    - [Papirus Icon Theme](#papirus-icon-theme)
  - [命令行](#命令行)
    - [Zsh](#zsh)
    - [Oh-my-zsh](#oh-my-zsh)
    - [Tmux](#tmux)
    - [git](#git)
    - [Ranger](#ranger)
    - [xmodmap](#xmodmap)
    - [xdotool](#xdotool)
    - [NeoFetch](#neofetch)
    - [The Fuck](#the-fuck)
  - [其他](#其他)
    - [tele，gram  ，gram.org/](#telegram-gramorg)
    - [7zip](#7zip)
    - [Xmind](#xmind)
    - [CrossOver](#crossover)
    - [Gparted](#gparted)
    - [virtualbox](#virtualbox)
    - [undistract me](#undistract-me)
    - [搜狗输入法](#搜狗输入法)

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

## Manjaro  
如果嫌弃 Archlinux 麻烦的安装步骤。还可以使用 Archlinux 的下游发行版 [Manjaro](https://manjaro.org/) 。安装很无脑，基本可以做到开箱即用。并且有多种桌面环境可供选择。我试用过 I3WM 版本的 Manjaro ，默认的配置就非常的不错。我现在使用的配置文件就有一部分是抄的 Manjaro 。  
Manjaro 还有个转 Archlinux 的骚操作。亲测没什么问题，可以正常使用。  

## Deepin
[Deepin](https://www.deepin.org/download/) 是一个国产、相当傻瓜化、基于 Debian 的发行版。安装非常非常简单，将官方的 ISO 镜像文件解压后会有制作安装U盘的和直接硬盘安装的软件，直接无脑下一步就行。自带有一个能免费使用的 CrossOver。之前有段时间我的 Arch 被我玩坏了，而手上又刚好没有u盘，所以就试着换成了可以硬盘安装的 deepin。使用了一段时间感觉还挺不错的。非常的简单，默认的桌面环境是 DDE ，颜值挺不错的。也作了很多针对国内的优化，可以说是国内发行版里做的最良心的。

#  二、Linux 网站介绍
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
### Firefox

### Chromium
信仰加成浏览器，Chromium是Google为发展自家的浏览器Google Chrome而开启的计画，所以Chromium相当于Google Chrome的工程版或实验版（尽管Google Chrome本身也有β版），新功能会率先在Chromium上开放，待验证后才会应用在Google Chrome上，故Google Chrome的功能会相对落后但较稳定。
Chromium的更新速度很快，每隔数小时即有新的开发版本发布，而且可以免安装，下载zip封装版后解压缩即可使用（Windows下也有安装版）。Chrome虽然理论上也可以免安装，但Google仅提供安装版。
顺带一提，chrome 是闭源的，而chromium是开源的。

## 下载工具
### Persepolis Download Manager
PDM是一款封装了 Aria2 作为内核，并为其套上图形界面的开源免费下载软件。它能让你享受 Aria2 一切的特性，同时又帮助你完全跳过安装和配置 Aria2 那些繁琐的过程，并且有一个图形化的直观界面供你用鼠标进行操作，你就像用迅雷、Folx 等下载工具一样的简单明了，而不必再对着命令行发愁。
是的，PDM也是有Linux版的。

### Syncthing
Syncthing 最大的特色是采用了与 (BitTorrent Sync) 类似的 P2P 分布式技术，无需中心服务器，即可让多台设备互相实时同步文件，用过 的朋友都明白这种同步方式的优势了。它们两者的实现方式很相似，区别是 属于商业软件，需付费使用，在国内也已被土·啬，而 Syncthing 不仅完全免费且开源，相比 还增加了「文件版本控制」、「单向同步」等堪称杀手级的功能特性。

Syncthing 功能上非常接近于 ，不过说它是一款用于搭建网盘的服务器软件或者云存储服务应用似乎并不十分恰当，相较于 Seafile、NextCloud 等服务器工具，Syncthing 实际上更像是一款文件/文件夹同步工具。

你可以非常轻松简单地让同一路由器下的多台 PC 电脑、NAS 设备实现局域网互相同步，也可以在 VPS 服务器或 24 小时不关机且有公网 IP 的电脑上安装和配置 Syncthing，让其成为真正意义上的云同步网盘。

### You-Get  
You-Get是一款命令行工具，用来下载网页中的视频、音频、图片，支持众多网站，包含 41 家国内主流视频、音乐网站，如 网易云音乐、AB 站、百度贴吧、斗鱼、熊猫、爱奇艺、凤凰视频、酷狗音乐、乐视、荔枝FM、秒拍、腾讯视频、优酷土豆、央视网、芒果TV 等等，只需一个命令就能直接下载视频、音频以及图片回来，并且可以自动合并视频。而对于有弹幕的网站，比如 B 站，还可以将弹幕下载回来。

### Send Anywhere  
我在各设备间传输文件使用的软件，免费全平台的文件分享利器，支持的系统、设备多的吓人，甚至连 Windows phone 和 Kindle 都有，而且传输体验非常舒畅，UI也非常漂亮，真的良心。我现在已经抛弃 AirDroid 还有 TeamViewer 了。

## 效率
### Cerebro  
简介：开源生产力提升工具，类似之前介绍过的Listary。可用于执行命令, 打开应用, 打开网页, 快捷翻译, 搜索. 支持插件, 有很多插件可以使用。
下载去它的 GitHub releases 页面，直接在主页点击下载的是 .appimage 的包……

### CopyQ
类似ditto的剪贴板管理软件，CopyQ 能够存储文本、HTML、以及图像，具有标签页，可通过内置或外部编辑器修改所保存的内容。此外，它也支持拖拉操作、打标签、以及定制命令。

### Double Commander  
 Double Commander 是一款跨平台的开源双栏文件管理器。它受 Total Commander 启发并有自己的新想法。我经常听说 total command 是神器，也看过善用佳软的教学安利，可以说是神往已久，但是一直因为种种原因没有去用，刚好看到这个打算试试。

### AngrySearch  
 类似Everything的Linux 文件搜索，结果输入即得。

## 安全

## 音乐
### Netease Music  
 网易与 deepin 团队合作开发的Linux版，使用体验和其他平台的没什么差距。

### vocal  
 Linux 的播客软件，颜值很棒，操作简单。虽然我不常用电脑听播客，不过偶尔用用也不错。

### Audacious  
 免费，开源，跨平台的声音录制、编辑软件。

### Let's make music  
 在你的 PC 上制作音乐，创造旋律和节拍，合成，混音，编曲小样以及更多内容。

## 视频
### VLC  
 VLC 是一个免费且开源的跨平台媒体播放器以及框架，可以播放大多数格式的多媒体文件以及 DVS，音频 CD，VCD，以及各种流媒体协议。

### Open Broadcaster Software(OBS)  
 OBS在屏幕录制软件里还是挺有名的，开源、免费、操作简单，录制效果也很不错，很棒。

### Kdenlive  
 还不错的视频编辑软件，虽然功能没有 Adobe 家的强大，但对我来说已经足够了。
入门推荐看官方的这个： 

### FFmpeg  
 神器，FFmpeg 是一个多媒体编解码器库，并提供了命令行前端。许多软件都使用了 FFmpeg 来进行音频和视频的编解码，特别是像 MPlayer 这样的多媒体播放器。
入门教程推荐看这个： 

B站专栏： 

实际应用（B站专栏）： 

## 图片
### GIMP  
 GIMP 是一个免费的、分布式的图片润饰、图象制作和处理软件，内含几乎所有图象处理所需的功能，号称Linux下的PhotoShop。 GIMP在Linux系统推出时就风靡了许多绘图爱好者的喜爱，它的接口相当轻巧，但其功能却不输于专业的绘图软件；它提供了各种的影像处理工具、滤镜， 还有许多的组件模块，对于要制作一个又酷又炫的网页按钮或网站Logo来说是一个非常方便好用的绘图软件，因为它也提供了许多的组件模块，你只要稍加修改一下，便可制作出一个属于你的网页按钮或网站Logo。

教程推荐看善用佳软的文章，在文章末尾还有一些相关优秀教程的链接：  

视频（生肉）：  

### LibreCAD  
 虽然可以直接用 CrossOver 装 AutoCAD 但是尝试一下使用Linux版的 CAD 也是有必要的。在外观方面比 AutoCAD 高到不知道那里去了。不过其他各种功能有很多微妙的差距，比如说命令行不能按空格确定、偏移指令没找到、修剪之类的操作方式变了好多……图画出来是没啥问题，不过对我这种用惯了 AutoCAD 的人来说，还需要一段时间适应。
教程的话……官方Wiki（英文）： 

## 文本
### Atom  
 21 世纪的可 hack 文本编辑器。拥有大量的插件、主题，不仅仅能用作写代码，作为markdown编辑器也是不错的选择，再加上 git 相关的插件，能非常方便地修改GitHub上的内容。
我正在使用主题：
使用的插件有：
file-icons — 增加许多图标,在侧边蓝文件名前面的 icon。

filetype-color — 在标签栏不同格式文件显示不同的颜色的标题，支持二度设置

activate-power-mode — 超级酷炫的效果，不过

顺带一提，atom下载插件的速度很糟糕，推荐更换淘宝源:apm config set registry  

入门教程推荐：  

### Emacs  
 Emacs 是一个架构在编辑器上的集成环境，除了最基本的编辑功能，还可以完成文件管理、终端模拟、浏览网页、收发邮件、编译程序等工作。因其强大的功能被称为神的文本编辑器。

我使用的配置是直接用的spacemacs  

入门和进阶推荐观看这个项目，有视频和文本版： 

### VIM
 Vim是从vi发展出来的一个文本编辑器。代码补完、编译及错误跳转等方便编程的功能特别丰富，在程序员中被广泛使用。和Emacs并列成为类Unix系统用户最喜欢的编辑器。被称为文本编辑器之神。

我用的配置是 

入门和进阶推荐这个 

### IntelliJ IDEA  
 强大的 Java IDE。
教程可以看这个视频：  

### Typora  
 非常优秀的 Markdowm 编辑器，虽然 Atom 作为 Markdown 也是很棒的选择，不过这个使用起来更加舒服。导出选项丰富，界面简洁美观。「所见即所得」的编辑模式也方便。

具体介绍推荐少数派的这篇文章：  

## 游戏
### Minecraft  
简评我一直都在玩的游戏，详细介绍请看 

### CMPDL  
简评vazkii制作的整合包下载工具。
详细介绍推荐酒石酸的B站视频 

## 美化
### GNOME  
 GNOME 桌面环境是一个有吸引力且直观的的桌面，拥有大量的插件。
(虽然我现在并不是这个)

### Adapta Theme  
 一款自适应的 Gtk+ 主题，遵循 Material 设计指南。

### Papirus Icon Theme  
简评这个也是质感设计的图标包，跟adapta搭配起来还挺好看的。Linux 系统 SVG 图标主题，基于 Paper 主题并有一些额外的特性（如硬编码托盘支持，kde 颜色方案支持，libreoffice 图标主题，filezilla 主题，smplayer 主题...）以及其它的修改。这个主题适用于 GTK 以及 KDE。

## 命令行
命令行对Linux来说依然非常重要，虽然这些桌面端的发行版可以完全离开命令行，但是使用命令行可以大幅提高使Linux系统的效率，而且……这是一件非常有趣而且逼格很高的事。

### Zsh  
 一款强大的命令行 shell。我在github写的文章里有过介绍。

进阶推荐《Zsh 开发指南》  

### Oh-my-zsh  
 一个由社区驱动，优雅的 zsh 配置管理框架。

我使用时主题是 gentoo，之前用的是 agnoster
扩展：
git — 简化 git 命令
bebian — 简化 apt 指令
autojump — 快速跳转目录
sudo — 双击 ESC 键为当前命令
zsh-autosuggestions — 类似 fish 的补全
zsh-syntax-highlighting — 命令行的语法高亮
zsh-completions — 应该是自动补全，不过我没试出来怎么用，网上也没找到具体介绍……

### Tmux  
 它让你在一个终端中在多个程序间方便地切换，分离他们（保持在后台运行）并另一个终端中重新连接上去。以及还有好多事情可以做。据说是神器，不过我不会用，之后学习一下。
配置我用的是这个：  

### git  
 Git 是一款免费和开源的分布式版本管理系统，被设计用来快速和高效地处理从小项目到大项目的一切内容。

### Ranger  
 一款使用 VI 快捷键的终端文件管理器。还挺好用，不过不知道怎么才能看到隐藏文件夹。

### xmodmap
 xmodmap 是一个在 X 图形环境下用于修改键盘和鼠标按钮映射的工具。我习惯将大写锁定键设为Ctrl键，Ctrl键设为ESC键，ESC键设为Delete键。
教程：  

### xdotool  
 模拟按键的工具，可以做一些自动化，不过我还没搞好……

### NeoFetch  
 快速，高度定制化的系统信息获取脚本。

### The Fuck  
 杰出的应用，它能纠正你的输入的错误命令。

## 其他
### tele，gram  ，gram.org/
 可以说是在聊天体验方面做的最好一款软件。(虽然在酷安都已经是连名字都不能说的软件了……)

### 7zip
 解压缩……

### Xmind  
 脑图工具，免费版我觉得已经够用。

### CrossOver
 不需要虚拟机即可在Linux运行Windows的程序。在deepin免费。

### Gparted
 分区工具。

### virtualbox
 虚拟机

### undistract me  
简介：在长时间执行的终端命令结束的时候提醒你。

### 搜狗输入法
简介：deepin自带，使用起来还不错。
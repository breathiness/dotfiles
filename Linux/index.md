
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [零、前言](#零-前言)
- [一、发行版](#一-发行版)
  - [Archlinux](#archlinux)
  - [Manjaro](#manjaro)
  - [Deepin](#deepin)

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


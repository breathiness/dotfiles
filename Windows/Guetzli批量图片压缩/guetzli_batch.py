import os
import subprocess
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed

def compress_image(input_path, output_path):
    """使用Guetzli压缩单个图像"""
    try:
        # 检查输出文件是否已存在，避免重复处理
        if os.path.exists(output_path):
            print(f"跳过已存在的文件: {output_path}")
            return True, input_path
            
        subprocess.run(['guetzli', '--quality', '84', input_path, output_path], 
                      check=True, 
                      stderr=subprocess.PIPE,
                      stdout=subprocess.PIPE)
        return True, input_path
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode('utf-8') if e.stderr else str(e)
        print(f"压缩失败: {input_path}, 错误: {error_msg}")
        return False, input_path
    except Exception as e:
        print(f"处理 {input_path} 时发生意外错误: {str(e)}")
        traceback.print_exc()  # 打印完整的错误堆栈
        return False, input_path

def batch_compress(input_folder, max_workers=3):
    """批量压缩文件夹中的图像"""
    # 创建输出文件夹
    output_folder = input_folder.rstrip('/') + '-N'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"已创建输出文件夹: {output_folder}")
    
    # 获取支持的图像文件
    supported_extensions = ['.jpg', '.jpeg', '.png']
    files_to_compress = []
    
    for filename in os.listdir(input_folder):
        try:
            file_ext = os.path.splitext(filename.lower())[1]
            if file_ext in supported_extensions:
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                files_to_compress.append((input_path, output_path))
        except Exception as e:
            print(f"处理文件 {filename} 时出错，跳过此文件: {str(e)}")
            continue
    
    if not files_to_compress:
        print("没有找到可压缩的图像文件 (支持 JPG/JPEG/PNG)")
        return
    
    print(f"找到 {len(files_to_compress)} 个可压缩的图像文件")
    
    # 使用线程池并行处理 (每次3个)
    success_count = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(compress_image, inp, out) for inp, out in files_to_compress]
        
        for future in as_completed(futures):
            try:
                success, filepath = future.result()
                if success:
                    success_count += 1
                    print(f"成功压缩: {os.path.basename(filepath)}")
            except Exception as e:
                print(f"处理结果时出错: {str(e)}")
                continue
    
    print(f"\n压缩完成! 成功: {success_count}/{len(files_to_compress)}")
    print(f"失败: {len(files_to_compress)-success_count}")
    print(f"输出文件夹: {output_folder}")

def check_guetzli_installed():
    """检查Guetzli是否安装"""
    try:
        subprocess.run(['guetzli', '--help'], 
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE,
                     check=True)
        return True
    except FileNotFoundError:
        print("错误: Guetzli 未安装或不在系统路径中")
        print("请先安装Guetzli: https://github.com/google/guetzli")
        return False
    except subprocess.CalledProcessError:
        # 有些版本的guetzli --help会返回非零退出码，但工具实际可用
        return True

def main():
    """主程序循环"""
    # 检查Guetzli是否安装
    if not check_guetzli_installed():
        input("按Enter键退出...")
        return
    
    while True:
        try:
            # 获取用户输入
            print("\n" + "="*50)
            input_folder = input("请输入包含图像的文件夹路径(或按Enter退出): ").strip()
            
            if not input_folder:  # 用户直接按Enter退出
                print("程序退出")
                break
                
            # 验证文件夹是否存在
            if not os.path.isdir(input_folder):
                print(f"错误: '{input_folder}' 不是一个有效的文件夹路径")
                continue
            
            # 开始批量压缩
            batch_compress(input_folder)
            
            # 询问用户是否继续
            while True:
                choice = input("\n操作完成，请选择: [1]处理另一个文件夹 [Enter]退出: ").strip()
                if choice == '1':
                    break
                elif choice == '':
                    print("程序退出")
                    return
                else:
                    print("无效输入，请重新选择")
                    
        except KeyboardInterrupt:
            print("\n用户中断操作，是否退出?")
            choice = input("按Enter退出，或输入1继续: ").strip()
            if choice != '1':
                print("程序退出")
                break
        except Exception as e:
            print(f"发生未处理的错误: {str(e)}")
            traceback.print_exc()
            choice = input("\n发生错误，是否继续? [1]继续 [Enter]退出: ").strip()
            if choice != '1':
                print("程序退出")
                break

if __name__ == "__main__":
    main()
import os
import subprocess
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, as_completed

def compress_image(input_path, output_path):
    """使用Guetzli压缩单个图像"""
    try:
        subprocess.run(['guetzli', '--quality', '84', input_path, output_path], check=True)
        return True, input_path
    except subprocess.CalledProcessError as e:
        print(f"压缩失败: {input_path}, 错误: {e}")
        return False, input_path
    except Exception as e:
        print(f"处理 {input_path} 时发生意外错误: {e}")
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
        file_ext = os.path.splitext(filename.lower())[1]
        if file_ext in supported_extensions:
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            files_to_compress.append((input_path, output_path))
    
    if not files_to_compress:
        print("没有找到可压缩的图像文件 (支持 JPG/JPEG/PNG)")
        return
    
    print(f"找到 {len(files_to_compress)} 个可压缩的图像文件")
    
    # 使用线程池并行处理 (每次3个)
    success_count = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(compress_image, inp, out) for inp, out in files_to_compress]
        
        for future in as_completed(futures):
            success, filepath = future.result()
            if success:
                success_count += 1
                print(f"成功压缩: {os.path.basename(filepath)}")
    
    print(f"\n压缩完成! 成功: {success_count}/{len(files_to_compress)}")

if __name__ == "__main__":
    # 获取用户输入
    input_folder = input("请输入包含图像的文件夹路径: ").strip()
    
    # 验证文件夹是否存在
    while not os.path.isdir(input_folder):
        print(f"错误: '{input_folder}' 不是一个有效的文件夹路径")
        input_folder = input("请重新输入有效的文件夹路径: ").strip()
    
    # 检查Guetzli是否安装
    try:
        subprocess.run(['guetzli', '--help'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("错误: Guetzli 未安装或不在系统路径中")
        print("请先安装Guetzli: https://github.com/google/guetzli")
        exit(1)
    
    # 开始批量压缩
    batch_compress(input_folder)
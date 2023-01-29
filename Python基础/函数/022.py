# os 与 shutil 模块
# os模块具有 新建/删除
# os.mknod 创建文件
# os.remove 删除文件
# os.mkdir 创建目录(文件夹)
# os.rmdir 删除目录(文件夹)
# os.rename 对文件，目录重命名
# os.makedirs 递归创建文件夹
# os.removedirs 递归删除文件夹(空文件夹)

# -- shutil模块 复制/移动/
# copyfileobj(fsrc,fdst[,length=16*1024]) 复制文件 (length的单位是字符(表达一次读多少个字符))
# copyfile(src,dst) # 单纯的仅复制文件内容，底层调用了copyfileobj
# copymode(src,dst) # 单纯的仅复制文件权限，不包括内容 (虚拟机共享目录都是777)
# copystat(src,dst) # 复制所有状态信息，包括权限，组，用户，修改时间等，不包括内容
# copy(src,dst) # 复制文件权限和内容
# copy2(src,dst) # 复制文件权限和内容，还包括权限，组，用户，时间等
# copytree(src,dst) # 拷贝文件夹里所有内容(递归拷贝)
# rmtree(path) # 删除当前文件夹及其中所有内容(递归删除)
# move(path1,path2) # 移动文件或者文件夹
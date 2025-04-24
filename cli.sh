function ag {
    # 检查是否有管道输入
    if ($input.MoveNext()) {
        # 重置迭代器以便再次读取
        $input.Reset()
        
        # 收集所有管道输入
        $pipeContent = $input | Out-String
        
        # 将管道内容通过临时文件传给 Python
        $tempFile = [System.IO.Path]::GetTempFileName()
        $pipeContent | Set-Content -Path $tempFile -Encoding UTF8
        
        # 使用 -m stdin 模式并从临时文件读取
        C:\Develop\miniconda3\python.exe C:\Develop\common\ag_cli\ag.py -m stdin < $tempFile
        
        # 清理临时文件
        Remove-Item -Path $tempFile
    } else {
        # 没有管道输入，直接传递参数
        C:\Develop\miniconda3\python.exe C:\Develop\common\ag_cli\ag.py $args
    }
}
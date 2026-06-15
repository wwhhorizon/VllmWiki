# vllm-project/vllm#10575: [Installation]: Segmentation fault when building Docker container on WSL

| 字段 | 值 |
| --- | --- |
| Issue | [#10575](https://github.com/vllm-project/vllm/issues/10575) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Segmentation fault when building Docker container on WSL

### Issue 正文摘录

### Your current environment ```text escription I am encountering a segmentation fault error when building the Docker container for VLLM on WSL following the instructions for CPU installation. Steps to Reproduce Follow the CPU installation instructions from [the documentation](vscode-file://vscode-app/c:/Users/NicolasFERRARA/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html). Run the Docker build command. Error Message: subprocess.CalledProcessError: Command '['cmake', '/workspace/vllm', '-G', 'Ninja', '-DCMAKE_BUILD_TYPE=RelWithDebInfo', '-DVLLM_TARGET_DEVICE=cpu', '-DCMAKE_C_COMPILER_LAUNCHER=ccache', '-DCMAKE_CXX_COMPILER_LAUNCHER=ccache', '-DCMAKE_CUDA_COMPILER_LAUNCHER=ccache', '-DCMAKE_HIP_COMPILER_LAUNCHER=ccache', '-DVLLM_PYTHON_EXECUTABLE=/usr/bin/python3', '-DVLLM_PYTHON_PATH=/workspace/vllm:/usr/lib/python310.zip:/usr/lib/python3.10:/usr/lib/python3.10/lib-dynload:/usr/local/lib/python3.10/dist-packages:/usr/lib/python3/dist-packages:/usr/local/lib/python3.10/dist-packages/setuptools/_vendor', '-DFETCHCONTENT_BASE_DIR=/workspace/vllm/.deps', '-DCMAKE_JOB_POOL_COMPILE:STRING=compile', '-DCMAKE_JOB_POOLS:STRIN...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: Segmentation fault when building Docker container on WSL installation;stale ### Your current environment ```text escription I am encountering a segmentation fault error when building the Docker container
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: PILER_LAUNCHER=ccache', '-DCMAKE_CXX_COMPILER_LAUNCHER=ccache', '-DCMAKE_CUDA_COMPILER_LAUNCHER=ccache', '-DCMAKE_HIP_COMPILER_LAUNCHER=ccache', '-DVLLM_PYTHON_EXECUTABLE=/usr/bin/python3', '-DVLLM_PYTHON_PATH=/workspac...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: r VLLM on WSL following the instructions for CPU installation. Steps to Reproduce Follow the CPU installation instructions from [the documentation](vscode-file://vscode-app/c:/Users/NicolasFERRARA/AppData/Local/Programs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rm -rf dist" did not complete successfully: exit code: 139 Additional Information Environment: Operating System: WSL (Windows Subsystem for Linux) Docker version 27.3.1, build ce12230 Version WSL : 2.3.26.0 ``` ### How...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Segmentation fault when building Docker container on WSL installation;stale ### Your current environment ```text escription I am encountering a segmentation fault error when building the Docker container for VLLM on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

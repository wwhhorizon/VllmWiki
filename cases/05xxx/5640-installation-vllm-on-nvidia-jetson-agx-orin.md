# vllm-project/vllm#5640: [Installation]: vllm on NVIDIA jetson AGX orin

| 字段 | 值 |
| --- | --- |
| Issue | [#5640](https://github.com/vllm-project/vllm/issues/5640) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vllm on NVIDIA jetson AGX orin

### Issue 正文摘录

### Your current environment ```text root@jetson:/workspace# python collect_env.py File "collect_env.py", line 724 print(msg, file=sys.stderr) ^ SyntaxError: invalid syntax root@jetson:/workspace# python3 collect_env.py Collecting environment information... PyTorch version: 2.0.0a0+ec3941ad.nv23.02 Is debug build: False CUDA used to build PyTorch: 11.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (aarch64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.25.2 Libc version: glibc-2.31 Python version: 3.8.10 (default, Nov 14 2022, 12:59:47) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.10.120-tegra-aarch64-with-glibc2.29 Is CUDA available: True CUDA runtime version: 11.4.315 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Probably one of the following: /usr/lib/aarch64-linux-gnu/libcudnn.so.8.6.0 /usr/lib/aarch64-linux-gnu/libcudnn_adv_infer.so.8.6.0 /usr/lib/aarch64-linux-gnu/libcudnn_adv_train.so.8.6.0 /usr/lib/aarch64-linux-gnu/libcudnn_cnn_infer.so.8.6.0 /usr/lib/aarch64-linux-gnu/libcudnn_cnn_train.so.8.6.0 /usr/l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: vllm on NVIDIA jetson AGX orin installation;stale ### Your current environment ```text root@jetson:/workspace# python collect_env.py File "collect_env.py", line 724 print(msg, file=sys.stderr)
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ation... PyTorch version: 2.0.0a0+ec3941ad.nv23.02 Is debug build: False CUDA used to build PyTorch: 11.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (aarch64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: root@jetson:/workspace# python3 collect_env.py Collecting environment information... PyTorch version: 2.0.0a0+ec3941ad.nv23.02 Is debug build: False CUDA used to build PyTorch: 11.4 ROCM used to build PyTorch: N/A OS: U...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: vllm on NVIDIA jetson AGX orin installation;stale ### Your current environment ```text root@jetson:/workspace# python collect_env.py File "collect_env.py", line 724 print(msg, file=sys.stderr) ^ SyntaxEr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: formation... PyTorch version: 2.0.0a0+ec3941ad.nv23.02 Is debug build: False CUDA used to build PyTorch: 11.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (aarch64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

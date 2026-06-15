# vllm-project/vllm#10615: [Usage]:  Does speculative decoding support pipeline parallelism ? 

| 字段 | 值 |
| --- | --- |
| Issue | [#10615](https://github.com/vllm-project/vllm/issues/10615) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:  Does speculative decoding support pipeline parallelism ? 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` --2024-11-25 12:55:12-- https://raw.githubusercontent.com/vllm-project/vllm/main/collect_env.py Resolving mgt (mgt)... 172.16.8.200 Connecting to mgt (mgt)|172.16.8.200|:8890... connected. Proxy request sent, awaiting response... 200 OK Length: 26218 (26K) [text/plain] Saving to: ‘collect_env.py.1’ collect_env.py.1 100%[========================================================================================>] 25.60K --.-KB/s in 0.05s 2024-11-25 12:55:13 (561 KB/s) - ‘collect_env.py.1’ saved [26218/26218] Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0 Clang version: 14.0.6 CMake version: version 3.25.1 Libc version: glibc-2.36 Python version: 3.10.15 (main, Oct 3 2024, 07:27:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.1.0-26-amd64-x86_64-with-glibc2.36 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-PCIE-40GB GPU 1: NVI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: py.1’ saved [26218/26218] Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Usage]: Does speculative decoding support pipeline parallelism ? usage;stale ### Your current environment ```text The output of `python collect_env.py` --2024-11-25 12:55:12-- https://raw.githubusercontent.com/vllm-pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: Does speculative decoding support pipeline parallelism ? usage;stale ### Your current environment ```text The output of `python collect_env.py` --2024-11-25 12:55:12-- https://raw.githubusercontent.com/vllm-pro...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: nvironment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: KB/s) - ‘collect_env.py.1’ saved [26218/26218] Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Lin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

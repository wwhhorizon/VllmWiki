# vllm-project/vllm#10147: [Installation]: where is vllm.envs

| 字段 | 值 |
| --- | --- |
| Issue | [#10147](https://github.com/vllm-project/vllm/issues/10147) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: where is vllm.envs

### Issue 正文摘录

### Your current environment not found vllm.envs in vllm source code git clone https://github.com/vllm-project/vllm.git ```text python collect_env.py from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm.envs' ``` the envs from python -m torch.utils.collect_env ================================================================================== /data/anaconda3/envs/bvllm/lib/python3.10/runpy.py:126: RuntimeWarning: 'torch.utils.collect_env' found in sys.modules after import of package 'torch.utils', but prior to execution of 'torch.utils.collect_env'; this may result in unpredictable behaviour warn(RuntimeWarning(msg)) Collecting environment information... PyTorch version: 2.5.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.5 Libc version: glibc-2.31 Python version: 3.10.15 (main, Oct 3 2024, 07:27:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-107-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOA...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: where is vllm.envs installation;stale ### Your current environment not found vllm.envs in vllm source code git clone https://github.com/vllm-project/vllm.git ```text python collect_env.py from vllm
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.5.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: edictable behaviour warn(RuntimeWarning(msg)) Collecting environment information... PyTorch version: 2.5.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ties Versions of relevant libraries: [pip3] numpy==2.1.2 [pip3] pytorch-triton==3.1.0+cf34004b8a [pip3] torch==2.5.1+cu118 [pip3] torchaudio==2.5.1+cu118 [pip3] torchvision==0.20.1+cu118 [pip3] triton==3.1.0 [conda] num...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: where is vllm.envs installation;stale ### Your current environment not found vllm.envs in vllm source code git clone https://github.com/vllm-project/vllm.git ```text python collect_env.py from vllm.envs...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

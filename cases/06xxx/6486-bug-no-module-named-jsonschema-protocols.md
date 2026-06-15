# vllm-project/vllm#6486: [Bug]: No module named `jsonschema.protocols`. 

| 字段 | 值 |
| --- | --- |
| Issue | [#6486](https://github.com/vllm-project/vllm/issues/6486) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: No module named `jsonschema.protocols`. 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... /home/ubuntu/.local/lib/python3.8/site-packages/torch/cuda/__init__.py:118: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11060). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at ../c10/cuda/CUDAFunctions.cpp:108.) return torch._C._cuda_getDeviceCount() > 0 WARNING 07-16 23:02:53 _custom_ops.py:14] Failed to import from vllm._C with ImportError("/lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found (required by /home/ubuntu/.local/lib/python3.8/site-packages/vllm/_C.abi3.so)") PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.24.3 Libc version: glibc-2.31 Python version: 3.8.10...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: CUDA initialization: The NVIDIA driver on your system is too old (found version 11060). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx A...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ent information... /home/ubuntu/.local/lib/python3.8/site-packages/torch/cuda/__init__.py:118: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11060). Please update your GPU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```text The output of `python collect_env.py` Collecting environment information... /home/ubuntu/.local/lib/python3.8/site-packages/torch/cuda/__init__.py:118: UserWarning: CUDA initialization: The NVIDIA driver on your...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: No module named `jsonschema.protocols`. bug;unstale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... /home/ubuntu/.local/lib/python3.8/site-packages...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.42.4 [pip3] triton==2.3.1 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.2 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

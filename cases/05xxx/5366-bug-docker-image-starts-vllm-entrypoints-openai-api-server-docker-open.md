# vllm-project/vllm#5366: [Bug]: Docker image starts vllm.entrypoints.openai.api_server , Docker opens port 8000 but vllm isn't listening on 8000 

| 字段 | 值 |
| --- | --- |
| Issue | [#5366](https://github.com/vllm-project/vllm/issues/5366) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker image starts vllm.entrypoints.openai.api_server , Docker opens port 8000 but vllm isn't listening on 8000 

### Issue 正文摘录

### Your current environment Please note this is inside a Docker container built locally, so the collect_env.py was run as `docker exec -it vllm-openai sh -c '/usr/bin/python3 /vllm-workspace/collect_env.py'` ```text docker exec -it vllm-openai sh -c '/usr/bin/python3 /vllm-workspace/collect_env.py' Collecting environment information... logging interval: 5 PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.0-35-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA P104-100 Nvidia driver version: 550.78 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Ord...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: Docker image starts vllm.entrypoints.openai.api_server , Docker opens port 8000 but vllm isn't listening on 8000 bug ### Your current environment Please note this is inside a Docker container built locally, so th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: usr/bin/python3 /vllm-workspace/collect_env.py' Collecting environment information... logging interval: 5 PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: . logging interval: 5 PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT disabled Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Mitigation; IBRS Vulnerabilit...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 8000 --model=astronomer/Llama-3-8B-Instruct-GPTQ-4-Bit --enforce-eager --dtype=half --gpu-memory-utilization 0.95 --tensor-parallel-size=1 root 59 0 0 14:40 pts/0 Rs+ 0:00 ps -ef ww ``` install nettools: `docker exec -i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

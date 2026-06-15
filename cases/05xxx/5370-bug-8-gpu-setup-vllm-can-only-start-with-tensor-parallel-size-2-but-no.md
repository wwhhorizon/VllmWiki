# vllm-project/vllm#5370: [Bug]: 8 GPU setup - vLLM can only start with --tensor-parallel-size=2 but not 4 or 8

| 字段 | 值 |
| --- | --- |
| Issue | [#5370](https://github.com/vllm-project/vllm/issues/5370) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 8 GPU setup - vLLM can only start with --tensor-parallel-size=2 but not 4 or 8

### Issue 正文摘录

### Your current environment Please note that this is inside Docker, and this was collected after several of the GPUs locked up as a result of this issue, so it has GPU Topology: Could not collect. However, this is a 8 x P106-100 GPUs rig. All GPUs are working on their own, working with ollama and working in pairs, but never `--tensor-parallel-size=4` or `--tensor-parallel-size=8` When started with 4 or 8, the model starts to load and at some point during the process one , then two or more GPUs lock up (those with fans start spinning like crazy) . In some cases 5 out of 8 become unresponsive and computer needs to be rebooted. Will appreciate any help or a nudge in the right direction with multi GPU setup ```text docker exec -it vllm-openai sh -c '/usr/bin/python3 /vllm-workspace/collect_env.py' Collecting environment information... logging interval: 5 /usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py:619: UserWarning: Can't initialize NVML warnings.warn("Can't initialize NVML") PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: bug;stale ### Your current environment Please note that this is inside Docker, and this was collected after several of the GPUs locked up as a result of this issue, so it has GPU Topology: Could not collect. However, th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 8 x P106-100 GPUs rig. All GPUs are working on their own, working with ollama and working in pairs, but never `--tensor-parallel-size=4` or `--tensor-parallel-size=8` When started with 4 or 8, the model starts to load a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: p - vLLM can only start with --tensor-parallel-size=2 but not 4 or 8 bug;stale ### Your current environment Please note that this is inside Docker, and this was collected after several of the GPUs locked up as a result...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ion... logging interval: 5 /usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py:619: UserWarning: Can't initialize NVML warnings.warn("Can't initialize NVML") PyTorch version: 2.3.0+cu121 Is debug build: False...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.3 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

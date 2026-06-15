# vllm-project/vllm#39682: [BUGS] vLLM V1 Engine Hangs After Weight Loading on Blackwell (sm_121) Multi-Node Ray Setup (TP=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#39682](https://github.com/vllm-project/vllm/issues/39682) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [BUGS] vLLM V1 Engine Hangs After Weight Loading on Blackwell (sm_121) Multi-Node Ray Setup (TP=2)

### Issue 正文摘录

I am experiencing an indefinite hang during the memory profiling stage after model weights have successfully loaded. Hardware: 2x NVIDIA Blackwell GPUs (Distributed: 1 per node across 2 nodes) vLLM Version: 0.19.1+ (V1 Engine enabled) Interconnect: ConnectX-7 (RoCE/Ethernet) Model: Qwen3-30B-A3B (FP8) Serving Command: vllm serve Qwen/Qwen3-30B-A3B --tensor-parallel-size 2 --distributed-executor-backend ray --quantization fp8 --kv-cache-dtype fp8 --enforce-eager ### The BUg The Issue: The logs show that model weights (approx 14.53 GiB) load successfully on both nodes. However, the process hangs immediately after. I do not see the "Profiling KV cache" or "Uvicorn running" messages. Logs: (EngineCore pid=...) INFO ... Model loading took 14.53 GiB memory and 172.4 seconds (Stuck here indefinitely) My attempt to fix it: Used --enforce-eager to skip CUDA graph capture. Set VLLM_DISABLE_FRONTEND_MULTIPROCESSING=1, but received a warning that the variable is unknown/unsupported in this version. Set NCCL_P2P_DISABLE=1 and increased Ray CGRAPH timeouts. Lowered --gpu-memory-utilization to 0.7. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [BUGS] vLLM V1 Engine Hangs After Weight Loading on Blackwell (sm_121) Multi-Node Ray Setup (TP=2) bug I am experiencing an indefinite hang during the memory profiling stage after model weights have successfully loaded....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: enabled) Interconnect: ConnectX-7 (RoCE/Ethernet) Model: Qwen3-30B-A3B (FP8) Serving Command: vllm serve Qwen/Qwen3-30B-A3B --tensor-parallel-size 2 --distributed-executor-backend ray --quantization fp8 --kv-cache-dtype...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ading on Blackwell (sm_121) Multi-Node Ray Setup (TP=2) bug I am experiencing an indefinite hang during the memory profiling stage after model weights have successfully loaded. Hardware: 2x NVIDIA Blackwell GPUs (Distri...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: -parallel-size 2 --distributed-executor-backend ray --quantization fp8 --kv-cache-dtype fp8 --enforce-eager ### The BUg The Issue: The logs show that model weights (approx 14.53 GiB) load successfully on both nodes. How...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: experiencing an indefinite hang during the memory profiling stage after model weights have successfully loaded. Hardware: 2x NVIDIA Blackwell GPUs (Distributed: 1 per node across 2 nodes) vLLM Version: 0.19.1+ (V1 Engin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

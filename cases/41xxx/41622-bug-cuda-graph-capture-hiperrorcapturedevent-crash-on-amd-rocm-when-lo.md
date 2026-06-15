# vllm-project/vllm#41622: [Bug]: cuda graph capture hipErrorCapturedEvent crash on AMD ROCM when LoRA is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#41622](https://github.com/vllm-project/vllm/issues/41622) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: cuda graph capture hipErrorCapturedEvent crash on AMD ROCM when LoRA is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running vLLM on AMD ROCm GPUs with LoRA enabled and tensor parallelism > 1, the engine crashes during CUDA graph capture with hipErrorCapturedEvent across all ranks. This happens for any model with LoRA enabled. The same config on Nvidia CUDA GPUs deploys just fine. `--enforce-eager` allows it to run but performance is predictably terrible without graph capture. Running the models without LoRA also deploys just fine. vllm commit 6ec9bbec384b14401f901af189754f7d8a6754e2 installed from source Start command used: ``` vllm serve /home/arli/models/Llama-3.3-70B-Instruct-GPTQModel-Int8 \ --port 8000 \ --scheduling-policy priority \ --max-num-seqs 16 \ -tp 8 \ --attention-backend TRITON_ATTN \ --dtype float16 \ --gpu-memory-utilization 0.95 --max-model-len 32768 \ --max-num-batched-tokens 1024 \ --served-model-name Llama-3.3-70B-Instruct \ --enable-lora --max-lora-rank 64 --max-loras 1 --max-cpu-loras 1 --lora-modules \ test-lora=/home/arli/loras-70b/Llama-3.3-70B-ArliAI-RPMax-v3-LoRA \ ``` Crash dump: ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 0%| | 0/14 [00:00 , std::allocator >) + 0x98 (0x700a67970648 in /home/...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: cuda graph capture hipErrorCapturedEvent crash on AMD ROCM when LoRA is enabled bug;rocm ### Your current environment ### 🐛 Describe the bug When running vLLM on AMD ROCm GPUs with LoRA enabled and tensor paralle...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ArliAI-RPMax-v3-LoRA \ ``` Crash dump: ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 0%| | 0/14 [00:00 , std::allocator >) + 0x98 (0x700a67970648 in /hom
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: deploys just fine. vllm commit 6ec9bbec384b14401f901af189754f7d8a6754e2 installed from source Start command used: ``` vllm serve /home/arli/models/Llama-3.3-70B-Instruct-GPTQModel-Int8 \ --port 8000 \ --scheduling-polic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: apture with hipErrorCapturedEvent across all ranks. This happens for any model with LoRA enabled. The same config on Nvidia CUDA GPUs deploys just fine. `--enforce-eager` allows it to run but performance is predictably...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: \ --scheduling-policy priority \ --max-num-seqs 16 \ -tp 8 \ --attention-backend TRITON_ATTN \ --dtype float16 \ --gpu-memory-utilization 0.95 --max-model-len 32768 \ --max-num-batched-tokens 1024 \ --served-model-name...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | > + 0x9caa4 (0x7b73bea9caa4 in /lib/x86_64-linux-gnu/libc.so.6) frame #4: <unknown function> + 0x129c6c (0x7b73beb29c6c in /lib/x86_64-linux-gnu/libc.so.6) (enginecore pid=26621)… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | m/.venv/lib/python3.12/site-packages/torch/lib/libtorch_hip.so) frame #6: c10d::processgroupnccl::watchdog::run() + 0x14f (0x7b7389a9a33f in /home/arli/vllm-amd/vllm/.venv/lib/pyt… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | m/.venv/lib/python3.12/site-packages/torch/lib/libtorch_hip.so) frame #7: <unknown function> + 0xecdb4 (0x7b730e2ecdb4 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknown… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

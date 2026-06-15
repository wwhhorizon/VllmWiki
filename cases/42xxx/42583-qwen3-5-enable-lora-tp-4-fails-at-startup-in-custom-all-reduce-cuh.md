# vllm-project/vllm#42583: Qwen3.5 + --enable-lora + TP=4 fails at startup in custom_all_reduce.cuh

| 字段 | 值 |
| --- | --- |
| Issue | [#42583](https://github.com/vllm-project/vllm/issues/42583) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Qwen3.5 + --enable-lora + TP=4 fails at startup in custom_all_reduce.cuh

### Issue 正文摘录

### Summary Starting the vLLM OpenAI server with a Qwen3.5 model, tensor parallel size 4, and LoRA enabled fails during engine startup unless custom all-reduce is disabled. The failure happens before any adapter is loaded; starting the server with `--enable-lora --max-lora-rank 64 --max-loras 2` is enough to hit the failing path. ### Environment - GPUs: NVIDIA H200, single node - vLLM: 0.19.0 - Python: 3.10 - Model: local Qwen3.5-9B HF checkpoint - Tensor parallel: 4 - LoRA flags: `--enable-lora --max-lora-rank 64 --max-loras 2` ### Minimal command ```bash export VLLM_ALLOW_RUNTIME_LORA_UPDATING=1 python -m vllm.entrypoints.openai.api_server \ --model /path/to/Qwen3.5-9B \ --served-model-name qwen35 \ --host 127.0.0.1 \ --port 8899 \ --tensor-parallel-size 4 \ --max-model-len 32768 \ --gpu-memory-utilization 0.85 \ --trust-remote-code \ --enable-prefix-caching \ --enable-lora \ --max-lora-rank 64 \ --max-loras 2 ``` ### Observed failure The server never opens `/v1/models`. The worker logs contain: ```text Failed: Cuda error /workspace/csrc/custom_all_reduce.cuh:455 'invalid argument' Worker proc VllmWorker-3 died unexpectedly, shutting down executor. EngineCore failed to start. .....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Qwen3.5 + --enable-lora + TP=4 fails at startup in custom_all_reduce.cuh ### Summary Starting the vLLM OpenAI server with a Qwen3.5 model, tensor parallel size 4, and LoRA enabled fails during engine startup unless cust
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on. performance distributed_parallel;frontend_api;model_support cuda env_dependency Summary
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rver never opens `/v1/models`. The worker logs contain: ```text Failed: Cuda error /workspace/csrc/custom_all_reduce.cuh:455 'invalid argument' Worker proc VllmWorker-3 died unexpectedly, shutting down executor. EngineC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: failed to start. ... RuntimeError: cancelled ... TimeoutError: Timed out waiting for engine core processes to start. ``` ### Workaround The same model and environment start successfully when adding: ```bash --enforce-ea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

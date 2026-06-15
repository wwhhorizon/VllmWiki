# vllm-project/vllm#19254: [Bug]: N-gram speculative decoding performs slower than Qwen3-32B-FP8 with vLLM 0.9.0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#19254](https://github.com/vllm-project/vllm/issues/19254) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: N-gram speculative decoding performs slower than Qwen3-32B-FP8 with vLLM 0.9.0.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Why is n-gram speculative decoding performing slower than the baseline on Qwen3-32B-FP8? I'm using vLLM version 0.9.0.1 with H20 GPU. I have tried various combinations of num_speculative_tokens/prompt_lookup_max including 5/4, 3/3, and 2/2, but all show the same slower performance compared to the original setup. ```bash VLLM_FLASH_ATTN_VERSION=3 VLLM_USE_V1=1 vllm serve /mnt/models/Qwen/Qwen3-32B-FP8 --tensor-parallel-size 4 --speculative_config '{"method": "ngram", "num_speculative_tokens": 3, "prompt_lookup_max":3}' ``` Some logs for testing with ShareGPT: ```text INFO 06-06 14:20:34 [loggers.py:116] Engine 000: Avg prompt throughput: 11244.6 tokens/s, Avg generation throughput: 267.6 tokens/s, Running: 337 reqs, Waiting: 633 reqs, GPU KV cache usage: 9.5%, Prefix cache hit rate: 0.5% INFO 06-06 14:20:34 [metrics.py:86] SpecDecoding metrics: Draft acceptance rate: 38.8%, Mean acceptance length: 2.16, Accepted: 150 tokens, Drafted: 387 tokens, Per-position acceptance rate: 0.543, 0.357, 0.264 INFO 06-06 14:20:44 [loggers.py:116] Engine 000: Avg prompt throughput: 11528.5 tokens/s, Avg generation throughput: 826.0 tokens/s, Runni...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: N-gram speculative decoding performs slower than Qwen3-32B-FP8 with vLLM 0.9.0.1 bug;stale ### Your current environment ### 🐛 Describe the bug Why is n-gram speculative decoding performing slower than the baselin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ing performing slower than the baseline on Qwen3-32B-FP8? I'm using vLLM version 0.9.0.1 with H20 GPU. I have tried various combinations of num_speculative_tokens/prompt_lookup_max including 5/4, 3/3, and 2/2, but all s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: N-gram speculative decoding performs slower than Qwen3-32B-FP8 with vLLM 0.9.0.1 bug;stale ### Your current environment ### 🐛 Describe the bug Why is n-gram speculative decoding performing slower than the baselin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: N-gram speculative decoding performs slower than Qwen3-32B-FP8 with vLLM 0.9.0.1 bug;stale ### Your current environment ### 🐛 Describe the bug Why is n-gram speculative decoding performing slower than the baselin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

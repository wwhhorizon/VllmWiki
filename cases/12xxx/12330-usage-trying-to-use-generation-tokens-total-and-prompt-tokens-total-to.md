# vllm-project/vllm#12330: [Usage]: trying to use generation_tokens_total and prompt_tokens_total to get total tokens in the current batch

| 字段 | 值 |
| --- | --- |
| Issue | [#12330](https://github.com/vllm-project/vllm/issues/12330) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;model_support |
| 子分类 | wrong_output |
| Operator 关键词 | cache |
| 症状 | mismatch |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: trying to use generation_tokens_total and prompt_tokens_total to get total tokens in the current batch

### Issue 正文摘录

### Your current environment I'm testing this with a single A100 40GB GPU using meta-llama/Meta-Llama-3-8B model weights. The server prints out the following info around expected memory reserved for the kv cache on startup: ``` INFO 01-13 11:35:21 model_runner.py:1099] Loading model weights took 14.9595 GB INFO 01-13 11:35:23 worker.py:241] Memory profiling takes 1.32 seconds INFO 01-13 11:35:23 worker.py:241] the current vLLM instance can use total_gpu_memory (39.50GiB) x gpu_memory_utilization (0.90) = 35.55GiB INFO 01-13 11:35:23 worker.py:241] model weights take 14.96GiB; non_torch_memory takes 0.10GiB; PyTorch activation peak memory takes 9.37GiB; the rest of the memory reserved for KV Cache is 11.12GiB. INFO 01-13 11:35:23 gpu_executor.py:76] # GPU blocks: 5691, # CPU blocks: 2048 INFO 01-13 11:35:23 gpu_executor.py:80] Maximum concurrency for 8192 tokens per request: 11.12x ``` ### How would you like to use vllm I'm currently trying to use the sum of these two metrics, prompt_tokens_total and generation_tokens_total, to track how many tokens are in the current kv cache (aka how many tokens in the current batch per iteration). Based on the above environment information, I wo...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: batch usage ### Your current environment I'm testing this with a single A100 40GB GPU using meta-llama/Meta-Llama-3-8B model weights. The server prints out the following info around expected memory reserved for the kv c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ent environment I'm testing this with a single A100 40GB GPU using meta-llama/Meta-Llama-3-8B model weights. The server prints out the following info around expected memory reserved for the kv cache on startup: ``` INFO...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: otal tokens in the current batch usage ### Your current environment I'm testing this with a single A100 40GB GPU using meta-llama/Meta-Llama-3-8B model weights. The server prints out the following info around expected m...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e metrics represent the total tokens in the batch? If so, why is there a mismatch between the expected tokens for a full kv cache and the actual metrics emitted? If not, is there any metric that exists today that can gi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: er prints out the following info around expected memory reserved for the kv cache on startup: ``` INFO 01-13 11:35:21 model_runner.py:1099] Loading model weights took 14.9595 GB INFO 01-13 11:35:23 worker.py:241] Memory...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

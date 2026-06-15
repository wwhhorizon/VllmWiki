# vllm-project/vllm#21344: [Bug]: Large image requests silently dropped with Llama-Guard-4

| 字段 | 值 |
| --- | --- |
| Issue | [#21344](https://github.com/vllm-project/vllm/issues/21344) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Large image requests silently dropped with Llama-Guard-4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM never completes requests to Llama-4-Guard with images of size 2kx2k or larger, causing the client side to hang. Server logs: ``` INFO: Started server process [1171423] INFO: Waiting for application startup. INFO: Application startup complete. DEBUG 07-22 00:46:39 [loggers.py:118] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% DEBUG 07-22 00:46:49 [loggers.py:118] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% DEBUG 07-22 00:46:59 [loggers.py:118] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% DEBUG 07-22 00:47:09 [loggers.py:118] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% INFO 07-22 00:47:16 [chat_utils.py:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Large image requests silently dropped with Llama-Guard-4 bug;stale ### Your current environment ### 🐛 Describe the bug vLLM never completes requests to Llama-4-Guard with images of size 2kx2k or larger, causing t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Large image requests silently dropped with Llama-Guard-4 bug;stale ### Your current environment ### 🐛 Describe the bug vLLM never completes requests to Llama-4-Guard with images of size 2kx2k or larger, causing t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: imes.\nS3: Sex Crimes.\nS4: Child Exploitation.\nS5: Defamation.\nS6: Specialized Advice.\nS7: Privacy.\nS8: Intellectual Property.\nS9: Indiscriminate Weapons.\nS10: Hate.\nS11: Self-Harm.\nS12: Sexual Content.\nS13: E...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ns.\n \n\n \nUser: What is this?\\n\\n\n\n \n\nProvide your safety assessment for ONLY THE LAST User message in the above conversation:\n - First line must read 'safe' or 'unsafe'.\n - If unsafe, a second line must incl...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ns/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% DEBUG 07-22 00:46:49 [loggers.py:118] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

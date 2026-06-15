# vllm-project/vllm#13939: [Bug]: (v0.7.2): RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#13939](https://github.com/vllm-project/vllm/issues/13939) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (v0.7.2): RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I updated vllm to version `0.7.2` but still observed this error (already mentioned in #12233 ), but with different error log. ```sh INFO 02-25 11:11:31 metrics.py:455] Avg prompt throughput: 2082.8 tokens/s, Avg generation throughput: 194.4 tokens/s, Running: 3 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 4.8%, CPU KV cache usage: 0.0%. INFO 02-25 11:11:31 metrics.py:471] Prefix cache hit rate: GPU: 52.36%, CPU: 0.00% INFO: 172.27.0.4:60994 - "POST /v1/chat/completions HTTP/1.0" 200 OK INFO: 172.27.0.4:32774 - "POST /v1/chat/completions HTTP/1.0" 200 OK INFO: 172.27.0.4:32816 - "POST /v1/chat/completions HTTP/1.0" 200 OK INFO: 172.27.0.4:32790 - "POST /v1/chat/completions HTTP/1.0" 200 OK CRITICAL 02-25 11:11:34 launcher.py:101] MQLLMEngine is already dead, terminating server process CRITICAL 02-25 11:11:34 launcher.py:101] MQLLMEngine is already dead, terminating server process CRITICAL 02-25 11:11:34 launcher.py:101] MQLLMEngine is already dead, terminating server process CRITICAL 02-25 11:11:34 launcher.py:101] MQLLMEngine is already dead, terminating server process CRITICAL 02-25 11:11:34 launcher.py:101] MQLLM...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: # Your current environment ### 🐛 Describe the bug I updated vllm to version `0.7.2` but still observed this error (already mentioned in #12233 ), but with different error log. ```sh INFO 02-25 11:11:31 metrics.py:455] A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: y", line 200, in run_engine_loop ERROR 02-25 11:11:34 engine.py:139] request_outputs = self.engine_step() ERROR 02-25 11:11:34 engine.py:139] ^^^^^^^^^^^^^^^^^^ ERROR 02-25 11:11:34 engine.py:139] File "/usr/local/lib/p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: (v0.7.2): RuntimeError: CUDA error: an illegal memory access was encountered bug ### Your current environment ### 🐛 Describe the bug I updated vllm to version `0.7.2` but still observed this error (already mentio...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: 8%, CPU KV cache usage: 0.0%. INFO 02-25 11:11:31 metrics.py:471] Prefix cache hit rate: GPU: 52.36%, CPU: 0.00% INFO: 172.27.0.4:60994 - "POST /v1/chat/completions HTTP/1.0" 200 OK INFO: 172.27.0.4:32774 - "POST /v1/ch...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: : 194.4 tokens/s, Running: 3 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 4.8%, CPU KV cache usage: 0.0%. INFO 02-25 11:11:31 metrics.py:471] Prefix cache hit rate: GPU: 52.36%, CPU: 0.00% INFO: 172.27.0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

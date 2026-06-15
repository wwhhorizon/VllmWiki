# vllm-project/vllm#16151: [Bug]: [V1] Random infinite response generation followed by silent crash

| 字段 | 值 |
| --- | --- |
| Issue | [#16151](https://github.com/vllm-project/vllm/issues/16151) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1] Random infinite response generation followed by silent crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With the V1 engine and 0.8.2, it looks like vLLM will randomly generate an infinite number of tokens for one particular response and then crash on this assertion error. This happens with different LLMs and seems to be random but usually with higher (concurrent) load - we're currently testing if speculative decoding may be the culprit (jury's still out on this one though.) Keep in mind that while the vLLM worker processes die, the k8s pod itself continues to stay "alive" even though all requests now timeout. The last line repeats indefinitely until a manual pod restart is conducted. I've seen a similar report from another user in this Github comment: [https://github.com/vllm-project/vllm/issues/13673#issuecomment-2710414804](https://github.com/vllm-project/vllm/issues/13673#issuecomment-2710414804). We're currently using llama 3.3 70B at FP8. ``` INFO 04-06 16:11:52 [loggers.py:80] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 2.2 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.2%, Prefix cache hit rate: 21.7% -- INFO: 172.17.86.56:38282 - "GET /health HTTP/1.1" 200 OK CRITICAL 04-06 16:11:42 [...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: m but usually with higher (concurrent) load - we're currently testing if speculative decoding may be the culprit (jury's still out on this one though.) Keep in mind that while the vLLM worker processes die, the k8s pod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cache...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: s/13673#issuecomment-2710414804). We're currently using llama 3.3 70B at FP8. ``` INFO 04-06 16:11:52 [loggers.py:80] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 2.2 tokens/s, Running: 1 reqs, Waitin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ration throughput: 2.2 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.2%, Prefix cache hit rate: 21.7% -- INFO: 172.17.86.56:38282 - "GET /health HTTP/1.1" 200 OK CRITICAL 04-06 16:11:42 [core_client...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#16452: [Doc]: Update outdated note: LMCache now supports chunked prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#16452](https://github.com/vllm-project/vllm/issues/16452) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Update outdated note: LMCache now supports chunked prefill

### Issue 正文摘录

### 📚 The doc issue In the file [examples/offline_inference/cpu_offload_lmcache.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/cpu_offload_lmcache.py), line 43 states: `# Note that LMCache is not compatible with chunked prefill for now.` This is now outdated. Both vLLM and LMCache have merged PRs to fully support chunked prefill: [vLLM PR #14505](https://github.com/vllm-project/vllm/pull/14505), [LMCache PR #392](https://github.com/LMCache/LMCache/pull/392) The current note may mislead users into disabling a working feature. ### Suggest a potential alternative/fix Update the comment to either: `# Note: LMCache supports chunked prefill (see vLLM#14505, LMCache#392). ` Or remove it entirely if compatibility is now considered stable/default. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ntation ### 📚 The doc issue In the file [examples/offline_inference/cpu_offload_lmcache.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/cpu_offload_lmcache.py), line 43 states: `# Note that...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Update outdated note: LMCache now supports chunked prefill documentation ### 📚 The doc issue In the file [examples/offline_inference/cpu_offload_lmcache.py](https://github.com/vllm-project/vllm/blob/main/examples...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

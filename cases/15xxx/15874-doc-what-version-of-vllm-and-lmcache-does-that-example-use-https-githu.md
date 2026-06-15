# vllm-project/vllm#15874: [Doc]: What version of vllm and lmcache does that example use https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/cpu_offload_lmcache.py

| 字段 | 值 |
| --- | --- |
| Issue | [#15874](https://github.com/vllm-project/vllm/issues/15874) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: What version of vllm and lmcache does that example use https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/cpu_offload_lmcache.py

### Issue 正文摘录

### 📚 The doc issue I have tried to run it with lmcache==0.1.4 with all experimental features (built from source) and vllm==0.8.3.dev136+geffc5d24 and it crashes with the segmentation fault. ### Suggest a potential alternative/fix Add requirements.txt for this example https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/cpu_offload_lmcache.py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Doc]: What version of vllm and lmcache does that example use https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/cpu_offload_lmcache.py documentation;stale ### 📚 The doc issue I have tried to run...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ://github.com/vllm-project/vllm/blob/main/examples/offline_inference/cpu_offload_lmcache.py documentation;stale ### 📚 The doc issue I have tried to run it with lmcache==0.1.4 with all experimental features (built from s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lob/main/examples/offline_inference/cpu_offload_lmcache.py documentation;stale ### 📚 The doc issue I have tried to run it with lmcache==0.1.4 with all experimental features (built from source) and vllm==0.8.3.dev136+gef...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

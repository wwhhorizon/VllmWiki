# vllm-project/vllm#32593: [Doc]: Any plan to make POST /reset_prefix_cache public?

| 字段 | 值 |
| --- | --- |
| Issue | [#32593](https://github.com/vllm-project/vllm/issues/32593) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Any plan to make POST /reset_prefix_cache public?

### Issue 正文摘录

### 📚 The doc issue POST /reset_prefix_cache is currently a dev-only endpoint (gated by VLLM_SERVER_DEV_MODE) that invalidates the prefix/KV cache. Are there any plans to make this endpoint (or an equivalent, supported API) public/documented for use? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: nly endpoint (gated by VLLM_SERVER_DEV_MODE) that invalidates the prefix/KV cache. Are there any plans to make this endpoint (or an equivalent, supported API) public/documented for use? ### Suggest a potential alternati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Any plan to make POST /reset_prefix_cache public? documentation;stale ### 📚 The doc issue POST /reset_prefix_cache is currently a dev-only endpoint (gated by VLLM_SERVER_DEV_MODE) that invalidates the prefix/KV c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

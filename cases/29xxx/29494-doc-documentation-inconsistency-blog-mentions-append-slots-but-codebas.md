# vllm-project/vllm#29494: [Doc]: Documentation inconsistency: Blog mentions append_slots() but codebase uses allocate_slots()

| 字段 | 值 |
| --- | --- |
| Issue | [#29494](https://github.com/vllm-project/vllm/issues/29494) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Documentation inconsistency: Blog mentions append_slots() but codebase uses allocate_slots()

### Issue 正文摘录

### 📚 The doc issue The Automatic Prefix Caching blog post mentions: > "The scheduler calls kv_cache_manager.append_slots()" However, the actual codebase uses a unified `kv_cache_manager.allocate_slots()` method that handles both prefill and decode requests. **Location:** - Blog: [[link to blog post](https://docs.vllm.ai/en/v0.8.5/design/v1/prefix_caching.html#operations)] - Code: ./vllm/v1/core/kv_cache_manager.py ### Suggest a potential alternative/fix Update the blog post to reflect the actual implementation `kv_cache_manager.allocate_slots()` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 📚 The doc issue The Automatic Prefix Caching blog post mentions: > "The scheduler calls kv_cache_manager.append_slots()" However, the actual codebase uses a unified `kv_cache_manager.allocate_slots()` method that handle...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: that handles both prefill and decode requests. **Location:** - Blog: [[link to blog post](https://docs.vllm.ai/en/v0.8.5/design/v1/prefix_caching.html#operations)] - Code: ./vllm/v1/core/kv_cache_manager.py ### Suggest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ()` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Doc]: Documentation inconsistency: Blog mentions append_slots() but codebase uses allocate_slots() documentation ### 📚 The doc issue The Automatic Prefix Caching blog post mentions: > "The scheduler calls kv_cache_mana...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

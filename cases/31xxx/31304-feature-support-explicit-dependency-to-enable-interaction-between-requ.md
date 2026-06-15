# vllm-project/vllm#31304: [Feature]: Support explicit dependency to enable interaction between requests

| 字段 | 值 |
| --- | --- |
| Issue | [#31304](https://github.com/vllm-project/vllm/issues/31304) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support explicit dependency to enable interaction between requests

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **The Goal** Enable different requests to explicitly share and interact with the same KV cache context. **The Scenario** 1. **Request A** initializes a context (e.g. KV Blocks). 2. **Request B** needs to interact with the context established by Request A. **The Proposal** I propose adding a mechanism (e.g., `parent_id`) to link Request B to Request A. This allows **explicit interaction** between logically correlated requests, enabling Request B to "attach" to Request A's state without needing to provide the original raw data. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: Support explicit dependency to enable interaction between requests feature request;stale ### 🚀 The feature, motivation and pitch **The Goal** Enable different requests to explicitly share and interact with th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xt established by Request A. **The Proposal** I propose adding a mechanism (e.g., `parent_id`) to link Request B to Request A. This allows **explicit interaction** between logically correlated requests, enabling Request...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support explicit dependency to enable interaction between requests feature request;stale ### 🚀 The feature, motivation and pitch **The Goal** Enable different requests to explicitly share and interact with th...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Enable different requests to explicitly share and interact with the same KV cache context. **The Scenario** 1. **Request A** initializes a context (e.g. KV Blocks). 2. **Request B** needs to interact with the context es...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: text. **The Scenario** 1. **Request A** initializes a context (e.g. KV Blocks). 2. **Request B** needs to interact with the context established by Request A. **The Proposal** I propose adding a mechanism (e.g., `parent_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

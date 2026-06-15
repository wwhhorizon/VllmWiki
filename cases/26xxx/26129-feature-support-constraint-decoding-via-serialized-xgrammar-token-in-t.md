# vllm-project/vllm#26129: [Feature]: Support constraint decoding via serialized xgrammar (token-in/token-out RL use case)

| 字段 | 值 |
| --- | --- |
| Issue | [#26129](https://github.com/vllm-project/vllm/issues/26129) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support constraint decoding via serialized xgrammar (token-in/token-out RL use case)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **What we’d like:** Enable constrained decoding in vLLM by accepting a **compiled grammar JSON** (from [[xgrammar serialization/deserialization](https://xgrammar.mlc.ai/docs/xgrammar_features/serialization.html)]) **in the inference request**, so the server can load and apply the grammar **without requiring a tokenizer on the server**. **Why:** Our current setup runs **token-in / token-out RL training**, where the vLLM server does **not** host a tokenizer. But we still need **constraint decoding** for output format control. If vLLM could consume a client-provided, pre-compiled grammar (already aligned to the model’s tokenizer/token ids on the client side) and use it directly in decoding, we could fully bypass server-side tokenization. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: * host a tokenizer. But we still need **constraint decoding** for output format control. If vLLM could consume a client-provided, pre-compiled grammar (already aligned to the model’s tokenizer/token ids on the client si...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: **What we’d like:** Enable constrained decoding in vLLM by accepting a **compiled grammar JSON** (from [[xgrammar serialization/deserialization](https://xgrammar.mlc.ai/docs/xgrammar_features/serialization.html)]) **in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ecoding via serialized xgrammar (token-in/token-out RL use case) feature request ### 🚀 The feature, motivation and pitch **What we’d like:** Enable constrained decoding in vLLM by accepting a **compiled grammar JSON** (...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

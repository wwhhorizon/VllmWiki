# vllm-project/vllm#28465: [RFC]: Publishing KVBlocks event with mm_hash

| 字段 | 值 |
| --- | --- |
| Issue | [#28465](https://github.com/vllm-project/vllm/issues/28465) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Publishing KVBlocks event with mm_hash

### Issue 正文摘录

### Motivation. https://github.com/vllm-project/vllm/issues/16669 is designed to publish the kv state for better routting. However it can't handle multimodal request tasks well. The router typically uses token_ids to match a block, In multimodal scenarios, however, the visual token_ids is the placeholders number, can't be used for matching. ### Proposed Change. I plan to add mm_hash to BlockStored, and return the mm_hash if the vision's first token_ids in this kv block. The kv block matching process is： 1. matching tokens ids 2. Match the mm_hash if have BlockStored 0 with mm_hash 0 BlockStored 1 with mm_hash 1 ### Feedback Period. one week ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Publishing KVBlocks event with mm_hash RFC;stale ### Motivation. https://github.com/vllm-project/vllm/issues/16669 is designed to publish the kv state for better routting. However it can't handle multimodal reque...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [RFC]: Publishing KVBlocks event with mm_hash RFC;stale ### Motivation. https://github.com/vllm-project/vllm/issues/16669 is designed to publish the kv state for better routting. However it can't handle multimodal reque...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ned to publish the kv state for better routting. However it can't handle multimodal request tasks well. The router typically uses token_ids to match a block, In multimodal scenarios, however, the visual token_ids is the...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ter routting. However it can't handle multimodal request tasks well. The router typically uses token_ids to match a block, In multimodal scenarios, however, the visual token_ids is the placeholders number, can't be used...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

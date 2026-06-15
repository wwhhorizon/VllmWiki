# vllm-project/vllm#35992: [Doc]: Inconsistent hash notation in Prefix Caching "Time 5" diagram

| 字段 | 值 |
| --- | --- |
| Issue | [#35992](https://github.com/vllm-project/vllm/issues/35992) |
| 状态 | open |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Inconsistent hash notation in Prefix Caching "Time 5" diagram

### Issue 正文摘录

### 📚 The doc issue In the [Automatic Prefix Caching documentation](https://docs.vllm.ai/en/latest/design/prefix_caching/#example), there is an inconsistency in how block hashes are labeled in the example diagrams, specifically transitioning from Time 4 to Time 5. The core concept of prefix caching is that a block's hash is built using the parent hash (prefix) + the block tokens. In the Time 4 diagram, the Hash values inside the Block Pool correctly use the prefix notation (e.g., Block 0 is A-D, Block 1 is A-H, Block 3 is A-P). This perfectly matches the Cache Blocks (dict) on the left side. In the Time 5 diagram ("Request 1 is finished and free"), the Hash values inside the Block Pool suddenly switch to showing the local block tokens instead of the prefix hash (e.g., Block 0 becomes ABCD, Block 1 becomes EFGH, Block 2 becomes IJKL). ### Suggest a potential alternative/fix The Time 5 diagram should be updated so that the Block Pool boxes display the correct prefix hashes (A-D, A-H, A-L, A-P, A-J,kl, etc) to remain consistent with Time 4. I am a new contributor and would love to help fix this! I can edit the source diagram to correct the labels and open a Pull Request. Please let m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nconsistency in how block hashes are labeled in the example diagrams, specifically transitioning from Time 4 to Time 5. The core concept of prefix caching is that a block's hash is built using the parent hash (prefix) +...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: PR. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ck 0 is A-D, Block 1 is A-H, Block 3 is A-P). This perfectly matches the Cache Blocks (dict) on the left side. In the Time 5 diagram ("Request 1 is finished and free"), the Hash values inside the Block Pool suddenly swi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: latest/design/prefix_caching/#example), there is an inconsistency in how block hashes are labeled in the example diagrams, specifically transitioning from Time 4 to Time 5. The core concept of prefix caching is that a b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tches the Cache Blocks (dict) on the left side. In the Time 5 diagram ("Request 1 is finished and free"), the Hash values inside the Block Pool suddenly switch to showing the local block tokens instead of the prefix has...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#41823: [Feature]: Support Dynamic Pruning for Speculative Decoding Draft Trees in EAGLE-3

| 字段 | 值 |
| --- | --- |
| Issue | [#41823](https://github.com/vllm-project/vllm/issues/41823) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Dynamic Pruning for Speculative Decoding Draft Trees in EAGLE-3

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would like to request support for **dynamic pruning** in vLLM's speculative decoding draft tree (`--speculative-token-tree`) in EAGLE-3. Today, the tree topology is static at model load time, which makes the number of draft branches fixed during inference. A pruning mechanism would allow vLLM to trim low-value branches at runtime based on token probabilities, improving efficiency without requiring users to hand-tune multiple static tree shapes. ### Alternatives Motivation Current behavior The draft tree topology is configured via speculative_token_tree (for example, "[(0,), (1,), (0,0), (0,1), (1,0), (1,1)]" ) and is resolved to fixed per-level child counts stored in child_drafts_per_level (see vllm/v1/spec_decode/llm_base_proposer.py:282–302 ). During the propose_tree loop, each level expands every parent node by a fixed number of children: # llm_base_proposer.py ~L1006 num_children = self . child_drafts_per_level [ level ] if num_children == 1 : &nbsp; &nbsp; draft_token_ids = logits . argmax ( dim =- 1 ). view ( batch_size , - 1 ) else : &nbsp; &nbsp; draft_token_ids = torch . topk ( logits , num_children , dim =- 1 ). indices . view (...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Support Dynamic Pruning for Speculative Decoding Draft Trees in EAGLE-3 feature request ### 🚀 The feature, motivation and pitch I would like to request support for **dynamic pruning** in vLLM's speculative de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es the number of draft branches fixed during inference. A pruning mechanism would allow vLLM to trim low-value branches at runtime based on token probabilities, improving efficiency without requiring users to hand-tune...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ds = logits . argmax ( dim =- 1 ). view ( batch_size , - 1 ) else : &nbsp; &nbsp; draft_token_ids = torch . topk ( logits , num_children , dim =- 1 ). indices . view ( &nbsp; &nbsp; &nbsp; &nbsp; batch_size , - 1 &nbsp;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eculative-token-tree`) in EAGLE-3. Today, the tree topology is static at model load time, which makes the number of draft branches fixed during inference. A pruning mechanism would allow vLLM to trim low-value branches...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Fixed branching budget | Can avoid wasting work on low-probability paths Latency-sensitive serving | Constant overhead per step | Fewer draft tokens and lower average latency Mixed-difficulty batch | Same tree shape for...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

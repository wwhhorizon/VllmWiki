# vllm-project/vllm#1970: Lookahead decoding | forking + "appending" to child sequences.

| 字段 | 值 |
| --- | --- |
| Issue | [#1970](https://github.com/vllm-project/vllm/issues/1970) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Lookahead decoding \| forking + "appending" to child sequences.

### Issue 正文摘录

Hi, @WoosukKwon and @zhuohan123 , Fantastic project! I was taking a stab at implementing a version of **greedy** lookahead-decoding. Given some candidate completions, I was trying to: 1. Fork children from the parent sequence 2. Append new tokens (from the candidates) to the children sequences 3. Call `step` in the engine to parallelize the next token prediction across candidates 4. Verify and select the longest prefix 5. Append this to the parent sequence 6. Discard all children sequences created in step#1 I had a question about the behavior of `Sequence.append_token_id`, and its implications on the future engine steps. https://github.com/vllm-project/vllm/blob/24f60a54f42076e0bfa49fde113756bf4e95f9ef/vllm/sequence.py#L159-L167 From the looks of it, if I append a token here, it should add the token to the appropriate blocks. But when I try this in practice, I get a different output. Suppose the LLM was generating ```bash 912 -> 442 -> 42 ``` I intervene *after* it has generated `912`, and append `442` using `.append_token_id` , and then call `step()`. But I see ```bash 912 -> 442 -> 10 ``` Seeding is not the problem -- I have accounted for that. Tagging some folks who had previou...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: @zhuohan123 , Fantastic project! I was taking a stab at implementing a version of **greedy** lookahead-decoding. Given some candidate completions, I was trying to: 1. Fork children from the parent sequence 2. Append new...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ken to the appropriate blocks. But when I try this in practice, I get a different output. Suppose the LLM was generating ```bash 912 -> 442 -> 42 ``` I intervene *after* it has generated `912`, and append `442` using `....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: it, if I append a token here, it should add the token to the appropriate blocks. But when I try this in practice, I get a different output. Suppose the LLM was generating ```bash 912 -> 442 -> 42 ``` I intervene *after*...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: r that. Tagging some folks who had previously participated in lookahead/speculative decoding discussions. @simon-mo @LiuXiaoxuanPKU @skrider @beginlner

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

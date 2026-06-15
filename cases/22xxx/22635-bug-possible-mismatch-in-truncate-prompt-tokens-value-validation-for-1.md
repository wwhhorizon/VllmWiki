# vllm-project/vllm#22635: [Bug]: Possible mismatch in `truncate_prompt_tokens` value validation for `-1`

| 字段 | 值 |
| --- | --- |
| Issue | [#22635](https://github.com/vllm-project/vllm/issues/22635) |
| 状态 | closed |
| 标签 |  |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Possible mismatch in `truncate_prompt_tokens` value validation for `-1`

### Issue 正文摘录

Hello, I tried setting `truncate_prompt_tokens=-1`, but it looks like the value validation prevents this. This behavior seems inconsistent with the documentation (see below). Could you please clarify if `-1` is still a supported value? https://github.com/vllm-project/vllm/blob/ebf7605b0dd58ff5d572d1918e52ca732025eee0/vllm/sampling_params.py#L185-L188 https://github.com/vllm-project/vllm/blob/ebf7605b0dd58ff5d572d1918e52ca732025eee0/vllm/sampling_params.py#L413-L416

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Possible mismatch in `truncate_prompt_tokens` value validation for `-1` Hello, I tried setting `truncate_prompt_tokens=-1`, but it looks like the value validation prevents this. This behavior seems inconsistent w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Possible mismatch in `truncate_prompt_tokens` value validation for `-1` Hello, I tried setting `truncate_prompt_tokens=-1`, but it looks like the value validation prevents this. This behavior seems inconsistent w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#1933: 使用vllm推理gptj模型，相比较HF推理结果缺少一部分

| 字段 | 值 |
| --- | --- |
| Issue | [#1933](https://github.com/vllm-project/vllm/issues/1933) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 使用vllm推理gptj模型，相比较HF推理结果缺少一部分

### Issue 正文摘录

SamplingParams采样设置：(max_tokens=1024, use_beam_search=True, best_of=4, early_stopping=True, temperature=0, top_p=1, top_k=-1) repetition_penalties为1.2 vllm结果：up by Mark Noble led to a first-half goal for Diafra Sakho which was blocked by Courtois. Later in the 15th minute, a through pass from Hazard set Ramires clear on goal, but his delicate side-footed finish struck the inside of the far post and rebounded into the hands of Adrian . HF结果：up by Mark Noble led to a first-half goal for Diafra Sakho which was blocked by Courtois.\nLater in the 15th minute, a through pass from Hazard set Ramires clear on goal, but his delicate side-footed finish struck the inside of the far post and rebounded into the hands of Adrian.\nEden Hazard scored the only goal of the game in the 22nd minute to give Chelsea a hard-fought win at Upton Park.\nChelsea maintained their five-point lead at the top of the Premier League table.\nWest Ham failed to score in six of their last seven Premier League' 两结果相比较前半句一致，但vllm没有HF结果的后半句，max_tokens也已设为1024

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: m结果：up by Mark Noble led to a first-half goal for Diafra Sakho which was blocked by Courtois. Later in the 15th minute, a through pass from Hazard set Ramires clear on goal, but his delicate side-footed finish struck th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: m推理gptj模型，相比较HF推理结果缺少一部分 SamplingParams采样设置：(max_tokens=1024, use_beam_search=True, best_of=4, early_stopping=True, temperature=0, top_p=1, top_k=-1) repetition_penalties为1.2 vllm结果：up by Mark Noble led to a first-half...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 使用vllm推理gptj模型，相比较HF推理结果缺少一部分 SamplingParams采样设置：(max_tokens=1024, use_beam_search=True, best_of=4, early_stopping=True, temperature=0, top_p=1, top_k=-1) repetition_penalties为1.2 vllm结果：up by Mark Noble led to a first-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

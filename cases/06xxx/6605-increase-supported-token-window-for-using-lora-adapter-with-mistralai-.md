# vllm-project/vllm#6605: Increase supported token window for using LoRA Adapter with  mistralai/Mistral-Nemo-Instruct-2407

| 字段 | 值 |
| --- | --- |
| Issue | [#6605](https://github.com/vllm-project/vllm/issues/6605) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Increase supported token window for using LoRA Adapter with  mistralai/Mistral-Nemo-Instruct-2407

### Issue 正文摘录

### 🚀 The feature, motivation and pitch NeMO has Vocabulary size: 131072 if you try to use a LoRA Adapter with NeMO in vllm you get this error ` ValueError: When using LoRA, vocab size must be 32000 >= vocab_size <= 128512 ` @Yard1 I can try this myself, but just want to know your thoughts, if the below was updated where 131072 was added, would it work? Would there be some compatibility issues? https://github.com/vllm-project/vllm/commit/1e96c3341a4e055ae392085fecc7a672295b71c2

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: or using LoRA Adapter with mistralai/Mistral-Nemo-Instruct-2407 feature request ### 🚀 The feature, motivation and pitch NeMO has Vocabulary size: 131072 if you try to use a LoRA Adapter with NeMO in vllm you get this er...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

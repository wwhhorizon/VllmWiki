# vllm-project/vllm#1562: [FEATURE] Implement Dynamic SplitFuse

| 字段 | 值 |
| --- | --- |
| Issue | [#1562](https://github.com/vllm-project/vllm/issues/1562) |
| 状态 | closed |
| 标签 | performance;feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [FEATURE] Implement Dynamic SplitFuse

### Issue 正文摘录

Dear vLLM maintainers @WoosukKwon and @zhuohan123 (@Yard1), DeepSpeed has released its serving framework which claims to be faster than vLLM. The main speedup comes from [Dynamic SplitFuse](https://github.com/microsoft/DeepSpeed/tree/master/blogs/deepspeed-fastgen#b-dynamic-splitfuse-) which is a technique that does the following: - Long prompts are decomposed into much smaller chunks and scheduled across multiple forward passes (iterations) with only the final pass performing any generation. - Short prompts will be composed to exactly fill a target token budget. Even short prompts may be decomposed to ensure the budget is precisely met and the forward sizes are well-aligned. Code: https://github.com/microsoft/DeepSpeed-MII Background: https://github.com/microsoft/DeepSpeed/tree/master/blogs/deepspeed-fastgen Llama 13B (1x A100-80GB): ![image](https://github.com/vllm-project/vllm/assets/27340033/cc7842b8-e234-482d-8550-d38d39d94473) Llama 70B (4x A100x80GB with TP): ![image](https://github.com/vllm-project/vllm/assets/27340033/e035e094-0f10-463c-abf0-aafd67a61fed)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hnique that does the following: - Long prompts are decomposed into much smaller chunks and scheduled across multiple forward passes (iterations) with only the final pass performing any generation. - Short prompts will b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: budget. Even short prompts may be decomposed to ensure the budget is precisely met and the forward sizes are well-aligned. Code: https://github.com/microsoft/DeepSpeed-MII Background: https://github.com/microsoft/DeepSp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ps://github.com/microsoft/DeepSpeed/tree/master/blogs/deepspeed-fastgen Llama 13B (1x A100-80GB): ![image](https://github.com/vllm-project/vllm/assets/27340033/cc7842b8-e234-482d-8550-d38d39d94473) Llama 70B (4x A100x80...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [FEATURE] Implement Dynamic SplitFuse performance;feature request Dear vLLM maintainers @WoosukKwon and @zhuohan123 (@Yard1), DeepSpeed has released its serving framework which claims to be faster than vLLM. The main sp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

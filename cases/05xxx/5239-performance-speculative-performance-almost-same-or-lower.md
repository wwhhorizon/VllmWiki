# vllm-project/vllm#5239: [Performance]: Speculative Performance almost same or lower

| 字段 | 值 |
| --- | --- |
| Issue | [#5239](https://github.com/vllm-project/vllm/issues/5239) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Speculative Performance almost same or lower

### Issue 正文摘录

### Proposal to improve performance @LiuXiaoxuanPKU Good to see you again. Thank you for your work. I guess your working group releases SD a little by little. I'm wondering about current SD version. I had experiment result that using Speculative Decoding way is almost same performance or lower than normal(Only using Target Model) even low query per second. Is that reason for SD in progress? I attached result bellow. Could you tell me your thought about the result? ### Report of performance regression _No response_ ### Misc discussion on performance Case. 300 prompt examples (Average Input 158), Set max output 100 Tokens . Target Model "Llama-2-70B-chat" , Draft Model "TinyLlama 1.1B-chat-GPTQ " Attached result as bellow. ![question](https://github.com/vllm-project/vllm/assets/20792661/205afca4-1bb9-4046-aff1-ddecf896ab87)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: Speculative Performance almost same or lower performance;stale ### Proposal to improve performance @LiuXiaoxuanPKU Good to see you again. Thank you for your work. I guess your working group releases SD a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ng way is almost same performance or lower than normal(Only using Target Model) even low query per second. Is that reason for SD in progress? I attached result bellow. Could you tell me your thought about the result? ##...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng group releases SD a little by little. I'm wondering about current SD version. I had experiment result that using Speculative Decoding way is almost same performance or lower than normal(Only using Target Model) even...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: d you tell me your thought about the result? ### Report of performance regression _No response_ ### Misc discussion on performance Case. 300 prompt examples (Average Input 158), Set max output 100 Tokens . Target Model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

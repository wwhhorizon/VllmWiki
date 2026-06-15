# vllm-project/vllm#4499: [Bug]: Token accuracy not as expected  ad also got Junk values for starcoderbase-15b model with continuous batching 

| 字段 | 值 |
| --- | --- |
| Issue | [#4499](https://github.com/vllm-project/vllm/issues/4499) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Token accuracy not as expected  ad also got Junk values for starcoderbase-15b model with continuous batching 

### Issue 正文摘录

### 🐛 Describe the bug **Issue:** Getting Junk values and number of tokens generated less than the requested for starcoderbase -15b model And also accuracy of generated text is also low **Current behaviour:** we validated the output token accuracy using multipl-E datasets with both raw model inference script and also with Vllm 0.4.0 container. The Results are as below We observed that the output token accuracy score using VLLM container is too low compared to raw model token accuracy Could you please help us to resolve the issue?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ot Junk values for starcoderbase-15b model with continuous batching bug;stale ### 🐛 Describe the bug **Issue:** Getting Junk values and number of tokens generated less than the requested for starcoderbase -15b model And...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Token accuracy not as expected ad also got Junk values for starcoderbase-15b model with continuous batching bug;stale ### 🐛 Describe the bug **Issue:** Getting Junk values and number of tokens generated less than...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: accuracy not as expected ad also got Junk values for starcoderbase-15b model with continuous batching bug;stale ### 🐛 Describe the bug **Issue:** Getting Junk values and number of tokens generated less than the requeste...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Token accuracy not as expected ad also got Junk values for starcoderbase-15b model with continuous batching bug;stale ### 🐛 Describe the bug **Issue:** Getting Junk values and number of tokens generated less than...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

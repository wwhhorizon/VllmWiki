# vllm-project/vllm#5891: [Feature]: Add distributed inference support for lora adapters.

| 字段 | 值 |
| --- | --- |
| Issue | [#5891](https://github.com/vllm-project/vllm/issues/5891) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add distributed inference support for lora adapters.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Current Lora support only works on single GPU, which is useless for large models such as LLAMA3 70B. I have confirmed that loading lora adapter on a single GPU works fine with LLAMA3 8B model, but failed to do exactly the same thing with 70B model. The only difference between these two trials is that I used 4 A100s to load 70B model by setting --tensor-parallel-size to 4. Both lora adapters are directly created by the `save_pretrained` function from `peft` package. And the only warning message from the server is `{the path to the lora adapter} does not appear to have a file named config.json`, after which the server will always print `Running: 1 reqs`, while generation throughput and prompt throughput stay 0. ### Alternatives I haven't found any alternative yet. ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: urrent Lora support only works on single GPU, which is useless for large models such as LLAMA3 70B. I have confirmed that loading lora adapter on a single GPU works fine with LLAMA3 8B model, but failed to do exactly th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add distributed inference support for lora adapters. feature request;stale ### 🚀 The feature, motivation and pitch Current Lora support only works on single GPU, which is useless for large models such as LLAM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 70B model. The only difference between these two trials is that I used 4 A100s to load 70B model by setting --tensor-parallel-size to 4. Both lora adapters are directly created by the `save_pretrained` function from `pe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: r which the server will always print `Running: 1 reqs`, while generation throughput and prompt throughput stay 0. ### Alternatives I haven't found any alternative yet. ### Additional context _No response_

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

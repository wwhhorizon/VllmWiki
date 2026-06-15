# vllm-project/vllm#28239: [RFC]: Replace list[list[int]] to numpy arrays to mitigate GC overhead.

| 字段 | 值 |
| --- | --- |
| Issue | [#28239](https://github.com/vllm-project/vllm/issues/28239) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Replace list[list[int]] to numpy arrays to mitigate GC overhead.

### Issue 正文摘录

### Motivation. High GC overhead from multiple usages of list[list[int]] in the current implementation. - 1 usage in output tokens - 3 usage in LogprobsLists https://github.com/vllm-project/vllm/blob/7a8375f8a0cd37ee7e3d2be8498b5ae543694179/vllm/v1/worker/gpu_model_runner.py#L210 https://github.com/vllm-project/vllm/blob/7a8375f8a0cd37ee7e3d2be8498b5ae543694179/vllm/v1/outputs.py#L16-L22 In all these usage, after each decode batch, multiple list[list[int]] will be created which had +1 been allocated. For large batch size use cases, it means it's guarantee to invoke multiple GC0 per decode cycle (where the default GC0 threshold is 700). And ultimately, frequent GC0 triggering would also increase the frequency of GC1 and GC2 as well. ### Proposed Change. We're proposing to replace list[list[int]] with `list[np.ndarray]` or `np.ndarray` to reduce GC overhead. ### Feedback Period. _No response_ ### CC List. @zhuohan123 @njhill @robertgshaw2-redhat @22quinn @houseroad @yeqcharlotte ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentatio...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: C]: Replace list[list[int]] to numpy arrays to mitigate GC overhead. RFC;stale ### Motivation. High GC overhead from multiple usages of list[list[int]] in the current implementation. - 1 usage in output tokens - 3 usage...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ct/vllm/blob/7a8375f8a0cd37ee7e3d2be8498b5ae543694179/vllm/v1/worker/gpu_model_runner.py#L210 https://github.com/vllm-project/vllm/blob/7a8375f8a0cd37ee7e3d2be8498b5ae543694179/vllm/v1/outputs.py#L16-L22 In all these us...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

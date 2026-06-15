# vllm-project/vllm#26940: [Feature]: Support `inf` value for burstiness in benchmarks

| 字段 | 值 |
| --- | --- |
| Issue | [#26940](https://github.com/vllm-project/vllm/issues/26940) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support `inf` value for burstiness in benchmarks

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the benchmarks, the burstiness value is used in a gamma distribution to sample the delays between consecutive requests. ``` theta = 1.0 / (current_request_rate * burstiness) delay_ts.append(np.random.gamma(shape=burstiness, scale=theta)) ``` [Theoretically ](https://en.wikipedia.org/wiki/Gamma_distribution)(and this is also what is observed in practice), the generated delays have as mean `1.0 / current_request_rate` and the spread is controlled by the burstiness. When the burstiness is high, we observe lower variance in the delay values, all values being closer to the mean `1.0 / current_request_rate`. When burstiness tends to infinity, we should observe a single generated delay, which is `1.0 / current_request_rate`. In practice, the `np.random.gamma` function generates `nan` as results, so we need to manually condition on `burstiness` value and append `1.0 / current_request_rate` to the list of delays when burstiness becomes infinite. See attached image as mathematical proof ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, a...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Support `inf` value for burstiness in benchmarks feature request ### 🚀 The feature, motivation and pitch In the benchmarks, the burstiness value is used in a gamma distribution to sample the delays between co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: est_rate * burstiness) delay_ts.append(np.random.gamma(shape=burstiness, scale=theta)) ``` [Theoretically ](https://en.wikipedia.org/wiki/Gamma_distribution)(and this is also what is observed in practice), the generated...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support `inf` value for burstiness in benchmarks feature request ### 🚀 The feature, motivation and pitch In the benchmarks, the burstiness value is used in a gamma distribution to sample the delays between co...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

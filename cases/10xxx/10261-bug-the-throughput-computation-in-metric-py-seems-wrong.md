# vllm-project/vllm#10261: [Bug]: The throughput computation in metric.py seems wrong

| 字段 | 值 |
| --- | --- |
| Issue | [#10261](https://github.com/vllm-project/vllm/issues/10261) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The throughput computation in metric.py seems wrong

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Seems that prefill throughput and decode throughput are both divided by the overall time, i.e., $$\text{prefill throughput} = {\text{num of input tokens}\over\text{prefill time + decode time}}$$ $$\text{decode throughput} = {\text{num of output tokens}\over\text{prefill time + decode time}}$$. but should be $$\text{prefill throughput} = {\text{num of input tokens}\over\text{prefill time}}$$ $$\text{decode throughput} = {\text{num of output tokens}\over\text{decode time}}$$. This will significantly affect the model performance data in scenarios with long inputs and long outputs. See https://github.com/vllm-project/vllm/blob/main/vllm/engine/metrics.py#L440C1-L446C46 and https://github.com/vllm-project/vllm/blob/main/vllm/engine/metrics.py#L416C1-L418C59 ``` prompt_throughput = get_throughput(self.num_prompt_tokens, now=stats.now, last_log=self.last_local_log) generation_throughput = get_throughput( self.num_generation_tokens, now=stats.now, last_log=self.last_local_log) ``` ``` def get_throughput(tracked_stats: List[int], now: float, last_log: float) -> float: return float(np.sum(tracked_stats)...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ### Model Input Dumps _No response_ ### 🐛 Describe the bug Seems that prefill throughput and decode throughput are both divided by the overall time, i.e., $$\text{prefill throughput} = {\text{num of input tokens}\over\t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: The throughput computation in metric.py seems wrong bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Seems that prefill throughput and decode throughput are both divided...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tation in metric.py seems wrong bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Seems that prefill throughput and decode throughput are both divided by the overall time, i.e.,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

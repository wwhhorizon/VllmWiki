# vllm-project/vllm#12493: [Doc]: Example launch command for deepseek v3/R1 for 8-way H100/H200 and MI300X?

| 字段 | 值 |
| --- | --- |
| Issue | [#12493](https://github.com/vllm-project/vllm/issues/12493) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Example launch command for deepseek v3/R1 for 8-way H100/H200 and MI300X?

### Issue 正文摘录

### 📚 The doc issue When 405B was launched, it became apparent that certain options had to be chosen for long context to be properly well-handled, e.g.: ``` --max-num-batched-tokens=512 \ --enable_chunked_prefill=True \ ``` and with that I can run at full context of 131072 on 8xH100. I'm looking for similar guidance for deepseek V3/R1 on both NVIDIA and AMD hardware. Do the same options apply? vLLM points to AMD tuning guides, but I don't know if that's really what I want: https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/index.html https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html#vllm-performance-optimization That seems much more low-level. I just want to know what high-level options are to choose to maximize performance and context length as regular user of vLLM. Thanks! ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Doc]: Example launch command for deepseek v3/R1 for 8-way H100/H200 and MI300X? documentation;stale ### 📚 The doc issue When 405B was launched, it became apparent that certain options had to be chosen for long context...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: command for deepseek v3/R1 for 8-way H100/H200 and MI300X? documentation;stale ### 📚 The doc issue When 405B was launched, it became apparent that certain options had to be chosen for long context to be properly well-ha...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: don't know if that's really what I want: https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/index.html https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html#vllm-perfor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

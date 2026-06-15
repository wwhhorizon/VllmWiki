# vllm-project/vllm#10690: [Performance]: We need more processes to fully utilize the multi-core capabilities of the CPU.

| 字段 | 值 |
| --- | --- |
| Issue | [#10690](https://github.com/vllm-project/vllm/issues/10690) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: We need more processes to fully utilize the multi-core capabilities of the CPU.

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance We often encounter situations where the CPU is fully loaded during inference. So why not distribute the workload across more processes on the CPU? This way, we can take full advantage of the server's multi-core capabilities. For example, in this case. [https://github.com/vllm-project/vllm/pull/10640](https://github.com/vllm-project/vllm/issues/url) In this PR, the multimodal preprocessing workload has been shifted from the backend to the frontend, transferring part of the computational burden to the frontend processes. However, this process is CPU-intensive and will likely block subsequent requests in the frontend. Should we consider adding multiple additional processes to handle this type of computation? Just like the diagram below: ![image](https://github.com/user-attachments/assets/7b1d5aa3-6559-42ce-a35f-6b77dab60de1) ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot li...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ses to fully utilize the multi-core capabilities of the CPU. performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance We o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance We often encounter situations where the CPU is fully loaded during inference. So why not...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: this PR, the multimodal preprocessing workload has been shifted from the backend to the frontend, transferring part of the computational burden to the frontend processes. However, this process is CPU-intensive and will...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ontend processes. However, this process is CPU-intensive and will likely block subsequent requests in the frontend. Should we consider adding multiple additional processes to handle this type of computation? Just like t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

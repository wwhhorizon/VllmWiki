# vllm-project/vllm#29101: [Bug]: Pipeline parallelism issues on RTX 6000 + gpt-oss-120b

| 字段 | 值 |
| --- | --- |
| Issue | [#29101](https://github.com/vllm-project/vllm/issues/29101) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Pipeline parallelism issues on RTX 6000 + gpt-oss-120b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://docs.vllm.ai/en/stable/serving/parallelism_scaling.html mentions using pipeline parallelism when attention heads can't evenly be split across gpus when leveraging tensor parallelism. I have a node with 3 RTX 6000s. When running vllm with `vllm serve --tensor-parallel-size 1 --pipeline-parallel-size 3 openai/gpt-oss-120b` the model loads and the api comes up without issue. After some time of heavy usage with high KV cache usage the output is degraded/nonsensical. After the traffic subsides I find there still to be some KV cache usage with degraded output continuing. Restarting vllm resolves the issue (until heavy traffic occurs). Switching to tensor parallelism of 2 also resolves the issue though doesn't take full utilization of the node. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Pipeline parallelism issues on RTX 6000 + gpt-oss-120b bug;stale ### Your current environment ### 🐛 Describe the bug https://docs.vllm.ai/en/stable/serving/parallelism_scaling.html mentions using pipeline paralle...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Pipeline parallelism issues on RTX 6000 + gpt-oss-120b bug;stale ### Your current environment ### 🐛 Describe the bug https://docs.vllm.ai/en/stable/serving/parallelism_scaling.html mentions using pipeline paralle...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: the api comes up without issue. After some time of heavy usage with high KV cache usage the output is degraded/nonsensical. After the traffic subsides I find there still to be some KV cache usage with degraded output co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Pipeline parallelism issues on RTX 6000 + gpt-oss-120b bug;stale ### Your current environment ### 🐛 Describe the bug https://docs.vllm.ai/en/stable/serving/parallelism_scaling.html mentions using pipeline paralle...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

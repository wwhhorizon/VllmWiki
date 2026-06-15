# vllm-project/vllm#23326: [Bug]: In the deployment log of the latest version of vllm, after a successful request, the details of the input graph token are not displayed. How to set it up?

| 字段 | 值 |
| --- | --- |
| Issue | [#23326](https://github.com/vllm-project/vllm/issues/23326) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: In the deployment log of the latest version of vllm, after a successful request, the details of the input graph token are not displayed. How to set it up?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=7 VLLM_LOGGING_LEVEL=DEBUG vllm serve /data3/mingze/models/OpenGVLab/InternVL3-8B --tensor-parallel-size 1 --gpu-memory-utilization 0.8 --port 2558 --trust-remote-code > prompt自优化_internvl_38b_awq.log 2>&1 & ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t up? bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=7 VLLM_LOGGING_LEVEL=DEBUG vllm serve /data3/mingze/models/OpenGVLab/InternVL3-8B --tensor-parallel-size 1 --gpu-memory-utilizatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: CUDA_VISIBLE_DEVICES=7 VLLM_LOGGING_LEVEL=DEBUG vllm serve /data3/mingze/models/OpenGVLab/InternVL3-8B --tensor-parallel-size 1 --gpu-memory-utilization 0.8 --port 2558 --trust-remote-code > prompt自优化_internvl_38b_awq.l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: In the deployment log of the latest version of vllm, after a successful request, the details of the input graph token are not displayed. How to set it up? bug;stale ### Your current environment ### 🐛 Describe the bug CU...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: In the deployment log of the latest version of vllm, after a successful request, the details of the input graph token are not displayed. How to set it up? bug;stale ### Your current environment ### 🐛 Describe the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: In the deployment log of the latest version of vllm, after a successful request, the details of the input graph token are not displayed. How to set it up? bug;stale ### Your current environment ### 🐛 Describe the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

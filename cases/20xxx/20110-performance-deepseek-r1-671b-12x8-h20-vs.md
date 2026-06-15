# vllm-project/vllm#20110: [Performance]: 咨询部署方案：DeepSeek-R1-671B 在 12x8卡H20集群上 - 分布式推理 vs 多实例负载均衡的推理方案对比

| 字段 | 值 |
| --- | --- |
| Issue | [#20110](https://github.com/vllm-project/vllm/issues/20110) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: 咨询部署方案：DeepSeek-R1-671B 在 12x8卡H20集群上 - 分布式推理 vs 多实例负载均衡的推理方案对比

### Issue 正文摘录

### Proposal to improve performance 您好！感谢开发推理引擎。我正在计划部署 DeepSeek-R1-671B 模型，遇到一个关于部署架构选择的疑问，希望能得到一些建议或经验分享。 **环境描述：** - 硬件： 12 台服务器节点。 - - 单节点配置： 每台节点配备 8 张 NVIDIA H20 GPU。 - - 网络： 节点间通过 InfiniBand (IB) 网络互联 - - 总计资源： 96 张 H20 GPU。 **目标**： 部署 DeepSeek-R1-671B 模型进行推理服务。 考虑方案： 方案一：每节点独立实例 + 负载均衡 方案二：跨节点分布式推理 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 考虑方案： 方案一：每节点独立实例 + 负载均衡 方案二：跨节点分布式推理 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 署方案：DeepSeek-R1-671B 在 12x8卡H20集群上 - 分布式推理 vs 多实例负载均衡的推理方案对比 performance;stale ### Proposal to improve performance 您好！感谢开发推理引擎。我正在计划部署 DeepSeek-R1-671B 模型，遇到一个关于部署架构选择的疑问，希望能得到一些建议或经验分享。 **环境描述：** - 硬件： 12 台服务器节点。 - - 单...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

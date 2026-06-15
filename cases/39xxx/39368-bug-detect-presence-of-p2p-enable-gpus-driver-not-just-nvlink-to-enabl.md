# vllm-project/vllm#39368: [BUG]: Detect presence of p2p enable gpus/driver, not just nvlink, to enable direct connection

| 字段 | 值 |
| --- | --- |
| Issue | [#39368](https://github.com/vllm-project/vllm/issues/39368) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [BUG]: Detect presence of p2p enable gpus/driver, not just nvlink, to enable direct connection

### Issue 正文摘录

### 🚀 The feature, motivation and pitch with nvidia-smi topo -p2p r you can check if the gpus can talk to each other directly. as mentioned in this post, vllm does not check for this: https://www.reddit.com/r/LocalLLaMA/comments/1r66jyp/vllm_maximum_performance_on_multi3090/ Using the patched driver from here https://github.com/aikitoria/open-gpu-kernel-modules on 4x 3090 gives me a free ~+10% performance. should be a simple patch in def is_fully_connected(cls, physical_device_ids: list[int]) -> bool: ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [BUG]: Detect presence of p2p enable gpus/driver, not just nvlink, to enable direct connection feature request ### 🚀 The feature, motivation and pitch with nvidia-smi topo -p2p r you can check if the gpus can talk to ea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion feature request ### 🚀 The feature, motivation and pitch with nvidia-smi topo -p2p r you can check if the gpus can talk to each other directly. as mentioned in this post, vllm does not check for this: https://www.red...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n this post, vllm does not check for this: https://www.reddit.com/r/LocalLLaMA/comments/1r66jyp/vllm_maximum_performance_on_multi3090/ Using the patched driver from here https://github.com/aikitoria/open-gpu-kernel-modu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: enable gpus/driver, not just nvlink, to enable direct connection feature request ### 🚀 The feature, motivation and pitch with nvidia-smi topo -p2p r you can check if the gpus can talk to each other directly. as mentione...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance frontend_api kernel env_dependency 🚀 The feature, motivation and pitch

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

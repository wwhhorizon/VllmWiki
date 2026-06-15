# vllm-project/vllm#16706: [Bug]: Error executing method 'init_device'. This might cause deadlock in distributed execution.

| 字段 | 值 |
| --- | --- |
| Issue | [#16706](https://github.com/vllm-project/vllm/issues/16706) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error executing method 'init_device'. This might cause deadlock in distributed execution.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to deploy the model in a multi-machine and multi-GPU parallel manner using the **Docker (version: 0.8.4)** of vllm on three servers. Their hardware configurations are the same (8 * RTX 4090). When I deploy the model on Server 1, Server 2, and Server 3 separately, it works normally. When I deploy the model in parallel on Server 1 and Server 3, it also runs normally. However, when I try to deploy the model in a multi-machine and multi-GPU parallel manner using Server 1 and Server 3, or Server 2 and Server 3, or Server 1, Server 2 and Server 3, an error will occur. The error is as follows (**the following is the error when I tried to deploy on Server 1 and Server 2**). [docker_run.log](https://github.com/user-attachments/files/19773595/docker_run.log) Could anyone please tell me what the possible reasons are and how to solve it? Thank U all! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: y the model in a multi-machine and multi-GPU parallel manner using the **Docker (version: 0.8.4)** of vllm on three servers. Their hardware configurations are the same (8 * RTX 4090). When I deploy the model on Server 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: f vllm on three servers. Their hardware configurations are the same (8 * RTX 4090). When I deploy the model on Server 1, Server 2, and Server 3 separately, it works normally. When I deploy the model in parallel on Serve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ur current environment ### 🐛 Describe the bug I tried to deploy the model in a multi-machine and multi-GPU parallel manner using the **Docker (version: 0.8.4)** of vllm on three servers. Their hardware configurations ar...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Error executing method 'init_device'. This might cause deadlock in distributed execution. bug ### Your current environment ### 🐛 Describe the bug I tried to deploy the model in a multi-machine and multi-GPU paral...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

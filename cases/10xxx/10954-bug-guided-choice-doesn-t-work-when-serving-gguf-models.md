# vllm-project/vllm#10954: [Bug]: guided_choice doesn't work when serving gguf models.

| 字段 | 值 |
| --- | --- |
| Issue | [#10954](https://github.com/vllm-project/vllm/issues/10954) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: guided_choice doesn't work when serving gguf models.

### Issue 正文摘录

### Your current environment I'm running the docker image `vllm/vllm-openai:latest` on an ec2 instance with the following specs ``` `-/oydNNdyo:.` `.:+shmMMMMMMMMMMMMMMmhs+:.` ----------------------------------------------------- -+hNNMMMMMMMMMMMMMMMMMMMMMMNNho- OS: Amazon Linux 2 x86_64 .`` -/+shmNNMMMMMMNNmhs+/- ``. Host: g5.xlarge dNmhs+:. `.:/oo/:.` .:+shmNd Kernel: 5.10.223-212.873.amzn2.x86_64 dMMMMMMMNdhs+:.. ..:+shdNMMMMMMMd Uptime: 4 hours, 53 mins dMMMMMMMMMMMMMMNds odNMMMMMMMMMMMMMMd Packages: 761 (rpm) dMMMMMMMMMMMMMMMMh yMMMMMMMMMMMMMMMMd Shell: bash 4.2.46 dMMMMMMMMMMMMMMMMh yMMMMMMMMMMMMMMMMd Terminal: /dev/pts/1 dMMMMMMMMMMMMMMMMh yMMMMMMMMMMMMMMMMd CPU: AMD EPYC 7R32 (4) @ 2.811GHz dMMMMMMMMMMMMMMMMh yMMMMMMMMMMMMMMMMd GPU: NVIDIA 00:1e.0 NVIDIA Corporation Device 2237 dMMMMMMMMMMMMMMMMh yMMMMMMMMMMMMMMMMd Memory: 8564MiB / 15802MiB dMMMMMMMMMMMMMMMMh yMMMMMMMMMMMMMMMMd dMMMMMMMMMMMMMMMMh yMMMMMMMMMMMMMMMMd dMMMMMMMMMMMMMMMMh yMMMMMMMMMMMMMMMMd dMMMMMMMMMMMMMMMMh yMMMMMMMMMMMMMMMMd .:+ydNMMMMMMMMMMMh yMMMMMMMMMMMNdy+:. `.:+shNMMMMMh yMMMMMNhs+:`` `-+shy shs+: ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can't use "guided_choice" when hosting a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ing gguf models. bug;stale ### Your current environment I'm running the docker image `vllm/vllm-openai:latest` on an ec2 instance with the following specs ``` `-/oydNNdyo:.` `.:+shmMMMMMMMMMMMMMMmhs+:.` ----------------...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: guided_choice doesn't work when serving gguf models. bug;stale ### Your current environment I'm running the docker image `vllm/vllm-openai:latest` on an ec2 instance with the following specs ``` `-/oydNNdyo:.` `....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: guided_choice doesn't work when serving gguf models. bug;stale ### Your current environment I'm running the docker image `vllm/vllm-openai:latest` on an ec2 instance with the following specs ``` `-/oydNNdyo:.` `....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ur current environment I'm running the docker image `vllm/vllm-openai:latest` on an ec2 instance with the following specs ``` `-/oydNNdyo:.` `.:+shmMMMMMMMMMMMMMMmhs+:.` -------------------------------------------------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

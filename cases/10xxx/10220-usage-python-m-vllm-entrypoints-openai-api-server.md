# vllm-project/vllm#10220: [Usage]: 怎么修改python -m vllm.entrypoints.openai.api_server的提示词

| 字段 | 值 |
| --- | --- |
| Issue | [#10220](https://github.com/vllm-project/vllm/issues/10220) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 怎么修改python -m vllm.entrypoints.openai.api_server的提示词

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` python3.10.12 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ![108FCB7D-FBB6-429b-9B79-EA00E0A9AFDB](https://github.com/user-attachments/assets/a750281d-eed9-4036-8b22-361193adeb6c) 我希望修改系统提示词，不论是在代码里、模型文件里或者命令行里，怎么改变这个提示词呢 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 12 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ![108FCB7D-FBB6-429b-9B79-EA00E0A9AFDB](https://github.com/user-attachments...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 示词呢 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ![108FCB7D-FBB6-429b-9B79-EA00E0A9AFDB](https://github.com/user-attachments/asse...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: 怎么修改python -m vllm.entrypoints.openai.api_server的提示词 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` python3.10.12 ### How would you like to use vllm I want to run inf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

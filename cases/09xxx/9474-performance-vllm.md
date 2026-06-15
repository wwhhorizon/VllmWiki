# vllm-project/vllm#9474: [Performance]: VLLM 请求数量过多时太慢

| 字段 | 值 |
| --- | --- |
| Issue | [#9474](https://github.com/vllm-project/vllm/issues/9474) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: VLLM 请求数量过多时太慢

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm 我正在使用一张A100 部署的72B量化模型 这是启动脚本 python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --max-model-len 9000 --served-model-name chat-yzq --model /workspace/chat-v1-Int4 --enforce-eager --tensor-parallel-size 1 --gpu-memory-utilization 0.85 当1天有1万次请求时 回复会变得非常缓慢 有什么办法吗 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `python collect_env.py` ``` ### How would you like to use vllm 我正在使用一张A100 部署的72B量化模型 这是启动脚本 python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --max-model-len 9000 --served-model-name chat-yzq --model /workspa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: x-model-len 9000 --served-model-name chat-yzq --model /workspace/chat-v1-Int4 --enforce-eager --tensor-parallel-size 1 --gpu-memory-utilization 0.85 当1天有1万次请求时 回复会变得非常缓慢 有什么办法吗 ### Before submitting a new issue... - [X]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 启动脚本 python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --max-model-len 9000 --served-model-name chat-yzq --model /workspace/chat-v1-Int4 --enforce-eager --tensor-parallel-size 1 --gpu-memory-utilization 0.85 当...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: VLLM 请求数量过多时太慢 performance;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm 我正在使用一张A100 部署的72B量化模型 这是启动脚本 python -m vllm.entrypoints....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

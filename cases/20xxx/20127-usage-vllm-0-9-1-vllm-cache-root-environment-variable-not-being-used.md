# vllm-project/vllm#20127: [Usage]: vllm 0.9.1 VLLM_CACHE_ROOT environment variable not being used.

| 字段 | 值 |
| --- | --- |
| Issue | [#20127](https://github.com/vllm-project/vllm/issues/20127) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm 0.9.1 VLLM_CACHE_ROOT environment variable not being used.

### Issue 正文摘录

### Your current environment I am running the vllm 0.9.1 container on OpenShift. The VLLM_CACHE_ROOT environment variable is set to /vllm-workspace. I am getting this error from core.py: permissionError: [error 13] Permission denied: '/.cache' Is the environment variable being ignored? HF_HUB environment variables are being used. ### How would you like to use vllm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Permission denied: '/.cache' Is the environment variable being ignored? HF_HUB environment variables are being used. ### How would you like to use vllm ### Before submitting a new issue... - [x] Make sure you already se...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

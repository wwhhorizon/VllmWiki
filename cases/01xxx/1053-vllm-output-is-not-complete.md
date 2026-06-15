# vllm-project/vllm#1053: VLLM output is not complete

| 字段 | 值 |
| --- | --- |
| Issue | [#1053](https://github.com/vllm-project/vllm/issues/1053) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> VLLM output is not complete

### Issue 正文摘录

hai guys, thank you for making this super library. i have a question about the output of vllm i'm using GPU RTX A6000 50GB cuda 12 with model Vicuna13B-v1.5-4k from lmsys vllm is serve with gpu_memory_utilization 0.8 the parameter that i change for request is: 1. max_token 4096 2. temperature 0 i'm make custom prompt with context from text/document. why sometimes the output is not complete ?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: super library. i have a question about the output of vllm i'm using GPU RTX A6000 50GB cuda 12 with model Vicuna13B-v1.5-4k from lmsys vllm is serve with gpu_memory_utilization 0.8 the parameter that i change for reques...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tion about the output of vllm i'm using GPU RTX A6000 50GB cuda 12 with model Vicuna13B-v1.5-4k from lmsys vllm is serve with gpu_memory_utilization 0.8 the parameter that i change for request is: 1. max_token 4096 2. t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: is serve with gpu_memory_utilization 0.8 the parameter that i change for request is: 1. max_token 4096 2. temperature 0 i'm make custom prompt with context from text/document. why sometimes the output is not complete ?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

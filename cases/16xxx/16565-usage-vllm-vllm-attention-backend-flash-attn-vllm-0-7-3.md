# vllm-project/vllm#16565: [Usage]: vllm支持VLLM_ATTENTION_BACKEND=FLASH_ATTN吗？ vllm=0.7.3

| 字段 | 值 |
| --- | --- |
| Issue | [#16565](https://github.com/vllm-project/vllm/issues/16565) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm支持VLLM_ATTENTION_BACKEND=FLASH_ATTN吗？ vllm=0.7.3

### Issue 正文摘录

### Your current environment ```text 专家你好，请问下vllm支持VLLM_ATTENTION_BACKEND=FLASH_ATTN吗？ vllm=0.7.3 ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Usage]: vllm支持VLLM_ATTENTION_BACKEND=FLASH_ATTN吗？ vllm=0.7.3 usage ### Your current environment ```text 专家你好，请问下vllm支持VLLM_ATTENTION_BACKEND=FLASH_ATTN吗？ vllm=0.7.3 ``` ### How would you like to use vllm I want to run...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

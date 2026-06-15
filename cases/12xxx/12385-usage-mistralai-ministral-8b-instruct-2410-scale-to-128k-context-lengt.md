# vllm-project/vllm#12385: [Usage]: mistralai/Ministral-8B-Instruct-2410 scale to 128k context length.

| 字段 | 值 |
| --- | --- |
| Issue | [#12385](https://github.com/vllm-project/vllm/issues/12385) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: mistralai/Ministral-8B-Instruct-2410 scale to 128k context length.

### Issue 正文摘录

### Your current environment I'm trying to deploy mistralai/Ministral-8B-Instruct-2410 model for 128k context length, but the model config only allows 32768 max length. I encountered the same issue in Qwen 2.5 but they directly said rope scaling can be used to increase to 128k context length. Does anyone know what a similar config for this mistral model should be? ### How would you like to use vllm I want to run inference of a [mistralai/Ministral-8B-Instruct-2410](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: t environment I'm trying to deploy mistralai/Ministral-8B-Instruct-2410 model for 128k context length, but the model config only allows 32768 max length. I encountered the same issue in Qwen 2.5 but they directly said r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Usage]: mistralai/Ministral-8B-Instruct-2410 scale to 128k context length. usage;stale ### Your current environment I'm trying to deploy mistralai/Ministral-8B-Instruct-2410 model for 128k context length, but the model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: mistralai/Ministral-8B-Instruct-2410 scale to 128k context length. usage;stale ### Your current environment I'm trying to deploy mistralai/Ministral-8B-Instruct-2410 model for 128k context length, but the model config o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

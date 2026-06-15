# vllm-project/vllm#8813: [Usage]: How to use BitsAndBytesConfig with vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#8813](https://github.com/vllm-project/vllm/issues/8813) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use BitsAndBytesConfig with vllm serve

### Issue 正文摘录

### Your current environment I am running server using` vllm serve /models/Meta-Llama-3-70B-Instruct/ --quantization=bitsandbytes --disable-log-requests --load-format bitsandbytes` How can I specify Config for BitsAndBytes? Also I have the same question for other quantization for ex. deepspeed - How to pass the config file? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: How to use BitsAndBytesConfig with vllm serve usage;stale ### Your current environment I am running server using` vllm serve /models/Meta-Llama-3-70B-Instruct/ --quantization=bitsandbytes --disable-log-requests...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: dbytes --disable-log-requests --load-format bitsandbytes` How can I specify Config for BitsAndBytes? Also I have the same question for other quantization for ex. deepspeed - How to pass the config file? ### How would yo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to use BitsAndBytesConfig with vllm serve usage;stale ### Your current environment I am running server using` vllm serve /models/Meta-Llama-3-70B-Instruct/ --quantization=bitsandbytes --disable-log-requests...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: am running server using` vllm serve /models/Meta-Llama-3-70B-Instruct/ --quantization=bitsandbytes --disable-log-requests --load-format bitsandbytes` How can I specify Config for BitsAndBytes? Also I have the same quest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

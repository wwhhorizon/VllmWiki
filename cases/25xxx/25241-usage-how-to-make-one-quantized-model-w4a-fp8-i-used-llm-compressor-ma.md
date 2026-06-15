# vllm-project/vllm#25241: [Usage]: how to make one quantized model(w4a FP8). I used llm-compressor make one. But it not work in vllm 0.10.2.

| 字段 | 值 |
| --- | --- |
| Issue | [#25241](https://github.com/vllm-project/vllm/issues/25241) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to make one quantized model(w4a FP8). I used llm-compressor make one. But it not work in vllm 0.10.2.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` how to make one quantized model(w4a FP8). I used llm-compressor make one. But it not work in vllm 0.10.2. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 2. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Usage]: how to make one quantized model(w4a FP8). I used llm-compressor make one. But it not work in vllm 0.10.2. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` how to make o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: how to make one quantized model(w4a FP8). I used llm-compressor make one. But it not work in vllm 0.10.2. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` how to make o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ). I used llm-compressor make one. But it not work in vllm 0.10.2. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` how to make one quantized model(w4a FP8). I used llm-compress...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

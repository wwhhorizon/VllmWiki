# vllm-project/vllm#25862: [Usage]: How to change the video sample fps with Qwen3-VL?

| 字段 | 值 |
| --- | --- |
| Issue | [#25862](https://github.com/vllm-project/vllm/issues/25862) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to change the video sample fps with Qwen3-VL?

### Issue 正文摘录

### Your current environment vLLM Version : 0.11.0rc2.dev22+g27d7638b9 (git sha: 27d7638b9) ### How would you like to use vllm Hi, I want to change the fps of an video. I tried the following code, but it doesn't work, the inference speed doesn't change. How to do this? Thank you! `{ "type": "video_url", "video_url": { "url": f"file://{temp_video_path}" }, "fps": 1, "extra_body": { "mm_processor_kwargs": { "fps": 1 } } },` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sample fps with Qwen3-VL? usage;stale ### Your current environment vLLM Version : 0.11.0rc2.dev22+g27d7638b9 (git sha: 27d7638b9) ### How would you like to use vllm Hi, I want to change the fps of an video. I tried the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: },` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How to change the video sample fps with Qwen3-VL? usage;stale ### Your current environment vLLM Version : 0.11.0rc2.dev22+g27d7638b9 (git sha: 27d7638b9) ### How would you like to use vllm Hi, I want to change...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to change the video sample fps with Qwen3-VL? usage;stale ### Your current environment vLLM Version : 0.11.0rc2.dev22+g27d7638b9 (git sha: 27d7638b9) ### How would you like to use vllm Hi, I want to change...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

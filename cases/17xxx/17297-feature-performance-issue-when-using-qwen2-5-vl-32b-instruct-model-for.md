# vllm-project/vllm#17297: [Feature]: Performance issue, when using Qwen2.5-VL-32B-Instruct model for multi graph inference

| 字段 | 值 |
| --- | --- |
| Issue | [#17297](https://github.com/vllm-project/vllm/issues/17297) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Performance issue, when using Qwen2.5-VL-32B-Instruct model for multi graph inference

### Issue 正文摘录

### 🚀 The feature, motivation and pitch 1、Question When using the Qwen2.5-VL-32B-Instruct model with 9 1080P images as input, after input_preprocessor processing, the pixel_values tensor dimension in mm_kwargs within processed_inputs is [96876,1176]. This high dimensionality causes very long serialization and deserialization times between processes. In this example, both serialization and deserialization take about 8 seconds each (multi-GPU process communication). Are there any solutions to optimize this? Multi-image preprocessing is currently performed on the CPU. Is it possible to move the preprocessing to the GPU? The preprocessing takes approximately 10 seconds. 2、The following is a reproduction environment 1）VLLM version: 0.8.3 2）Start command: python3 -m vllm.entrypoints.openai.api_server --model /models/Qwen2.5-VL-32B-Instruct/ --limit-mm-per-prompt image=12 --tensor-parallel-size 4 --max-model-len 64000 3、Requests: curl --location '127.0.0.1:8000/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{ "model": "/models/Qwen2.5-VL-32B-Instruct/", "messages": [ { "role": "user", "content": [ { "type": "text", "text": "描述下列图片" }, { "type": "image_url", "i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Performance issue, when using Qwen2.5-VL-32B-Instruct model for multi graph inference feature request;stale ### 🚀 The feature, motivation and pitch 1、Question When using the Qwen2.5-VL-32B-Instruct model with...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: en using Qwen2.5-VL-32B-Instruct model for multi graph inference feature request;stale ### 🚀 The feature, motivation and pitch 1、Question When using the Qwen2.5-VL-32B-Instruct model with 9 1080P images as input, after...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 0 seconds. 2、The following is a reproduction environment 1）VLLM version: 0.8.3 2）Start command: python3 -m vllm.entrypoints.openai.api_server --model /models/Qwen2.5-VL-32B-Instruct/ --limit-mm-per-prompt image=12 --ten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#18372: [Bug]: Dynamic loading LoRA is not working properly

| 字段 | 值 |
| --- | --- |
| Issue | [#18372](https://github.com/vllm-project/vllm/issues/18372) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Dynamic loading LoRA is not working properly

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using vllm 0.6.5 version now. And, I make a script for unloading and loading lora weights dynamically while vllm serving. For example curl -X POST "http://localhost:8012/v1/unload_lora_adapter" -H "Content-Type":"application/json" --data '{ "lora_name":"ex" }' curl -X POST "http://localhost:8012/v1/load_lora_adapter" -H "Content-Type":"application/json" --data '{ "lora_name":"ex", "lora_path":"${LORA_PATH}"}' When I run this script, it return success always even I pass a path as a "LORA_PATH" which is not exist. And model output does not affected. This is server log. INFO: ::1:43228 - "POST /v1/load_lora_adapter HTTP/1.1" 200 OK But, if I use `--lora-modules` explicitly when I run vllm serve, it works fine. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: our current environment ### 🐛 Describe the bug I'm using vllm 0.6.5 version now. And, I make a script for unloading and loading lora weights dynamically while vllm serving. For example curl -X POST "http://localhost:801...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ccess always even I pass a path as a "LORA_PATH" which is not exist. And model output does not affected. This is server log. INFO: ::1:43228 - "POST /v1/load_lora_adapter HTTP/1.1" 200 OK But, if I use `--lora-modules`...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Dynamic loading LoRA is not working properly bug;stale ### Your current environment ### 🐛 Describe the bug I'm using vllm 0.6.5 version now. And, I make a script for unloading and loading lora weights dynamically...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

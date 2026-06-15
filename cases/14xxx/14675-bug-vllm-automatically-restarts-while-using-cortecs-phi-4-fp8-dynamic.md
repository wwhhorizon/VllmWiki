# vllm-project/vllm#14675: [Bug]: Vllm automatically restarts while using cortecs/phi-4-FP8-Dynamic

| 字段 | 值 |
| --- | --- |
| Issue | [#14675](https://github.com/vllm-project/vllm/issues/14675) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Vllm automatically restarts while using cortecs/phi-4-FP8-Dynamic

### Issue 正文摘录

### Your current environment Vllm version used : vllm/vllm-openai:v0.7.3 ### 🐛 Describe the bug Vllm restarts randomly while running multiple subsequent request with **cortecs/phi-4-FP8-Dynamic.** DEBUG 03-12 03:19:03 launcher.py:59] python3 -m vllm.entrypoints.openai.api_server --model cortecs/phi-4-FP8-Dynamic --dtype auto --max-model-len 14336 --tensor-parallel-size 1 --host=0.0.0.0 --port=9000 --gpu-memory-utilization=0.9 --trust-remote-code --api-key mits-d326429bf1aa6c4c7f6f0c910fd0aa04c8976498df5e06ab --enable-prefix-caching INFO 03-12 03:19:03 launcher.py:62] Shutting down FastAPI HTTP server. INFO: Shutting down DEBUG 03-12 03:19:07 client.py:174] Shutting down MQLLMEngineClient check health loop. DEBUG 03-12 03:19:07 client.py:257] Shutting down MQLLMEngineClient output handler. Here the last few logs after restarted unexpectedly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Vllm automatically restarts while using cortecs/phi-4-FP8-Dynamic bug;stale ### Your current environment Vllm version used : vllm/vllm-openai:v0.7.3 ### 🐛 Describe the bug Vllm restarts randomly while running mul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Vllm automatically restarts while using cortecs/phi-4-FP8-Dynamic bug;stale ### Your current environment Vllm version used : vllm/vllm-openai:v0.7.3 ### 🐛 Describe the bug Vllm restarts randomly while running multipl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g cortecs/phi-4-FP8-Dynamic bug;stale ### Your current environment Vllm version used : vllm/vllm-openai:v0.7.3 ### 🐛 Describe the bug Vllm restarts randomly while running multiple subsequent request with **cortecs/phi-4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: y. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 03:19:03 launcher.py:59] python3 -m vllm.entrypoints.openai.api_server --model cortecs/phi-4-FP8-Dynamic --dtype auto --max-model-len 14336 --tensor-parallel-size 1 --host=0.0.0.0 --port=9000 --gpu-memory-utilization=0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

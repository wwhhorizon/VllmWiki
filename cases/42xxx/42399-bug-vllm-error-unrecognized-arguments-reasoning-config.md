# vllm-project/vllm#42399: [Bug]: vllm: error: unrecognized arguments: --reasoning-config

| 字段 | 值 |
| --- | --- |
| Issue | [#42399](https://github.com/vllm-project/vllm/issues/42399) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm: error: unrecognized arguments: --reasoning-config

### Issue 正文摘录

### Your current environment docker ### 🐛 Describe the bug ``` docker run -d --ipc host \ -p "8000:8000" \ "vllm/vllm-openai:v0.20.1" \ "cyankiwi/Qwen3.6-35B-A3B-AWQ-4bit" \ --dtype auto \ --max-model-len "${VLLM_MAX_MODEL_LEN:-20480}" \ --gpu-memory-utilization "${VLLM_GPU_MEM_UTIL:-0.95}" \ --reasoning-parser qwen3 \ --reasoning-config '{"reasoning_start_str":" ","reasoning_end_str": " -- Reasoning preempted. Answer now. "}' --enable-prefix-caching \ --enable-chunked-prefill \ --trust-remote-code \ --language-model-only ``` but it gives: vllm: error: unrecognized arguments: --reasoning-config {"reasoning_start_str":" ","reasoning_end_str":" -- Reasoning preempted. Answer now. "} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm: error: unrecognized arguments: --reasoning-config bug ### Your current environment docker ### 🐛 Describe the bug ``` docker run -d --ipc host \ -p "8000:8000" \ "vllm/vllm-openai:v0.20.1" \ "cyankiwi/Qwen3....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cognized arguments: --reasoning-config bug ### Your current environment docker ### 🐛 Describe the bug ``` docker run -d --ipc host \ -p "8000:8000" \ "vllm/vllm-openai:v0.20.1" \ "cyankiwi/Qwen3.6-35B-A3B-AWQ-4bit" \ --...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: m/vllm-openai:v0.20.1" \ "cyankiwi/Qwen3.6-35B-A3B-AWQ-4bit" \ --dtype auto \ --max-model-len "${VLLM_MAX_MODEL_LEN:-20480}" \ --gpu-memory-utilization "${VLLM_GPU_MEM_UTIL:-0.95}" \ --reasoning-parser qwen3 \ --reasoni...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: "} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted. Answer now. "}' --enable-prefix-caching \ --enable-chunked-prefill \ --trust-remote-code \ --language-model-only ``` but it gives: vllm: error: unrecognized arguments: --reasoning-config {"reasoning_start_str":" ",...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#29006: [Bug]: OpenAI completion error: 500 Unable to allocate 31.6 GiB for an array with shape (65158, 65158) and data type int64

| 字段 | 值 |
| --- | --- |
| Issue | [#29006](https://github.com/vllm-project/vllm/issues/29006) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenAI completion error: 500 Unable to allocate 31.6 GiB for an array with shape (65158, 65158) and data type int64

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when running [baidu-ernie 4.5](https://huggingface.co/cyankiwi/ERNIE-4.5-VL-28B-A3B-Thinking-AWQ-4bit) on the given system either the process gets killed( without `export NCCL_P2P_DISABLE=1`) when i send the request or the errors just come in like this on the cli (APIServer pid=14800) INFO: 128.77.32.149:0 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error Running the model locally on nightly build i installed the day of launch of the model ```bash vllm serve models/baidu-ernie/ --trust-remote-code --reasoning-parser ernie45 --tool-call-parser ernie45 --enable-auto-tool-choice --max-model-len 95000 --served-model-name baidu-ernie ``` iand i recieve these on the client's end `Unable to allocate 31.6 GiB for an array with shape (65158, 65158) and data type int64` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: HTTP/1.1" 500 Internal Server Error Running the model locally on nightly build i installed the day of launch of the model ```bash vllm serve models/baidu-ernie/ --trust-remote-code --reasoning-parser ernie45 --tool-call...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 31.6 GiB for an array with shape (65158, 65158) and data type int64 bug;stale ### Your current environment ### 🐛 Describe the bug when running [baidu-ernie 4.5](https://huggingface.co/cyankiwi/ERNIE-4.5-VL-28B-A3B-Think...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 64` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nment ### 🐛 Describe the bug when running [baidu-ernie 4.5](https://huggingface.co/cyankiwi/ERNIE-4.5-VL-28B-A3B-Thinking-AWQ-4bit) on the given system either the process gets killed( without `export NCCL_P2P_DISABLE=1`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

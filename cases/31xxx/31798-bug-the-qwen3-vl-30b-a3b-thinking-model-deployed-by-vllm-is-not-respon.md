# vllm-project/vllm#31798: [Bug]: The Qwen3-VL-30B-A3B-Thinking model deployed by vllm  is not responding to requests.

| 字段 | 值 |
| --- | --- |
| Issue | [#31798](https://github.com/vllm-project/vllm/issues/31798) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The Qwen3-VL-30B-A3B-Thinking model deployed by vllm  is not responding to requests.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug root@qwen3-vl-30b-a3b-7d895d6bb6-mfc2r:/workspace/pytorch# curl -m 30 http://localhost:8080/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen3-VL-30B-A3B-Thinking", "prompt": "Hello, how are you?", "max_tokens": 10, "temperature": 0, "skip_special_tokens": true }' curl: (28) Operation timed out after 30002 milliseconds with 0 bytes received # thread trace from gdb can get from here ``` https://zcy-distribute.oss-cn-hangzhou.aliyuncs.com/zdebug/gdb_threads.log ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: how are you?", "max_tokens": 10, "temperature": 0, "skip_special_tokens": true }' curl: (28) Operation timed out after 30002 milliseconds with 0 bytes received # thread trace from gdb can get from here ``` https://zcy-d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The Qwen3-VL-30B-A3B-Thinking model deployed by vllm is not responding to requests. bug;stale ### Your current environment ### 🐛 Describe the bug root@qwen3-vl-30b-a3b-7d895d6bb6-mfc2r:/workspace/pytorch# curl -m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e Qwen3-VL-30B-A3B-Thinking model deployed by vllm is not responding to requests. bug;stale ### Your current environment ### 🐛 Describe the bug root@qwen3-vl-30b-a3b-7d895d6bb6-mfc2r:/workspace/pytorch# curl -m 30 http:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nt ci_build;hardware_porting;model_support;sampling_logits cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

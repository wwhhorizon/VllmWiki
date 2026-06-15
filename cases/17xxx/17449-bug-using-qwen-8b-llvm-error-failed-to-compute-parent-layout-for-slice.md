# vllm-project/vllm#17449: [Bug]: using qwen-8B , LLVM ERROR: Failed to compute parent layout for slice layout

| 字段 | 值 |
| --- | --- |
| Issue | [#17449](https://github.com/vllm-project/vllm/issues/17449) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: using qwen-8B , LLVM ERROR: Failed to compute parent layout for slice layout

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm 0.8.5 vllm serve /root/model/Qwen3-8B --dtype half --port 8075 --gpu-memory-utilization 0.8 INFO: 115.239.217.175:36366 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 04-30 14:30:44 [engine.py:310] Added request chatcmpl-dbc9987ce4734f5b8321adfdb5ae22b7. LLVM ERROR: Failed to compute parent layout for slice layout. ERROR 04-30 14:30:50 [client.py:305] RuntimeError('Engine process (pid 2837204) died.') ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: using qwen-8B , LLVM ERROR: Failed to compute parent layout for slice layout bug ### Your current environment ### 🐛 Describe the bug vllm 0.8.5 vllm serve /root/model/Qwen3-8B --dtype half --port 8075 --gpu-memor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ### 🐛 Describe the bug vllm 0.8.5 vllm serve /root/model/Qwen3-8B --dtype half --port 8075 --gpu-memory-utilization 0.8 INFO: 115.239.217.175:36366 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 04-30 14:30:44 [engi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .') ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: using qwen-8B , LLVM ERROR: Failed to compute parent layout for slice layout bug ### Your current environment ### 🐛 Describe the bug vllm 0.8.5 vllm serve /root/model/Qwen3-8B --dtype half --port 8075 --gpu-memor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t/completions HTTP/1.1" 200 OK INFO 04-30 14:30:44 [engine.py:310] Added request chatcmpl-dbc9987ce4734f5b8321adfdb5ae22b7. LLVM ERROR: Failed to compute parent layout for slice layout. ERROR 04-30 14:30:50 [client.py:3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

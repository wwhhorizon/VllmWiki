# vllm-project/vllm#25571: [Bug]: Qwen3-Next-80B-A3B-Instruction pressure test error through vllm 0.10.2

| 字段 | 值 |
| --- | --- |
| Issue | [#25571](https://github.com/vllm-project/vllm/issues/25571) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next-80B-A3B-Instruction pressure test error through vllm 0.10.2

### Issue 正文摘录

### Your current environment Environment: 4xH20, 32C MEM240G vllm 0.10.2 ### 🐛 Describe the bug startup command: nohup python -m vllm.entrypoints.openai.api_server \ --model /workspace/model \ --tensor-parallel-size 4 \ --dtype bfloat16 \ --max-model-len 4096 \ --max-num-seqs 4 \ --max-num-batched-tokens 8192 \ --gpu-memory-utilization 0.85 > go.log 2>&1 & When I used JMeter to test the chat interface with 3 concurrent attempts, the service encountered an error and crashed request param: { "model": ".....", "stream": false, "messages": [ { "role": "system", "content": ".........." }, { "role": "user", "content": "..........." } ] } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nai.api_server \ --model /workspace/model \ --tensor-parallel-size 4 \ --dtype bfloat16 \ --max-model-len 4096 \ --max-num-seqs 4 \ --max-num-batched-tokens 8192 \ --gpu-memory-utilization 0.85 > go.log 2>&1 & When I us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-Next-80B-A3B-Instruction pressure test error through vllm 0.10.2 bug;stale ### Your current environment Environment: 4xH20, 32C MEM240G vllm 0.10.2 ### 🐛 Describe the bug startup command: nohup python -m vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: en3-Next-80B-A3B-Instruction pressure test error through vllm 0.10.2 bug;stale ### Your current environment Environment: 4xH20, 32C MEM240G vllm 0.10.2 ### 🐛 Describe the bug startup command: nohup python -m vllm.entryp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ror and crashed request param: { "model": ".....", "stream": false, "messages": [ { "role": "system", "content": ".........." }, { "role": "user", "content": "..........." } ] } ### Before subm

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

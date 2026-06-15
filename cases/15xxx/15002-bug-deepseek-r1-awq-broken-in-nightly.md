# vllm-project/vllm#15002: [Bug]: DeepSeek-R1-AWQ broken in nightly

| 字段 | 值 |
| --- | --- |
| Issue | [#15002](https://github.com/vllm-project/vllm/issues/15002) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-R1-AWQ broken in nightly

### Issue 正文摘录

### Your current environment Model: `cognitivecomputations/DeepSeek-R1-AWQ` Served on 8xH100s: `vllm serve "cognitivecomputations/DeepSeek-R1-AWQ" -tp 8 --gpu-memory-utilization 0.8 --max-model-len 4096 --enable-chunked-prefill --trust-remote-code --max-num-batched-tokens 4096 --dtype float16 --port 1234` Prompted with: ``` curl -X POST http://localhost:1234/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "cognitivecomputations/DeepSeek-R1-AWQ", "messages": [ {"role": "user", "content": "What is the capital of France?"} ], "temperature": 0.7, "max_tokens": 512 }' ``` ### 🐛 Describe the bug In `vllm==0.7.3`, everything looks good: ``` {"id":"chatcmpl-acf69072a2a545c4baedcf93efbde64e","object":"chat.completion","created":1742275076,"model":"local-awq","choices":[{"index":0,"message":{"role":"assistant","reasoning_content":null,"content":"Okay, so the question is asking for the capital of France. Let me think. I know France is a country in Europe. I've heard of Paris being mentioned a lot in relation to France. Wait, is Paris the capital? I remember seeing the Eiffel Tower in Paris, so maybe that's the capital. But let me double-check in my mind. Are there othe...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: able-chunked-prefill --trust-remote-code --max-num-batched-tokens 4096 --dtype float16 --port 1234` Prompted with: ``` curl -X POST http://localhost:1234/v1/chat/completions -H "Content-Type: application/json" -d '{ "mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: environment Model: `cognitivecomputations/DeepSeek-R1-AWQ` Served on 8xH100s: `vllm serve "cognitivecomputations/DeepSeek-R1-AWQ" -tp 8 --gpu-memory-utilization 0.8 --max-model-len 4096 --enable-chunked-prefill --trust-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s the capital. But let me double-check in my mind. Are there other major cities in France that could be the capital? Lyon, Marseille, maybe Toulouse? No, I think Paris is the most well-known. Also, I think the governmen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ug]: DeepSeek-R1-AWQ broken in nightly bug ### Your current environment Model: `cognitivecomputations/DeepSeek-R1-AWQ` Served on 8xH100s: `vllm serve "cognitivecomputations/DeepSeek-R1-AWQ" -tp 8 --gpu-memory-utilizatio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -tp 8 --gpu-memory-utilization 0.8 --max-model-len 4096 --enable-chunked-prefill --trust-remote-code --max-num-batched-tokens 4096 --dtype float16 --port 1234` Prompted with: ``` curl -X POST http://localhost:1234/v1/ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

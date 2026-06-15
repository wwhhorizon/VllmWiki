# vllm-project/vllm#13197: [Usage]:  'CompletionChoice' object has no attribute 'delta'

| 字段 | 值 |
| --- | --- |
| Issue | [#13197](https://github.com/vllm-project/vllm/issues/13197) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  'CompletionChoice' object has no attribute 'delta'

### Issue 正文摘录

### Your current environment vllm 0.7.2 ### How would you like to use vllm - Service initiation ``` python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --max-model-len 16384 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.8 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-reasoner --model DeepSeek-R1-awq/ ``` - Request body ``` completion = client.completions.create(model="deepseek-reasoner", prompt=prompts, max_tokens = 20, temperature = 0.6, stream=True) for chunk in completion: print(chunk) ``` - return to the result ``` Completion(id='cmpl-75fac4e9a40048f49fbd9ac58fa64eb4', choices=[CompletionChoice(finish_reason='length', index=0, logprobs=None, text='那么', stop_reason=None)], created=1739415321, model='deepseek-reasoner', object='text_completion', system_fingerprint=None, usage=None) ``` - question Why is there no delta field in the returned result chunk.choices [0].delta.reasoning_content ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.v...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 000 --max-model-len 16384 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.8 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-reasoner --model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ent ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: -parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.8 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-reasoner --model DeepSeek-R1-awq/ ``` - Request body ``` completion = c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --max-model-len 16384 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.8 --kv-cache-dtype fp8_e5m2 --cal...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: el-len 16384 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.8 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-reasoner --model DeepSeek-R1-a...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

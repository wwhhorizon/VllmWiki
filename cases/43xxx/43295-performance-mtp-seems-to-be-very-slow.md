# vllm-project/vllm#43295: [Performance]: MTP seems to be very slow

| 字段 | 值 |
| --- | --- |
| Issue | [#43295](https://github.com/vllm-project/vllm/issues/43295) |
| 状态 | open |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: MTP seems to be very slow

### Issue 正文摘录

### Proposal to improve performance I have tried with your [quantized model](https://huggingface.co/RedHatAI/Qwen3.6-35B-A3B-NVFP4) an I found other issues regarding MTP. The MTP model is clearly slower, am I doing something wrong? ## `config.yaml` used: ```yaml model: RedHatAI/Qwen3.6-35B-A3B-NVFP4 dtype: bfloat16 kv-cache-dtype: fp8 gpu-memory-utilization: 0.95 max-model-len: 262144 max-num-batched-tokens: 4096 max-num-seqs: 200 max-cudagraph-capture-size: 209 enable-prefix-caching: true reasoning-parser: qwen3 trust-remote-code: true enable-auto-tool-choice: true tool-call-parser: qwen3_coder default-chat-template-kwargs: '{"enable_thinking": false}' #speculative-config: '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' # with or without this line download-dir: /workspace/models host: 0.0.0.0 port: 18000 ``` ## Command for benchmarks: ``` vllm bench serve --base-url "http://0.0.0.0:18000" --backend openai-chat --endpoint "/v1/chat/completions" --model "RedHatAI/Qwen3.6-35B-A3B-NVFP4" --dataset-name random --random-input-len 16384 --random-output-len 4096 --num-prompts 100 --request-rate 20 ``` ## Experiment 1 (NO MTP): ``` (APIServer pid=3646) INFO 05-19 10:10:01 [logger...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: performance ### Proposal to improve performance I have tried with your [quantized model](https://huggingface.co/RedHatAI/Qwen3.6-35B-A3B-NVFP4) an I found other issues regarding MTP. The MTP model is clearly slower, am...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: ad-dir: /workspace/models host: 0.0.0.0 port: 18000 ``` ## Command for benchmarks: ``` vllm bench serve --base-url "http://0.0.0.0:18000" --backend openai-chat --endpoint "/v1/chat/completions" --model "RedHatAI/Qwen3.6...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e ### Proposal to improve performance I have tried with your [quantized model](https://huggingface.co/RedHatAI/Qwen3.6-35B-A3B-NVFP4) an I found other issues regarding MTP. The MTP model is clearly slower, am I doing so...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: qwen3_coder default-chat-template-kwargs: '{"enable_thinking": false}' #speculative-config: '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' # with or without this line download-dir: /workspace/models host: 0.0....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: aml` used: ```yaml model: RedHatAI/Qwen3.6-35B-A3B-NVFP4 dtype: bfloat16 kv-cache-dtype: fp8 gpu-memory-utilization: 0.95 max-model-len: 262144 max-num-batched-tokens: 4096 max-num-seqs: 200 max-cudagraph-capture-size:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

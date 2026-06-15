# vllm-project/vllm#13219: [Bug]: when i use docker vllm/vllm-openai:v0.7.2 to deploy r1 awq, i got empty content

| 字段 | 值 |
| --- | --- |
| Issue | [#13219](https://github.com/vllm-project/vllm/issues/13219) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: when i use docker vllm/vllm-openai:v0.7.2 to deploy r1 awq, i got empty content

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug device ：8 * H100 python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 23333 --max-model-len 60000 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.92 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-reasoner --model cognitivecomputations/DeepSeek-R1-AWQ curl http://localhost:23333/v1/chat/completions -H "Content-Type: application/json" -d '{"model": "deepseek-reasoner", "messages": [ {"role": "user", "content": "你是谁"} ], "stream":true, "temperature":1.2 }' data: {"id":"chatcmpl-c7e88282efa547cfba27b429df7df593","object":"chat.completion.chunk","created":1739440234,"model":"deepseek-reasoner","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-c7e88282efa547cfba27b429df7df593","object":"chat.completion.chunk","created":1739440234,"model":"deepseek-reasoner","choices":[{"index":0,"delta":{"content":""},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-c7e88282efa547cfba27b429df7df593","object":"chat.completion.chunk","created":1739440234,"model":"deepseek-re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: when i use docker vllm/vllm-openai:v0.7.2 to deploy r1 awq, i got empty content bug;stale ### Your current environment ### 🐛 Describe the bug device ：8 * H100 python3 -m vllm.entrypoints.openai.api_server --host...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 333 --max-model-len 60000 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.92 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-reasoner --model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ale ### Your current environment ### 🐛 Describe the bug device ：8 * H100 python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 23333 --max-model-len 60000 --trust-remote-code --tensor-parallel-size 8 --qua...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.92 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-reasoner --model cognitivecomputations/DeepSeek-R1-AWQ curl http://loca...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 23333 --max-model-len 60000 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.92 --kv-cache-dtype fp8_e5m2 --cal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

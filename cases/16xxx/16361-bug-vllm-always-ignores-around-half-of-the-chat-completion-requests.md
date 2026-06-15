# vllm-project/vllm#16361: [Bug]: vLLM always ignores around half of the chat completion requests

| 字段 | 值 |
| --- | --- |
| Issue | [#16361](https://github.com/vllm-project/vllm/issues/16361) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM always ignores around half of the chat completion requests

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running official qwen2.5 VL AWQ quant: ```bash CUDA_VISIBLE_DEVICES=0 vllm serve /mnt/e/models/Qwen_Qwen2.5-VL-7B-Instruct-AWQ --max-model-len 32768 --gpu-memory-utilization 0.9 --limit-mm-per-prompt image=1,video=1 --port 11440 ``` Then, i'm doing ten parallel very simple requests: ```bash (vllm) ubuntu@gpupc:~/Desktop/worker$ seq 10 | xargs -n1 -P10 curl -X POST "http://localhost:11440/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "model": "/mnt/e/models/Qwen_Qwen2.5-VL-7B-Instruct-AWQ", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello! Tell me something interesting."} ], "temperature": 0.7 }' \ -s | jq '.choices[0].message.content' "Sure, here's an interesting fact: Did you know that the human brain has about 86 billion neurons? Neurons are the basic units of the nervous system and are responsible for transmitting information throughout the body. Each neuron can connect with up to 10,000 other neurons, which means there are over 860 trillion connections in the human brain alone! This incredible complexity allows us to perform complex tasks...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: vLLM always ignores around half of the chat completion requests bug ### Your current environment ### 🐛 Describe the bug I'm running official qwen2.5 VL AWQ quant: ```bash CUDA_VISIBLE_DEVICES=0 vllm serve /mnt/e/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ### Your current environment ### 🐛 Describe the bug I'm running official qwen2.5 VL AWQ quant: ```bash CUDA_VISIBLE_DEVICES=0 vllm serve /mnt/e/models/Qwen_Qwen2.5-VL-7B-Instruct-AWQ --max-model-len 32768 --gpu-memory-u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 🐛 Describe the bug I'm running official qwen2.5 VL AWQ quant: ```bash CUDA_VISIBLE_DEVICES=0 vllm serve /mnt/e/models/Qwen_Qwen2.5-VL-7B-Instruct-AWQ --max-model-len 32768 --gpu-memory-utilization 0.9 --limit-mm-per-pro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: our current environment ### 🐛 Describe the bug I'm running official qwen2.5 VL AWQ quant: ```bash CUDA_VISIBLE_DEVICES=0 vllm serve /mnt/e/models/Qwen_Qwen2.5-VL-7B-Instruct-AWQ --max-model-len 32768 --gpu-memory-utiliz...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: eration throughput: 52.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 80.0% INFO 04-10 03:35:37 [loggers.py:80] Avg prompt throughput: 0.0 tokens/s, Avg generation through...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

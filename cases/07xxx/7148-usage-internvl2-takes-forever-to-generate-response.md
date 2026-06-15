# vllm-project/vllm#7148: [Usage]: Internvl2 takes forever to generate response

| 字段 | 值 |
| --- | --- |
| Issue | [#7148](https://github.com/vllm-project/vllm/issues/7148) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;sampling |
| 症状 | build_error;slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Internvl2 takes forever to generate response

### Issue 正文摘录

### Your current environment PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ### How would you like to use vllm I used this script to start the server: vllm serve OpenGVLab/InternVL2-8B --trust_remote_code --chat-template examples/template_chatml.jinja request: > curl http://localhost:8000/v1/chat/completions \ > -H "Content-Type: application/json" \ > -d '{ > "model": "OpenGVLab/InternVL2-8B", > "messages": [ > {"role": "system", "content": "You are a helpful assistant."}, > {"role": "user", "content": "Who won the world series in 2020?"} > ] > }' I got this in the log and the request never finish: INFO 08-05 15:09:11 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. INFO 08-05 15:09:16 logger.py:36] Received request chat-79478648dc964a728b624eae407d9e74: prompt: ' system\nYou are a helpful assistant. \n user\nWho won the world series in 2020? \n assistant\n', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r to generate response usage;stale ### Your current environment PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ### How would you like to use vllm I used this script to start the serv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: current environment PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ### How would you like to use vllm I used this script to start the server: vllm serve OpenGVLab/InternVL2-8B --trus...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Internvl2 takes forever to generate response usage;stale ### Your current environment PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ### How would you like to use vllm I use...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Internvl2 takes forever to generate response usage;stale ### Your current environment PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ### How would you like to use vllm I use...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. INFO 08-05 15:09:16 logger.py:36] Received request chat-79478648dc964a728b624eae407d9e74: prompt:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

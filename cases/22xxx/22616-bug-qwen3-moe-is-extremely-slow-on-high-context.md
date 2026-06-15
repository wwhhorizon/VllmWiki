# vllm-project/vllm#22616: [Bug]: Qwen3 Moe is extremely slow on high context

| 字段 | 值 |
| --- | --- |
| Issue | [#22616](https://github.com/vllm-project/vllm/issues/22616) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 Moe is extremely slow on high context

### Issue 正文摘录

### Your current environment to run a block-wise quantized model on rtx pro 6000, I compiled vllm from source code as the tutorial on docs.vllm.ai ### 🐛 Describe the bug Qwen3 Moe is extremely slow on high context. for Qwen3-30b-a3b-gptq on 4*2080ti 22gb, the critical value is 2k tokens. for Qwen3-235b-a22b-fp8(block-wise) on 4*rtx pro 6000, it's 140k tokens(max-model-len=256k). `(APIServer pid=12152) INFO 08-11 03:54:05 [loggers.py:123] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 35.4 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.8%, Prefix cache hit rate: 66.4% (APIServer pid=12152) INFO 08-11 03:54:15 [loggers.py:123] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 35.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.9%, Prefix cache hit rate: 66.4% (APIServer pid=12152) INFO 08-11 03:54:25 [loggers.py:123] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 33.8 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.9%, Prefix cache hit rate: 66.4% (APIServer pid=12152) INFO 08-11 03:54:35 [loggers.py:123] Engine 000: Avg prompt throughput: 0....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Qwen3 Moe is extremely slow on high context bug;stale ### Your current environment to run a block-wise quantized model on rtx pro 6000, I compiled vllm from source code as the tutorial on docs.vllm.ai ### 🐛 Descr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t environment to run a block-wise quantized model on rtx pro 6000, I compiled vllm from source code as the tutorial on docs.vllm.ai ### 🐛 Describe the bug Qwen3 Moe is extremely slow on high context. for Qwen3-30b-a3b-g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: h context bug;stale ### Your current environment to run a block-wise quantized model on rtx pro 6000, I compiled vllm from source code as the tutorial on docs.vllm.ai ### 🐛 Describe the bug Qwen3 Moe is extremely slow o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Your current environment to run a block-wise quantized model on rtx pro 6000, I compiled vllm from source code as the tutorial on docs.vllm.ai ### 🐛 Describe the bug Qwen3 Moe is extremely slow on high context. for...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: onfirmed this is not a promblem with xfromers or v0 engine,V1 engine and Flashattention also have this problem. in #17650 no one responsed to me. so I create a issue again, hope someone will fix this issue. ### Before s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

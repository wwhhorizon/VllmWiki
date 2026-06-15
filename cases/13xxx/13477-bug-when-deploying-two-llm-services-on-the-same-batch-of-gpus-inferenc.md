# vllm-project/vllm#13477: [Bug]:  When deploying two llm services on the same batch of GPUs. Inference will be twice as slow

| 字段 | 值 |
| --- | --- |
| Issue | [#13477](https://github.com/vllm-project/vllm/issues/13477) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  When deploying two llm services on the same batch of GPUs. Inference will be twice as slow

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The startup instructions for my two services respectively `vllm serve Kotokin/sophosympatheia_Midnight-Miqu-70B-v1.0_GPTQ32G --tensor-parallel-size 8 --gpu-memory-utilization .24 --max-model-len 16384 --enable-prefix-caching --kv-cache-dtype auto --max-num-seqs 128 --block-size 32 -q gptq_marlin` `vllm serve Kotokin/sophosympatheia_Midnight-Miqu-70B-v1.0_GPTQ32G --tensor-parallel-size 8 --gpu-memory-utilization .24 --max-model-len 16384 --enable-prefix-caching --kv-cache-dtype auto --max-num-seqs 128 --block-size 32 -q gptq_marlin --port 8101` And used flashinfer for acceleration `export VLLM_ATTENTION_BACKEND=FLASHINFER` When I make a request to a single service, 10 requests are made concurrently. very fast. However, when I request two services at the same time, each service makes 10 concurrent requests at the same time. It's twice as slow. What is the principle and mechanism of this? Or is it a bug? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lo...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: --max-num-seqs 128 --block-size 32 -q gptq_marlin --port 8101` And used flashinfer for acceleration `export VLLM_ATTENTION_BACKEND=FLASHINFER` When I make a request to a single service, 10 requests are made concurrently...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: current requests at the same time. It's twice as slow. What is the principle and mechanism of this? Or is it a bug? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and aske...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: at the same time. It's twice as slow. What is the principle and mechanism of this? Or is it a bug? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot liv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: services on the same batch of GPUs. Inference will be twice as slow bug;stale ### Your current environment ### 🐛 Describe the bug The startup instructions for my two services respectively `vllm serve Kotokin/sophosympat...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 16384 --enable-prefix-caching --kv-cache-dtype auto --max-num-seqs 128 --block-size 32 -q gptq_marlin` `vllm serve Kotokin/sophosympatheia_Midnight-Miqu-70B-v1.0_GPTQ32G --tensor-parallel-size 8 --gpu-memory-utilization...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

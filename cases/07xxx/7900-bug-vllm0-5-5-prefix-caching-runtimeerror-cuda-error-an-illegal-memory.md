# vllm-project/vllm#7900: [Bug]: vllm0.5.5+Prefix caching RuntimeError: CUDA error: an illegal memory access was encountered 

| 字段 | 值 |
| --- | --- |
| Issue | [#7900](https://github.com/vllm-project/vllm/issues/7900) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.5.5+Prefix caching RuntimeError: CUDA error: an illegal memory access was encountered 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **[Package Version]** vllm == 0.5.5 torch == 2.4.0 vllm-flash-attn == 2.6.1 transformers == 4.44.0 **[Start CMD]** vllm is started using cmd below: CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /Qwen1.5-32B-Chat-AWQ \ --served-model-name qwen \ --enable-lora \ --lora-modules abs_lora=lora_path \ --max-loras 1 \ --quantization awq \ --max-cpu-loras 1 \ --gpu-memory-utilization 0.75 \ --port port_num \ --max-model-len 8192 \ --max-num-batched-tokens 16384 \ --max-num-seqs 100 \ --enable-prefix-caching **[Workload]** I post lots of requests using a threadpoll which thread_num=100. These requests share some identical prefix and I found prefix cache in vllm output: Prefix cache hit rate: GPU: 88.27%, CPU: 0.00%. The process was working perfectly until the vllm server was suddenly down and reported bug below. This bug is sometime triggerd when 10000+ of request has been successfully processed and sometime it was triggerd when 100000+ of request has been successfully processed. **The interesting thing is when i turned off the prefix caching, this bug was never triggerd. So I assume this bug is relevant wi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: tale ### Your current environment ### 🐛 Describe the bug **[Package Version]** vllm == 0.5.5 torch == 2.4.0 vllm-flash-attn == 2.6.1 transformers == 4.44.0 **[Start CMD]** vllm is started using cmd below: CUDA_VISIBLE_D...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vllm0.5.5+Prefix caching RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug **[Package Version]** vllm == 0.5.5 torch == 2.4.0 vllm-fl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug **[Package Version]** vllm == 0.5.5 torch == 2.4.0 vllm-flash-attn == 2.6.1 transformers =...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: e some identical prefix and I found prefix cache in vllm output: Prefix cache hit rate: GPU: 88.27%, CPU: 0.00%. The process was working perfectly until the vllm server was suddenly down and reported bug below. This bug...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lora \ --lora-modules abs_lora=lora_path \ --max-loras 1 \ --quantization awq \ --max-cpu-loras 1 \ --gpu-memory-utilization 0.75 \ --port port_num \ --max-model-len 8192 \ --max-num-batched-tokens 16384 \ --max-num-seq...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

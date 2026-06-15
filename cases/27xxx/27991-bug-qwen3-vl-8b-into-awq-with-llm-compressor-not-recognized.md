# vllm-project/vllm#27991: [Bug]: Qwen3-VL-8B into AWQ with llm-compressor not recognized.

| 字段 | 值 |
| --- | --- |
| Issue | [#27991](https://github.com/vllm-project/vllm/issues/27991) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-8B into AWQ with llm-compressor not recognized.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using VLLM version v0.11.0 with the following config (on a A10 GPU): ``` vllm serve mymodel --enable-prefix-caching --max-model-len 32768 api-server-count=4 --trust-remote-code '--mm-processor-cache-gb 0 --max-num-batched-tokens 8192 --max-num-seqs 4 ``` I was using https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct-AWQ which was working like a charm. In VLLM logs, I was able to read : [1;36m(EngineCore_DP0 pid=117)[0;0m INFO 11-03 05:09:44 [gpu_model_runner.py:2653] Model loading took 6.5936 GiB and 19.377722 seconds [1;36m(EngineCore_DP0 pid=117)[0;0m INFO 11-03 05:09:45 [gpu_model_runner.py:3344] Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size. [1;36m(EngineCore_DP0 pid=117)[0;0m INFO 11-03 05:09:54 [backends.py:548] Using cache directory: /root/.cache/vllm/torch_compile_cache/314439bf50/rank_0_0/backbone for vLLM's torch.compile [1;36m(EngineCore_DP0 pid=117)[0;0m INFO 11-03 05:09:54 [backends.py:559] Dynamo bytecode transform time: 4.51 s [1;36m(EngineCore_DP0 pid=117)[0;0m INFO 11-03 05:09:57 [backends.py:197] Cache the graph for dyn...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ### Your current environment ### 🐛 Describe the bug I am using VLLM version v0.11.0 with the following config (on a A10 GPU): ``` vllm serve mymodel --enable-prefix-caching --max-model-len 32768 api-server-count=4 --tru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen3-VL-8B into AWQ with llm-compressor not recognized. bug;stale ### Your current environment ### 🐛 Describe the bug I am using VLLM version v0.11.0 with the following config (on a A10 GPU): ``` vllm serve mymo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: g to convert into AWQ Qwen/Qwen3-VL-8B-Instruct but it seems that the my quantized model is not recognized as an AWQ one (in VLLM logs, no mention about awq or awq_marlin kernel). Moreover, I have a concurency of only 1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: feature size. [1;36m(EngineCore_DP0 pid=117)[0;0m INFO 11-03 05:09:54 [backends.py:548] Using cache directory: /root/.cache/vllm/torch_compile_cache/314439bf50/rank_0_0/backbone for vLLM's torch.compile [1;36m(Engine...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Qwen3-VL-8B into AWQ with llm-compressor not recognized. bug;stale ### Your current environment ### 🐛 Describe the bug I am using VLLM version v0.11.0 with the following config (on a A10 GPU): ``` vllm serve mymo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

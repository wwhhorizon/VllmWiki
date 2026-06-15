# vllm-project/vllm#2348: OOM with meta-llama/Llama-2-70b-chat-hf

| 字段 | 值 |
| --- | --- |
| Issue | [#2348](https://github.com/vllm-project/vllm/issues/2348) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling |
| 症状 | build_error;mismatch;oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> OOM with meta-llama/Llama-2-70b-chat-hf

### Issue 正文摘录

I have 8 Tesla V100 32 GB GPUS, and set tensor_parallel_size tp 8, which should be enough to run meta-llama/Llama-2-70b-chat-hf but I am getting an ``` RuntimeError: CUDA error: out of memory CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` This is my setup, I can't use quantization since my GPUs are version 7 ``` llm = VLLM( model='meta-llama/Llama-2-70b-chat-hf, trust_remote_code=True, max_new_tokens=512, top_k=10, top_p=0.95, temperature=0, dtype="float16", tensor_parallel_size=8, gpu_memory_utilization=1, disable_log_stats=True, enforce_eager=True, max_model_len=1024 ) ```

## 现有链接修复摘要

#40110 [Attention] Add flash-attn-4 CuTe DSL backend for SM120

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ght be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` This is my setup, I can't use quantization since my GPUs are version 7 ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: to enable device-side assertions. ``` This is my setup, I can't use quantization since my GPUs are version 7 ``` llm = VLLM( model='meta-llama/Llama-2-70b-chat-hf, trust_remote_code=True, max_new_tokens=512, top_k=10, t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: OOM with meta-llama/Llama-2-70b-chat-hf stale I have 8 Tesla V100 32 GB GPUS, and set tensor_parallel_size tp 8, which should be enough to run meta-llama/Llama-2-70b-chat-hf but I am getting an ``` RuntimeError: CUDA er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: run meta-llama/Llama-2-70b-chat-hf but I am getting an ``` RuntimeError: CUDA error: out of memory CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld_error;mismatch;oom dtype #40110 [Attention] Add flash-attn-4 CuTe DSL backend for SM120 I have 8 Tesla V100 32 GB GPUS, and set tensor_parallel_size tp 8, which should be enough to run meta-llama/Llama-2-70b-chat-hf...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40110](https://github.com/vllm-project/vllm/pull/40110) | mentioned | 0.6 | [Attention] Add flash-attn-4 CuTe DSL backend for SM120 | (pre-validated SM120 bundle of the five open upstream FA4 PRs: #2336, #2348, #2349, #2389, #2439), falls back to local `flash_attn.cute.interface` when `kernels` isn't installed o… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

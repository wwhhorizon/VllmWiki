# vllm-project/vllm#23921: [Bug]: 5090 Qwen3-30B-A3B-FP8 fails when TP=2！

| 字段 | 值 |
| --- | --- |
| Issue | [#23921](https://github.com/vllm-project/vllm/issues/23921) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 5090 Qwen3-30B-A3B-FP8 fails when TP=2！

### Issue 正文摘录

### Your current environment I'm currently running the Qwen3-30B-A3B-FP8 model on a 5090 machine with 32GB of video memory. When TP=1, I can run it with CPU offload enabled, but when TP=2, it fails, as follows: ``` NCCL_P2P_LEVEL=SYS \ CUDA_VISIBLE_DEVICES=0,1 \ VLLM_USE_V1=1 \ VLLM_USE_MODELSCOPE=true \ vllm serve /work/Qwen/Qwen3-30B-A3B-FP8 \ --served-model-name Qwen3-30B-A3B-FP8 \ --max-model-len 32000 \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 2 \ --trust-remote-code \ --port 8000 ``` result: ``` NCCL_P2P_LEVEL=SYS \ CUDA_VISIBLE_DEVICES=0,1 \ VLLM_USE_V1=1 \ VLLM_USE_MODELSCOPE=true \ vllm serve /work/Qwen/Qwen3-30B-A3B-FP8 \ --served-model-name Qwen3-30B-A3B-FP8 \ --max-model-len 32000 \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 2 \ --trust-remote-code \ --port 8000 INFO 08-29 02:02:10 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=28) INFO 08-29 02:02:14 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=28) INFO 08-29 02:02:14 [utils.py:326] non-default args: {'model_tag': '/work/Qwen/Qwen3-30B-A3B-FP8', 'model': '/work/Qwen/Qwen3-30B-A3B-FP8', 'trust_remote_code': True, 'max_model_len': 32000, 'served_mod...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: IServer pid=28) INFO 08-29 02:02:14 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=28) INFO 08-29 02:02:14 [utils.py:326] non-default args: {'model_tag': '/work/Qwen/Qwen3-30B-A3B-FP8', 'model': '/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 8: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: 5090 Qwen3-30B-A3B-FP8 fails when TP=2！ bug;stale ### Your current environment I'm currently running the Qwen3-30B-A3B-FP8 model on a 5090 machine with 32GB of video memory. When TP=1, I can run it with CPU offlo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: 5090 Qwen3-30B-A3B-FP8 fails when TP=2！ bug;stale ### Your current environment I'm currently running the Qwen3-30B-A3B-FP8 model on a 5090 machine with 32GB of video memory. When TP=1, I can run it with CPU offlo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: 5090 Qwen3-30B-A3B-FP8 fails when TP=2！ bug;stale ### Your current environment I'm currently running the Qwen3-30B-A3B-FP8 model on a 5090 machine with 32GB of video memory. When TP=1, I can run it with CPU offlo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23922: Should have ROCm label: NO (0 matches) #23921: Should have ROCm label: NO (0 matches) #23916: Should have ROCm label: YES (8 matches) • ROCm System M |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

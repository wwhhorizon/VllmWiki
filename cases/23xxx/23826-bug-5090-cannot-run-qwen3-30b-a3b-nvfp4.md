# vllm-project/vllm#23826: [Bug]: 5090 cannot run Qwen3-30B-A3B-NVFP4!

| 字段 | 值 |
| --- | --- |
| Issue | [#23826](https://github.com/vllm-project/vllm/issues/23826) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 5090 cannot run Qwen3-30B-A3B-NVFP4!

### Issue 正文摘录

### Your current environment ``` # serve CUDA_VISIBLE_DEVICES=0 \ VLLM_USE_MODELSCOPE=true \ vllm serve /work/nm-testing/Qwen3-30B-A3B-NVFP4 \ --served-model-name Qwen3-30B-A3B-NVFP4 \ --gpu-memory-utilization 0.8 \ --tensor-parallel-size 1 \ --trust-remote-code \ --port 8000 ``` result: ``` CUDA_VISIBLE_DEVICES=0 \ VLLM_USE_MODELSCOPE=true \ vllm serve /work/nm-testing/Qwen3-30B-A3B-NVFP4 \ --served-model-name Qwen3-30B-A3B-NVFP4 \ --gpu-memory-utilization 0.8 \ --tensor-parallel-size 1 \ --trust-remote-code \ --port 8000 INFO 08-28 04:23:57 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=302) INFO 08-28 04:24:00 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=302) INFO 08-28 04:24:00 [utils.py:326] non-default args: {'model_tag': '/work/nm-testing/Qwen3-30B-A3B-NVFP4', 'model': '/work/nm-testing/Qwen3-30B-A3B-NVFP4', 'trust_remote_code': True, 'served_model_name': ['Qwen3-30B-A3B-NVFP4'], 'gpu_memory_utilization': 0.8} (APIServer pid=302) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=302) INFO 08-28 04:24:07 [__init__.py:711] Resolved architecture: Qwen3MoeForCaus...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: Server pid=302) INFO 08-28 04:24:00 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=302) INFO 08-28 04:24:00 [utils.py:326] non-default args: {'model_tag': '/work/nm-testing/Qwen3-30B-A3B-NVFP4', 'm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 8: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: 5090 cannot run Qwen3-30B-A3B-NVFP4! bug;unstale ### Your current environment ``` # serve CUDA_VISIBLE_DEVICES=0 \ VLLM_USE_MODELSCOPE=true \ vllm serve /work/nm-testing/Qwen3-30B-A3B-NVFP4 \ --served-model-name...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: 5090 cannot run Qwen3-30B-A3B-NVFP4! bug;unstale ### Your current environment ``` # serve CUDA_VISIBLE_DEVICES=0 \ VLLM_USE_MODELSCOPE=true \ vllm serve /work/nm-testing/Qwen3-30B-A3B-NVFP4 \ --served-model-name...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: 5090 cannot run Qwen3-30B-A3B-NVFP4! bug;unstale ### Your current environment ``` # serve CUDA_VISIBLE_DEVICES=0 \ VLLM_USE_MODELSCOPE=true \ vllm serve /work/nm-testing/Qwen3-30B-A3B-NVFP4 \ --served-model-name...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23832: Should have ROCm label: NO (0 matches) #23826: Should have ROCm label: NO (0 matches) #23821: Should have ROCm label: NO (0 matches) #23820: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

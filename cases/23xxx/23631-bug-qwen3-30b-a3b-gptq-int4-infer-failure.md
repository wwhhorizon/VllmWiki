# vllm-project/vllm#23631: [Bug]: Qwen3-30B-A3B-GPTQ-Int4 infer failure！

| 字段 | 值 |
| --- | --- |
| Issue | [#23631](https://github.com/vllm-project/vllm/issues/23631) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-30B-A3B-GPTQ-Int4 infer failure！

### Issue 正文摘录

### Your current environment ``` VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=4 vllm serve /work/models/Qwen/Qwen3-30B-A3B-GPTQ-Int4 \ --host 0.0.0.0 \ --port 20001 \ --tensor-parallel-size 1 \ --seed 1024 \ --served-model-name Qwen3-30B-A3B-GPTQ-Int4 \ --max-model-len 10240 \ --trust-remote-code \ --gpu-memory-utilization 0.8 ``` err info： ``` INFO 08-26 01:09:25 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=15) INFO 08-26 01:09:30 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=15) INFO 08-26 01:09:30 [utils.py:326] non-default args: {'model_tag': '/work/models/Qwen/Qwen3-30B-A3B-GPTQ-Int4', 'host': '0.0.0.0', 'port': 20001, 'model': '/work/models/Qwen/Qwen3-30B-A3B-GPTQ-Int4', 'trust_remote_code': True, 'seed': 1024, 'max_model_len': 10240, 'served_model_name': ['Qwen3-30B-A3B-GPTQ-Int4'], 'gpu_memory_utilization': 0.8} (APIServer pid=15) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=15) INFO 08-26 01:09:36 [__init__.py:711] Resolved architecture: Qwen3MoeForCausalLM (APIServer pid=15) INFO 08-26 01:09:36 [__init__.py:1750] Using max model len 10240 (APIServer pid=15) IN...

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: IServer pid=15) INFO 08-26 01:09:30 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=15) INFO 08-26 01:09:30 [utils.py:326] non-default args: {'model_tag': '/work/models/Qwen/Qwen3-30B-A3B-GPTQ-Int4'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen3-30B-A3B-GPTQ-Int4 infer failure！ bug ### Your current environment ``` VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=4 vllm serve /work/models/Qwen/Qwen3-30B-A3B-GPTQ-Int4 \ --host 0.0.0.0 \ --port 20001 \ --tenso
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ntime. Using gptq_marlin kernel. (APIServer pid=15) INFO 08-26 01:09:36 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 08-26 01:09:40 [__init__.py:241] Automatically detected platfo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Qwen3-30B-A3B-GPTQ-Int4 infer failure！ bug ### Your current environment ``` VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=4 vllm serve /work/models/Qwen/Qwen3-30B-A3B-GPTQ-Int4 \ --host 0.0.0.0 \ --port 20001 \ --tensor-par...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | ure]: AttributeError: Model GptOssForCausalLM does not ... [bug] 6. #23631: [Bug]: Qwen3-30B-A3B-GPTQ-Int4 infer failure！... [bug] 7. #23627: [Usage]: How to start deepseek with p… |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23632: Should have ROCm label: NO (0 matches) #23631: Should have ROCm label: NO (0 matches) #23627: Should have ROCm label: NO (0 matches) #23626: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

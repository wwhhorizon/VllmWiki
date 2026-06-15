# vllm-project/vllm#23714: [Bug]: vllm fails to run internvl hf format multimodal model but works with the default vllm one

| 字段 | 值 |
| --- | --- |
| Issue | [#23714](https://github.com/vllm-project/vllm/issues/23714) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 63; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm fails to run internvl hf format multimodal model but works with the default vllm one

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve works for `OpenGVLab/InternVL3-8B` but fails for `OpenGVLab/InternVL3-8B-hf` works - `vllm serve OpenGVLab/InternVL3-8B --tensor-parallel-size 4 --trust-remote-code` fails for - `vllm serve OpenGVLab/InternVL3-8B-hf --tensor-parallel-size 4 --trust-remote-code` trace - ``` INFO 08-27 05:51:43 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1518045) INFO 08-27 05:51:46 [api_server.py:1875] vLLM API server version 0.10.1rc2.dev267+g714872f1a (APIServer pid=1518045) INFO 08-27 05:51:46 [utils.py:326] non-default args: {'model_tag': 'OpenGVLab/InternVL3-8B-hf', 'model': 'OpenGVLab/InternVL3-8B-hf', 'trust_remote_code': True, 'tensor_parallel_size': 4} (APIServer pid=1518045) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=1518045) INFO 08-27 05:51:54 [__init__.py:742] Resolved architecture: TransformersForMultimodalLM (APIServer pid=1518045) INFO 08-27 05:51:54 [__init__.py:1786] Using max model len 65536 (APIServer pid=1518045) INFO 08-27 05:51:55 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048. (AP...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: vllm fails to run internvl hf format multimodal model but works with the default vllm one bug ### Your current environment ### 🐛 Describe the bug vllm serve works for `OpenGVLab/InternVL3-8B` but fails for `OpenG...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: er pid=1518045) INFO 08-27 05:51:46 [api_server.py:1875] vLLM API server version 0.10.1rc2.dev267+g714872f1a (APIServer pid=1518045) INFO 08-27 05:51:46 [utils.py:326] non-default args: {'model_tag': 'OpenGVLab/InternVL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ] Using max model len 65536 (APIServer pid=1518045) INFO 08-27 05:51:55 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=1518045) WARNING 08-27 05:51:56 [utils.py:196] Trans...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rride_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=65536, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23719: Should have ROCm label: NO (0 matches) #23714: Should have ROCm label: NO (0 matches) #23710: Should have ROCm label: NO (0 matches) #23707: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

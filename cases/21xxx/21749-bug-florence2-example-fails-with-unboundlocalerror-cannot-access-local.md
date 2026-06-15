# vllm-project/vllm#21749: [Bug]: Florence2 example fails with UnboundLocalError: cannot access local variable 'key_cache'

| 字段 | 值 |
| --- | --- |
| Issue | [#21749](https://github.com/vllm-project/vllm/issues/21749) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Florence2 example fails with UnboundLocalError: cannot access local variable 'key_cache'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I installed vLLM v0.10.0 on a HPC cluster with access to an A100 GPU. I want to experiment with Florence-2 and other multimodal LLMs. Install was simply `pip install vllm` I tried running the Florence2 example which is part of the [Encode Decode Multimodal](https://docs.vllm.ai/en/stable/examples/offline_inference/encoder_decoder_multimodal.html) example script. ``` wget https://raw.githubusercontent.com/vllm-project/vllm/refs/heads/main/examples/offline_inference/encoder_decoder_multimodal.py python encoder_decoder_multimodal.py -m florence2 ``` vLLM crashes during CUDA graph capture. The error is: UnboundLocalError: cannot access local variable 'key_cache' where it is not associated with a value Here is the full output: ``` INFO 07-28 14:14:45 [__init__.py:235] Automatically detected platform cuda. INFO 07-28 14:14:56 [config.py:1604] Using max model len 4096 WARNING 07-28 14:14:56 [arg_utils.py:1690] ['Florence2ForConditionalGeneration', 'TransformersForMultimodalLM'] is not supported by the V1 Engine. Falling back to V0. INFO 07-28 14:14:56 [llm_engine.py:228] Initializing a V0 LLM engine (v0.10.0) with config: model='microso...

## 现有链接修复摘要

#14570 [Attention] Flash Attention 3 - fp8

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: he' bug;stale ### Your current environment ### 🐛 Describe the bug I installed vLLM v0.10.0 on a HPC cluster with access to an A100 GPU. I want to experiment with Florence-2 and other multimodal LLMs. Install was simply...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: rride_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: th access to an A100 GPU. I want to experiment with Florence-2 and other multimodal LLMs. Install was simply `pip install vllm` I tried running the Florence2 example which is part of the [Encode Decode Multimodal](https...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ils with UnboundLocalError: cannot access local variable 'key_cache' bug;stale ### Your current environment ### 🐛 Describe the bug I installed vLLM v0.10.0 on a HPC cluster with access to an A100 GPU. I want to experime...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14570](https://github.com/vllm-project/vllm/pull/14570) | mentioned | 0.45 | [Attention] Flash Attention 3 - fp8 | commits and one that seems suspicious is a597a57, which is part of pr #14570 (merged before v0.8.2) - it adds the line (currently 904) where the crash happens and also initializes… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

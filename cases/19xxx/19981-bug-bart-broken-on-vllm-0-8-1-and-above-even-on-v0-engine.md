# vllm-project/vllm#19981: [Bug]: BART broken on vLLM 0.8.1 and above. (Even on v0 engine).

| 字段 | 值 |
| --- | --- |
| Issue | [#19981](https://github.com/vllm-project/vllm/issues/19981) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: BART broken on vLLM 0.8.1 and above. (Even on v0 engine).

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Support for BART model appears to be broken since vLLM 0.8.1 on the v0 engine(It is not yet supported on the v1 engine nor do I think there is a plan to do so). The last known version on which the model works appears to be 0.8.0. ``` INFO 06-23 07:50:04 [__init__.py:244] Automatically detected platform cuda. INFO 06-23 07:50:09 [api_server.py:1287] vLLM API server version 0.9.1 INFO 06-23 07:50:09 [cli_args.py:309] non-default args: {'port': 9000, 'model': 'facebook/bart-large-cnn'} INFO 06-23 07:50:15 [config.py:823] This model supports multiple tasks: {'score', 'reward', 'embed', 'classify', 'generate'}. Defaulting to 'generate'. INFO 06-23 07:50:15 [config.py:3268] Downcasting torch.float32 to torch.bfloat16. WARNING 06-23 07:50:15 [arg_utils.py:1642] ['BartForConditionalGeneration'] is not supported by the V1 Engine. Falling back to V0. INFO 06-23 07:50:15 [api_server.py:265] Started engine process with PID 253868 WARNING 06-23 07:50:17 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234 INFO 06-23 07:50:1...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: the v1 engine nor do I think there is a plan to do so). The last known version on which the model works appears to be 0.8.0. ``` INFO 06-23 07:50:04 [__init__.py:244] Automatically detected platform cuda. INFO 06-23 07:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ng to 'generate'. INFO 06-23 07:50:15 [config.py:3268] Downcasting torch.float32 to torch.bfloat16. WARNING 06-23 07:50:15 [arg_utils.py:1642] ['BartForConditionalGeneration'] is not supported by the V1 Engine. Falling...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: `` INFO 06-23 07:50:04 [__init__.py:244] Automatically detected platform cuda. INFO 06-23 07:50:09 [api_server.py:1287] vLLM API server version 0.9.1 INFO 06-23 07:50:09 [cli_args.py:309] non-default args: {'port': 9000...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ## Your current environment ### 🐛 Describe the bug Support for BART model appears to be broken since vLLM 0.8.1 on the v0 engine(It is not yet supported on the v1 engine nor do I think there is a plan to do so). The las...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#19098: [Bug]: Unable to Run W4A16 GPTQ Quantized Models

| 字段 | 值 |
| --- | --- |
| Issue | [#19098](https://github.com/vllm-project/vllm/issues/19098) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to Run W4A16 GPTQ Quantized Models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I've been attempting to run vLLM with a GPTQ quantized model on an RTX5090 Laptop GPU and have been running into the following stacktrace. I believe that it is the quantization causing the issue as I've tried multiple other GPTQ quantized models and faced the same issue while unquantized models load properly. If anyone else has faced this issue and has any suggestions any help would be greatly appreciated. Command used: `vllm serve ISTA-DASLab/Mistral-Small-3.1-24B-Instruct-2503-GPTQ-4b-128g --max-model-len 8192 --max-seq-len 8192` Stacktrace: ``` DEBUG 06-03 13:24:40 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 06-03 13:24:40 [__init__.py:34] Checking if TPU platform is available. DEBUG 06-03 13:24:40 [__init__.py:44] TPU platform is not available because: No module named 'libtpu' DEBUG 06-03 13:24:40 [__init__.py:51] Checking if CUDA platform is available. DEBUG 06-03 13:24:40 [__init__.py:71] Confirmed CUDA platform is available. DEBUG 06-03 13:24:40 [__init__.py:99] Checking if ROCm platform is available. DEBUG 06-03 13:24:40 [__init__.py:113] ROCm platform is not available because: No module named...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: faced this issue and has any suggestions any help would be greatly appreciated. Command used: `vllm serve ISTA-DASLab/Mistral-Small-3.1-24B-Instruct-2503-GPTQ-4b-128g --max-model-len 8192 --max-seq-len 8192` Stacktrace:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: bug I've been attempting to run vLLM with a GPTQ quantized model on an RTX5090 Laptop GPU and have been running into the following stacktrace. I believe that it is the quantization causing the issue as I've tried multip...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Unable to Run W4A16 GPTQ Quantized Models bug ### Your current environment ### 🐛 Describe the bug I've been attempting to run vLLM with a GPTQ quantized model on an RTX5090 Laptop GPU and have been running into t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Unable to Run W4A16 GPTQ Quantized Models bug ### Your current environment ### 🐛 Describe the bug I've been attempting to run vLLM with a GPTQ quantized model on an RTX5090 Laptop GPU and have been running into t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

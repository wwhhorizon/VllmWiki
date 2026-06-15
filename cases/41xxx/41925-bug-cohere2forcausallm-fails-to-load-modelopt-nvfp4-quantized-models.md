# vllm-project/vllm#41925: [Bug] Cohere2ForCausalLM fails to load ModelOpt NVFP4 quantized models

| 字段 | 值 |
| --- | --- |
| Issue | [#41925](https://github.com/vllm-project/vllm/issues/41925) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | gemm_linear;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;gemm;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Cohere2ForCausalLM fails to load ModelOpt NVFP4 quantized models

### Issue 正文摘录

### Your current environment - vLLM version: 0.20.2rc1.dev53+g01b9b5af6 - Hardware: NVIDIA GB10 (DGX Spark, sm_121, 128GB unified memory) - PyTorch: 2.11.0+cu130 - Model: TheDrummer/Fallen-Command-A-111B-v1.1 quantized to NVFP4 with nvidia-modelopt 0.43.0 ### 🐛 Describe the bug Loading a Cohere2 model quantized with NVIDIA ModelOpt to NVFP4 format fails with KeyError because `commandr.py` weight loader doesn't recognize ModelOpt's `_double_scale` parameter naming. The same export format works correctly for Llama and Gemma architectures via ModelOpt → vLLM, but Cohere2 lacks the equivalent name mapping. ### Reproduction ```bash # Quantize Fallen-Command (Cohere2ForCausalLM, 111B) with ModelOpt python3 hf_ptq.py \ --pyt_ckpt_path Fallen-Command-A-111B-v1.1 \ --qformat nvfp4 \ --kv_cache_qformat fp8 \ --export_path Fallen-Command-NVFP4 \ --trust_remote_code \ --low_memory_mode \ --use_seq_device_map # Try to serve with vLLM vllm serve Fallen-Command-NVFP4 --quantization compressed-tensors --trust-remote-code ``` ### Error ``` File ".../vllm/model_executor/models/commandr.py", line 392, in load_weights param = params_dict[name] KeyError: 'layers.0.mlp.down_proj.weight_quantizer._doubl...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug] Cohere2ForCausalLM fails to load ModelOpt NVFP4 quantized models bug ### Your current environment - vLLM version: 0.20.2rc1.dev53+g01b9b5af6 - Hardware: NVIDIA GB10 (DGX Spark, sm_121, 128GB unified memory) - PyTo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug] Cohere2ForCausalLM fails to load ModelOpt NVFP4 quantized models bug ### Your current environment - vLLM version: 0.20.2rc1.dev53+g01b9b5af6 - Hardware: NVIDIA GB10 (DGX Spark, sm_121, 128GB unified memory) - PyTo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: _proj.weight_quantizer._double_scale' ``` vLLM correctly detects `Using FlashInferCutlassNvFp4LinearKernel for NVFP4 GEMM` but fails during weight loading for Cohere2 models. ### Expected behavior Cohere2ForCausalLM sho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: version: 0.20.2rc1.dev53+g01b9b5af6 - Hardware: NVIDIA GB10 (DGX Spark, sm_121, 128GB unified memory) - PyTorch: 2.11.0+cu130 - Model: TheDrummer/Fallen-Command-A-111B-v1.1 quantized to NVFP4 with nvidia-modelopt 0.43.0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ModelOpt NVFP4 quantized models bug ### Your current environment - vLLM version: 0.20.2rc1.dev53+g01b9b5af6 - Hardware: NVIDIA GB10 (DGX Spark, sm_121, 128GB unified memory) - PyTorch: 2.11.0+cu130 - Model: TheDrummer/F...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

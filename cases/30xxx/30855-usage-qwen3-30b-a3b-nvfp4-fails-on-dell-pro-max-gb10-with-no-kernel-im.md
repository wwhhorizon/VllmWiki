# vllm-project/vllm#30855: [Usage]: Qwen3-30B-A3B-NVFP4 fails on Dell Pro Max GB10 with "no kernel image is available for execution on the device"

| 字段 | 值 |
| --- | --- |
| Issue | [#30855](https://github.com/vllm-project/vllm/issues/30855) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;kernel;moe;operator;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Qwen3-30B-A3B-NVFP4 fails on Dell Pro Max GB10 with "no kernel image is available for execution on the device"

### Issue 正文摘录

### Your current environment ``` Hardware: Dell Pro Max GB10 OS: Ubuntu 24 CUDA: cuda_13.0.r13.0 Cuda compilation tools, release 13.0, V13.0.88; vllm: V0.12.0 torch_version: 2.9.0+cu128 model: RedHatAI/Qwen3-30B-A3B-NVFP4 or nvidia/Qwen3-30B-A3B-NVFP4 or nvidia/Qwen3-30B-A3B-FP4 ``` ### How would you like to use vllm ### I'm trying to run the quantized model RedHatAI/Qwen3-30B-A3B-NVFP4 using vLLM v0.12.0 on a Dell Pro Max GB10.However, I get the following error during model loading: torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device vllm serve RedHatAI/Qwen3-30B-A3B-NVFP4 --port 8002 --gpu-memory-utilization 0.7 (APIServer pid=731925) INFO 12-17 16:03:13 [api_server.py:1772] vLLM API server version 0.12.0 (APIServer pid=731925) INFO 12-17 16:03:13 [utils.py:253] non-default args: {'model_tag': 'RedHatAI/Qwen3-30B-A3B-NVFP4', 'port': 8002, 'model': 'RedHatAI/Qwen3-30B-A3B-NVFP4', 'gpu_memory_utilization': 0.7} (APIServer pid=731925) Downloading Model from https://www.modelscope.cn to directory: /home/smc01/.cache/modelscope/hub/models/RedHatAI/Qwen3-30B-A3B-NVFP4 (APIServer pid=731925) Downloading Model from https://www.modelscope.cn to di...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Usage]: Qwen3-30B-A3B-NVFP4 fails on Dell Pro Max GB10 with "no kernel image is available for execution on the device" usage;stale ### Your current environment ``` Hardware: Dell Pro Max GB10 OS: Ubuntu 24 CUDA: cuda_1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 13.0 Cuda compilation tools, release 13.0, V13.0.88; vllm: V0.12.0 torch_version: 2.9.0+cu128 model: RedHatAI/Qwen3-30B-A3B-NVFP4 or nvidia/Qwen3-30B-A3B-NVFP4 or nvidia/Qwen3-30B-A3B-FP4 ``` ### How would you like to u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Your current environment ``` Hardware: Dell Pro Max GB10 OS: Ubuntu 24 CUDA: cuda_13.0.r13.0 Cuda compilation tools, release 13.0, V13.0.88; vllm: V0.12.0 torch_version: 2.9.0+cu128 model: RedHatAI/Qwen3-30B-A3B-NVFP4 o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Qwen3-30B-A3B-NVFP4 fails on Dell Pro Max GB10 with "no kernel image is available for execution on the device" usage;stale ### Your current environment ``` Hardware: Dell Pro Max GB10 OS: Ubuntu 24 CUDA: cuda_1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

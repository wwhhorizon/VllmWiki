# vllm-project/vllm#33661: [Bug]: Hadamard Transform R4 weight length assertion

| 字段 | 值 |
| --- | --- |
| Issue | [#33661](https://github.com/vllm-project/vllm/issues/33661) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;gemm;kernel;operator;quantization |
| 症状 | build_error;crash;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hadamard Transform R4 weight length assertion

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I tried to run inference on a W4A4-NVFP4 model using vLLM by applying Hadamard transforms at R1, R2, and R4 with llmcompressor on the Qwen3-1.7B model. However, I encountered the error shown below, and it seems that the online rotation (R4) configuration is not being applied properly. Do you have any suggestions on how to resolve this issue? My current environment is DGX Spark, and I am using the NVIDIA-vLLM-26.01 container. Also, I am attaching and uploading the checkpoint’s config.json file. [Error Log] /usr/local/lib/python3.12/dist-packages/torchvision/io/image.py:14: UserWarning: Failed to load image Python extension: 'Could not load this library: /usr/local/lib/python3.12/dist-packages/torchvision/image.so'If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning. Otherwise, there might be something wrong with your environment. Did you have `libjpeg` or `libpng` installed before building `torchvision` from source? warn( Saving outputs to ./generations/Qwen3-1.7B-NVFP4-R124-dim16/normal/32768/aime2025 README.md: 100%|██████████████████████████████████████████████████████████████...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: nt ### 🐛 Describe the bug Hello, I tried to run inference on a W4A4-NVFP4 model using vLLM by applying Hadamard transforms at R1, R2, and R4 with llmcompressor on the Qwen3-1.7B model. However, I encountered the error s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: sr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:926 dispatch key: ADInplaceOrView previous kernel: no debug info new kernel: registered at /usr/local/lib/python3.12/dist-packages/torch/_library/custom...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: omething wrong with your environment. Did you have `libjpeg` or `libpng` installed before building `torchvision` from source? warn( Saving outputs to ./generations/Qwen3-1.7B-NVFP4-R124-dim16/normal/32768/aime2025 READM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ### 🐛 Describe the bug Hello, I tried to run inference on a W4A4-NVFP4 model using vLLM by applying Hadamard transforms at R1, R2, and R4 with llmcompressor on the Qwen3-1.7B model. However, I encountered the error show...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Hadamard Transform R4 weight length assertion bug;stale ### Your current environment ### 🐛 Describe the bug Hello, I tried to run inference on a W4A4-NVFP4 model using vLLM by applying Hadamard transforms at R1,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

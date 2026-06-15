# vllm-project/vllm#29368: [Bug]:llama4 AttributeError: 'dict' object has no attribute 'model_type'

| 字段 | 值 |
| --- | --- |
| Issue | [#29368](https://github.com/vllm-project/vllm/issues/29368) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:llama4 AttributeError: 'dict' object has no attribute 'model_type'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug PS E:\Ollama-MMLU-Pro> docker run --rm -it --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -p 8000:8000 -e VLLM_USE_FLASHINFER_MOE_FP4=1 -e VLLM_USE_FLASHINFER_MOE_FP8=1 -e VLLM_FLASHINFER_MOE_BACKEND=latency -e VLLM_FLASHINFER_ALLREDUCE_FUSION_THRESHOLDS_MB='{"2":32,"4":32,"8":8}' -v E:/text-generation-webui-1.14/user_data/models:/model vllm-blackwell:latest python -m vllm.entrypoints.openai.api_server --model /model/Llama4-Scout17B-NVFP4 --trust-remote-code --host 0.0.0.0 --port 8000 --max-model-len 131072 --gpu-memory-utilization 0.95 --served-model-name Llama4-Scout17B-NVFP4 --chat-template /model/Llama4-Scout17B-NVFP4/chat_template.jinja --kv-cache-dtype fp8 --no-enable-prefix-caching true --async-scheduling --mm-encoder-tp-mode data --enable-auto-tool-choice --tool-call-parser llama4_pythonic --quantization modelopt_fp4 ============= == PyTorch == ============= NVIDIA Release 25.05 (build 170559088) PyTorch Version 2.8.0a0+5228986 Container image Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES. All rights reserved. Copyright (c) 2014-2024 Facebook Inc. Copyright (c) 2011-2014 Idiap Research Institute (...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: r current environment ### 🐛 Describe the bug PS E:\Ollama-MMLU-Pro> docker run --rm -it --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -p 8000:8000 -e VLLM_USE_FLASHINFER_MOE_FP4=1 -e VLLM_USE_FLASHIN...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: lock=-1 --ulimit stack=67108864 -p 8000:8000 -e VLLM_USE_FLASHINFER_MOE_FP4=1 -e VLLM_USE_FLASHINFER_MOE_FP8=1 -e VLLM_FLASHINFER_MOE_BACKEND=latency -e VLLM_FLASHINFER_ALLREDUCE_FUSION_THRESHOLDS_MB='{"2":32,"4":32,"8"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]:llama4 AttributeError: 'dict' object has no attribute 'model_type' bug;stale ### Your current environment ### 🐛 Describe the bug PS E:\Ollama-MMLU-Pro> docker run --rm -it --gpus all --ipc=host --ulimit memlock=-1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]:llama4 AttributeError: 'dict' object has no attribute 'model_type' bug;stale ### Your current environment ### 🐛 Describe the bug PS E:\Ollama-MMLU-Pro> docker run --rm -it --gpus all --ipc=host --ulimit memlock=-1 --u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: P4=1 -e VLLM_USE_FLASHINFER_MOE_FP8=1 -e VLLM_FLASHINFER_MOE_BACKEND=latency -e VLLM_FLASHINFER_ALLREDUCE_FUSION_THRESHOLDS_MB='{"2":32,"4":32,"8":8}' -v E:/text-generation-webui-1.14/user_data/models:/model vllm-blackw...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

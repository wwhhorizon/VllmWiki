# vllm-project/vllm#9363: [Bug]: Qwen2-VL-72B Inference on Multiple-GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#9363](https://github.com/vllm-project/vllm/issues/9363) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2-VL-72B Inference on Multiple-GPUs

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug running the Qwen2-VL-72B-INT4 GPTQ quantized model on multiple GPU. After running the model checkpoints are loading properly as shown below but after loading it is throwing an error because of memory issue. ![image](https://github.com/user-attachments/assets/9ad1a3c5-3fbc-4636-bd7a-e2d823a37d5b) The complete process logs are below: ========== == CUDA == ========== CUDA Version 12.1.1 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container image and its contents are governed by the NVIDIA Deep Learning Container License. By pulling and using the container, you accept the terms and conditions of this license: https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience. /opt/conda/lib/python3.10/site-packages/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION INFO 10-15 06:52:06 api_server.py:528] vLLM API server version dev I...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: complete process logs are below: ========== == CUDA == ========== CUDA Version 12.1.1 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container image and its contents...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: t Dumps _No response_ ### 🐛 Describe the bug running the Qwen2-VL-72B-INT4 GPTQ quantized model on multiple GPU. After running the model checkpoints are loading properly as shown below but after loading it is throwing a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loadin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2-VL-72B Inference on Multiple-GPUs bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug running the Qwen2-VL-72B-INT4 GPTQ quantized model on multiple GPU. After running

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#18302: [Bug]: AttributeError: 'MultiprocExecutor' object has no attribute 'io_thread_pool'

| 字段 | 值 |
| --- | --- |
| Issue | [#18302](https://github.com/vllm-project/vllm/issues/18302) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'MultiprocExecutor' object has no attribute 'io_thread_pool'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried many images from https://gallery.ecr.aws/q9t5s3a7/vllm-ci-postmerge-repo but got the same issue: ========== == CUDA == ========== CUDA Version 12.8.1 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container image and its contents are governed by the NVIDIA Deep Learning Container License. By pulling and using the container, you accept the terms and conditions of this license: https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience. INFO 05-17 01:57:15 [__init__.py:248] Automatically detected platform cuda. INFO 05-17 01:57:21 [__init__.py:30] Available plugins for group vllm.general_plugins: INFO 05-17 01:57:21 [__init__.py:32] name=lora_filesystem_resolver, value=vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 05-17 01:57:21 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded. INFO 05-17 01:57:21 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to lo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: the bug I tried many images from https://gallery.ecr.aws/q9t5s3a7/vllm-ci-postmerge-repo but got the same issue: ========== == CUDA == ========== CUDA Version 12.8.1 Container image Copyright (c) 2016-2023, NVIDIA CORPO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: p for distributed inference INFO 05-17 01:57:47 [config.py:2112] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 05-17 01:57:51 [__init__.py:248] Automatically detected platform cuda. INFO 05-17 01:57:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: v49+g3e0d43502 INFO 05-17 01:57:22 [cli_args.py:297] non-default args: {'model': '/models/deepseek-r1-distill-qwen-32b-awq', 'served_model_name': ['qwen2.5_32b_awq'], 'tensor_parallel_size': 2, 'gpu_memory_utilization':...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: /q9t5s3a7/vllm-ci-postmerge-repo but got the same issue: ========== == CUDA == ========== CUDA Version 12.8.1 Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

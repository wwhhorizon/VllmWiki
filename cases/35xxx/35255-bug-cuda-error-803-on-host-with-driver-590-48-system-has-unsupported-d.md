# vllm-project/vllm#35255: [Bug]: CUDA Error 803 on host with driver 590.48: `system has unsupported display driver / cuda driver combination

| 字段 | 值 |
| --- | --- |
| Issue | [#35255](https://github.com/vllm-project/vllm/issues/35255) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Error 803 on host with driver 590.48: `system has unsupported display driver / cuda driver combination

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description vLLM fails to initialize the CUDA engine when running on a host with NVIDIA Driver 590.48.01. The error RuntimeError: Unexpected error from cudaGetDeviceCount() ... Error 803 occurs. This is likely due to a conflict between the image's internal cuda-compat libraries and the high-version host driver. Environment - vLLM Version: 0.15.1 and 0.16.0rc2.dev (nightly) - Docker Image: docker.1ms.run/vllm/vllm-openai:v0.15.1-cu130 and vllm-openai:nightly - GPU: NVIDIA GeForce RTX 5060 Ti (16GB) - Host Driver Version: 590.48.01 - Host OS: Linux root@jxj:~/34-node-bak# docker run -d -p 8000:8000 -v /root/model-file/Qwen3-0.6B:/model --gpus all --name vllm --entrypoint /bin/bash vllm/vllm-openai:v0.15.1-cu130 -c "sleep infinity" 3217527acd26ea9ae3e35c82df07e73fc32d49dda09677c6cae221e3da5416bc root@jxj:~/34-node-bak# docker exec -it vllm bash root@3217527acd26:/vllm-workspace# vllm serve /model --max-model-len 512 (APIServer pid=53) INFO 02-24 18:59:19 [utils.py:325] (APIServer pid=53) INFO 02-24 18:59:19 [utils.py:325] █ █ █▄ ▄█ (APIServer pid=53) INFO 02-24 18:59:19 [utils.py:325] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.1 (APIServer pid=...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: conflict between the image's internal cuda-compat libraries and the high-version host driver. Environment - vLLM Version: 0.15.1 and 0.16.0rc2.dev (nightly) - Docker Image: docker.1ms.run/vllm/vllm-openai:v0.15.1-cu130...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: py:1561] Using max model len 512 (APIServer pid=53) INFO 02-24 18:59:23 [scheduler.py:226] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=53) INFO 02-24 18:59:23 [vllm.py:624] Asynchronous s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=512, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: CUDA Error 803 on host with driver 590.48: `system has unsupported display driver / cuda driver combination bug ### Your current environment ### 🐛 Describe the bug Description vLLM fails to initialize the CUDA e

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

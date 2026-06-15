# vllm-project/vllm#17527: [Bug]: Training with vllm not supports Qwen3

| 字段 | 值 |
| --- | --- |
| Issue | [#17527](https://github.com/vllm-project/vllm/issues/17527) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Training with vllm not supports Qwen3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If I use Qwen3 GRPO with vLLM for training, with a config like below: config.yaml: ``` use_vllm: true vllm_device: auto vllm_gpu_memory_utilization: 0.2 vllm_dtype: "bf16" ``` I encounter errors related to vLLM, even though vLLM works fine when used alone. Here is the error I encountered: --- ``` [INFO|configuration_utils.py:1142] 2025-04-29 17:04:33,305 >> Generate config GenerationConfig { "bos_token_id": 151643, "do_sample": true, "eos_token_id": [ 151645, 151643 ], "pad_token_id": 151643, "temperature": 0.6, "top_k": 20, "top_p": 0.95 } WARNING 04-29 17:04:33 [utils.py:2382] We must use the `spawn` multiprocessing start method. Overriding VLLM_WORKER_MULTIPROC_METHOD to 'spawn'. See https://docs.vllm.ai/en/latest/getting_started/troubleshooting.html#python-multiprocessing for more information. Reason: CUDA is initialized [2025-04-29 17:04:38,900] [INFO] [real_accelerator.py:222:get_accelerator] Setting ds_accelerator to cuda (auto detect) INFO 04-29 17:04:40 [importing.py:53] Triton module has been replaced with a placeholder. INFO 04-29 17:04:40 [__init__.py:239] Automatically detected platform cuda. INFO 04-29 17:04:45 [cor...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rator] Setting ds_accelerator to cuda (auto detect) INFO 04-29 17:04:40 [importing.py:53] Triton module has been replaced with a placeholder. INFO 04-29 17:04:40 [__init__.py:239] Automatically detected platform cuda. I...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ` use_vllm: true vllm_device: auto vllm_gpu_memory_utilization: 0.2 vllm_dtype: "bf16" ``` I encounter errors related to vLLM, even though vLLM works fine when used alone. Here is the error I encountered: --- ``` [INFO|...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: _accelerator to cuda (auto detect) INFO 04-29 17:04:40 [importing.py:53] Triton module has been replaced with a placeholder. INFO 04-29 17:04:40 [__init__.py:239] Automatically detected platform cuda. INFO 04-29 17:04:4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Training with vllm not supports Qwen3 bug;stale ### Your current environment ### 🐛 Describe the bug If I use Qwen3 GRPO with vLLM for training, with a config like below: config.yaml: ``` use_vllm: true vllm_devic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Training with vllm not supports Qwen3 bug;stale ### Your current environment ### 🐛 Describe the bug If I use Qwen3 GRPO with vLLM for training, with a config like below: config.yaml: ``` use_vllm: true vllm_devic...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | -3.10.6/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #4: <unknown function> + 0x63507f4 (0x7f0aba7237f4 in /data/miniconda3/envs/env-3.10.6/lib/python3.10/site-pa… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | -3.10.6/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #6: c10d::tcpstore::tcpstore(std::string, c10d::tcpstoreoptions const&) + 0x20c (0x7f0aba6e314c in /data/mini… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | -3.10.6/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #7: <unknown function> + 0xe402df (0x7f0aca2cf2df in /data/miniconda3/envs/env-3.10.6/lib/python3.10/site-pac… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | e #11: /data/miniconda3/envs/env-3.10.6/bin/python() [0x50c73f] frame #12: pyvectorcall_call + 0x92 (0x50d2c2 in /data/miniconda3/envs/env-3.10.6/bin/python) frame #13: /data/mini… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | 10.6/lib/python3.10/site-packages/torch/lib/libtorch_python.so) frame #16: _pyobject_maketpcall + 0x25b (0x4f95eb in /data/miniconda3/envs/env-3.10.6/bin/python) frame #17: _pyeva… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | 0x321 (0x4f0501 in /data/miniconda3/envs/env-3.10.6/bin/python) frame #20: /data/miniconda3/envs/env-3.10.6/bin/python() [0x576577] frame #21: /data/miniconda3/envs/env-3.10.6/bin… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | e #20: /data/miniconda3/envs/env-3.10.6/bin/python() [0x576577] frame #21: /data/miniconda3/envs/env-3.10.6/bin/python() [0x5003e4] frame #22: _pyeval_evalframedefault + 0x321 (0x… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | 0x6f (0x5001ff in /data/miniconda3/envs/env-3.10.6/bin/python) frame #27: pyobject_call + 0xb8 (0x50cf88 in /data/miniconda3/envs/env-3.10.6/bin/python) frame #28: _pyeval_evalfra… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | x2a52 (0x4f2c32 in /data/miniconda3/envs/env-3.10.6/bin/python) frame #29: _pyfunction_vectorcall + 0x6f (0x5001ff in /data/miniconda3/envs/env-3.10.6/bin/python) frame #30: _pyev… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | 0x6f (0x5001ff in /data/miniconda3/envs/env-3.10.6/bin/python) frame #32: _pyeval_evalframedefault + 0x321 (0x4f0501 in /data/miniconda3/envs/env-3.10.6/bin/python) frame #33: _py… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | 0x17d (0x4f89ed in /data/miniconda3/envs/env-3.10.6/bin/python) frame #53: /data/miniconda3/envs/env-3.10.6/bin/python() [0x509bc8] frame #54: /data/miniconda3/envs/env-3.10.6/bin… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#38228: [Bug]: Based on vllm 0.18.0 version, when the number of tensor parallelizations is greater than 1, an error message will be reported: [AMP ERROR] [CudaFrontend. cpp: 94] [failed to call cuCtxGetDevice (&device), error code: CUDA-ERROR-INVALIDFHIR TEXT

| 字段 | 值 |
| --- | --- |
| Issue | [#38228](https://github.com/vllm-project/vllm/issues/38228) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Based on vllm 0.18.0 version, when the number of tensor parallelizations is greater than 1, an error message will be reported: [AMP ERROR] [CudaFrontend. cpp: 94] [failed to call cuCtxGetDevice (&device), error code: CUDA-ERROR-INVALIDFHIR TEXT

### Issue 正文摘录

### Your current environment My ENV: +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 570.133.20 Driver Version: 570.133.20 CUDA Version: 12.8 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA H20-3e On | 00000000:08:00.0 Off | 0 | | N/A 37C P0 77W / 500W | 0MiB / 143771MiB | 0% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA H20-3e On | 00000001:7F:00.0 Off | 0 | | N/A 36C P0 79W / 500W | 0MiB / 143771MiB | 0% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ +-----------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |===========================================================...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Based on vllm 0.18.0 version, when the number of tensor parallelizations is greater than 1, an error message will be reported: [AMP ERROR] [CudaFrontend. cpp: 94] [failed to call cuCtxGetDevice (&device), error c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: l_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: tions is greater than 1, an error message will be reported: [AMP ERROR] [CudaFrontend. cpp: 94] [failed to call cuCtxGetDevice (&device), error code: CUDA-ERROR-INVALIDFHIR TEXT bug ### Your current environment My ENV:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: PIServer pid=3842) INFO 03-26 11:55:57 [config.py:212] Setting attention block size to 1056 tokens to ensure that attention page size is >= mamba page size. (APIServer pid=3842) INFO 03-26 11:55:57 [config.py:243] Paddi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0xdc253 (0x7feee96b0253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #5: <unknown… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | > + 0x94ac3 (0x7fef23a94ac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #6: <unknown function> + 0x1268d0 (0x7fef23b268d0 in /lib/x86_64-linux-gnu/libc.so.6) [rank1]:[w326 11:56:29.… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

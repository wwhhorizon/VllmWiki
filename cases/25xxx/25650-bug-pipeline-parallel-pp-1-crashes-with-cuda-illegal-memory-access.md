# vllm-project/vllm#25650: [Bug]: Pipeline parallel (pp>1) crashes with CUDA illegal memory access

| 字段 | 值 |
| --- | --- |
| Issue | [#25650](https://github.com/vllm-project/vllm/issues/25650) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Pipeline parallel (pp>1) crashes with CUDA illegal memory access

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the **throughput benchmark** of vLLM v1 engine with pipeline parallelism (`--pipeline-parallel-size > 1`), the run crashes with **CUDA illegal memory access**. ### Description When running vLLM v1 engine with pipeline parallelism (--pipeline-parallel-size > 1), the benchmark crashes with CUDA illegal memory access. ### Environment: * vLLM version: 0.10.2 (V1 engine) * GPUs: 4× L20 (48GB) * Model: * `codellama/CodeLlama-34b-hf` * Same issue also reproduced on `Qwen/Qwen2.5-32B-Instruct` → not model-specific. ### Command ``` vllm bench throughput \ --model codellama/CodeLlama-34b-hf \ --dataset ShareGPT_V3_unfiltered_cleaned_split.json \ -pp 4 \ --gpu-memory-utilization 0.8 ``` ### Notes * Reproduces consistently with different models (CodeLlama-34B, Qwen2.5-32B). * Issue is specific to **v1 engine + pipeline parallelism**. * Using the **same configuration with tensor parallelism (`tp > 1`, `pp = 1`) runs without issues**. * Likely related to PP communication. ### Error Log ``` ...... (Worker_PP1 pid=2729458) INFO 09-25 00:15:07 [default_loader.py:268] Loading weights took 4.05 seconds Loading safetensors checkpoint sh...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: g]: Pipeline parallel (pp>1) crashes with CUDA illegal memory access bug;stale ### Your current environment ### 🐛 Describe the bug When running the **throughput benchmark** of vLLM v1 engine with pipeline parallelism (`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: Environment: * vLLM version: 0.10.2 (V1 engine) * GPUs: 4× L20 (48GB) * Model: * `codellama/CodeLlama-34b-hf` * Same issue also reproduced on `Qwen/Qwen2.5-32B-Instruct` → not model-specific. ### Command ``` vllm bench...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: gnu/libc.so.6) terminate called after throwing an instance of 'c10::DistBackendError' what(): [PG ID 4 PG GUID 19 Rank 0] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: hmark crashes with CUDA illegal memory access. ### Environment: * vLLM version: 0.10.2 (V1 engine) * GPUs: 4× L20 (48GB) * Model: * `codellama/CodeLlama-34b-hf` * Same issue also reproduced on `Qwen/Qwen2.5-32B-Instruct...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=4, data_parallel_size...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | b/.venv/lib/python3.12/site-packages/torch/lib/libtorch_cpu.so) frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /.venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdc253 (0x7f2bdde43253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | xdc253 (0x7f2bdde43253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x7f2c57cc8ac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown funct… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

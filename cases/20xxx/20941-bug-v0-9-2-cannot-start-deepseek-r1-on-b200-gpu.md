# vllm-project/vllm#20941: [Bug]: v0.9.2 cannot start deepseek r1 on B200 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#20941](https://github.com/vllm-project/vllm/issues/20941) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: v0.9.2 cannot start deepseek r1 on B200 GPU

### Issue 正文摘录

### Your current environment Starting the model with: ``` vllm - serve - deepseek-ai/DeepSeek-R1-0528 - '--host' - 0.0.0.0 - '--port' - '8000' - '--max-model-len' - '16384' - '--served-model-name' - deepseekr1 - '--tensor-parallel-size' - '8' - '--max-num-seqs' - '2' - '--cpu-offload-gb' - '400' ``` fails: ``` (VllmWorker rank=7 pid=438) INFO 07-14 12:14:57 [gpu_model_runner.py:1770] Starting to load model deepseek-ai/DeepSeek-R1-0528... (VllmWorker rank=0 pid=431) INFO 07-14 12:14:57 [gpu_model_runner.py:1770] Starting to load model deepseek-ai/DeepSeek-R1-0528... (VllmWorker rank=5 pid=436) INFO 07-14 12:14:58 [gpu_model_runner.py:1775] Loading model from scratch... (VllmWorker rank=5 pid=436) INFO 07-14 12:14:58 [cuda.py:208] Using Triton MLA backend on V1 engine. (VllmWorker rank=4 pid=435) INFO 07-14 12:14:58 [gpu_model_runner.py:1775] Loading model from scratch... (VllmWorker rank=6 pid=437) INFO 07-14 12:14:58 [gpu_model_runner.py:1775] Loading model from scratch... (VllmWorker rank=7 pid=438) INFO 07-14 12:14:58 [gpu_model_runner.py:1775] Loading model from scratch... (VllmWorker rank=3 pid=434) INFO 07-14 12:14:58 [gpu_model_runner.py:1775] Loading model from scratch... (...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: h... (VllmWorker rank=5 pid=436) INFO 07-14 12:14:58 [cuda.py:208] Using Triton MLA backend on V1 engine. (VllmWorker rank=4 pid=435) INFO 07-14 12:14:58 [gpu_model_runner.py:1775] Loading model from scratch... (VllmWor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: A backend on V1 engine. (VllmWorker rank=5 pid=436) INFO 07-14 12:14:58 [fp8.py:483] Using CutlassBlockScaledGroupedGemm kernels for Fp8MoEMethod. (VllmWorker rank=3 pid=434) INFO 07-14 12:14:58 [cuda.py:208] Using Trit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: v0.9.2 cannot start deepseek r1 on B200 GPU bug;stale ### Your current environment Starting the model with: ``` vllm - serve - deepseek-ai/DeepSeek-R1-0528 - '--host' - 0.0.0.0 - '--port' - '8000' -
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: seek r1 on B200 GPU bug;stale ### Your current environment Starting the model with: ``` vllm - serve - deepseek-ai/DeepSeek-R1-0528 - '--host' - 0.0.0.0 - '--port' - '8000' - '--max-model-len' - '16384' - '--served-model

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | r/local/lib/python3.12/dist-packages/torch/lib/libtorch_cpu.so) frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdc253 (0x7443ac3b3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unkn… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 53 (0x7443ac3b3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x74442d1d0ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #8: clone + 0x… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

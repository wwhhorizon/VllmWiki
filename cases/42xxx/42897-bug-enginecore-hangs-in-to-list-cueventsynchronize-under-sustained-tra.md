# vllm-project/vllm#42897: [Bug]: EngineCore hangs in `_to_list` -> `cuEventSynchronize` under sustained traffic (Qwen3.6-35B-A3B-NVFP4 hybrid MoE, RTX 5090 sm_120; v0.21.0 + nightly dev39/dev42)

| 字段 | 值 |
| --- | --- |
| Issue | [#42897](https://github.com/vllm-project/vllm/issues/42897) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: EngineCore hangs in `_to_list` -> `cuEventSynchronize` under sustained traffic (Qwen3.6-35B-A3B-NVFP4 hybrid MoE, RTX 5090 sm_120; v0.21.0 + nightly dev39/dev42)

### Issue 正文摘录

## Symptom After some hours of sustained chat-completion traffic, the engine stops producing tokens. The HTTP layer continues returning `200 OK` on `/health` and on `POST /v1/chat/completions`, so the API server remains alive and keeps queueing new requests. Inside the engine, however: - No tokens are emitted for any in-flight or new request. - The periodic stats line (`Avg prompt throughput: ... tokens/s`) that vLLM normally logs every ~10 s stops appearing in the journal. - The last stats line before the silence consistently shows `Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s` with `Running: N reqs` for some N>0 — i.e. the engine reported zero throughput while still having sequences in flight, then stopped logging entirely. - No exception, traceback, or other error appears anywhere in the log after the last successful step — the log just goes silent. The engine never recovers; only a restart clears the state. ## Where it is stuck `py-spy dump --pid --native` consistently shows the engine `MainThread` blocked inside the CUDA driver in `cuEventSynchronize`: ``` Thread (active): "MainThread" cuEventSynchronize (libcuda.so.595.45.04) ← blocked cudaEve...

## 现有链接修复摘要

#22760 [Disagg][Perf] Use CUDA event sync instead of blocking `tolist` to avoid unintentional copy ops blocking across different CUDA strea…

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: r some hours of sustained chat-completion traffic, the engine stops producing tokens. The HTTP layer continues returning `200 OK` on `/health` and on `POST /v1/chat/completions`, so the API server remains alive and keep...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: o_list` -> `cuEventSynchronize` under sustained traffic (Qwen3.6-35B-A3B-NVFP4 hybrid MoE, RTX 5090 sm_120; v0.21.0 + nightly dev39/dev42) ## Symptom After some hours of sustained chat-completion traffic, the engine sto...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: tSynchronize` under sustained traffic (Qwen3.6-35B-A3B-NVFP4 hybrid MoE, RTX 5090 sm_120; v0.21.0 + nightly dev39/dev42) ## Symptom After some hours of sustained chat-completion traffic, the engine stops producing token...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ore hangs in `_to_list` -> `cuEventSynchronize` under sustained traffic (Qwen3.6-35B-A3B-NVFP4 hybrid MoE, RTX 5090 sm_120; v0.21.0 + nightly dev39/dev42) ## Symptom After some hours of sustained chat-completion traffic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: n `POST /v1/chat/completions`, so the API server remains alive and keeps queueing new requests. Inside the engine, however: - No tokens are emitted for any in-flight or new request. - The periodic stats line (`Avg promp...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#22760](https://github.com/vllm-project/vllm/pull/22760) | mentioned | 0.45 | [Disagg][Perf] Use CUDA event sync instead of blocking `tolist` to avoid unintentional copy ops blocking across different CUDA streams, improving disagg TTIT/TTFT | the function itself is already a workaround introduced by #22754 / pr #22760 to avoid blocking other cuda streams during the gpu→cpu copy of sampled token ids. the hang is steady-… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

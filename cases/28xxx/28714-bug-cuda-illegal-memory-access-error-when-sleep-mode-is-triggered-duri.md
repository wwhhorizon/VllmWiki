# vllm-project/vllm#28714: [Bug]: CUDA Illegal Memory Access Error When Sleep Mode is Triggered During Request Processing

| 字段 | 值 |
| --- | --- |
| Issue | [#28714](https://github.com/vllm-project/vllm/issues/28714) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Illegal Memory Access Error When Sleep Mode is Triggered During Request Processing

### Issue 正文摘录

## Describe the bug When the model instance is processing requests and `sleep_mode` is triggered, a `CUDA error: an illegal memory access was encountered` error occurs. The cause may be that vLLM releases the GPU memory used by the model, but the scheduler is not aware of this event and continues to schedule and process requests. ## Error Logs ``` (EngineCore_DP0 pid=1778746) INFO 11-14 15:11:23 [device_allocator/cumem.py:239] CuMemAllocator: sleep freed 34.06 GiB memory in total, of which 7.56 GiB is backed up in CPU and the rest 26.51 GiB is discarded directly. (EngineCore_DP0 pid=1778746) INFO 11-14 15:11:23 [v1/worker/gpu_worker.py:144] Sleep mode freed 35.43 GiB memory, 1.19 GiB memory is still in use. (EngineCore_DP0 pid=1778746) INFO 11-14 15:11:23 [v1/executor/abstract.py:306] It took 3.152677 seconds to fall asleep. (APIServer pid=1778096) INFO: 127.0.0.1:50356 - "POST /sleep HTTP/1.1" 200 OK (EngineCore_DP0 pid=1778746) ERROR 11-14 15:11:23 [logging_utils/dump_input.py:72] Dumping input data for V1 LLM engine (v0.11.1rc7.dev145+gb39a5026e) with config: model='/data/nfs_shared_data/Qwen3-4B', speculative_config=None, tokenizer='/data/nfs_shared_data/Qwen3-4B', skip_tokeni...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: g]: CUDA Illegal Memory Access Error When Sleep Mode is Triggered During Request Processing bug;stale ## Describe the bug When the model instance is processing requests and `sleep_mode` is triggered, a `CUDA error: an i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=qwen3-4b, enable_prefix_caching=False, chunked_p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ggered During Request Processing bug;stale ## Describe the bug When the model instance is processing requests and `sleep_mode` is triggered, a `CUDA error: an illegal memory access was encountered` error occurs. The cau...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA Illegal Memory Access Error When Sleep Mode is Triggered During Request Processing bug;stale ## Describe the bug When the model instance is processing requests and `sleep_mode` is triggered, a `CUDA error: a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

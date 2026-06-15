# vllm-project/vllm#27906: [Bug]: Qwen3-Omni Thinker audio input failing

| 字段 | 值 |
| --- | --- |
| Issue | [#27906](https://github.com/vllm-project/vllm/issues/27906) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Omni Thinker audio input failing

### Issue 正文摘录

### Your current environment v0.11.1rc5, vllm/vllm-openai:nightly, and also head ### 🐛 Describe the bug ```bash vllm serve Qwen/Qwen3-Omni-30B-A3B-Instruct --enforce-eager --tensor-parallel-size curl http://localhost:8000/v1/chat/completions \ -X POST \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen/Qwen3-Omni-30B-A3B-Instruct", "messages": [ { "role": "user", "content": [ { "type": "image_url", "image_url": { "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cars.jpg" } }, { "type": "audio_url", "audio_url": { "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cough.wav" } }, { "type": "text", "text": "What can you see and hear? Answer in one short sentence." } ] } ] }' ``` Logs: ```bash (Worker_TP1 pid=1245304) ERROR 11-01 03:48:09 [v1/executor/multiproc_executor.py:703] WorkerProc hit an exception. (Worker_TP1 pid=1245304) ERROR 11-01 03:48:09 [v1/executor/multiproc_executor.py:703] Traceback (most recent call last): (Worker_TP1 pid=1245304) ERROR 11-01 03:48:09 [v1/executor/multiproc_executor.py:703] File "/workspace/c-vllm/vllm/v1/executor/multiproc_executor.py", line 698, in worker_busy_loop (Worker_TP1 pid=1245304) ERRO...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: executor/multiproc_executor.py:703] return self.worker.execute_model(scheduler_output, *args, **kwargs) (Worker_TP1 pid=1245304) ERROR 11-01 03:48:09 [v1/executor/multiproc_executor.py:703] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen3-Omni-30B-A3B-Instruct, enable_prefix_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-Omni Thinker audio input failing bug ### Your current environment v0.11.1rc5, vllm/vllm-openai:nightly, and also head ### 🐛 Describe the bug ```bash vllm serve Qwen/Qwen3-Omni-30B-A3B-Instruct --enforce-eag...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=65536, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: one, tokenizer='Qwen/Qwen3-Omni-30B-A3B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=65536, download_dir=N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#5785: [Bug]: vLLM 0.4.2 8xH100 init failed

| 字段 | 值 |
| --- | --- |
| Issue | [#5785](https://github.com/vllm-project/vllm/issues/5785) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.4.2 8xH100 init failed

### Issue 正文摘录

### Your current environment **environment:** vllm 0.4.2 python3.10 cuda11.8 cpu: 52 mem: 375Gi **model:** llama3-70B ### 🐛 Describe the bug **description**: vLLM engine init failed, when use 8xH100, tensor_parallel_size=8 Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors. **log:** 024-06-24 02:48:44,378 INFO MainProcess logger.py:58 darwin logger initialized Starting Python Closure container 2024-06-24 02:48:44,438 INFO MainProcess python_closure_container.py:77 load mms model from: /mms/download/models, mms_info: llm-demo-project:llama-3-70B-Instruct:1 2024-06-24 02:48:44,438 INFO MainProcess python_closure_container.py:91 darwin entrypoint not found in MMS path /mms/download/models 2024-06-24 02:48:44,438 INFO MainProcess python_closure_container.py:97 load model from /model 2024-06-24 02:48:44,438 INFO MainProcess python_closure_container.py:17 load serialized func from /model/func....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: able to free up space by deleting files in /dev/shm. If you are inside a Docker container, you can increase /dev/shm size by passing '--shm-size=10.24gb' to 'docker run' (or add it to the run_options list in a Ray clust...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t **environment:** vllm 0.4.2 python3.10 cuda11.8 cpu: 52 mem: 375Gi **model:** llama3-70B ### 🐛 Describe the bug **description**: vLLM engine init failed, when use 8xH100, tensor_parallel_size=8 Worker exit type: SYSTE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=8, disable_custom_all_reduce=False, q...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: lizing an LLM engine (v0.4.2) with config: model='/mms/download/models', speculative_config=None, tokenizer='/mms/download/models', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vLLM 0.4.2 8xH100 init failed bug ### Your current environment **environment:** vllm 0.4.2 python3.10 cuda11.8 cpu: 52 mem: 375Gi **model:** llama3-70B ### 🐛 Describe the bug **description**: vLLM engine init fai...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

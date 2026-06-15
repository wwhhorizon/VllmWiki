# vllm-project/vllm#20241: [Bug]: v0.9.1 - ignoring the input arguments to engine

| 字段 | 值 |
| --- | --- |
| Issue | [#20241](https://github.com/vllm-project/vllm/issues/20241) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.9.1 - ignoring the input arguments to engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I call vllm serve using this command: ``` vllm serve deepseek-ai/DeepSeek-R1 \ --served-model-name "DeepSeek-R1" \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --max-num-seqs 100 \ --dtype auto \ --max-model-len 65536 \ --max-seq-len-to-capture 32768 \ --gpu-memory-utilization 0.85 \ --trust-remote-code \ --port $PORT ``` And it shows `65536` as max length in the ` non-default args` in the log. But then vllm decides to ignore this and load the model with max_seq_len=16384 (see the line that starts with `Initializing a V1 LLM engine (v0.9.1) with config`). ``` INFO 06-30 05:57:38 [api_server.py:1287] vLLM API server version 0.9.1 INFO 06-30 05:57:38 [cli_args.py:309] non-default args: {'port': 30069, 'model': 'deepseek-ai/DeepSeek-R1', 'trust_remote_code': True, 'max_model_len': 65536, 'max_seq_len_to_capture': 32768, 'served_model_name': ['DeepSeek-R1'], 'pipeline_parallel_size': 2, 'tensor_parallel_size': 8, 'gpu_memory_utilization': 0.85, 'max_num_seqs': 100} INFO 06-30 05:57:39 [config.py:224] Replacing legacy 'type' key with 'rope_type' INFO 06-30 05:57:46 [config.py:823] This model supports multiple tasks: {'embed...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 6` as max length in the ` non-default args` in the log. But then vllm decides to ignore this and load the model with max_seq_len=16384 (see the line that starts with `Initializing a V1 LLM engine (v0.9.1) with config`)....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: --pipeline-parallel-size 2 \ --max-num-seqs 100 \ --dtype auto \ --max-model-len 65536 \ --max-seq-len-to-capture 32768 \ --gpu-memory-utilization 0.85 \ --trust-remote-code \ --port $PORT ``` And it shows `65536` as ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: y for distributed inference INFO 06-30 05:57:46 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 06-30 05:57:46 [cuda.py:154] Forcing kv cache block size to 64 for FlashMLA backend. WAR...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: _batched_tokens=8192. INFO 06-30 05:57:46 [cuda.py:154] Forcing kv cache block size to 64 for FlashMLA backend. WARNING 06-30 05:57:48 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may incr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: this command: ``` vllm serve deepseek-ai/DeepSeek-R1 \ --served-model-name "DeepSeek-R1" \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --max-num-seqs 100 \ --dtype auto \ --max-model-len 65536 \ --max-seq-le...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

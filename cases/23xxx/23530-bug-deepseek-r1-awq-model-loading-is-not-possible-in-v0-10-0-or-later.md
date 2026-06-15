# vllm-project/vllm#23530: [Bug]: DeepSeek-R1 AWQ model loading is not possible in v0.10.0 or later.

| 字段 | 值 |
| --- | --- |
| Issue | [#23530](https://github.com/vllm-project/vllm/issues/23530) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-R1 AWQ model loading is not possible in v0.10.0 or later.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to load the QuixiAI/DeepSeek-R1-AWQ model from huggingface in vLLM v0.10.0 or later, an error occurs. Up to vLLM v0.9.2, the model loaded normally and inference was possible. I'm using 8xH100, The parameters used when running vLLM are as follows. ```command - args: - --model - /models/deepseek-r1-awq - --tensor-parallel-size - "8" - --load-format - "auto" - --max-model-len - "65536" - --max-seq-len-to-capture - "65536" - --disable-log-requests - --uvicorn-log-level - "warning" - --gpu-memory-utilization - "0.95" - --trust-remote-code - --enable-prefix-caching - --prefix-caching-hash-algo #not supported in v0 engine - "sha256" - --reasoning-parser - "deepseek_r1" env: - name: VLLM_USE_V1 value: "1" ``` The error log is as follows. ``` INFO 08-25 00:08:45 [__init__.py:235] Automatically detected platform cuda. INFO 08-25 00:08:47 [api_server.py:1755] vLLM API server version 0.10.1.dev1+gbcc0a3cbe INFO 08-25 00:08:47 [cli_args.py:261] non-default args: {'uvicorn_log_level': 'warning', 'model': '/data/models/DeepSeek-R1-awq-64g', 'trust_remote_code': True, 'max_model_len': 65536, 'max_seq_len_to_capture': 65536, 'serv...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: " - --max-seq-len-to-capture - "65536" - --disable-log-requests - --uvicorn-log-level - "warning" - --gpu-memory-utilization - "0.95" - --trust-remote-code - --enable-prefix-caching - --prefix-caching-hash-algo #not sup...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 08-25 00:08:47 [api_server.py:1755] vLLM API server version 0.10.1.dev1+gbcc0a3cbe INFO 08-25 00:08:47 [cli_args.py:261] non-default args: {'uvicorn_log_level': 'warning', 'model': '/data/models/Deep...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: rride_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=65536, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=8, pipeline_parallel_size=1, disable...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 25 00:08:55 [cuda.py:162] Forcing kv cache block size to 64 for FlashMLA backend. INFO 08-25 00:08:59 [__init__.py:235] Automatically detected platform cuda. INFO 08-25 00:09:01 [core.py:572] Waiting for init message fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: .9.2, the model loaded normally and inference was possible. I'm using 8xH100, The parameters used when running vLLM are as follows. ```command - args: - --model - /models/deepseek-r1-awq - --tensor-parallel-size - "8" -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

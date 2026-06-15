# vllm-project/vllm#21336: [Bug]: vLLM crashes when using --enable-sleep-mode with Blackwell PRO 6000 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#21336](https://github.com/vllm-project/vllm/issues/21336) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crashes when using --enable-sleep-mode with Blackwell PRO 6000 GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM crashes when passed the `--enable-sleep-mode` flag. Command-line: `vllm serve Qwen/Qwen3-235B-A22B-GPTQ-Int4 --max-model-len 32768 --port 8080 --tensor-parallel 2 --max_num_seqs 1 --reasoning-parser qwen3 --no-enforce-eager --enable-sleep-mode` The crash: ``` > vllm serve Qwen/Qwen3-235B-A22B-GPTQ-Int4 --max-model-len 32768 --port 8080 --tensor-parallel 2 --max_num_seqs 1 --reasoning-parser qwen3 --no-enforce-eager --enable-sleep-mode INFO 07-21 15:36:40 [__init__.py:235] Automatically detected platform cuda. INFO 07-21 15:36:42 [api_server.py:1756] vLLM API server version 0.9.2rc2.dev201+gf45a33288.d20250713 INFO 07-21 15:36:42 [cli_args.py:302] non-default args: {'model_tag': 'Qwen/Qwen3-235B-A22B-GPTQ-Int4', 'port': 8080, 'model': 'Qwen/Qwen3-235B-A22B-GPTQ-Int4', 'max_model_len': 32768, 'enable_sleep_mode': True, 'reasoning_parser': 'qwen3', 'tensor_parallel_size': 2, 'max_num_seqs': 1} INFO 07-21 15:36:46 [config.py:1593] Using max model len 32768 INFO 07-21 15:36:46 [gptq_marlin.py:170] The model is convertible to gptq_marlin during runtime. Using gptq_marlin kernel. INFO 07-21 15:36:47 [config.py:2405] Chunked prefill...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: rashes when using --enable-sleep-mode with Blackwell PRO 6000 GPUs bug;unstale ### Your current environment ### 🐛 Describe the bug vLLM crashes when passed the `--enable-sleep-mode` flag. Command-line: `vllm serve Qwen/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend='qwen3'), observabilit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 07-21 15:36:42 [api_server.py:1756] vLLM API server version 0.9.2rc2.dev201+gf45a33288.d20250713 INFO 07-21 15:36:42 [cli_args.py:302] non-default args: {'model_tag': 'Qwen/Qwen3-235B-A22B-GPTQ-Int4'...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e-sleep-mode` flag. Command-line: `vllm serve Qwen/Qwen3-235B-A22B-GPTQ-Int4 --max-model-len 32768 --port 8080 --tensor-parallel 2 --max_num_seqs 1 --reasoning-parser qwen3 --no-enforce-eager --enable-sleep-mode` The cr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: vLLM crashes when using --enable-sleep-mode with Blackwell PRO 6000 GPUs bug;unstale ### Your current environment ### 🐛 Describe the bug vLLM crashes when passed the `--enable-sleep-mode` flag. Command-line: `vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

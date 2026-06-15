# vllm-project/vllm#25861: [Bug]: vLLM failed to run Qwen3-VL with ray executor

| 字段 | 值 |
| --- | --- |
| Issue | [#25861](https://github.com/vllm-project/vllm/issues/25861) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM failed to run Qwen3-VL with ray executor

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM crashes when running Qwen/Qwen3-VL-235B-A22B-Instruct with ray distributed executor. The error says AsyncGPUModelRunnerOutput is not serializable. It works fine with mp executor. It also works fine with ray after I set VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE to nccl and turn off async-scheduling and remove -mm-processor-cache-type shm. command: ```bash vllm serve Qwen/Qwen3-VL-235B-A22B-Instruct --tensor-parallel-size 8 --mm-encoder-tp-mode data --mm-processor-cache-type shm --async-scheduling --distributed-executor-backend ray ``` errors: ``` (APIServer pid=281640) INFO 09-29 07:35:15 [entrypoints/chat_utils.py:560] Detected the chat template content format to be 'openai'. You can set `--chat-template-content-format` to override this. (EngineCore_DP0 pid=281777) DEBUG 09-29 07:35:15 [v1/engine/core.py:747] EngineCore loop active. (EngineCore_DP0 pid=281777) INFO 09-29 07:35:15 [executor/ray_distributed_executor.py:552] RAY_CGRAPH_get_timeout is set to 300 (EngineCore_DP0 pid=281777) INFO 09-29 07:35:15 [executor/ray_distributed_executor.py:554] VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE = auto (EngineCore_DP0 pid=281777) INFO 09...

## 现有链接修复摘要

#26148 Fix V1 engine serialization error with Ray distributed executor

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: e (v0.11.0rc2.dev41+g0307428d6) with config: model='qwen3-vl-instruct/', speculative_config=None, tokenizer='qwen3-vl-instruct/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: e with mp executor. It also works fine with ray after I set VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE to nccl and turn off async-scheduling and remove -mm-processor-cache-type shm. command: ```bash vllm serve Qwen/Qwen3-VL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, data_parallel_siz...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM failed to run Qwen3-VL with ray executor bug;ray ### Your current environment ### 🐛 Describe the bug vLLM crashes when running Qwen/Qwen3-VL-235B-A22B-Instruct with ray distributed executor. The error says A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: -mm-processor-cache-type shm --async-scheduling --distributed-executor-backend ray ``` errors: ``` (APIServer pid=281640) INFO 09-29 07:35:15 [entrypoints/chat_utils.py:560] Detected the chat template content format to...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26148](https://github.com/vllm-project/vllm/pull/26148) | closes_keyword | 0.95 | Fix V1 engine serialization error with Ray distributed executor | Fixes** - [Ray #57039](https://github.com/ray-project/ray/issues/57039) - [vLLM #25861](https://github.com/vllm-project/vllm/issues/25861) **Root Cause:** `AsyncGPUModelRunnerOutp |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

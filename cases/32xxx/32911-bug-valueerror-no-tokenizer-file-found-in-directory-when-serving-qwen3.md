# vllm-project/vllm#32911: [Bug]: "ValueError: No tokenizer file found in directory" when serving Qwen3-Omni

| 字段 | 值 |
| --- | --- |
| Issue | [#32911](https://github.com/vllm-project/vllm/issues/32911) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "ValueError: No tokenizer file found in directory" when serving Qwen3-Omni

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run following command: ``` vllm serve /hdd2/ltg/Qwen3-Omni-30B-A3B-Instruct \ --host 0.0.0.0 \ --port 12333 \ --gpu-memory-utilization 0.9 \ --enable-chunked-prefill \ --enable-prefix-caching \ --pipeline-parallel-size 1 \ --tensor-parallel-size 2 \ --max-num-seqs 256 \ --max-model-len 32768 \ --disable-fastapi-docs ``` I got following error message: ``` WARNING 01-23 13:48:43 [mooncake_connector.py:18] Mooncake not available, MooncakeOmniConnector will not work (APIServer pid=79770) INFO 01-23 13:48:44 [api_server.py:1272] vLLM API server version 0.14.0 (APIServer pid=79770) INFO 01-23 13:48:44 [utils.py:263] non-default args: {'model_tag': '/hdd2/ltg/Qwen3-Omni-30B-A3B-Instruct', 'host': '0.0.0.0', 'port': 12333, 'disable_fastapi_docs': True, 'model': '/hdd2/ltg/Qwen3-Omni-30B-A3B-Instruct', 'max_model_len': 32768, 'tensor_parallel_size': 2, 'enable_prefix_caching': True, 'max_num_seqs': 256, 'enable_chunked_prefill': True} (APIServer pid=79770) Unrecognized keys in `rope_scaling` for 'rope_type'='default': {'interleaved', 'mrope_section', 'mrope_interleaved'} (APIServer pid=79770) Unrecognized keys in `rope_scaling` for...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rver pid=79770) INFO 01-23 13:48:44 [api_server.py:1272] vLLM API server version 0.14.0 (APIServer pid=79770) INFO 01-23 13:48:44 [utils.py:263] non-default args: {'model_tag': '/hdd2/ltg/Qwen3-Omni-30B-A3B-Instruct', '...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Error: No tokenizer file found in directory" when serving Qwen3-Omni bug;stale ### Your current environment ### 🐛 Describe the bug When I run following command: ``` vllm serve /hdd2/ltg/Qwen3-Omni-30B-A3B-Instruct \ --h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ntrypoints/cli/main.py", line 73, in main (APIServer pid=79770) args.dispatch_function(args) (APIServer pid=79770) File "/hdd2/ltg/Qwen3-Omni-30B-A3B-Instruct/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/serv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: "ValueError: No tokenizer file found in directory" when serving Qwen3-Omni bug;stale ### Your current environment ### 🐛 Describe the bug When I run following command: ``` vllm serve /hdd2/ltg/Qwen3-Omni-30B-A3B-I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion'} (APIServer pid=79770) INFO 01-23 13:48:44 [model.py:530] Resolved architecture: Qwen3OmniMoeForConditionalGeneration (APIServer pid=79770) INFO 01-23 13:48:44 [model.py:1545] Using max model len 32768 (APIServer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

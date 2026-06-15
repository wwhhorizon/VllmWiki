# vllm-project/vllm#23321: [Bug]: VLLM does not work with gguf files

| 字段 | 值 |
| --- | --- |
| Issue | [#23321](https://github.com/vllm-project/vllm/issues/23321) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM does not work with gguf files

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve /slow_data_new/vladlen/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf \ --tensor-parallel-size 4 \ --quantization gguf \ --max-model-len 4500 the path to model: /slow_data_new/vladlen/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf --- /slow_data_new/vladlen/LLMEvaluation/.venv/lib/python3.11/site-packages/transformers/utils/hub.py:111: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( INFO 08-21 08:11:19 [__init__.py:235] Automatically detected platform cuda. INFO 08-21 08:11:21 [api_server.py:1755] vLLM API server version 0.10.0 INFO 08-21 08:11:21 [cli_args.py:261] non-default args: {'model_tag': '/slow_data_new/vladlen/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf', 'model': '/slow_data_new/vladlen/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf', 'max_model_len': 4500, 'quantization': 'gguf', 'tensor_parallel_size': 4} ERROR 08-21 08:11:47 [config.py:133] Error retrieving safetensors: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/slow_data_new/vladlen/meta-llama-3...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: -instruct-abliterated.Q4_K_M.gguf \ --tensor-parallel-size 4 \ --quantization gguf \ --max-model-len 4500 the path to model: /slow_data_new/vladlen/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf --- /slow_data_new/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bug CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve /slow_data_new/vladlen/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf \ --tensor-parallel-size 4 \ --quantization gguf \ --max-model-len 4500 the path to model: /slow_data...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: platform cuda. INFO 08-21 08:11:21 [api_server.py:1755] vLLM API server version 0.10.0 INFO 08-21 08:11:21 [cli_args.py:261] non-default args: {'model_tag': '/slow_data_new/vladlen/meta-llama-3.1-8b-instruct-abliterated...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 1/site-packages/vllm/entrypoints/cli/main.py", line 54, in main args.dispatch_function(args) File "/slow_data_new/vladlen/LLMEvaluation/.venv/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 52, in cmd...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gguf files bug ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve /slow_data_new/vladlen/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf \ --tensor-parallel-size 4 \ --quantiz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

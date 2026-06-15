# vllm-project/vllm#22416: [Bug]: mistralai/Mixtral-8x7B-Instruct-v0.1 will not load from local path

| 字段 | 值 |
| --- | --- |
| Issue | [#22416](https://github.com/vllm-project/vllm/issues/22416) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: mistralai/Mixtral-8x7B-Instruct-v0.1 will not load from local path

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run mistralai/Mixtral-8x7B-Instruct-v0.1 model using vLLM, I get an Value error about "Repo id" and then the program exits. Note: I see this same error message for other models that then go on to successfully load/run, so have a suspicion it is a red herring. Command line: `/path/to/vllm serve /data/huggingface/models/mistralai/Mixtral-8x7B-Instruct-v0.1 --port 8011 --dtype float16 --tokenizer_mode mistral --config_format --mistral --load_format mistral --tensor-parallel-size 2` Full output: ``` INFO 08-06 21:22:58 [__init__.py:244] Automatically detected platform cuda. INFO 08-06 21:23:02 [api_server.py:1287] vLLM API server version 0.9.1 INFO 08-06 21:23:02 [cli_args.py:309] non-default args: {'port': 8011, 'model': '/data/huggingface/models/mistralai/Mixtral-8x7B-Instruct-v0.1', 'tokenizer_mode': 'mistral', 'dtype': 'float16', 'config_format': 'mistral', 'load_format': 'mistral', 'tensor_parallel_size': 2} Traceback (most recent call last): File "/path/to/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/path/to/vllm/entrypoints/cli/main.py", line 59, in main args.dispatch_function(args) File "/path/to/vllm/entrypoints/c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: or other models that then go on to successfully load/run, so have a suspicion it is a red herring. Command line: `/path/to/vllm serve /data/huggingface/models/mistralai/Mixtral-8x7B-Instruct-v0.1 --port 8011 --dtype flo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug When I run mistralai/Mixtral-8x7B-Instruct-v0.1 model using vLLM, I get an Value error about "Repo id" and then the program exits. Note: I see this same error message for other models that then go...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: File "/path/to/vllm/entrypoints/cli/main.py", line 59, in main args.dispatch_function(args) File "/path/to/vllm/entrypoints/cli/serve.py", line 58, in cmd uvloop.run(run_server(args)) File "/path/to/uvloop/__init__.py",...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ta/huggingface/models/mistralai/Mixtral-8x7B-Instruct-v0.1 --port 8011 --dtype float16 --tokenizer_mode mistral --config_format --mistral --load_format mistral --tensor-parallel-size 2` Full output: ``` INFO 08-06 21:22...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `` INFO 08-06 21:22:58 [__init__.py:244] Automatically detected platform cuda. INFO 08-06 21:23:02 [api_server.py:1287] vLLM API server version 0.9.1 INFO 08-06 21:23:02 [cli_args.py:309] non-default args: {'port': 8011...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

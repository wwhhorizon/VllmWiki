# vllm-project/vllm#22301: [Bug]: ModelConfig validation error when serving chatgpt-oss models

| 字段 | 值 |
| --- | --- |
| Issue | [#22301](https://github.com/vllm-project/vllm/issues/22301) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ModelConfig validation error when serving chatgpt-oss models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The env is setup by: ``` uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 \ --index-strategy unsafe-best-match vllm serve openai/gpt-oss-120b ``` error message is: ``` (py312) ➜ transformers git:(main) vllm serve openai/gpt-oss-120b INFO 08-06 03:05:28 [__init__.py:235] Automatically detected platform cuda. INFO 08-06 03:05:31 [api_server.py:1755] vLLM API server version 0.10.0 INFO 08-06 03:05:31 [cli_args.py:261] non-default args: {'model_tag': 'openai/gpt-oss-120b', 'model': 'openai/gpt-oss-120b'} Traceback (most recent call last): File "/root/miniconda3/bin/vllm", line 8, in sys.exit(main()) File "/root/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 54, in main args.dispatch_function(args) File "/root/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 52, in cmd uvloop.run(run_server(args)) File "/root/miniconda3/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run return loop.run_until_complete(wrapper()) File "uvloop/loop.pyx", line 1518, in uvloop...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: environment ### 🐛 Describe the bug The env is setup by: ``` uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ModelConfig validation error when serving chatgpt-oss models bug ### Your current environment ### 🐛 Describe the bug The env is setup by: ``` uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 0/site-packages/vllm/entrypoints/cli/main.py", line 54, in main args.dispatch_function(args) File "/root/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 52, in cmd uvloop.run(run_server(args...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0b INFO 08-06 03:05:28 [__init__.py:235] Automatically detected platform cuda. INFO 08-06 03:05:31 [api_server.py:1755] vLLM API server version 0.10.0 INFO 08-06 03:05:31 [cli_args.py:261] non-default args: {'model_tag'...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: it` [type=value_error, input_value=ArgsKwargs((), {'model': ...attention_dtype': None}), input_type=ArgsKwargs] For further information visit https://errors.pydantic.dev/2.11/v/value_error (py312) ➜ transformers git:(ma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

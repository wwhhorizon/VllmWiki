# vllm-project/vllm#22013: [Bug]: Random Dataset Serve Benchmark throws AttributeError when using MistralTokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#22013](https://github.com/vllm-project/vllm/issues/22013) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Random Dataset Serve Benchmark throws AttributeError when using MistralTokenizer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running the random dataset serve benchmark for Mistral Small 3.2 24B Instruct 2506 using the MistralTokenizer with: ```bash vllm serve "/model" --served-model-name mistral-small-3-2-24b-instruct-2506 --port 5555 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --disable-log-requests ``` ```bash vllm bench serve --backend openai-chat --model "/model" --served-model-name mistral-small-3-2-24b-instruct-2506 --base-url "http://127.0.0.1:5555" --endpoint /v1/chat/completions --dataset-name random --num-prompts 100 --tokenizer_mode mistral ``` produces the following error: ```bash Traceback (most recent call last): File "/usr/local/bin/vllm", line 10, in sys.exit(main()) ^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 54, in main args.dispatch_function(args) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/benchmark/serve.py", line 21, in cmd main(args) File "/usr/local/lib/python3.12/dist-packages/vllm/benchmarks/serve.py", line 958, in main input_requests = get_samples(args, tokenizer) ^^^^^^^^^^^^^^^^...

## 现有链接修复摘要

#22121 [Bugfix] Add num_special_tokens_to_add to MistralTokenizer, fixes #22013

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: e-auto-tool-choice --disable-log-requests ``` ```bash vllm bench serve --backend openai-chat --model "/model" --served-model-name mistral-small-3-2-24b-instruct-2506 --base-url "http://127.0.0.1:5555" --endpoint /v1/cha...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: st-packages/vllm/benchmarks/datasets.py", line 342, in sample num_special_tokens = tokenizer.num_special_tokens_to_add() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ AttributeError: 'MistralTokenizer' object has no attribute 'nu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Describe the bug Running the random dataset serve benchmark for Mistral Small 3.2 24B Instruct 2506 using the MistralTokenizer with: ```bash vllm serve "/model" --served-model-name mistral-small-3-2-24b-instruct-2506 --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 24B Instruct 2506 using the MistralTokenizer with: ```bash vllm serve "/model" --served-model-name mistral-small-3-2-24b-instruct-2506 --port 5555 --tokenizer_mode mistral --config_format mistral --load_format mistral -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: stral --tool-call-parser mistral --enable-auto-tool-choice --disable-log-requests ``` ```bash vllm bench serve --backend openai-chat --model "/model" --served-model-name mistral-small-3-2-24b-instruct-2506 --base-url "h...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#22121](https://github.com/vllm-project/vllm/pull/22121) | closes_keyword | 0.95 | [Bugfix] Add num_special_tokens_to_add to MistralTokenizer, fixes #22013 | Fixes #22013 ## Test Plan Manually testing the serve benchmark without the changes and with the changes in place. ```bash uv run vllm/entrypoints/openai/api_server.py --model /mod |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

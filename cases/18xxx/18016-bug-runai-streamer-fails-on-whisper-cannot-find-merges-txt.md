# vllm-project/vllm#18016: [Bug]: runai streamer fails on whisper (cannot find merges.txt)

| 字段 | 值 |
| --- | --- |
| Issue | [#18016](https://github.com/vllm-project/vllm/issues/18016) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: runai streamer fails on whisper (cannot find merges.txt)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug RunAI streamer fails to load Whisper, cannot find `merges.txt` file. ```bash vllm serve s3:// /openai--whisper-large-v2 --host 0.0.0.0 --port "8000" --load_format "runai_streamer" ``` We observe the following error logs: ```text Loading safetensors using Runai Model Streamer: 0% Completed | 0/1 [00:00 sys.exit(main()) ^^^^^^ File "/usr/local/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 51, in main args.dispatch_function(args) File "/usr/local/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 27, in cmd uvloop.run(run_server(args)) File "/usr/local/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/usr/local/lib/python3.12/site-packages/uvloop/__init__.py", line 61, in wrapper return await main ^^^^^^^^^^ Fil...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: erve s3:// /openai--whisper-large-v2 --host 0.0.0.0 --port "8000" --load_format "runai_streamer" ``` We observe the following error logs: ```text Loading safetensors using Runai Model Streamer: 0% Completed | 0/1 [00:00...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/loca...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2/site-packages/vllm/entrypoints/cli/main.py", line 51, in main args.dispatch_function(args) File "/usr/local/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 27, in cmd uvloop.run(run_server(args)) Fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

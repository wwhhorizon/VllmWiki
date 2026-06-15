# vllm-project/vllm#17372: [Bug]:Qwen2.5vl vllm serve  Engine process failed to start

| 字段 | 值 |
| --- | --- |
| Issue | [#17372](https://github.com/vllm-project/vllm/issues/17372) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Qwen2.5vl vllm serve  Engine process failed to start

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the `vllm serve` command with a Qwen2.5 model, the engine fails to start and terminates with a `RuntimeError`. The logs show the engine shutting down immediately after initialization. A warning about leaked semaphore objects also appears. ```bash vllm serve /data/qwen2.5/Qwen2.5-VL-7B-Instruct-AWQ/ \ --port 8000 \ --host 0.0.0.0 \ --dtype bfloat16 \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.99 \ --trust-remote-code ``` ```text DEBUG 04-29 09:38:15 [client.py:260] Shutting down MQLLMEngineClient output handler. Traceback (most recent call last): File "/data/anaconda3/envs/vllm/bin/vllm", line 8, in sys.exit(main()) File "/data/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 53, in main args.dispatch_function(args) File "/data/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 27, in cmd uvloop.run(run_server(args)) File "/data/anaconda3/envs/vllm/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run return loop.run_until_complete(wrapper()) File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/dat...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 2.5/Qwen2.5-VL-7B-Instruct-AWQ/ \ --port 8000 \ --host 0.0.0.0 \ --dtype bfloat16 \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.99 \ --trust-remote-code ``` ```text DEBUG 04-29 09:38:15 [client.py:260] Shuttin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: trypoints/openai/api_server.py", line 1078, in run_server async with build_async_engine_client(args) as engine_client: File "/data/anaconda3/envs/vllm/lib/python3.10/contextlib.py", line 199, in __aenter__ return await...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 0/site-packages/vllm/entrypoints/cli/main.py", line 53, in main args.dispatch_function(args) File "/data/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 27, in cmd uvloop.run(run_se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]:Qwen2.5vl vllm serve Engine process failed to start bug;stale ### Your current environment ### 🐛 Describe the bug When running the `vllm serve` command with a Qwen2.5 model, the engine fails to start and terminates

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

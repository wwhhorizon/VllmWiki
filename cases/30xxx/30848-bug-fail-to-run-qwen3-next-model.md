# vllm-project/vllm#30848: [Bug]: Fail to run Qwen3-Next model.

| 字段 | 值 |
| --- | --- |
| Issue | [#30848](https://github.com/vllm-project/vllm/issues/30848) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Fail to run Qwen3-Next model.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Start the vllm by: ``` VLLM_CPU_KVCACHE_SPACE=30 vllm serve \ /root/dataDisk/Qwen3-Next-80B-A3B-Instruct/ \ --port 8000 \ --served-model-name Qwen3-Next-80B-A3B-Instruct \ --trust-remote-code \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` Fail when loading the model at 83%. It can be re-produced. ``` Loading safetensors checkpoint shards: 78% Completed | 32/41 [01:50 (APIServer pid=1529037) sys.exit(main()) (APIServer pid=1529037) ^^^^^^ (APIServer pid=1529037) File "/root/vllm_project/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 73, in main (APIServer pid=1529037) args.dispatch_function(args) (APIServer pid=1529037) File "/root/vllm_project/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 60, in cmd (APIServer pid=1529037) uvloop.run(run_server(args)) (APIServer pid=1529037) File "/root/vllm_project/.venv/lib/python3.12/site-packages/uvloop/__init__.py", line 96, in run (APIServer pid=1529037) return __asyncio.run( (APIServer pid=1529037) ^^^^^^^^^^^^^^ (APIServer pid=1529037) File "/root/miniconda3/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Fail to run Qwen3-Next model. bug;stale ### Your current environment ### 🐛 Describe the bug Start the vllm by: ``` VLLM_CPU_KVCACHE_SPACE=30 vllm serve \ /root/dataDisk/Qwen3-Next-80B-A3B-Instruct/ \ --port 8000...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: p/__init__.py", line 96, in run (APIServer pid=1529037) return __asyncio.run( (APIServer pid=1529037) ^^^^^^^^^^^^^^ (APIServer pid=1529037) File "/root/miniconda3/lib/python3.12/asyncio/runners.py", line 195, in run (A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rypoints/cli/main.py", line 73, in main (APIServer pid=1529037) args.dispatch_function(args) (APIServer pid=1529037) File "/root/vllm_project/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 60, i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Fail to run Qwen3-Next model. bug;stale ### Your current environment ### 🐛 Describe the bug Start the vllm by: ``` VLLM_CPU_KVCACHE_SPACE=30 vllm serve \ /root/dataDisk/Qwen3-Next-80B-A3B-Instruct/ \ --port 8000...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

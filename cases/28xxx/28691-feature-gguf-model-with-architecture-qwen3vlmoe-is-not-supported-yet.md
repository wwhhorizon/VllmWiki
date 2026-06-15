# vllm-project/vllm#28691: [Feature]: GGUF model with architecture qwen3vlmoe is not supported yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#28691](https://github.com/vllm-project/vllm/issues/28691) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: GGUF model with architecture qwen3vlmoe is not supported yet.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In `0.11.1rc7.dev109+gca00b1bfc` and `0.11.0` we can't use `models--Qwen--Qwen3-VL-30B-A3B-Instruct-GGUF/snapshots/f54435e6cc31258f04b0969105c3f6badb197931/Qwen3VL-30B-A3B-Instruct-Q4_K_M.gguf` (in a RTX-5090 just in case). ### Alternatives _No response_ ### Additional context ``` [llm] | (APIServer pid=1) Traceback (most recent call last): [llm] | (APIServer pid=1) File "/usr/local/bin/vllm", line 10, in [llm] | (APIServer pid=1) sys.exit(main()) [llm] | (APIServer pid=1) ^^^^^^ [llm] | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 73, in main [llm] | (APIServer pid=1) args.dispatch_function(args) [llm] | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 59, in cmd [llm] | (APIServer pid=1) uvloop.run(run_server(args)) [llm] | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 96, in run [llm] | (APIServer pid=1) return __asyncio.run( [llm] | (APIServer pid=1) ^^^^^^^^^^^^^^ [llm] | (APIServer pid=1) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run [llm] | (APIServer pid=1) return run...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: GGUF model with architecture qwen3vlmoe is not supported yet. feature request;stale ### 🚀 The feature, motivation and pitch In `0.11.1rc7.dev109+gca00b1bfc` and `0.11.0` we can't use `models--Qwen--Qwen3-VL-3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: _.py", line 96, in run [llm] | (APIServer pid=1) return __asyncio.run( [llm] | (APIServer pid=1) ^^^^^^^^^^^^^^ [llm] | (APIServer pid=1) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run [llm] | (APIServe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: GGUF model with architecture qwen3vlmoe is not supported yet. feature request;stale ### 🚀 The feature, motivation and pitch In `0.11.1rc7.dev109+gca00b1bfc` and `0.11.0` we can't use `models--Qwen--Qwen3-VL-3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: GGUF model with architecture qwen3vlmoe is not supported yet. feature request;stale ### 🚀 The feature, motivation and pitch In `0.11.1rc7.dev109+gca00b1bfc` and `0.11.0` we can't use `models--Qwen--Qwen3-VL-30B-A3B-I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: cli/main.py", line 73, in main [llm] | (APIServer pid=1) args.dispatch_function(args) [llm] | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 59, in cmd [llm] | (APIS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#36411: [Bug]: vLLM not working with qwen3.5 27B

| 字段 | 值 |
| --- | --- |
| Issue | [#36411](https://github.com/vllm-project/vllm/issues/36411) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM not working with qwen3.5 27B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug logs ``` bash (APIServer pid=4161) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 73, in main (APIServer pid=4161) args.dispatch_function(args) (APIServer pid=4161) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 111, in cmd (APIServer pid=4161) uvloop.run(run_server(args)) (APIServer pid=4161) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 96, in run (APIServer pid=4161) return __asyncio.run( (APIServer pid=4161) ^^^^^^^^^^^^^^ (APIServer pid=4161) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=4161) return runner.run(main) (APIServer pid=4161) ^^^^^^^^^^^^^^^^ (APIServer pid=4161) File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run (APIServer pid=4161) return self._loop.run_until_complete(task) (APIServer pid=4161) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=4161) File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete (APIServer pid=4161) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 48, in wrapper (APIServer pid=4161) return await main (AP...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vLLM not working with qwen3.5 27B bug ### Your current environment ### 🐛 Describe the bug logs ``` bash (APIServer pid=4161) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 73, i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: loop/__init__.py", line 96, in run (APIServer pid=4161) return __asyncio.run( (APIServer pid=4161) ^^^^^^^^^^^^^^ (APIServer pid=4161) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=4161)...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: entrypoints/cli/main.py", line 73, in main (APIServer pid=4161) args.dispatch_function(args) (APIServer pid=4161) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 111, in cmd (APIServer...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [utils.py:287] █▄█▀ █ █ █ █ model Qwen/Qwen3.5-27B-GPTQ-Int4 (APIServer pid=4317) INFO 03-06 01:53:38 [utils.py:287] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=4317) INFO 03-06 01:53:38 [utils.py:287] (APIServer pid=4317) INFO 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: o load has model type `qwen3_5` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. (APIServer pid=4161)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

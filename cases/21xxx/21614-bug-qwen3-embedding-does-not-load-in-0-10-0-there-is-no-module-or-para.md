# vllm-project/vllm#21614: [Bug]: Qwen3 Embedding does not load in 0.10.0 - There is no module or parameter named 'layers' in Qwen3ForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#21614](https://github.com/vllm-project/vllm/issues/21614) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 Embedding does not load in 0.10.0 - There is no module or parameter named 'layers' in Qwen3ForCausalLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```$ kubectl logs llm-qwen3-embedding-8b-bc6ffb955-77g9g -f Defaulted container "qwen3-embedding-8b" out of: qwen3-embedding-8b, qwen3-embedding-8b-gpu-test (init) Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00 ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 1856, in uvloop.run(run_server(args)) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 61, in wrapper return await main ^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 1791, in run_server await run_server_worker(listen_address, sock, args,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3 Embedding does not load in 0.10.0 - There is no module or parameter named 'layers' in Qwen3ForCausalLM bug ### Your current environment ### 🐛 Describe the bug ```$ kubectl logs llm-qwen3-embedding-8b-bc6ffb...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: "qwen3-embedding-8b" out of: qwen3-embedding-8b, qwen3-embedding-8b-gpu-test (init) Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00 ", line 198, in _run_module_as_main File " ", line 88, in _run_code Fi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

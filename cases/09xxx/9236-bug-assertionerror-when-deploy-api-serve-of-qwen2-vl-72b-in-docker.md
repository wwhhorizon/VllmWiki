# vllm-project/vllm#9236: [Bug]: AssertionError When deploy API serve of Qwen2-VL-72B in Docker

| 字段 | 值 |
| --- | --- |
| Issue | [#9236](https://github.com/vllm-project/vllm/issues/9236) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AssertionError When deploy API serve of Qwen2-VL-72B in Docker

### Issue 正文摘录

### Your current environment I'm using vLLM-Docker latest (0.6.2) ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO 10-10 00:56:44 api_server.py:164] Multiprocessing frontend to use ipc:///tmp/6f288ab9-add1-4cfb-a217-af1687e882b5 for IPC Path. qwen72-1 | INFO 10-10 00:56:44 api_server.py:177] Started engine process with PID 36 qwen72-1 | Unrecognized keys in `rope_scaling` for 'rope_type'='default': {'mrope_section'} qwen72-1 | Traceback (most recent call last): qwen72-1 | File " ", line 198, in _run_module_as_main qwen72-1 | File " ", line 88, in _run_code qwen72-1 | File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 571, in qwen72-1 | uvloop.run(run_server(args)) qwen72-1 | File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run qwen72-1 | return __asyncio.run( qwen72-1 | ^^^^^^^^^^^^^^ qwen72-1 | File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run qwen72-1 | return runner.run(main) qwen72-1 | ^^^^^^^^^^^^^^^^ qwen72-1 | File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run qwen72-1 | return self._loop.run_until_complete(task) qwen72-1 | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ qwe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: AssertionError When deploy API serve of Qwen2-VL-72B in Docker bug ### Your current environment I'm using vLLM-Docker latest (0.6.2) ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO 10-10 00:56:44...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: AssertionError When deploy API serve of Qwen2-VL-72B in Docker bug ### Your current environment I'm using vLLM-Docker latest (0.6.2) ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO 10-10 00:56:44...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ror ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: -72B in Docker bug ### Your current environment I'm using vLLM-Docker latest (0.6.2) ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO 10-10 00:56:44 api_server.py:164] Multiprocessing frontend to use ipc:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

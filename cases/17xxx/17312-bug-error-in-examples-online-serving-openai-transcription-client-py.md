# vllm-project/vllm#17312: [Bug]: error in examples/online_serving/openai_transcription_client.py

| 字段 | 值 |
| --- | --- |
| Issue | [#17312](https://github.com/vllm-project/vllm/issues/17312) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash;slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: error in examples/online_serving/openai_transcription_client.py

### Issue 正文摘录

### Your current environment Hi everyone, I'm trying to run the code in examples/online_serving/openai_transcription_client.py I'm using vllm 0.8.4 ### 🐛 Describe the bug > INFO 04-28 17:06:48 [__init__.py:239] Automatically detected platform cuda. > transcription result: The first words I spoke in the original phonograph, a little piece of practical poetry. Mary had a little lamb, its streets were quite as slow, and everywhere that Mary went the lamb was sure to go. > transcription result: Traceback (most recent call last): > File "/home/aptikal/abdalfar/InterviewSim/vllm_project/openai_transcription_client.py", line 66, in > asyncio.run(stream_openai_response()) > File "/usr/lib/python3.11/asyncio/runners.py", line 190, in run > return runner.run(main) > ^^^^^^^^^^^^^^^^ > File "/usr/lib/python3.11/asyncio/runners.py", line 118, in run > return self._loop.run_until_complete(task) > ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ > File "/usr/lib/python3.11/asyncio/base_events.py", line 653, in run_until_complete > return future.result() > ^^^^^^^^^^^^^^^ > File "/home/aptikal/abdalfar/InterviewSim/vllm_project/openai_transcription_client.py", line 60, in stream_openai_response > content = c...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: > INFO 04-28 17:06:48 [__init__.py:239] Automatically detected platform cuda. > transcription result: The first words I spoke in the original phonograph, a little piece of practical poetry. Mary had a little lamb, its s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: im/vllm_project/openai_transcription_client.py", line 66, in > asyncio.run(stream_openai_response()) > File "/usr/lib/python3.11/asyncio/runners.py", line 190, in run > return runner.run(main) > ^^^^^^^^^^^^^^^^ > File...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance cuda crash;slowdown Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

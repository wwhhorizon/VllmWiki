# vllm-project/vllm#27036: [CI Failure]: microsoft/Phi-3.5 model broken

| 字段 | 值 |
| --- | --- |
| Issue | [#27036](https://github.com/vllm-project/vllm/issues/27036) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: microsoft/Phi-3.5 model broken

### Issue 正文摘录

### Name of failing test entrypoints/openai/test_vision.py::test_single_chat_session_image_base64encoded_beamsearch[2-microsoft/Phi-3.5-vision-instruct] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test AFAIK microsoft/Phi-3.5 is known to have accuracy issues. Not sure why this only started happening recently. Currently not able to reproduce locally with error: ``` (APIServer pid=437241) INFO 10-16 11:29:26 [chat_utils.py:545] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this. (APIServer pid=437241) WARNING 10-16 11:29:27 [async_llm.py:287] Processor has been moved under OpenAIServing and will be removed from AsyncLLM in v0.13. (EngineCore_DP0 pid=440286) Exception in thread Thread-4 (process_input_sockets): (EngineCore_DP0 pid=440286) Traceback (most recent call last): (EngineCore_DP0 pid=440286) File "/usr/lib/python3.12/threading.py", line 1073, in _bootstrap_inner (EngineCore_DP0 pid=440286) self.run() (EngineCore_DP0 pid=440286) File "/usr/lib/python3.12/threading.py", line 1010, in run (EngineCo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: microsoft/Phi-3.5 model broken ci-failure ### Name of failing test entrypoints/openai/test_vision.py::test_single_chat_session_image_base64encoded_beamsearch[2-microsoft/Phi-3.5-vision-instruct] ### Basic...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: -3.5-vision-instruct] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test AFAIK microsoft/Phi-3.5 is known t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Failure]: microsoft/Phi-3.5 model broken ci-failure ### Name of failing test entrypoints/openai/test_vision.py::test_single_chat_session_image_base64encoded_beamsearch[2-microsoft/Phi-3.5-vision-instruct] ### Basic info...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: microsoft/Phi-3.5 model broken ci-failure ### Name of failing test entrypoints/openai/test_vision.py::test_single_chat_session_image_base64encoded_beamsearch[2-microsoft/Phi-3.5-vision-instruct] ### Basic
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: penai/test_vision.py::test_single_chat_session_image_base64encoded_beamsearch[2-microsoft/Phi-3.5-vision-instruct] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

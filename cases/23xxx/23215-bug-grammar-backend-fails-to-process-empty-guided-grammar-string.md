# vllm-project/vllm#23215: [Bug]: Grammar backend fails to process empty `guided_grammar` string

| 字段 | 值 |
| --- | --- |
| Issue | [#23215](https://github.com/vllm-project/vllm/issues/23215) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Grammar backend fails to process empty `guided_grammar` string

### Issue 正文摘录

### Your current environment v0.10.1 / v0.10.2 ### 🐛 Describe the bug The grammar backend (`vllm/v1/structured_output/backend_xgrammar.py`) crashes when given an empty string (`""`) as `guided_grammar`. This results in a runtime error during compilation: ``` [2025-08-15T21:12:10Z] �[1;36m(EngineCore_0 pid=11496)�[0;0m File "/usr/local/lib/python3.12/dist-packages/vllm/v1/structured_output/__init__.py", line 132, in _async_create_grammar [2025-08-15T21:12:10Z] �[1;36m(EngineCore_0 pid=11496)�[0;0m return self.backend.compile_grammar(request_type, grammar_spec) [2025-08-15T21:12:10Z] �[1;36m(EngineCore_0 pid=11496)�[0;0m ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-08-15T21:12:10Z] �[1;36m(EngineCore_0 pid=11496)�[0;0m File "/usr/local/lib/python3.12/dist-packages/vllm/v1/structured_output/backend_xgrammar.py", line 99, in compile_grammar [2025-08-15T21:12:10Z] �[1;36m(EngineCore_0 pid=11496)�[0;0m ctx = self.compiler.compile_grammar(grammar_spec) [2025-08-15T21:12:10Z] �[1;36m(EngineCore_0 pid=11496)�[0;0m ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-08-15T21:12:10Z] �[1;36m(EngineCore_0 pid=11496)�[0;0m File "/usr/local/lib/python3.12/dist-packages/xgrammar/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 21:12:10Z] �[1;36m(EngineCore_0 pid=11496)�[0;0m return self.backend.compile_grammar(request_type, grammar_spec) [2025-08-15T21:12:10Z] �[1;36m(EngineCore_0 pid=11496)�[0;0m ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: Grammar backend fails to process empty `guided_grammar` string bug;stale ### Your current environment v0.10.1 / v0.10.2 ### 🐛 Describe the bug The grammar backend (`vllm/v1/structured_output/backend_xgrammar.py`)...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Grammar backend fails to process empty `guided_grammar` string bug;stale ### Your current environment v0.10.1 / v0.10.2 ### 🐛 Describe the bug The grammar backend (`vllm/v1/structured_output/backend_xgrammar.py`)...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: kely due to differences in random state), which is why the issue was not reproducible outside CI. * The issue is not criticial because empty grammar is not a regular use case. **Impact:** Causes server-side 500 errors a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 7). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

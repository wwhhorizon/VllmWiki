# vllm-project/vllm#29567: [Bug]: Arbitrary Code Execution via Unsafe cloudpickle.loads() in run_method()

| 字段 | 值 |
| --- | --- |
| Issue | [#29567](https://github.com/vllm-project/vllm/issues/29567) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Arbitrary Code Execution via Unsafe cloudpickle.loads() in run_method()

### Issue 正文摘录

### Your current environment / ### 🐛 Describe the bug # **[Security] Arbitrary Code Execution via Unsafe `cloudpickle.loads()` in `run_method()`** ## **Summary** The function `run_method()` in vLLM contains a critical security issue: it **directly deserializes attacker-controlled bytes using `cloudpickle.loads()`**, which can lead to **arbitrary code execution (RCE)**. Location: vllm-main\vllm\v1\serial_utils.py ```python if isinstance(method, bytes): func = partial(cloudpickle.loads(method), obj) ``` Because cloudpickle.loads() deserializes arbitrary Python objects—including objects with custom \_\_reduce\_\_() methods—this allows execution of attacker-controlled code if a malicious payload reaches this code path. This behavior is equivalent to executing arbitrary Python code. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _\_() methods—this allows execution of attacker-controlled code if a malicious payload reaches this code path. This behavior is equivalent to executing arbitrary Python code. ### Before submitting a new issue... - [x] M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: de. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

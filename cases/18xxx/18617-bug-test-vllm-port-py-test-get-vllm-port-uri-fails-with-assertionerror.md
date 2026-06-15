# vllm-project/vllm#18617: [Bug]: test_vllm_port.py::test_get_vllm_port_uri  fails with AssertionError: Regex pattern did not match

| 字段 | 值 |
| --- | --- |
| Issue | [#18617](https://github.com/vllm-project/vllm/issues/18617) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: test_vllm_port.py::test_get_vllm_port_uri  fails with AssertionError: Regex pattern did not match

### Issue 正文摘录

### Your current environment Issue seems to have been introduced in https://github.com/vllm-project/vllm/pull/18209 ### 🐛 Describe the bug Test fails with below traceback. ``` def test_get_vllm_port_uri(): """Test when VLLM_PORT is set to a URI.""" with (patch.dict(os.environ, {"VLLM_PORT": "tcp://localhost:5678"}, clear=True), > pytest.raises(ValueError, match="appears to be a URI")): E AssertionError: Regex pattern did not match. E Regex: 'appears to be a URI' E Input: "VLLM_PORT 'tcp://localhost:5678' must be a valid integer" tests/test_vllm_port.py:34: AssertionError ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: test_vllm_port.py::test_get_vllm_port_uri fails with AssertionError: Regex pattern did not match bug ### Your current environment Issue seems to have been introduced in https://github.com/vllm-project/vllm/pull/1...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

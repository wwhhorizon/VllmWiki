# vllm-project/vllm#13969: [Bug]:  Have the same bug with Issue #11762, using vllm>=0.7.2

| 字段 | 值 |
| --- | --- |
| Issue | [#13969](https://github.com/vllm-project/vllm/issues/13969) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Have the same bug with Issue #11762, using vllm>=0.7.2

### Issue 正文摘录

### Your current environment vllm = 0.7.2 or 0.7.3 ### 🐛 Describe the bug Exactly the same bug on Qwen2.5 VL with issue [#11732](https://github.com/vllm-project/vllm/issues/11762) ```python ERROR 02-27 18:50:20 engine.py:389] RuntimeError: Failed to apply Qwen2_5_VLProcessor on data={'text': ' ', 'images': [ , , , ], 'videos': [array([[[[0., 0., 0.], ERROR 02-27 18:50:20 engine.py:389] [0., 0., 0.], ERROR 02-27 18:50:20 engine.py:389] [0., 0., 0.], ERROR 02-27 18:50:20 engine.py:389] ..., ERROR 02-27 18:50:20 engine.py:389] [0., 0., 0.], ERROR 02-27 18:50:20 engine.py:389] [0., 0., 0.], ERROR 02-27 18:50:20 engine.py:389] [0., 0., 0.]], ERROR 02-27 18:50:20 engine.py:389] ERROR 02-27 18:50:20 engine.py:389] [[0., 0., 0.], ERROR 02-27 18:50:20 engine.py:389] [0., 0., 0.], ERROR 02-27 18:50:20 engine.py:389] [0., 0., 0.], ERROR 02-27 18:50:20 engine.py:389] ..., ERROR 02-27 18:50:20 engine.py:389] [0., 0., 0.], ERROR 02-27 18:50:20 engine.py:389] [0., 0., 0.], ERROR 02-27 18:50:20 engine.py:389] [0., 0., 0.]], ....... ``` The issue [#11732](https://github.com/vllm-project/vllm/issues/11762) has been closed, but I face the same problem with the latest vllm. Thank you. ### Before subm...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ou. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm = 0.7.2 or 0.7.3 ### 🐛 Describe the bug Exactly the same bug on Qwen2.5 VL with issue [#11732](https://github.com/vllm-project/vllm/issues/11762) ```python ERROR 02-27 18:50:20 engine.py:389] RuntimeError: Failed t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lm/issues/11762) has been closed, but I face the same problem with the latest vllm. Thank you. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

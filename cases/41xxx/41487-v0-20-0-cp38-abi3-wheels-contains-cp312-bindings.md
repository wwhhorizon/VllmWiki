# vllm-project/vllm#41487: [v0.20.0] cp38-abi3 wheels contains cp312 bindings

| 字段 | 值 |
| --- | --- |
| Issue | [#41487](https://github.com/vllm-project/vllm/issues/41487) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [v0.20.0] cp38-abi3 wheels contains cp312 bindings

### Issue 正文摘录

### Your current environment Version 0.20.0 PyPI wheels. ### 🐛 Describe the bug The pre-built wheel on PyPI is tagged `cp38-abi3` and contains ``` $ unzip -v vllm-0.20.0-cp38-abi3-manylinux_2_35_x86_64.whl | grep cpython 1352656 Defl:N 483912 64% 04-27-2026 07:59 cdda9112 vllm/third_party/deep_gemm/_C.cpython-312-x86_64-linux-gnu.so ``` which will break if one use python 3.8-3.11, 3.13-3.14 and deep-gemm. This wheel only correctly works (can be imported) for Python 3.12. Or that SO is mistagged and should be abi3? Alternatively, one can build from source with the desired cpython version. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [v0.20.0] cp38-abi3 wheels contains cp312 bindings bug ### Your current environment Version 0.20.0 PyPI wheels. ### 🐛 Describe the bug The pre-built wheel on PyPI is tagged `cp38-abi3` and contains ``` $ unzip -v vllm-0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 6 Defl:N 483912 64% 04-27-2026 07:59 cdda9112 vllm/third_party/deep_gemm/_C.cpython-312-x86_64-linux-gnu.so ``` which will break if one use python 3.8-3.11, 3.13-3.14 and deep-gemm. This wheel only correctly works (can...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

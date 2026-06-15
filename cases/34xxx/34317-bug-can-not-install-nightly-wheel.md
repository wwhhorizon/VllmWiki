# vllm-project/vllm#34317: [Bug]: can not install nightly wheel

| 字段 | 值 |
| --- | --- |
| Issue | [#34317](https://github.com/vllm-project/vllm/issues/34317) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: can not install nightly wheel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug error: Distribution `vllm==0.16.0rc2.dev87+g0b20469c6 @ registry+https://wheels.vllm.ai/nightly` can't be installed because it doesn't have a source distribution or wheel for the current platform hint: You're on Linux (`manylinux_2_31_x86_64`), but `vllm` (v0.16.0rc2.dev87+g0b20469c6) only has wheels for the following platform: `manylinux_2_31_aarch64`; consider adding "sys_platform == 'linux' and platform_machine == 'x86_64'" to `tool.uv.required-environments` to ensure uv resolves to a version with compatible wheels ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: can not install nightly wheel bug ### Your current environment ### 🐛 Describe the bug error: Distribution `vllm==0.16.0rc2.dev87+g0b20469c6 @ registry+https://wheels.vllm.ai/nightly` can't be installed because it...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g0b20469c6) only has wheels for the following platform: `manylinux_2_31_aarch64`; consider adding "sys_platform == 'linux' and platform_machine == 'x86_64'" to `tool.uv.required-environments` to ensure uv resolves to a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

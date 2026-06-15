# vllm-project/vllm#28150: [Bug]: -O.mode=NONE (or -cc.mode=NONE) should work

| 字段 | 值 |
| --- | --- |
| Issue | [#28150](https://github.com/vllm-project/vllm/issues/28150) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue;torch.compile |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: -O.mode=NONE (or -cc.mode=NONE) should work

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug Right now -O.mode only accepts integer levels. Ideally it would accept ints and the string. `vllm serve -O.mode=NONE` # doesn't work `vllm serve -O.mode=0` # does work ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: NE (or -cc.mode=NONE) should work bug;help wanted;good first issue;torch.compile ### Your current environment main ### 🐛 Describe the bug Right now -O.mode only accepts integer levels. Ideally it would accept ints and t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ork ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

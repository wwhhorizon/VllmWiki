# vllm-project/vllm#18538: [Usage]: unrecognized arguments: --enable-reasoning --reasoning-parser deepseek_r1

| 字段 | 值 |
| --- | --- |
| Issue | [#18538](https://github.com/vllm-project/vllm/issues/18538) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: unrecognized arguments: --enable-reasoning --reasoning-parser deepseek_r1

### Issue 正文摘录

### Your current environment Hello, when I run ``` vllm serve /xxx/hf_models/Qwen3-32B --port 8000 --enable-reasoning --reasoning-parser deepseek_r1 usage: vllm [-h] {serve,complete,chat} ... ``` it shows error： ``` vllm: error: unrecognized arguments: --enable-reasoning --reasoning-parser deepseek_r1 ``` my envs: vllm 0.8.5 Can you give some advises? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: age ### Your current environment Hello, when I run ``` vllm serve /xxx/hf_models/Qwen3-32B --port 8000 --enable-reasoning --reasoning-parser deepseek_r1 usage: vllm [-h] {serve,complete,chat} ... ``` it shows error： ```...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

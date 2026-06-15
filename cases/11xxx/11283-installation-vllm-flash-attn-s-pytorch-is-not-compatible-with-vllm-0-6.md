# vllm-project/vllm#11283: [Installation]: vllm-flash-attn's pytorch is not compatible with vllm 0.6.5's

| 字段 | 值 |
| --- | --- |
| Issue | [#11283](https://github.com/vllm-project/vllm/issues/11283) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: vllm-flash-attn's pytorch is not compatible with vllm 0.6.5's

### Issue 正文摘录

### Your current environment As the title, `vllm-flash-attn` pins `torch==2.4.0` but `vllm` 0.6.5 requires `torch==2.5.1`. ### How you are installing vllm ```sh $ uv pip install vllm==0.6.5 vllm-flash-attn × No solution found when resolving dependencies: ╰─▶ Because vllm==0.6.5 depends on torch{platform_machine != 'aarch64'}==2.5.1 and vllm-flash-attn>=2.6.1 depends on torch==2.4.0, we can conclude that vllm==0.6.5 and all of: vllm-flash-attn==2.6.1 vllm-flash-attn==2.6.2 are incompatible. (1) ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: vllm-flash-attn's pytorch is not compatible with vllm 0.6.5's installation ### Your current environment As the title, `vllm-flash-attn` pins `torch==2.4.0` but `vllm` 0.6.5 requires `torch==2.5.1`. ### H
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: encies: ╰─▶ Because vllm==0.6.5 depends on torch{platform_machine != 'aarch64'}==2.5.1 and vllm-flash-attn>=2.6.1 depends on torch==2.4.0, we can conclude that vllm==0.6.5 and all of: vllm-flash-attn==2.6.1 vllm-flash-a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

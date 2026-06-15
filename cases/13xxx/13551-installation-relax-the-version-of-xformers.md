# vllm-project/vllm#13551: [Installation]: Relax the version of `xformers`

| 字段 | 值 |
| --- | --- |
| Issue | [#13551](https://github.com/vllm-project/vllm/issues/13551) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Relax the version of `xformers`

### Issue 正文摘录

### Your current environment `xformers` supports `torch 2.5.1` from `0.0.28.post3` to `0.0.29.post1`. Some other packages uses a different version of `xformers` from the one constrained by `vllm`. Now `vllm` uses `0.0.28.post3`: https://github.com/vllm-project/vllm/blob/81dabf24a837ced3f4fc6131e8a7c99a63e646a5/requirements-cuda.txt#L10C13-L10C25. While `unsloth` uses `0.0.29.post1`: https://github.com/unslothai/unsloth/blob/d1d15f1d14f1168837d29b9c08e9b6d63945d469/pyproject.toml#L168-L177 ### How you are installing vllm Could you consider relaxing the version of `xformers`, like `xformers >= 0.0.28.post3, <=0.0.29.post1`? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: Relax the version of `xformers` installation ### Your current environment `xformers` supports `torch 2.5.1` from `0.0.28.post3` to `0.0.29.post1`. Some other packages uses a different version of `xformer
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -project/vllm/blob/81dabf24a837ced3f4fc6131e8a7c99a63e646a5/requirements-cuda.txt#L10C13-L10C25. While `unsloth` uses `0.0.29.post1`: https://github.com/unslothai/unsloth/blob/d1d15f1d14f1168837d29b9c08e9b6d63945d469/py...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: d3f4fc6131e8a7c99a63e646a5/requirements-cuda.txt#L10C13-L10C25. While `unsloth` uses `0.0.29.post1`: https://github.com/unslothai/unsloth/blob/d1d15f1d14f1168837d29b9c08e9b6d63945d469/pyproject.toml#L168-L177 ### How yo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

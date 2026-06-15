# vllm-project/vllm#27028: [Bug]: PostGradPassManager should not reference the compilation_config

| 字段 | 值 |
| --- | --- |
| Issue | [#27028](https://github.com/vllm-project/vllm/issues/27028) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: PostGradPassManager should not reference the compilation_config

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug Inductor configs need to be serializable and deepcopy-able, the PostGradPassManager is added to the Inductor config, and the CompilationConfig holds some nn.Modules. The Inductor config gets deepcopied sometimes, plus we have observed OOMs due to nn.Modules being in the PostGradPassManager. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: PostGradPassManager should not reference the compilation_config bug;torch.compile ### Your current environment main ### 🐛 Describe the bug Inductor configs need to be serializable and deepcopy-able, the PostGradP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ostGradPassManager should not reference the compilation_config bug;torch.compile ### Your current environment main ### 🐛 Describe the bug Inductor configs need to be serializable and deepcopy-able, the PostGradPassManag...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: es. The Inductor config gets deepcopied sometimes, plus we have observed OOMs due to nn.Modules being in the PostGradPassManager. ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: PostGradPassManager should not reference the compilation_config bug;torch.compile ### Your current environment main ### 🐛 Describe the bug Inductor configs need to be serializable and deepcopy-able, the PostGradP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#17068: [Bug]: CI Build image failure due to mamba-ssm==2.2.4 installation error

| 字段 | 值 |
| --- | --- |
| Issue | [#17068](https://github.com/vllm-project/vllm/issues/17068) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CI Build image failure due to mamba-ssm==2.2.4 installation error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are currently encountering errors during the build image step of all Buildkite CI pipelines, caused by a failure when installing and building `mamba-ssm==2.2.4`. The same issue occurs locally as well. Interestingly, the package installs successfully when using pip, but fails consistently with uv pip, which appears to be triggering a source build instead of using a prebuilt wheel. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: CI Build image failure due to mamba-ssm==2.2.4 installation error bug ### Your current environment ### 🐛 Describe the bug We are currently encountering errors during the build image step of all Buildkite CI pipel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CI Build image failure due to mamba-ssm==2.2.4 installation error bug ### Your current environment ### 🐛 Describe the bug We are currently encountering errors during the build image step of all Buildkite CI pipel...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ention_kv_cache;ci_build;distributed_parallel;frontend_api cuda;operator;triton build_error;crash;mismatch env_dependency;memory_layout Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: distributed_parallel;frontend_api cuda;operator;triton build_error;crash;mismatch env_dependency;memory_layout Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: pi cuda;operator;triton build_error;crash;mismatch env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

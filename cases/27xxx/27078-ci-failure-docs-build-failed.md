# vllm-project/vllm#27078: [CI Failure]: docs build failed

| 字段 | 值 |
| --- | --- |
| Issue | [#27078](https://github.com/vllm-project/vllm/issues/27078) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: docs build failed

### Issue 正文摘录

### Name of failing test docs/readthedocs.org:vllm — Read the Docs build failed! ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://app.readthedocs.org/api/v2/build/29977714.txt ``` INFO - Doc file 'README.md' contains an unrecognized relative link './usage', it was left as is. Did you mean 'usage/README.md'? INFO - Doc file 'README.md' contains an unrecognized relative link './contributing', it was left as is. Did you mean 'contributing/README.md'? INFO - Doc file 'features/spec_decode.md' contains an unrecognized relative link '../../tests/spec_decode/e2e', it was left as is. WARNING - Doc file 'models/supported_models.md' contains a link '../../vllm/model_executor/models/transformers.py', but the target '../vllm/model_executor/models/transformers.py' is not found among documentation files. INFO - Doc file 'usage/README.md' contains an unrecognized relative link '../getting_started/installation/', it was left as is. Did you mean '../getting_started/installation/README.md'? INFO - Doc file 'configuration/serve_args.md' contains a link '../cli/README.md#options',...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: docs build failed ci-failure ### Name of failing test docs/readthedocs.org:vllm — Read the Docs build failed! ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external li
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: E.md' does not contain an anchor '#options'. INFO - Doc file 'design/arch_overview.md' contains a link '#offline-inference-api', but there is no such anchor on this page. INFO - Doc file 'getting_started/installation/RE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: st docs/readthedocs.org:vllm — Read the Docs build failed! ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: he Docs build failed! ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://app.readthedocs.org/api/v2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: id you mean 'contributing/README.md'? INFO - Doc file 'features/spec_decode.md' contains an unrecognized relative link '../../tests/spec_decode/e2e', it was left as is. WARNING - Doc file 'models/supported_models.md' co...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

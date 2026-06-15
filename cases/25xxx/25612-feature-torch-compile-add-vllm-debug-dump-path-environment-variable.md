# vllm-project/vllm#25612: [Feature][torch.compile]: Add `VLLM_DEBUG_DUMP_PATH` environment variable

| 字段 | 值 |
| --- | --- |
| Issue | [#25612](https://github.com/vllm-project/vllm/issues/25612) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][torch.compile]: Add `VLLM_DEBUG_DUMP_PATH` environment variable

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, to debug compilation and pattern matching, we often use `CompilationConfig.debug_dump_path` to dump fx graphs at every stage of compilation. Since #24542, we also dump pattern matching patterns there. If debugging unit tests, the developer has to manually edit the compilation config to add `debug_dump_path`. Instead, we should add an environment variable that overrides the config-specified path. Debugging/logging/dumping switches should generally be environment variables, so that users can debug their deployment even if they don't have access to the runtime command or are running a script. This override should happen in `VllmConfig.__post_init__`. `debug_dump_path` will stick around and its users will be unaffected. Additionally, rank should be appended to the `debug_dump_path` at the same spot so that users should use it directly, and its type should be `pathlib.Path`. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature][torch.compile]: Add `VLLM_DEBUG_DUMP_PATH` environment variable feature request ### 🚀 The feature, motivation and pitch Currently, to debug compilation and pattern matching, we often use `CompilationConfig.deb...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tly, to debug compilation and pattern matching, we often use `CompilationConfig.debug_dump_path` to dump fx graphs at every stage of compilation. Since #24542, we also dump pattern matching patterns there. If debugging...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [torch.compile]: Add `VLLM_DEBUG_DUMP_PATH` environment variable feature request ### 🚀 The feature, motivation and pitch Currently, to debug compilation and pattern matching, we often use `CompilationConfig.debug_dump_p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: #24542, we also dump pattern matching patterns there. If debugging unit tests, the developer has to manually edit the compilation config to add `debug_dump_path`. Instead, we should add an environment variable that over...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

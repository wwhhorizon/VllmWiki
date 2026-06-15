# vllm-project/vllm#30859: [Bug]: set_current_vllm_config() is only done during the initialization stage but not the runtime stage

| 字段 | 值 |
| --- | --- |
| Issue | [#30859](https://github.com/vllm-project/vllm/issues/30859) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: set_current_vllm_config() is only done during the initialization stage but not the runtime stage

### Issue 正文摘录

### Your current environment Any env ### 🐛 Describe the bug # Issue Statement Currently, `set_current_vllm_config()` is only done during the initialization stage but not the runtime stage. If the code tries to call `get_current_vllm_config()`, vLLM prints a warning "Current vLLM config is not set." and returns a default config. However, this approach is problematic because: 1. When contributors change the code, many of us did not realize the fact that `get_current_vllm_config()` should only be called during init stage and should not be called during runtime stage. 2. It's just a warning instead of a hard failure, so contributors may not notice this when they run local tests. 3. Such warnings could be annoying to users because it may be printed for every single decoding step. Plus, the warning doesn't carry any useful info about how to fix/bypass the issue. 4. The default config may be completely incorrect for the caller function. 5. Warning prints on every step might impact performance, because print isn't fast operation. (thanks to @vadiklyutiy ) # Requirements We should change the behavior such that: - `get_current_vllm_config()` either returns the real config set by the user or...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: m_config()` to a hard failure But this means we may need to fix lots of CI failures. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bot...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: set_current_vllm_config() is only done during the initialization stage but not the runtime stage bug ### Your current environment Any env ### 🐛 Describe the bug # Issue Statement Currently, `set_current_vllm_conf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: a hard failure, so contributors may not notice this when they run local tests. 3. Such warnings could be annoying to users because it may be printed for every single decoding step. Plus, the warning doesn't carry any us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

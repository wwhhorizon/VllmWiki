# vllm-project/vllm#37966: [Bug]: spec decoding nonparallel 路径 draft/target hidden size 不兼容，建议适配不同hidden size

| 字段 | 值 |
| --- | --- |
| Issue | [#37966](https://github.com/vllm-project/vllm/issues/37966) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: spec decoding nonparallel 路径 draft/target hidden size 不兼容，建议适配不同hidden size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - 使用 Qwen3-0.6B 作为 draft，Qwen3-1.7B或Qwen3-8B 作为 target，nonparallel draft 路径 - 服务能够启动，/health 和 /v1/models 接口正常，但首条 /v1/chat/completions 请求立即崩溃，报错见下： - 崩溃原因位于 vllm_ascend/spec_decode/eagle_proposer.py 的 hidden state 直拷操作：`self.hidden_states[:num_tokens] = target_hidden_states`，报 1024 vs 2048 错误（具体见日志 benchmark_test/qwen17b-qwen06b-nonparallel-serve-dev6.log） **分析与讨论：** - 现实现假设 draft/target hidden size 相等，实际上不同的 Qwen3 规模（如 0.6B/1.7B/8B）对应 hidden size 不一致，因此无法兼容 - 跟踪 vllm/vllm/v1/spec_decode/eagle.py 源码，`self.hidden_states` 缓冲区是按 draft hidden size 分配，而 nonparallel 路径里直接把 target hidden states 拷贝进 draft 缓冲区，导致 shape mismatch - 算法上这两者并不要求 shape 必须一致，只是当前实现偷懒强绑定了维度 - 合理做法应包括：引入 projection 映射、恢复 mtp_proposer 兼容路径，或改为传递其他 draft 可消费的条件表达 **预期行为：** - 支持 draft/target hidden size 不一致的 nonparallel draft 路径，提升大/小模型搭配推理兼容性 **建议修改方向：** - 在 draft hidden size ≠ target hidden size 时，增加桥接层（如 projection），或设计适配接口 - 或提供清晰的报错/文档说明当前实现的 shape 要求，提示用户限制 **相关文件与定位：** - vllm_ascend/spec_decode/eagle_proposer.py - vllm/vllm/v1/spec_decode/eagle.py - 详细日志见 benchmark_test/qwen17b-qwen06b-nonparallel-serve-dev6.log 🐛 该问题导致 spec decoding nonparallel 路径下，不同 hidden...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n size bug ### Your current environment ### 🐛 Describe the bug - 使用 Qwen3-0.6B 作为 draft，Qwen3-1.7B或Qwen3-8B 作为 target，nonparallel draft 路径 - 服务能够启动，/health 和 /v1/models 接口正常，但首条 /v1/chat/completions 请求立即崩溃，报错见下： - 崩溃原因位...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ze 分配，而 nonparallel 路径里直接把 target hidden states 拷贝进 draft 缓冲区，导致 shape mismatch - 算法上这两者并不要求 shape 必须一致，只是当前实现偷懒强绑定了维度 - 合理做法应包括：引入 projection 映射、恢复 mtp_proposer 兼容路径，或改为传递其他 draft 可消费的条件表达 **预期行为：** - 支持 draft/target h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: spec decoding nonparallel 路径 draft/target hidden size 不兼容，建议适配不同hidden size bug ### Your current environment ### 🐛 Describe the bug - 使用 Qwen3-0.6B 作为 draft，Qwen3-1.7B或Qwen3-8B 作为 target，nonparallel draft 路径 - 服务...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: dden_states[:num_tokens] = target_hidden_states`，报 1024 vs 2048 错误（具体见日志 benchmark_test/qwen17b-qwen06b-nonparallel-serve-dev6.log） **分析与讨论：** - 现实现假设 draft/target hidden size 相等，实际上不同的 Qwen3 规模（如 0.6B/1.7B/8B）对应 hidden...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: size 分配，而 nonparallel 路径里直接把 target hidden states 拷贝进 draft 缓冲区，导致 shape mismatch - 算法上这两者并不要求 shape 必须一致，只是当前实现偷懒强绑定了维度 - 合理做法应包括：引入 projection 映射、恢复 mtp_proposer 兼容路径，或改为传递其他 draft 可消费的条件表达 **预期行为：** - 支持 draft/target...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

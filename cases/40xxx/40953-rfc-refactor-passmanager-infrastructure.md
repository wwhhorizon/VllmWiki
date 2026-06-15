# vllm-project/vllm#40953: [RFC]: Refactor PassManager infrastructure

| 字段 | 值 |
| --- | --- |
| Issue | [#40953](https://github.com/vllm-project/vllm/issues/40953) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Refactor PassManager infrastructure

### Issue 正文摘录

### Motivation. This RFC is to slove https://github.com/vllm-project/vllm/issues/39356. Currently, all custom `torch.compile` passes in vLLM are managed by a single `PostGradPassManager`. Passes are registered by mounting them onto the Inductor hook identified by `current_platform.pass_key`, and each pass is individually enabled or disabled through boolean fields in `PassConfig`. This pattern has several problems: ### 1. Inflexible Configuration Interface Every new pass requires a new boolean field in `PassConfig`. When debugging and you only want to enable one pass, you must explicitly disable all others on the CLI. Some utility passes have no independent flag at all, so users cannot temporarily disable or adjust them without modifying source code. ### 2. Difficult OOT Platform Extension For vLLM-Spyre, vLLM forcibly absorbs external passes into `PostGradPassManager` via an `absorb` hack in `configure_post_pass`. OOT backends that define their own `PassManager` must re-implement shared infrastructure such as pass execution ordering and cache hash computation from scratch. ### 3. Non-switchable Hook Points `current_platform.pass_key` is hardcoded to `"post_grad_custom_post_pass"`,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: /github.com/vllm-project/vllm/issues/39356. Currently, all custom `torch.compile` passes in vLLM are managed by a single `PostGradPassManager`. Passes are registered by mounting them onto the Inductor hook identified by...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Refactor PassManager infrastructure RFC ### Motivation. This RFC is to slove https://github.com/vllm-project/vllm/issues/39356. Currently, all custom `torch.compile` passes in vLLM are managed by a single `PostGr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: owering logic from being moved into a standalone `vllm/ir/` sub-package, blocking IR modularization. ### Proposed Change. - **Flexible configuration**: provide an explicitly configurable pass pipeline that supports enab...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: `PostGradPassManager` via an `absorb` hack in `configure_post_pass`. OOT backends that define their own `PassManager` must re-implement shared infrastructure such as pass execution ordering and cache hash computation fr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: lf, set())) @config class PostGradPassConfig(PassConfig): fuse_norm_quant: bool = None fuse_act_quant: bool = None fuse_allreduce_rms: bool = None # ... ``` note: should define `get_pass_config_cls` in Platform interfac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

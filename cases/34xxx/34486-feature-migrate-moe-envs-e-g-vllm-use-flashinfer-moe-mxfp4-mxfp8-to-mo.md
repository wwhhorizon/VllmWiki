# vllm-project/vllm#34486: [Feature]: Migrate MoE envs(e.g. `VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8`) to model flags

| 字段 | 值 |
| --- | --- |
| Issue | [#34486](https://github.com/vllm-project/vllm/issues/34486) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Migrate MoE envs(e.g. `VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8`) to model flags

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We would like to migrate the MoE envs to model flags. Here are some possible designs, using `VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8` as an example: Option 1: Individual boolean flags under `KernelConfig` --- This is a 1:1 migration. Each env var becomes a KernelConfig field exposed as its own CLI flag: ``` vllm serve model --use-flashinfer-moe-mxfp4-mxfp8 ... ``` Or equivalently via the JSON config: ``` vllm serve model --kernel-config '{"use_flashinfer_moe_mxfp4_mxfp8": true}' ... ``` Option 2: Extend `--quantization` with backend-aware values --- Instead of separate boolean flags, express the MoE kernel choice as a quantization variant: ``` vllm serve model --quantization mxfp4_mxfp8_act ... ``` cc @ProExpertProg @nvpohanh ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: Migrate MoE envs(e.g. `VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8`) to model flags feature request;stale ### 🚀 The feature, motivation and pitch We would like to migrate the MoE envs to model flags. Here are some po...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Migrate MoE envs(e.g. `VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8`) to model flags feature request;stale ### 🚀 The feature, motivation and pitch We would like to migrate the MoE envs to model flags. Here are some po...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eature]: Migrate MoE envs(e.g. `VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8`) to model flags feature request;stale ### 🚀 The feature, motivation and pitch We would like to migrate the MoE envs to model flags. Here are some poss...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Migrate MoE envs(e.g. `VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8`) to model flags feature request;stale ### 🚀 The feature, motivation and pitch We would like to migrate the MoE envs to model flags. Here are some po...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: envs(e.g. `VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8`) to model flags feature request;stale ### 🚀 The feature, motivation and pitch We would like to migrate the MoE envs to model flags. Here are some possible designs, using `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

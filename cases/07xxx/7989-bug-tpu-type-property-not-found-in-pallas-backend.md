# vllm-project/vllm#7989: [Bug]: TPU 'TYPE' property not found in Pallas backend

| 字段 | 值 |
| --- | --- |
| Issue | [#7989](https://github.com/vllm-project/vllm/issues/7989) |
| 状态 | closed |
| 标签 | bug;tpu |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TPU 'TYPE' property not found in Pallas backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was trying to deploy VLLM on GKE Autopilot with v5e accelerators. However the Pallas backend seems to wrongly query the accelerator TYPE. By changing line line 126 (v0.5.5) to the following resolves this issue (file attention/backends/pallas.py): ```python tpu_env = torch_xla.tpu.get_tpu_env() tpu_type = (tpu_env["TYPE"] if "TYPE" in tpu_env else tpu_env["ACCELERATOR_TYPE"]).lower() ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;triton build_error;nan_inf env_depen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: TPU 'TYPE' property not found in Pallas backend bug;tpu ### Your current environment ### 🐛 Describe the bug I was trying to deploy VLLM on GKE Autopilot with v5e accelerators. However the Pallas backend seems to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .get_tpu_env() tpu_type = (tpu_env["TYPE"] if "TYPE" in tpu_env else tpu_env["ACCELERATOR_TYPE"]).lower() ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sked questions. correctness attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

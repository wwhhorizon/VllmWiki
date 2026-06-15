# vllm-project/vllm#24291: [Bug]: ARM V1 version dependency on OneDNN

| 字段 | 值 |
| --- | --- |
| Issue | [#24291](https://github.com/vllm-project/vllm/issues/24291) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ARM V1 version dependency on OneDNN

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM on ARM in CPU mode does not support V1 mode, both single region and piecewise due to a dependency on OneDNN. Followed the steps to build sources on ARM and test. There is an issue for MacOS (https://github.com/vllm-project/vllm/issues/19645), but not for Linux ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: ARM V1 version dependency on OneDNN bug ### Your current environment ### 🐛 Describe the bug vLLM on ARM in CPU mode does not support V1 mode, both single region and piecewise due to a dependency on OneDNN. Follow...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nux ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: g_logits;speculative_decoding cuda;operator;sampling build_error;nan_inf dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ots of frequently asked questions. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling build_error;nan_inf dtype;env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ons. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

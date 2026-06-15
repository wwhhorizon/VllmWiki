# vllm-project/vllm#7512: [Bug] : ROCM quantization check fail in version 0.5.4 for GPTQ and AWQ 

| 字段 | 值 |
| --- | --- |
| Issue | [#7512](https://github.com/vllm-project/vllm/issues/7512) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] : ROCM quantization check fail in version 0.5.4 for GPTQ and AWQ 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [`model_is_embedding` ](https://github.com/vllm-project/vllm/blob/d3d9cb6e4b8185b4e56e1dda92c6fc31cdc05de1/vllm/entrypoints/openai/api_server.py#L100) is introduced in version 0.5.4, but missing quantization parameter. This may cause the following quantization check failures when performing model inference on ROCm GPU using GPTQ or AWQ quantization methods.

## 现有链接修复摘要

#7513 [Bugfix][Hardware][AMD][Frontend] add quantization param to embedding checking method

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug] : ROCM quantization check fail in version 0.5.4 for GPTQ and AWQ bug;rocm ### Your current environment ### 🐛 Describe the bug [`model_is_embedding` ](https://github.com/vllm-project/vllm/blob/d3d9cb6e4b8185b4e56e1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug] : ROCM quantization check fail in version 0.5.4 for GPTQ and AWQ bug;rocm ### Your current environment ### 🐛 Describe the bug [`model_is_embedding` ](https://github.com/vllm-project/vllm/blob/d3d9cb6e4b8185b4e56e1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency #7513 [Bugfix][Hardware][AMD][Frontend] add quantization param to embedding checking method Your current...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug] : ROCM quantization check fail in version 0.5.4 for GPTQ and AWQ bug;rocm ### Your current environment ### 🐛 Describe the bug [`model_is_embedding` ](https://github.com/vllm-project/vllm/blob/d3d9cb6e4b8185b4e56e1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: AWQ bug;rocm ### Your current environment ### 🐛 Describe the bug [`model_is_embedding` ](https://github.com/vllm-project/vllm/blob/d3d9cb6e4b8185b4e56e1dda92c6fc31cdc05de1/vllm/entrypoints/openai/api_server.py#L100) is...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7513](https://github.com/vllm-project/vllm/pull/7513) | closes_keyword | 0.95 | [Bugfix][Hardware][AMD][Frontend] add quantization param to embedding checking method | FIX #7512 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

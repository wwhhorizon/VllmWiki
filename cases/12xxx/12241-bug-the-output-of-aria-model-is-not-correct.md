# vllm-project/vllm#12241: [Bug]: The output of Aria model is not correct

| 字段 | 值 |
| --- | --- |
| Issue | [#12241](https://github.com/vllm-project/vllm/issues/12241) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The output of Aria model is not correct

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The issue was observed in the comment posted by @DarkLight1337 https://github.com/vllm-project/vllm/pull/12207#issuecomment-2601802654. I've tested the output of different versions of vllm and transformers and have some observations: 1. The output becomes nonsensical after #12203 ``` CEÕ̃ Ã...’ CEOÃ ÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃ...’...’...’...’ tomorrow tomorrow tomorrow tomorrow CEO tomorrow CEO tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow tomorrow t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /pull/12207#issuecomment-2601802654. I've tested the output of different versions of vllm and transformers and have some observations: 1. The output becomes nonsensical after #12203 ``` CEÕ̃ Ã...’ CEOÃ ÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: a beautiful and serene atmosphere to the scene. The contrast between the architectural element and the natural elements creates a visually striking and harmonious composition. The image captures the essence of a peacefu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The output of Aria model is not correct bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The issue was observed in the comment posted by @DarkLight1337 https://github.co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown dtype;env_dependency;shape Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: tive_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

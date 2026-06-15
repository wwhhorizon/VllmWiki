# vllm-project/vllm#27542: [Bug]: vllm 0.11.1 rc4 (triton on sm120a RTX6000)

| 字段 | 值 |
| --- | --- |
| Issue | [#27542](https://github.com/vllm-project/vllm/issues/27542) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.11.1 rc4 (triton on sm120a RTX6000)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Since 0.11.1 RC4 vllm will use triton instead of marlin for RTX6000 and probably other RTX cards on sm120a. That would be Amazing, but the issue is that it doesnt work with models like gpt-oss-120B. gather4 doesnt work on that cards, maybe completely mxfp4 (im not sure) However, RC3 worked without issues, since that used the Marlin kernel for sm120a. Since RC4 this issue happens: It would be amazing if we could fix the triton Kernel, since it would give a lot more performance probably. But since i don't know how, i would suggest disabling the triton kernel for sm120a in the meantime. Cheers ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: vllm 0.11.1 rc4 (triton on sm120a RTX6000) bug ### Your current environment ### 🐛 Describe the bug Since 0.11.1 RC4 vllm will use triton instead of marlin for RTX6000 and probably other RTX cards on sm120a. That...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization cuda;kernel;moe;operator;quantization;triton build_error;crash env_d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: s like gpt-oss-120B. gather4 doesnt work on that cards, maybe completely mxfp4 (im not sure) However, RC3 worked without issues, since that used the Marlin kernel for sm120a. Since RC4 this issue happens: It would be am...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m120a. That would be Amazing, but the issue is that it doesnt work with models like gpt-oss-120B. gather4 doesnt work on that cards, maybe completely mxfp4 (im not sure) However, RC3 worked without issues, since that us...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: vllm 0.11.1 rc4 (triton on sm120a RTX6000) bug ### Your current environment ### 🐛 Describe the bug Since 0.11.1 RC4 vllm will use triton instead of marlin for RTX6000 and probably other RTX cards on sm120a. That...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

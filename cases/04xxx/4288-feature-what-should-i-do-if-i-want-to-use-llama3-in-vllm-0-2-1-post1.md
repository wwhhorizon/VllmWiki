# vllm-project/vllm#4288: [Feature]: What should I do if I want to use llama3 in vllm-0.2.1.post1?

| 字段 | 值 |
| --- | --- |
| Issue | [#4288](https://github.com/vllm-project/vllm/issues/4288) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: What should I do if I want to use llama3 in vllm-0.2.1.post1?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have a lower cuda (11.7), so I can not install latest version vllm successfully, can you tell me how to change the code in vllm-0.2.1.post1 or add llama3 in past version? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: feature, motivation and pitch I have a lower cuda (11.7), so I can not install latest version vllm successfully, can you tell me how to change the code in vllm-0.2.1.post1 or add llama3 in past version? ### Alternatives...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: feature request ### 🚀 The feature, motivation and pitch I have a lower cuda (11.7), so I can not install latest version vllm successfully, can you tell me how to change the code in vllm-0.2.1.post1 or add llama3 in past...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: What should I do if I want to use llama3 in vllm-0.2.1.post1? feature request ### 🚀 The feature, motivation and pitch I have a lower cuda (11.7), so I can not install latest version vllm successfully, can you...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: What should I do if I want to use llama3 in vllm-0.2.1.post1? feature request ### 🚀 The feature, motivation and pitch I have a lower cuda (11.7), so I can not install latest version vllm successfully, can you tell me...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: motivation and pitch I have a lower cuda (11.7), so I can not install latest version vllm successfully, can you tell me how to change the code in vllm-0.2.1.post1 or add llama3 in past version? ### Alternatives _No resp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

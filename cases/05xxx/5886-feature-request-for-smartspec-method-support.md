# vllm-project/vllm#5886: [Feature]: Request for SmartSpec Method Support

| 字段 | 值 |
| --- | --- |
| Issue | [#5886](https://github.com/vllm-project/vllm/issues/5886) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Request for SmartSpec Method Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Recently, we read a paper where the vLLM team proposed a method called **SmartSpec**. We believe that the research, which dynamically adjusts the speculation length in a commercialized LLM serving system, is superior in terms of practicality compared to existing dynamic speculative length studies. - [Optimizing Speculative Decoding for Serving Large Language Models Using Goodput](https://arxiv.org/pdf/2406.14066v1) This idea could be applied to the current vLLM speculative decoding with Batch Expansion enabled, and it might also be applicable to future versions of vLLM with Batch Expansion disabled. (I am curious whether the SmartSpec research was conducted on vLLM with Batch Expansion enabled. :thinking:) **I wonder if the SmartSpec method will be implemented into the main repository in the near future.** ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: he research, which dynamically adjusts the speculation length in a commercialized LLM serving system, is superior in terms of practicality compared to existing dynamic speculative length studies. - [Optimizing Speculati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Request for SmartSpec Method Support feature request ### 🚀 The feature, motivation and pitch Recently, we read a paper where the vLLM team proposed a method called **SmartSpec**. We believe that the research,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Request for SmartSpec Method Support feature request ### 🚀 The feature, motivation and pitch Recently, we read a paper where the vLLM team proposed a method called **SmartSpec**. We believe that the research,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: h studies. - [Optimizing Speculative Decoding for Serving Large Language Models Using Goodput](https://arxiv.org/pdf/2406.14066v1) This idea could be applied to the current vLLM speculative decoding with Batch Expansion...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

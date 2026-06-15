# vllm-project/vllm#1853: Speed between gptq w4a16 and awq w4a16?

| 字段 | 值 |
| --- | --- |
| Issue | [#1853](https://github.com/vllm-project/vllm/issues/1853) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Speed between gptq w4a16 and awq w4a16?

### Issue 正文摘录

Hi, I am wondering the implementation of gptq w4a16(exllama) and awq w4a16(llm-awq), which is faster? It seems the mathematical computation is similar between the two, so can these two share the same copy of cuda function? Hoping for your reply, thank you

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ame copy of cuda function? Hoping for your reply, thank you performance quantization cuda;quantization Hi, I am wondering the implementation of gptq w4a16(exllama) and awq w4a16(llm-awq), which is faster?
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tion is similar between the two, so can these two share the same copy of cuda function? Hoping for your reply, thank you performance quantization cuda;quantization Hi, I am wondering the implementation of gptq w4a16(exl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: a16 and awq w4a16? Hi, I am wondering the implementation of gptq w4a16(exllama) and awq w4a16(llm-awq), which is faster? It seems the mathematical computation is similar between the two, so can these two share the same...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#5066: [Feature]: Integration of transformers past_key_values into the vllm kvcache Function

| 字段 | 值 |
| --- | --- |
| Issue | [#5066](https://github.com/vllm-project/vllm/issues/5066) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integration of transformers past_key_values into the vllm kvcache Function

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Background:** The past_key_values parameter in the transformers library is integral for maintaining state information when processing sequential data. However, within our vllm project, we utilize a kvcache mechanism. To enhance model performance and state management, we aim to integrate the transformers past_key_values with the vllm kvcache. **Feature Description:** We propose the development of a conversion function that will transform the transformers past_key_values into a format compatible with the vllm kvcache. This function will enable us to initialize the vllm kvcache with a non-empty tensor tuple list, thereby increasing the model's flexibility and performance. **Specific Requirements:** 1. Conversion Function Design: Develop a function that accepts past_key_values as input and converts it into a format that the vllm kvcache can utilize. 2. Compatibility Consideration: Ensure that the converted kvcache integrates seamlessly with the existing architecture and features of vllm. 3. Performance Optimization: The conversion process should be as efficient as possible to avoid unnecessary performance overhead during model execution. 4. Do...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: lm kvcache. **Feature Description:** We propose the development of a conversion function that will transform the transformers past_key_values into a format compatible with the vllm kvcache. This function will enable us...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tial data. However, within our vllm project, we utilize a kvcache mechanism. To enhance model performance and state management, we aim to integrate the transformers past_key_values with the vllm kvcache. **Feature Descr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: arameter in the transformers library is integral for maintaining state information when processing sequential data. However, within our vllm project, we utilize a kvcache mechanism. To enhance model performance and stat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n of transformers past_key_values into the vllm kvcache Function feature request ### 🚀 The feature, motivation and pitch **Background:** The past_key_values parameter in the transformers library is integral for maintain...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

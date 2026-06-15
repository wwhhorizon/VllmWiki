# vllm-project/vllm#15625: DeciLMConfig object has no attribute ‘num_key_value_heads_per_layer’ 

| 字段 | 值 |
| --- | --- |
| Issue | [#15625](https://github.com/vllm-project/vllm/issues/15625) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> DeciLMConfig object has no attribute ‘num_key_value_heads_per_layer’ 

### Issue 正文摘录

### Your current environment VLLM version: 0.7.3 Model: nvidia/Llama-3_3-Nemotron-Super-49B-v1 ### 🐛 Describe the bug I am trying to run the new Nvidia model Nemotron 49B-v1 using the VLLM 0.7.3 version but I got this error DeciLMConfig object has no attribute ‘num_key_value_heads_per_layer’ I have two questions: I know there are PR such as https://github.com/vllm-project/vllm/issues/15068 https://github.com/vllm-project/vllm/pull/15008 I am wondering about if the error would be resolved after adding the support for the model. Or the error is unrelated and something is wrong in my end?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: DeciLMConfig object has no attribute ‘num_key_value_heads_per_layer’ bug;stale ### Your current environment VLLM version: 0.7.3 Model: nvidia/Llama-3_3-Nemotron-Super-49B-v1 ### 🐛 Describe the bug I am trying to run the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: DeciLMConfig object has no attribute ‘num_key_value_heads_per_layer’ bug;stale ### Your current environment VLLM version: 0.7.3 Model: nvidia/Llama-3_3-Nemotron-Super-49B-v1 ### 🐛 Describe the bug I am trying to run th
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eciLMConfig object has no attribute ‘num_key_value_heads_per_layer’ bug;stale ### Your current environment VLLM version: 0.7.3 Model: nvidia/Llama-3_3-Nemotron-Super-49B-v1 ### 🐛 Describe the bug I am trying to run the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

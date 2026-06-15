# vllm-project/vllm#9313: [Bug]: different generation result when changing parameters using `copy_` and `=` method

| 字段 | 值 |
| --- | --- |
| Issue | [#9313](https://github.com/vllm-project/vllm/issues/9313) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: different generation result when changing parameters using `copy_` and `=` method

### Issue 正文摘录

### Your current environment ### Model Input Dumps ``` for k, v in llm.llm_engine.model_executor.driver_worker.model_runner.model.named_parameters(): v.data.copy_(state_dict[k ]) outputs1 = llm.generate(prompts, sampling_params) v.data = state_dict[k ] # k is final_layernorm.weight outputs2 = llm.generate(prompts, sampling_params) ``` outputs1 is ok and outputs is messy，but the parameter value are the same. Why `v.data.copy_(state_dict[k ]) ` and `v.data = state_dict[k ]` would lead to different generation result? ### 🐛 Describe the bug ``` for k, v in llm.llm_engine.model_executor.driver_worker.model_runner.model.named_parameters(): v.data.copy_(state_dict[k ]) outputs1 = llm.generate(prompts, sampling_params) v.data = state_dict[k ] # k is final_layernorm.weight outputs2 = llm.generate(prompts, sampling_params) ``` outputs1 is ok and outputs is2 messy，but the parameter value are same. Why `v.data.copy_(state_dict[k ]) ` and `v.data = state_dict[k ]` would lead to different generation result? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://doc...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lt? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rs using `copy_` and `=` method bug ### Your current environment ### Model Input Dumps ``` for k, v in llm.llm_engine.model_executor.driver_worker.model_runner.model.named_parameters(): v.data.copy_(state_dict[k ]) outp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

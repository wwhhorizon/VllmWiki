# vllm-project/vllm#14341: [Bug]: online-rl sampling is different from offline-sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#14341](https://github.com/vllm-project/vllm/issues/14341) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: online-rl sampling is different from offline-sampling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to run ppo/reinforce++ using openrlhf. The dataset and reward-func is same to https://github.com/Open-Reasoner-Zero/Open-Reasoner-Zero/ However, when i tried to filter data before training, I use the exact the same ENV and sampling-params, the accuracy and format-accuracy is different from the first step of online-sampling. Since the first step of online-sampling should be identical to offline-sampling, the format-accuracy should be similar. However, there exists a huge gap. The sampling-params: ``` sampling_params = SamplingParams(temperature=1.0, top_p=1.0, top_k=-1, max_tokens=16000+4096, min_tokens=1, stop=[tokenizer.eos_token, "User:", "Human:", "Assistant:", " "], skip_special_tokens=False, include_stop_str_in_output=True, n=1) ``` online-sampling while offline-sampling, the format-rewards is nearly 15%, while online-sampling is 57%. ``` When I remove from the stop-token, online-sampling of the first step is similar to offline-sampling. It's so odd. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docume...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t ### 🐛 Describe the bug I tried to run ppo/reinforce++ using openrlhf. The dataset and reward-func is same to https://github.com/Open-Reasoner-Zero/Open-Reasoner-Zero/ However, when i tried to filter data before traini...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: a before training, I use the exact the same ENV and sampling-params, the accuracy and format-accuracy is different from the first step of online-sampling. Since the first step of online-sampling should be identical to o...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: a before training, I use the exact the same ENV and sampling-params, the accuracy and format-accuracy is different from the first step of online-sampling. Since the first step of online-sampling should be identical to o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , "Human:", "Assistant:", " "], skip_special_tokens=False, include_stop_str_in_output=True, n=1) ``` online-sampling while offline-sampling, the format-rewards is nearly 15%, while online-sampl
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

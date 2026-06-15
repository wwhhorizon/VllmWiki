# vllm-project/vllm#15025: [Bug]: Speculative decoding with a draft model makes generation slower

| 字段 | 值 |
| --- | --- |
| Issue | [#15025](https://github.com/vllm-project/vllm/issues/15025) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | sampling |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative decoding with a draft model makes generation slower

### Issue 正文摘录

### Your current environment I tried several vLLM versions (0.6.2 and latest 0.7.3) and have consistent speed drop when using speculative decoding with draft model. Tried on L4 and T4 GPU in Colab. ### 🐛 Describe the bug Main model - `1.7B,` speculative model - `135M` parameters (`SmolLMv2` family of models) I trained the small model using logits distillation of main model, so it has a good level of generation (acceptance rate is very high) Still I get consistent performance drop ~30% in terms of speed when using 5 speculative tokens, when I reduce number speculative tokens - speed increases, but the best speed in achieved when using main model only without speculative. Here are my parameters: ```python llm = LLM( model=MODEL_PATH, speculative_model=SPECULATIVE_MODEL_PATH, max_model_len=2500, num_speculative_tokens=5, gpu_memory_utilization=0.9 ) sampling_params = SamplingParams( temperature=0, top_k=1, max_tokens=256, ) outputs = llm.generate(prompts, sampling_params) ``` Is it expected? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vll...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Speculative decoding with a draft model makes generation slower bug;stale ### Your current environment I tried several vLLM versions (0.6.2 and latest 0.7.3) and have consistent speed drop when using speculative...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tion slower bug;stale ### Your current environment I tried several vLLM versions (0.6.2 and latest 0.7.3) and have consistent speed drop when using speculative decoding with draft model. Tried on L4 and T4 GPU in Colab....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: be the bug Main model - `1.7B,` speculative model - `135M` parameters (`SmolLMv2` family of models) I trained the small model using logits distillation of main model, so it has a good level of generation (acceptance rat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Speculative decoding with a draft model makes generation slower bug;stale ### Your current environment I tried several vLLM versions (0.6.2 and latest 0.7.3) and have consistent speed drop when using speculative...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ### Your current environment I tried several vLLM versions (0.6.2 and latest 0.7.3) and have consistent speed drop when using speculative decoding with draft model. Tried on L4 and T4 GPU in Colab. ### 🐛 Describe the bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

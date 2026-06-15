# vllm-project/vllm#7684: [Feature]: Pipeline Parallelism support for the Vision Language Models

| 字段 | 值 |
| --- | --- |
| Issue | [#7684](https://github.com/vllm-project/vllm/issues/7684) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Pipeline Parallelism support for the Vision Language Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch If I am not wrong, currently vllm supports only the **Language models** not the **Vision models**. NotImplementedError: Pipeline parallelism is only supported for the following architectures: ['AquilaModel', 'AquilaForCausalLM', 'DeepseekV2ForCausalLM', 'InternLMForCausalLM', 'JAISLMHeadModel', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'Phi3ForCausalLM', 'GPT2LMHeadModel', 'MixtralForCausalLM', 'NemotronForCausalLM', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'QWenLMHeadModel']. This feature would greatly benefit teams and projects working with vision-language models, allowing them to scale out their workloads efficiently and maintain performance as model sizes continue to grow. Also It would be greatly helpful, if someone can point me out on other possibilities for pipeline parallelism. Thanks in advance ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Pipeline Parallelism support for the Vision Language Models feature request ### 🚀 The feature, motivation and pitch If I am not wrong, currently vllm supports only the **Language models** not the **Vision mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Pipeline Parallelism support for the Vision Language Models feature request ### 🚀 The feature, motivation and pitch If I am not wrong, currently vllm supports only the **Language models** not the **Vision mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: h vision-language models, allowing them to scale out their workloads efficiently and maintain performance as model sizes continue to grow. Also It would be greatly helpful, if someone can point me out on other possibili...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: teams and projects working with vision-language models, allowing them to scale out their workloads efficiently and maintain performance as model sizes continue to grow. Also It would be greatly helpful, if someone can p...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: , 'MixtralForCausalLM', 'NemotronForCausalLM', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'QWenLMHeadModel']. This feature would greatly benefit teams and projects working with vision-language models, allowing them to s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

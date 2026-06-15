# vllm-project/vllm#9844: [Feature]: Pipeline Parallelism support for the IBM Granite models 

| 字段 | 值 |
| --- | --- |
| Issue | [#9844](https://github.com/vllm-project/vllm/issues/9844) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Pipeline Parallelism support for the IBM Granite models 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch From the [distributed serving and inference docs](https://docs.vllm.ai/en/latest/serving/distributed_serving.html#details-for-distributed-inference-and-serving), it seems that currently, vllm only supports LLaMa, GPT2, Mixtral, Qwen, Qwen2, and Nemotron style models. `NotImplementedError: Pipeline parallelism is only supported for the following architectures: ['AquilaModel', 'AquilaForCausalLM', 'DeepseekV2ForCausalLM', 'InternLMForCausalLM', 'JAISLMHeadModel', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'Phi3ForCausalLM', 'GPT2LMHeadModel', 'MixtralForCausalLM', 'NemotronForCausalLM', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'QWenLMHeadModel'].` Adding Granite models would benefit teams and projects working with these model types, allowing them to scale out their workloads efficiently and maintain performance as model sizes continue to grow. Thanks in advance! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Pipeline Parallelism support for the IBM Granite models feature request ### 🚀 The feature, motivation and pitch From the [distributed serving and inference docs](https://docs.vllm.ai/en/latest/serving/distrib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Pipeline Parallelism support for the IBM Granite models feature request ### 🚀 The feature, motivation and pitch From the [distributed serving and inference docs](https://docs.vllm.ai/en/latest/serving/distrib...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g with these model types, allowing them to scale out their workloads efficiently and maintain performance as model sizes continue to grow. Thanks in advance! ### Alternatives _No response_ ### Additional context _No res...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: efit teams and projects working with these model types, allowing them to scale out their workloads efficiently and maintain performance as model sizes continue to grow. Thanks in advance! ### Alternatives _No response_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: , 'MixtralForCausalLM', 'NemotronForCausalLM', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'QWenLMHeadModel'].` Adding Granite models would benefit teams and projects working with these model types, allowing them to scal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#9015: [Feature]: Pipeline Parallelism support for LLaMA3.2 90B Vision Model

| 字段 | 值 |
| --- | --- |
| Issue | [#9015](https://github.com/vllm-project/vllm/issues/9015) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Pipeline Parallelism support for LLaMA3.2 90B Vision Model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to load LLaMA 3.2 90B Vision model across two nodes. Each node has 2 A100 80GB GPUs. I'm using tensor parallel size=1 and pipeline parallel size = 4. I get the following not implemented error. I'm using the latest published version of vLLM (version: 0.6.2). Any help to resolve this would be greatly received. Thank you. raise NotImplementedError( NotImplementedError: Pipeline parallelism is only supported for the following architectures: ['AquilaForCausalLM', 'AquilaModel', 'DeepseekV2ForCausalLM', 'GPT2LMHeadModel', 'InternLM2ForCausalLM', 'InternLMForCausalLM', 'InternVLChatModel', 'JAISLMHeadModel', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'NemotronForCausalLM', 'Phi3ForCausalLM', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'QWenLMHeadModel', 'Qwen2VLForConditionalGeneration']. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Pipeline Parallelism support for LLaMA3.2 90B Vision Model feature request;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to load LLaMA 3.2 90B Vision...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Pipeline Parallelism support for LLaMA3.2 90B Vision Model feature request;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to load LLaMA 3.2 90B Vision...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: Pipeline Parallelism support for LLaMA3.2 90B Vision Model feature request;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to load LLaMA 3.2 90B Vision mode...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: get the following not implemented error. I'm using the latest published version of vLLM (version: 0.6.2). Any help to resolve this would be greatly received. Thank you. raise NotImplementedError( NotImplementedError: Pi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: LM', 'NemotronForCausalLM', 'Phi3ForCausalLM', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'QWenLMHeadModel', 'Qwen2VLForConditionalGeneration']. ### Before submitting a new issue... - [X] Make sure you already searched...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

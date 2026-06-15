# vllm-project/vllm#366: Stuck while inferring with WizardCoder model

| 字段 | 值 |
| --- | --- |
| Issue | [#366](https://github.com/vllm-project/vllm/issues/366) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Stuck while inferring with WizardCoder model

### Issue 正文摘录

My code: ```python llm_model = LLM(model=model_path) ... ... sampling_params = SamplingParams( temperature=temperature, top_p=top_p, top_k=top_k, max_tokens=max_new_tokens ,frequency_penalty=repetition_penalty,ignore_eos=True ) outputs = llm_model.generate([prompt], sampling_params) ``` My parameters: ```json { "Temperature":0.01, "Top-k":70, "Top-p":0.85, "Max new tokens":4096, "Repetition Penalty":1.2 } ``` Does anyone know where the problem is?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Stuck while inferring with WizardCoder model bug My code: ```python llm_model = LLM(model=model_path) ... ... sampling_params = SamplingParams( temperature=temperature, top_p=top_p, top_k=top_k, max_tokens=max_new_token...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: mpling_params) ``` My parameters: ```json { "Temperature":0.01, "Top-k":70, "Top-p":0.85, "Max new tokens":4096, "Repetition Penalty":1.2 } ``` Does anyone know where the problem is?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

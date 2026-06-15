# vllm-project/vllm#22808: [Bug]: Prefix caching with larger batch-sizes and large prompts is much slower and occasionally outputs garbage

| 字段 | 值 |
| --- | --- |
| Issue | [#22808](https://github.com/vllm-project/vllm/issues/22808) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix caching with larger batch-sizes and large prompts is much slower and occasionally outputs garbage

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We have been noticing a very strange behavior with batched inference using Qwen2.5-VL-7B. It turns out, the issue is related to prefix caching, which is enabled by default in V1. Not only does prefix caching slow down inference by almost 2x (for batches sharing the system prompt which is supposed to speed-up), it also outputs garbage sometimes, affecting longer predictions, especially in structured output scenarios. The example below, on the A100 SXM4, by default the prediction speed is `0.7752 sec/sample`, if I turn off prefix caching, I get `0.4190 sec/sample`. Moreover, with prefix caching, the outputs are pretty bad. In the example below, it starts to repeat "addCriterion" randomly. Full code ``` Python import torch, random, time from vllm import LLM, SamplingParams model_id = "Qwen/Qwen2.5-VL-7B-Instruct" llm = LLM(model=model_id, dtype=torch.float16, enable_prefix_caching=True) sampling_params = SamplingParams( temperature=0.0, top_p=1.0, top_k=-1, max_tokens=2048, repetition_penalty=1., ) def predict(system_prompts, user_messages, sampling_params): bs_size = len(user_messages) conversation = [] for k in range(bs_size): con...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ## Your current environment ### 🐛 Describe the bug We have been noticing a very strange behavior with batched inference using Qwen2.5-VL-7B. It turns out, the issue is related to prefix caching, which is enabled by defa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rams model_id = "Qwen/Qwen2.5-VL-7B-Instruct" llm = LLM(model=model_id, dtype=torch.float16, enable_prefix_caching=True) sampling_params = SamplingParams( temperature=0.0, top_p=1.0, top_k=-1, max_tokens=2048, repetitio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: , especially in structured output scenarios. The example below, on the A100 SXM4, by default the prediction speed is `0.7752 sec/sample`, if I turn off prefix caching, I get `0.4190 sec/sample`. Moreover, with prefix ca...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: have been noticing a very strange behavior with batched inference using Qwen2.5-VL-7B. It turns out, the issue is related to prefix caching, which is enabled by default in V1. Not only does prefix caching slow down infe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ) output = llm.chat(conversation, sampling_params, use_tqdm=False) out = [output[k].outputs[0].text for k in range(bs_size)] return out system_prompt = """ Section 1 — Core Identity & Purpose You are AURELIAN, an advanc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

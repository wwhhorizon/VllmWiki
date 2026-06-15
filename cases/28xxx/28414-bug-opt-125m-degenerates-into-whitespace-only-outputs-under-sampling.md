# vllm-project/vllm#28414: [Bug]:  OPT-125M degenerates into whitespace-only outputs under sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#28414](https://github.com/vllm-project/vllm/issues/28414) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  OPT-125M degenerates into whitespace-only outputs under sampling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Summary Running `facebook/opt-125m` on CUDA produces generations that consist entirely of token `1437` (a single space) whenever I use non-greedy sampling (nucleus or top‑k). ### Minimal reproduction ```python from vllm import LLM, SamplingParams llm = LLM(model="facebook/opt-125m") params = SamplingParams( temperature=0.7, top_p=0.9, top_k=-1, # also happens with top_k=4 max_tokens=128, seed=5, ) output = llm.generate( prompts=["Generate a concise system test message for vLLM."], sampling_params=params, use_tqdm=False, )[0] print("finish_reason:", output.outputs[0].finish_reason) print("repr(text):", repr(output.outputs[0].text[:80])) print("first tokens:", output.outputs[0].token_ids[:10]) ``` Observed output: ``` finish_reason: length repr(text): ' ' first tokens: [1437, 1437, 1437, 1437, 1437, 1437, 1437, 1437, 1437, 1437] ``` Switching to greedy (`temperature=0, top_p=1`) produces normal text, so the issue seems confined to the sampling path. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](ht...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pling (nucleus or top‑k). ### Minimal reproduction ```python from vllm import LLM, SamplingParams llm = LLM(model="facebook/opt-125m") params = SamplingParams( temperature=0.7, top_p=0.9, top_k=-1, # also happens with t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t ### 🐛 Describe the bug ### Summary Running `facebook/opt-125m` on CUDA produces generations that consist entirely of token `1437` (a single space) whenever I use non-greedy sampling (nucleus or top‑k). ### Minimal rep...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tem test message for vLLM."], sampling_params=params, use_tqdm=False, )[0] print("finish_reason:", output.outputs[0].finish_reason) print("repr(text):", repr(output.outputs[0].text[:80])) print("first tokens:", output.o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: l reproduction ```python from vllm import LLM, SamplingParams llm = LLM(model="facebook/opt-125m") params = SamplingParams( temperature=0.7, top_p=0.9, top_k=-1, # also happens with top_k=4 max_tokens=128, seed=5, ) out...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

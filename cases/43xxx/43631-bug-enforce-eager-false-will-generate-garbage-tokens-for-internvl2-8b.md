# vllm-project/vllm#43631: [Bug]: enforce_eager=False will generate garbage tokens for InternVL2-8B

| 字段 | 值 |
| --- | --- |
| Issue | [#43631](https://github.com/vllm-project/vllm/issues/43631) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: enforce_eager=False will generate garbage tokens for InternVL2-8B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary When running vLLM with the default compiled mode (`enforce_eager=False`) on an RTX 5090, the model produces incorrect/repetitive garbage tokens. Switching to `enforce_eager=True` immediately restores correct output. No exception, no NaN, no warning is raised — the failure is completely silent. --- ## Reproduction ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "1" from vllm import LLM, SamplingParams messages = [{"role": "user", "content": "What is the capital of France?"}] # BROKEN — compiled mode (default) llm = LLM(model="OpenGVLab/InternVL2-8B", trust_remote_code=True) out = llm.chat(messages, SamplingParams(temperature=0, max_tokens=50)) print(out[0].outputs[0].text) # → "down down down down down down down down down down ..." # WORKS — eager mode llm = LLM(model="OpenGVLab/InternVL2-8B", trust_remote_code=True, enforce_eager=True) out = llm.chat(messages, SamplingParams(temperature=0, max_tokens=50)) print(out[0].outputs[0].text) # → "The capital of France is Paris." ``` Tested with a **cold cache** (cache deleted before each run) — the issue is not caused by a stale compiled artifact. The freshly compile...

## 现有链接修复摘要

#43668 Fix InternVL2-8B compiled generation with InternLM2 backbone

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### 🐛 Describe the bug ## Summary When running vLLM with the default compiled mode (`enforce_eager=False`) on an RTX 5090, the model produces incorrect/repetitive garbage tokens. Switching to `enforce_eager=True` immedi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: unning vLLM with the default compiled mode (`enforce_eager=False`) on an RTX 5090, the model produces incorrect/repetitive garbage tokens. Switching to `enforce_eager=True` immediately restores correct output. No except...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: enforce_eager=False will generate garbage tokens for InternVL2-8B bug ### Your current environment ### 🐛 Describe the bug ## Summary When running vLLM with the default compiled mode (`enforce_eager=False`) on an...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ci_build;hardware_porting;model_support;sampling_logits cuda build_error;mismatch;nan_inf env_dependency #43668 Fix InternVL2-8B compiled generation with InternLM2 backbone Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: enforce_eager=False will generate garbage tokens for InternVL2-8B bug ### Your current environment ### 🐛 Describe the bug ## Summary When running vLLM with the default compiled mode (`enforce_eager=False`) on an...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43668](https://github.com/vllm-project/vllm/pull/43668) | closes_keyword | 0.95 | Fix InternVL2-8B compiled generation with InternLM2 backbone | Fixes #43631. InternVL feeds precomputed text+vision embeddings into the text backbone. For InternVL2 models whose text backbone is `InternLM2ForCausalLM`, the compiled internal I |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#26945: [Bug]: google/embeddinggemma-300m  when using transformers backend doesn't match the output of Sentence Transformers (or model_impl="vllm")

| 字段 | 值 |
| --- | --- |
| Issue | [#26945](https://github.com/vllm-project/vllm/issues/26945) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: google/embeddinggemma-300m  when using transformers backend doesn't match the output of Sentence Transformers (or model_impl="vllm")

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `google/embeddinggemma-300m` with transformers backend doesn't match the output of native vllm implementation and nor Sentence Transformers Repro ```python import numpy as np import torch import torch.nn.functional as F from vllm import LLM llm_kwargs = { "model": "google/embeddinggemma-300m", "max_model_len": 2048, "enforce_eager": False, } llm_vllm = LLM(model_impl="vllm", **llm_kwargs) llm_transformers = LLM(model_impl="transformers", **llm_kwargs) from sentence_transformers import SentenceTransformer # noqa: E402 sentence_transformer = SentenceTransformer(llm_kwargs["model"]) prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] outputs_vllm = llm_vllm.embed(prompts, truncate_prompt_tokens=-1) outputs_transformers = llm_transformers.embed(prompts, truncate_prompt_tokens=-1) outputs_sentence_transformer = sentence_transformer.encode(prompts) for prompt_idx, ( output_vllm, output_transformers, output_sentence_transformer, ) in enumerate(zip(outputs_vllm, outputs_transformers, outputs_sentence_transformer)): embedding_vllm = np.array(output_vllm.outputs.emb...

## 现有链接修复摘要

#26906 Refactor Transformers backend to use mixins

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ative vllm implementation and nor Sentence Transformers Repro ```python import numpy as np import torch import torch.nn.functional as F from vllm import LLM llm_kwargs = { "model": "google/embeddinggemma-300m", "max_mod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: google/embeddinggemma-300m when using transformers backend doesn't match the output of Sentence Transformers (or model_impl="vllm") bug ### Your current environment ### 🐛 Describe the bug `google/embeddinggemma-3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s d ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: google/embeddinggemma-300m when using transformers backend doesn't match the output of Sentence Transformers (or model_impl="vllm") bug ### Your current environment ### 🐛 Describe the bug `google/embeddinggemma-3...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: (f"\t {check_name}", end=" ") try: np.testing.assert_allclose(check_a, check_b, atol=1e-2) print("are close ✅") except Exception: cosine_similarity = F.cosine_similarity( torch.tensor(check_a), torch.tensor(check_b), di...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26906](https://github.com/vllm-project/vllm/pull/26906) | closes_keyword | 0.95 | Refactor Transformers backend to use mixins | Fixes #26945 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

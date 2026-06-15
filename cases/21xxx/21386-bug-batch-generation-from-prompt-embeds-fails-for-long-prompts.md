# vllm-project/vllm#21386: [Bug]: Batch generation from prompt_embeds fails for long prompts

| 字段 | 值 |
| --- | --- |
| Issue | [#21386](https://github.com/vllm-project/vllm/issues/21386) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Batch generation from prompt_embeds fails for long prompts

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Overview An error occurs in batch generation from prompt embeddings when prompts are long. This is a minimal reproducible script based on the [example code](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/prompt_embed_inference.py) provided in the [Prompt Embedding Inputs](https://docs.vllm.ai/en/latest/features/prompt_embeds.html?h=prompt+embedding+inputs) section of the document. Running this code with 1 GPU `CUDA_VIDIBLE_DEVICES=0 uv run python test.py` results in an error. ```python # test.py from transformers import AutoModelForCausalLM, AutoTokenizer, PreTrainedTokenizer from vllm import LLM text = "A long time ago, in a galaxy far, far away..." # this should be >= 1000 tokens def main(): model_name = "Qwen/Qwen3-0.6B" tokenizer = AutoTokenizer.from_pretrained(model_name) transformers_model = AutoModelForCausalLM.from_pretrained(model_name) embedding_layer = transformers_model.get_input_embeddings() llm = LLM(model=model_name, enable_prompt_embeds=True) token_ids_list = [tokenizer(text, return_tensors="pt")["input_ids"] for _ in range(8)] prompt_embeds_list = [embedding_layer(chat).squeeze(0) for...

## 现有链接修复摘要

#21390 [Bugfix]: Batch generation from prompt_embeds fails for long prompts

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: n from prompt embeddings when prompts are long. This is a minimal reproducible script based on the [example code](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/prompt_embed_inference.py) prov...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: embedding+inputs) section of the document. Running this code with 1 GPU `CUDA_VIDIBLE_DEVICES=0 uv run python test.py` results in an error. ```python # test.py from transformers import AutoModelForCausalLM, AutoTokenize...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ollowing fixes are considered. The first approach is to modify only the block starting at line [1948](https://github.com/vllm-project/vllm/blob/774d0c014b8699d244ba2889d872591ca535b80f/vllm/worker/model_runner.py#L1948)...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: neration from prompt embeddings when prompts are long. This is a minimal reproducible script based on the [example code](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/prompt_embed_inference.p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;mismatch;nan_inf;oo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21390](https://github.com/vllm-project/vllm/pull/21390) | closes_keyword | 0.95 | [Bugfix]: Batch generation from prompt_embeds fails for long prompts | fix for the issue [#21386](https://github.com/vllm-project/vllm/issues/21386): Batch generation from prompt_embeds fails for long prompts. An error occurs in batch generation from |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#8009: [Misc]/[Tracking]: FP8 Datatype parameter for Flashinfer backend Metadata accumulation for its decode wrapper. 

| 字段 | 值 |
| --- | --- |
| Issue | [#8009](https://github.com/vllm-project/vllm/issues/8009) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]/[Tracking]: FP8 Datatype parameter for Flashinfer backend Metadata accumulation for its decode wrapper. 

### Issue 正文摘录

Previous reference: https://github.com/vllm-project/vllm/pull/7985/files/26904dd78495ad1b18e43d9e52ee62e05cb71d04#r1736922768 Issue: With this configuration and test: ``` model_str="neuralmagic/Meta-Llama-3-8B-Instruct-FP8" model = LLM(model=model_str, quantization="fp8",kv_cache_dtype="fp8") params = SamplingParams(temperature=0) prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "New york times is politically sided to ", "The future holds infinite " ] result = model.generate(prompts=prompts, sampling_params=params) for output in result: prompt = output.prompt generated_text = output.outputs[0].text print( f"\n\n Prompt: {prompt!r}, \nGenerated text: {generated_text!r}, \ntoken_ids: {output.outputs[0].token_ids}" ) ``` and the execution: ``` VLLM_ATTENTION_BACKEND=FLASHINFER /bin/python3 /workspace/vllm_github/test_llm.py root@s4124-0013:/workspace/vllm_github# VLLM_ATTENTION_BACKEND=FLASHINFER /bin/python3 /workspace/vllm_github/test_llm.py INFO 08-29 19:17:01 config.py:628] Using fp8 data type to store kv cache. It reduces the GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a prope...

## 现有链接修复摘要

#8013 [Bugfix] Address #8009 and add model test for flashinfer fp8 kv cache.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Misc]/[Tracking]: FP8 Datatype parameter for Flashinfer backend Metadata accumulation for its decode wrapper. Previous reference: https://github.com/vllm-project/vllm/pull/7985/files/26904dd78495ad1b18e43d9e52ee62e05cb...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: /26904dd78495ad1b18e43d9e52ee62e05cb71d04#r1736922768 Issue: With this configuration and test: ``` model_str="neuralmagic/Meta-Llama-3-8B-Instruct-FP8" model = LLM(model=model_str, quantization="fp8",kv_cache_dtype="fp8...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Misc]/[Tracking]: FP8 Datatype parameter for Flashinfer backend Metadata accumulation for its decode wrapper. Previous reference: https://github.com/vllm-project/vllm/pull/7985/files/26904dd78495ad1b18e43d9e52ee62e05cb...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: t_llm.py INFO 08-29 19:17:01 config.py:628] Using fp8 data type to store kv cache. It reduces the GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scaling factor IN...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Misc]/[Tracking]: FP8 Datatype parameter for Flashinfer backend Metadata accumulation for its decode wrapper. Previous reference: https://github.com/vllm-project/vllm/pull/7985/files/26904dd78495ad1b18e43d9e52ee62e05cb...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8013](https://github.com/vllm-project/vllm/pull/8013) | mentioned | 0.6 | [Bugfix] Address #8009 and add model test for flashinfer fp8 kv cache. | test for flashinfer fp8 kv cache. This addresses the bug described in #8009. Fix is to consistently replace the fp8 type right before we call into Flashinfer API. Please note that… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

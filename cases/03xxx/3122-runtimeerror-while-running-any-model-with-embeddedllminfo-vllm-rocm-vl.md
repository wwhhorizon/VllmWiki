# vllm-project/vllm#3122: RuntimeError while running any model with embeddedllminfo/vllm-rocm:vllm-v0.2.4 image and rocm5.7 (rhel 8.7)

| 字段 | 值 |
| --- | --- |
| Issue | [#3122](https://github.com/vllm-project/vllm/issues/3122) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError while running any model with embeddedllminfo/vllm-rocm:vllm-v0.2.4 image and rocm5.7 (rhel 8.7)

### Issue 正文摘录

>>> from vllm import LLM, SamplingParams >>> >>> prompts = [ ... "Hello, my name is", ... "The president of the United States is", ... "The capital of France is", ... "The future of AI is", ... ] >>> >>> sampling_params = SamplingParams(temperature=0.8, top_p=0.95) >>> llm = LLM(model="openlm-research/open_llama_13b") config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████| 507/507 [00:00 . This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thoroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565 WARNING[XFORMERS]: xFormers can't load C++/CUDA extensions. xFormers was built for: PyTorch 2.1.1+cu121 with CUDA 1201 (you have 2.0.1+gita61a294) Python 3.10.13 (you have 3.10.13) Please reinstall xformers (see https://github.com/facebookresearch/xformers#installing-xformers) Memory-efficient attention, SwiGLU, sparse and more won't be available. Set XFORMERS_MORE_DETAILS=1 for more details MegaB...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: o/vllm-rocm:vllm-v0.2.4 image and rocm5.7 (rhel 8.7) stale >>> from vllm import LLM, SamplingParams >>> >>> prompts = [ ... "Hello, my name is", ... "The president of the United States is", ... "The capital of France is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: RuntimeError while running any model with embeddedllminfo/vllm-rocm:vllm-v0.2.4 image and rocm5.7 (rhel 8.7) stale >>> from vllm import LLM, SamplingParams >>> >>> prompts = [ ... "Hello, my name is", ... "The president...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: RuntimeError while running any model with embeddedllminfo/vllm-rocm:vllm-v0.2.4 image and rocm5.7 (rhel 8.7) stale >>> from vllm import LLM, SamplingParams >>> >>> prompts = [ ... "Hello, my name is", ... "The president...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits attention;cuda;kernel;quantization;sampling build_error;crash;mismatch dtype;env_dependency >>> from vllm import LLM,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thoroughly read the reason why this was added as explained in https://github.co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#641: RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

| 字段 | 值 |
| --- | --- |
| Issue | [#641](https://github.com/vllm-project/vllm/issues/641) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

### Issue 正文摘录

Hello everyone, I always got this error for Baichuan and LLaMA models. And I found it's caused by the **single_query_cached_kv_attention** method in vllm\model_executor\layers\\**attention.py**. After calling of this method, the hidden output has some **rows of "nan"**. How can I fix this? Thanks! Still have such errors even after installing xformers from source. This is my code: ```python from vllm import LLM, SamplingParams #from vllm.transformers_utils.configs.baichuan import BaiChuanConfig prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=1, top_p=0.95) llm = LLM( model="/.../Baichuan-7b", trust_remote_code=True, dtype='float16', gpu_memory_utilization=0.85, tokenizer_mode="slow" ) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` and this is my python environment: ``` accelerate 0.21.0 aiofiles 23.1.0 aiohttp 3.8.5 aiosignal 1.3.1 altair 5.0.1 annotated-types 0.5.0 anyio 3.7.1 appdirs 1.4.4 argon2-cffi 21...

## 现有链接修复摘要

#936 [BugFix] Fix NaN errors in paged attention kernel

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: "nan"**. How can I fix this? Thanks! Still have such errors even after installing xformers from source. This is my code: ```python from vllm import LLM, SamplingParams #from vllm.transformers_utils.configs.baichuan impo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: element < 0 bug Hello everyone, I always got this error for Baichuan and LLaMA models. And I found it's caused by the **single_query_cached_kv_attention** method in vllm\model_executor\layers\\**attention.py**. After ca...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: model="/.../Baichuan-7b", trust_remote_code=True, dtype='float16', gpu_memory_utilization=0.85, tokenizer_mode="slow" ) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt gene...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y 1.25.1 nvidia-cublas-cu11 11.10.3.66 nvidia-cuda-cupti-cu11 11.7.101 nvidia-cuda-nvrtc-cu11 11.7.99 nvidia-cuda-runtime-cu11 11.7.99 nvidia-cudnn-cu11 8.5.0.96 nvidia-cufft-cu11 10.9.0.58 nvidia-curand-cu11 10.2.10.91...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 4.65.0 traitlets 5.9.0 transformers 4.31.0 triton 2.0.0 trl 0.4.7 trove-classifiers 2023.7.6 typing_extensions 4.7.1 typing-inspect 0.9.0 tzdata 2023.3 uc-micro-py

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#936](https://github.com/vllm-project/vllm/pull/936) | closes_keyword | 0.95 | [BugFix] Fix NaN errors in paged attention kernel | Fixes #641 This PR fixes the paged attention kernel. Currently, the kernel computes `attn_weight * value` for all tokens in a value block, even if some of them are not included i |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

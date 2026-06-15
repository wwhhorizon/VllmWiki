# vllm-project/vllm#21452: [Bug]: Qwen2.5 1M models no longer working since v.0.8.5

| 字段 | 值 |
| --- | --- |
| Issue | [#21452](https://github.com/vllm-project/vllm/issues/21452) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5 1M models no longer working since v.0.8.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I can run the Qwen2.5-7B-Instruct-1M and its 14B variant in vLLM v.0.8.5 without any problem, using the default V1 mode with flash attention backend. However, with newer versions, it fails. The first symptom of the underlying problems is the following error message: ` TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'layer_idx' ` I also tried with flash-infer and dual_chunk_attn (V0 mode), but also without success. I though it might be due to the model's 'dual_chunk_attn' nature (see https://github.com/vllm-project/vllm/issues/20475 and https://github.com/vllm-project/vllm/issues/20484), however even after these issues were reported fixed, the model still doesn't work with any of the backends: flash_attn, flashinfer, dual_chunk_attn. Here's a simple script to serve the model that still works perfectly fine on my vllm 0.8.5 setup, but that doesn't work at all on newer versions, including if freshly built-from-source (see my collect_env.py above). ```bash #!/bin/bash clear MODEL='/Localstore/vllm_models/text/Qwen25/Qwen2.5-7B-Instruct-1M' vllm serve $MODEL --gpu-memory-utilization 0.9 --enable-prefix-cach...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: iant in vLLM v.0.8.5 without any problem, using the default V1 mode with flash attention backend. However, with newer versions, it fails. The first symptom of the underlying problems is the following error message: ` Ty...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: g the default V1 mode with flash attention backend. However, with newer versions, it fails. The first symptom of the underlying problems is the following error message: ` TypeError: FlashAttentionImpl.__init__() got an...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: formers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto") print(f'- Pipeline result is: {pipeline(f"A chicken is a ")}') ``` Because of the quality of the resul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lp. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5 1M models no longer working since v.0.8.5 bug ### Your current environment ### 🐛 Describe the bug I can run the Qwen2.5-7B-Instruct-1M and its 14B variant in vLLM v.0.8.5 without any problem, using the de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

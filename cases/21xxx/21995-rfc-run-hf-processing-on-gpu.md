# vllm-project/vllm#21995: [RFC] Run HF processing on GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#21995](https://github.com/vllm-project/vllm/issues/21995) |
| 状态 | open |
| 标签 | RFC;keep-open;multi-modality |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | oom;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] Run HF processing on GPU

### Issue 正文摘录

### Motivation. Now that fast processors have been merged into HF Transformers, we can call HF processors with `device="cuda"` to run them on GPU. This has been shown to improve the processing speed up to one order of magnitude (though that requires a large batch size which doesn't really happen in practice since we call the HF processor once per prompt). Benchmarks: https://github.com/huggingface/transformers/pull/39591 ### Proposed Change. We can support this via `mm_processor_kwargs`, e.g.: ```python # Use CUDA by default llm = LLM(model="Qwen/Qwen2.5-VL-3B-Instruct", mm_processor_kwargs={"use_fast": True, "device": "cuda"}) # Use CUDA for one request - technically possible but requires memory profiling # to assume GPU preprocessing usage even if no requests actually do this, # so likely not support this niche case to save code complexity llm = LLM(model="Qwen/Qwen2.5-VL-3B-Instruct", mm_processor_kwargs={"use_fast": True}) llm.generate({ "prompt": formatted_prompt, "multi_modal_data": {"image": image}, "mm_processor_kwargs": {"device": "cuda"}, }) # -- or -- llm.chat( messages=[ { "role": "user", "content": [ {"type": "text", "text": text}, {"type": "image_url", "image_url": {...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [RFC] Run HF processing on GPU RFC;keep-open;multi-modality ### Motivation. Now that fast processors have been merged into HF Transformers, we can call HF processors with `device="cuda"` to run them on GPU. This has bee...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: lly happen in practice since we call the HF processor once per prompt). Benchmarks: https://github.com/huggingface/transformers/pull/39591 ### Proposed Change. We can support this via `mm_processor_kwargs`, e.g.: ```pyt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: een merged into HF Transformers, we can call HF processors with `device="cuda"` to run them on GPU. This has been shown to improve the processing speed up to one order of magnitude (though that requires a large batch si...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: questions. performance frontend_api;model_support cuda oom;slowdown env_dependency;shape Motivation.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ] How to accommodate this in memory profiling so that users cannot cause OOM during inference? (#22070) - [ ] Release benchmarks on vLLM Follow-ups: - [ ] After processing, some (but not all!) of the inputs will be on G...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

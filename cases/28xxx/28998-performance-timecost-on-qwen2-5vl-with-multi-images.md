# vllm-project/vllm#28998: [Performance]: Timecost on Qwen2.5VL with multi images

| 字段 | 值 |
| --- | --- |
| Issue | [#28998](https://github.com/vllm-project/vllm/issues/28998) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Timecost on Qwen2.5VL with multi images

### Issue 正文摘录

### Proposal to improve performance I'm trying to use VLLM to infer the qwen2.5vl 7b model, but I've found that the latency increases significantly as the number of input images increases. When a single image is input in a multimodal request, the average latency is less than 1 second; however, when 8 images are input, the average latency increases to 3 seconds. Has anyone else encountered the same problem as me? I'd like to know if vllm optimizes the VIT part of qwen2.5vl, or if there are any areas in my code that need improvement. ``` self.model = LLM( model='Qwen25VL-7B', task="embed", gpu_memory_utilization=0.7, enforce_eager=False, override_pooler_config=pooler_config, trust_remote_code=True, dtype=torch.bfloat16, hf_overrides={"is_causal": False, "architectures": ["Qwen2_5_VLForConditionalGeneration"]}, limit_mm_per_prompt={"image":8}, mm_processor_kwargs={"max_pixels": 512**2} ) ...... for idx, (t, img) in enumerate(zip(texts, images)): t3 = time.time() input_str = '' if img is None or len(img) == 0: input_str += t msg = f' system\nYou are a helpful assistant. \n user\n{input_str} \n assistant\n ' (output,) = self.model.embed({"prompt": msg}, use_tqdm=False) else: input_str...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: Timecost on Qwen2.5VL with multi images performance;stale ### Proposal to improve performance I'm trying to use VLLM to infer the qwen2.5vl 7b model, but I've found that the latency increases significantl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ide_pooler_config=pooler_config, trust_remote_code=True, dtype=torch.bfloat16, hf_overrides={"is_causal": False, "architectures": ["Qwen2_5_VLForConditionalGeneration"]}, limit_mm_per_prompt={"image":8}, mm_processor_kw...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ing to use VLLM to infer the qwen2.5vl 7b model, but I've found that the latency increases significantly as the number of input images increases. When a single image is input in a multimodal request, the average latency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: dtype=torch.bfloat16, hf_overrides={"is_causal": False, "architectures": ["Qwen2_5_VLForConditionalGeneration"]}, limit_mm_per_prompt={"image":8}, mm_processor_kwargs={"max_pixels": 512**2} ) ...... for idx, (t, img) in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Timecost on Qwen2.5VL with multi images performance;stale ### Proposal to improve performance I'm trying to use VLLM to infer the qwen2.5vl 7b model, but I've found that the latency increases significantl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

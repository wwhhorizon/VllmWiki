# vllm-project/vllm#19876: [Bug]: InternVL3 poor (random) output with 8bit quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#19876](https://github.com/vllm-project/vllm/issues/19876) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVL3 poor (random) output with 8bit quantization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### InternVL3 8-Bit quantizations (FP8, BNB-8Bit) Produce Bad/Random outputs on vLLM When loading FP8 (compressed-tensors via llm-compressor) or BNB-8Bit (via transformers) quantized InternVL3 models in vllm, the output is bad/random. **However, loading these same models into Transformers - AutoModel.from_pretrained results in proper output as expected.** _Worth noting_, lm_head, vision, and the mlp1 layers are not quantized. (mlp1 contains linear layers, but, the vllm internvl.py model doesn't support scale values currently). Example: ``` model = LLM( model="brandonbeiler/InternVL3-38B-FP8-Dynamic", # also with 'brandonbeiler/InternVL3-38B-BNB-8bit' trust_remote_code=True, max_model_len=4096, tensor_parallel_size=1, gpu_memory_utilization=0.8, enforce_eager=True # attempted with and without eager ) sampling_params = SamplingParams( temperature=0.7, max_tokens=128, top_p=0.9, ) model.generate(['Hello! How are you today?'], sampling_params) ``` Output: ``` (\全全Rock separatoruta de尚未Java team com com com com com comett com com com com com com com com := Ne com com com com com com com com comett#!/ -- drummer delibernamespaceOffsetu...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: InternVL3 poor (random) output with 8bit quantization bug ### Your current environment ### 🐛 Describe the bug ### InternVL3 8-Bit quantizations (FP8, BNB-8Bit) Produce Bad/Random outputs on vLLM When loading FP8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: InternVL3 poor (random) output with 8bit quantization bug ### Your current environment ### 🐛 Describe the bug ### InternVL3 8-Bit quantizations (FP8, BNB-8Bit) Produce Bad/Random outputs on vLLM When loading FP8...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: edni Null StringIOKD comprehend国有 violet knit ETA<Key VGA performedCoefficientamus body ``` ### Quantization Notes - InternVL3 38B FP8 Dynamic: https://huggingface.co/brandonbeiler/InternVL3-38B-FP8-Dynamic - InternVL3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _flash_attn=True, max_memory={i: "92GB" for i in range(torch.cuda.device_count())}, ) processor = AutoProcessor.from_pretrained( source_model, trust_remote_code=True ) recipe = [ QuantizationModifier(
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;fp8;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

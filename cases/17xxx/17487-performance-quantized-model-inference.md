# vllm-project/vllm#17487: [Performance]: Quantized Model Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#17487](https://github.com/vllm-project/vllm/issues/17487) |
| 状态 | open |
| 标签 | performance;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | gemm_linear;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Quantized Model Inference

### Issue 正文摘录

### Report of performance regression Hello I recently quantized Llama 3 based 70B models using the [llm-compressor](https://github.com/vllm-project/llm-compressor) quantization recipes, specifically: 1. INT8 GPTQ: recipe = [ SmoothQuantModifier(smoothing_strength=0.8), GPTQModifier( targets="Linear", scheme="W8A8", ignore=["lm_head"], dampening_frac=0.1 ), ] 2. INT8 PTQ: recipe = [ SmoothQuantModifier(smoothing_strength=0.8), QuantizationModifier(targets="Linear", scheme="W8A8", ignore=["lm_head"]), ] 3. FP8 GPTQ: recipe = [ SmoothQuantModifier(smoothing_strength=0.8), GPTQModifier( targets="Linear", scheme="FP8", ignore=["lm_head"], dampening_frac=0.1 ), ] 3. FP8 PTQ: recipe = [ SmoothQuantModifier(smoothing_strength=0.8), QuantizationModifier(targets="Linear", scheme="FP8", ignore=["lm_head"]), ] 4. FP8 dynamic: recipe = QuantizationModifier( targets="Linear", scheme="FP8_DYNAMIC", ignore=["lm_head"] ) 4. INT4 PTQ: recipe = QuantizationModifier( targets="Linear", scheme="W4A16", ignore=["lm_head"] ) 5. INT4 GPTQ: recipe = GPTQModifier(targets="Linear", scheme="W4A16", ignore=["lm_head"]) I have tried to run some performance tests specifically the [benchmark_throughput.py](https:...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: Quantized Model Inference performance;unstale ### Report of performance regression Hello I recently quantized Llama 3 based 70B models using the [llm-compressor](https://github.com/vllm-project/llm-compre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: uantization recipes, specifically: 1. INT8 GPTQ: recipe = [ SmoothQuantModifier(smoothing_strength=0.8), GPTQModifier( targets="Linear", scheme="W8A8", ignore=["lm_head"], dampening_frac=0.1 ), ] 2. INT8 PTQ: recipe = [
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: Quantized Model Inference performance;unstale ### Report of performance regression Hello I recently quantized Llama 3 based 70B models using the [llm-compressor](https://github.com/vllm-project/llm-compressor) quantizat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: Quantized Model Inference performance;unstale ### Report of performance regression Hello I recently quantized Llama 3 based 70B models using the [llm-compressor](https://github.com/vllm-project/llm-compre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: mpressor](https://github.com/vllm-project/llm-compressor) quantization recipes, specifically: 1. INT8 GPTQ: recipe = [ SmoothQuantModifier(smoothing_strength=0.8), GPTQModifier( targets="Linear", scheme="W8A8", ignore=[...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

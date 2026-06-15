# vllm-project/vllm#8006: [Performance]: INT4 quantisation does not lead to any observable throughput increase 

| 字段 | 值 |
| --- | --- |
| Issue | [#8006](https://github.com/vllm-project/vllm/issues/8006) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: INT4 quantisation does not lead to any observable throughput increase 

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I have been using vLLM with prefix caching to optimise inference in cases where majority of operations are pre-fills with large shared prefix. Specially, most of the prompts are 130 tokens in size with 90% of it is a shared system prompt. The decode is only phase is only one token. There benchmark is a 100000 prompts (`formatted_prompts` below) executed via generate: ```python from outlines import models, generate llm = LLM("meta-llama/Meta-Llama-3-8B-Instruct", enable_prefix_caching=True) sampling_params = SamplingParams(temperature=0.5, top_p=0.2, max_tokens=1) model = models.VLLM(llm) generator = generate.choice(model, ["yes", "no"]) predictions = generator(formatted_prompts, sampling_params=sampling_params) ``` When I use INT4 quantised model `neuralmagic/Meta-Llama-3-8B-Instruct-quantized.w4a16` I observe no speed-up in inference. Since my use cases highly leverages prefix caching, I would have expected at least 60% speed up driven by corresponding increase in KV-cache given a smaller model. Many thanks for your suggestions in advance ### Misc discussion on performance _No response_ ### You...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: where majority of operations are pre-fills with large shared prefix. Specially, most of the prompts are 130 tokens in size with 90% of it is a shared system prompt. The decode is only phase is only one token. There benc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: least 60% speed up driven by corresponding increase in KV-cache given a smaller model. Many thanks for your suggestions in advance ### Misc discussion on performance _No response_ ### Your current environment (if you th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: e is only phase is only one token. There benchmark is a 100000 prompts (`formatted_prompts` below) executed via generate: ```python from outlines import models, generate llm = LLM("meta-llama/Meta-Llama-3-8B-Instruct",...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Performance]: INT4 quantisation does not lead to any observable throughput increase performance ### Proposal to improve performance _No response_ ### Report of performance regression I have been using vLLM with prefix...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: INT4 quantisation does not lead to any observable throughput increase performance ### Proposal to improve performance _No response_ ### Report of performance regression I have been using vLLM with prefix...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

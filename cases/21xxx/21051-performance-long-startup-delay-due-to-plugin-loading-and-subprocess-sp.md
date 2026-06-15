# vllm-project/vllm#21051: [Performance]: Long startup delay due to plugin loading and subprocess spawning

| 字段 | 值 |
| --- | --- |
| Issue | [#21051](https://github.com/vllm-project/vllm/issues/21051) |
| 状态 | closed |
| 标签 | performance;stale;startup-ux |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Long startup delay due to plugin loading and subprocess spawning

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I am currently profiling cold startup latency. Several factors are included here, like model loading, dynamo bytecode transformation, torch.compile, graph capturing, etc However, I have noticed that there is a good amount of time spent at the beginning to before the initialization of the engine even starts. From the output log, it appears to be due to platform detection, plugin loading and spawning subprocesses. During my profiling, this delay is constant (~17s) across different models, different parameters, with and without --enforce-eager, etc Here is an output example while running Qwen1.5-4B on A100 40GB on V1 Command used: ```bash VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0 VLLM_LOGGING_LEVEL=DEBUG python3 vllm_engine.py --model=/models/qwen-4b --gpu_memory_utilization=0.9 ``` You can see the time between the first line and `Initializing a V1 LLM engine` is ~17s ### Misc discussion on performance My question are: - Is this normal? - Why is there 2 platform detection? - How can I reduce this time? ### Your current environment (if you think it is necessary) ```text Collecting environment information...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: included here, like model loading, dynamo bytecode transformation, torch.compile, graph capturing, etc However, I have noticed that there is a good amount of time spent at the beginning to before the initialization of t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: nforce-eager, etc Here is an output example while running Qwen1.5-4B on A100 40GB on V1 Command used: ```bash VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0 VLLM_LOGGING_LEVEL=DEBUG python3 vllm_engine.py --model=/models/qwen-4b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: profiling cold startup latency. Several factors are included here, like model loading, dynamo bytecode transformation, torch.compile, graph capturing, etc However, I have noticed that there is a good amount of time spen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: roposal to improve performance _No response_ ### Report of performance regression I am currently profiling cold startup latency. Several factors are included here, like model loading, dynamo bytecode transformation, tor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits attention;cuda;operator;quantization;sampling;triton build_error;nan_inf;slowdown dtype;env_dependency;shape Proposal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

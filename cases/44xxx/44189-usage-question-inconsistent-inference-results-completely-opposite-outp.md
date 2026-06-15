# vllm-project/vllm#44189: [Usage]: [Question] Inconsistent inference results (completely opposite outputs) across identical environments despite temperature=0

| 字段 | 值 |
| --- | --- |
| Issue | [#44189](https://github.com/vllm-project/vllm/issues/44189) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;kernel;sampling |
| 症状 | nondeterministic |
| 根因提示 | dtype;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: [Question] Inconsistent inference results (completely opposite outputs) across identical environments despite temperature=0

### Issue 正文摘录

### Your current environment Hi everyone, I am experiencing a strange determinism issue with a safety detection model I deployed using vLLM. For some specific input data, the model occasionally returns completely opposite detection results (e.g., predicting unsafe instead of safe, or vice versa) depending on which Pod serves the request. What makes this confusing is that the environment is strictly controlled. This inconsistency occurs despite using the exact same Docker image, identical Pod configurations, and deploying on the exact same physical host machine. Two crucial details I have already verified: 1.Strict Single-Pod Consistency: If I send the exact same request to one specific Pod repeatedly, the output is 100% consistent every single time. The divergence strictly happens between Pod A and Pod B. 2.No Sampling Randomness: I am querying the model using the standard OpenAI API client with temperature=0.0, so random sampling is completely ruled out. Here is my deployment command: CMD ["vllm", "serve", "/data/wzg/ft_local/woerma", \ "--host", "0.0.0.0", \ "--port", "30000", \ "--served-model-name", "qwen", \ "--dtype", "bfloat16", \ "--gpu-memory-utilization", "0.9", \ "--lan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: erature=0 usage ### Your current environment Hi everyone, I am experiencing a strange determinism issue with a safety detection model I deployed using vLLM. For some specific input data, the model occasionally returns c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: fic Pod repeatedly, the output is 100% consistent every single time. The divergence strictly happens between Pod A and Pod B. 2.No Sampling Randomness: I am querying the model using the standard OpenAI API client with t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: "--port", "30000", \ "--served-model-name", "qwen", \ "--dtype", "bfloat16", \ "--gpu-memory-utilization", "0.9", \ "--language-model-only", \ "--enable-prefix-caching", \ "--trust-remote-code", \ "--max-model-len", "20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: , I am experiencing a strange determinism issue with a safety detection model I deployed using vLLM. For some specific input data, the model occasionally returns completely opposite detection results (e.g., predicting u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: current environment Hi everyone, I am experiencing a strange determinism issue with a safety detection model I deployed using vLLM. For some specific input data, the model occasionally returns completely opposite detect...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

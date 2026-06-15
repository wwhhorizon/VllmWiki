# vllm-project/vllm#13035: [Bug]: Llama-3.1-405B-Instruct-FP8 only generates exclamation marks

| 字段 | 值 |
| --- | --- |
| Issue | [#13035](https://github.com/vllm-project/vllm/issues/13035) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama-3.1-405B-Instruct-FP8 only generates exclamation marks

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I am running into bugs with Llama-3.1-405B-Instruct-FP8 since version 0.7.0. The initial bug (could not even start the model) was probably fixed with https://github.com/vllm-project/vllm/pull/12696 that was included in 0.7.2. I have tried this new latest version, the model is initiated and service is running but the **model generates endless exclamation marks** even with frequency penalties and different temperatures. **Run command:** ``` vllm serve Meta-Llama-3.1-405B-Instruct-FP8 -tp 8 --enable-prefix-caching --max-model-len 16384 --max-num-batched-tokens 16384 ``` **Replication:** ```py client.chat.completions.create( messages=[{'role': 'user', 'content': 'Hello, whats up?'}], model='Llama-3.1-405B-Instruct-FP8', max_tokens=100, temperature=0.0, ) ``` **Downgrading to vLLM v0.6.6 works.**

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e bug Hi, I am running into bugs with Llama-3.1-405B-Instruct-FP8 since version 0.7.0. The initial bug (could not even start the model) was probably fixed with https://github.com/vllm-project/vllm/pull/12696 that was in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Llama-3.1-405B-Instruct-FP8 only generates exclamation marks bug;stale ### Your current environment ### 🐛 Describe the bug Hi, I am running into bugs with Llama-3.1-405B-Instruct-FP8 since version 0.7.0. The init...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama-3.1-405B-Instruct-FP8 only generates exclamation marks bug;stale ### Your current environment ### 🐛 Describe the bug Hi, I am running into bugs with Llama-3.1-405B-Instruct-FP8 since version 0.7.0. The init...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: are_porting;model_support;quantization;sampling_logits cuda;fp8;operator;triton build_error dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ted_parallel;hardware_porting;model_support;quantization;sampling_logits cuda;fp8;operator;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

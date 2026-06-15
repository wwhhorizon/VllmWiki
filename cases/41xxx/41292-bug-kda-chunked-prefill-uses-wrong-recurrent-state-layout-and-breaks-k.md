# vllm-project/vllm#41292: [Bug]: KDA chunked prefill uses wrong recurrent state layout and breaks Kimi-linear long-context retrieval

| 字段 | 值 |
| --- | --- |
| Issue | [#41292](https://github.com/vllm-project/vllm/issues/41292) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;triton |
| 症状 | build_error;mismatch;nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KDA chunked prefill uses wrong recurrent state layout and breaks Kimi-linear long-context retrieval

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Kimi Delta Attention (KDA) chunked prefill appears to use an incorrect recurrent state layout after https://github.com/vllm-project/vllm/pull/33291 changed GDN/KDA state layout from `[N, HV, K, V]` to `[N, HV, V, K]`. This causes Kimi-linear long-context retrieval failures. Short prompts can remain coherent, but long prefill corrupts KDA state and causes the model to retrieve nearby filler text or start generic responses instead of the target phrase. I tested on both NVIDIA and AMD GPUs and the behaviors are the same. #### End-to-end symptom Using `moonshotai/Kimi-Linear-48B-A3B-Instruct`, [a needle retrieval test](https://github.com/yudigege86/vllm/blob/0c7b3ecf06acec26fa062ff3d8d1759894a3f911/scripts/kimi_linear_needle_repro.py) should output ``` COBALT PENGUIN WALKS AT DAWN ``` On v0.15.1 the output is correct. Bad versions (v0.16.0+, including v0.20.0) output generic/filler text such as: ``` The exact SECRET_PHRASE is: **FILLER 5793: ignore this line.** ``` First-token logprobs also show the difference before decode: Good v0.15.1: top token CO Bad v0.16.0+: top token The Layer instrumentation showed the first material diverge...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: v0.16.0+: top token The Layer instrumentation showed the first material divergence happens during prefill in layer 0 after KimiDeltaAttention; layer 0 norm1 is identical before KDA. **Minimal kernel-level test** I creat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: COBALT PENGUIN WALKS AT DAWN ``` On v0.15.1 the output is correct. Bad versions (v0.16.0+, including v0.20.0) output generic/filler text such as: ``` The exact SECRET_PHRASE is: **FILLER 5793: ignore this line.** ``` Fi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: es wrong recurrent state layout and breaks Kimi-linear long-context retrieval bug ### Your current environment ### 🐛 Describe the bug Kimi Delta Attention (KDA) chunked prefill appears to use an incorrect recurrent stat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: KDA chunked prefill uses wrong recurrent state layout and breaks Kimi-linear long-context retrieval bug ### Your current environment ### 🐛 Describe the bug Kimi Delta Attention (KDA) chunked prefill appears to us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

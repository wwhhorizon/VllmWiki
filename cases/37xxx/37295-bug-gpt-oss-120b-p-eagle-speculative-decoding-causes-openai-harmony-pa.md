# vllm-project/vllm#37295: [Bug] gpt-oss-120b + P-EAGLE speculative decoding causes openai_harmony parse errors and severe chat latency regression

| 字段 | 值 |
| --- | --- |
| Issue | [#37295](https://github.com/vllm-project/vllm/issues/37295) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] gpt-oss-120b + P-EAGLE speculative decoding causes openai_harmony parse errors and severe chat latency regression

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary When serving `openai/gpt-oss-120b` on one RTX6000 with our old baseline (no problems, stable) with speculative decoding (`p-eagle` drafter `amazon/gpt-oss-120b-p-eagle` which is a new approach (see vllm blog)) via vLLM OpenAI chat endpoint, I get repeated `openai_harmony.HarmonyError` during streaming and major mixed-workload latency/throughput regressions. Related https://github.com/vllm-project/vllm/issues/27626 and https://github.com/vllm-project/vllm/issues/22519 ## Baseline (stable and no HarmonyParser errors) Args (key): - `--max-model-len 131072` - `--max-num-batched-tokens 8192` - `--max-num-seqs 128` - `--long-prefill-token-threshold 100` - `--gpu-memory-utilization 0.95` - `--tool-call-parser openai` - `--enable-auto-tool-choice` - `--compilation-config {"pass_config":{"fuse_allreduce_rms":true,"eliminate_noops":true,"fuse_norm_quant":true,"fuse_act_quant":true,"enable_sp":true,"fuse_gemm_comms":true},"custom_ops":["+rms_norm"],"cudagraph_mode":"FULL_AND_PIECEWISE"}` ## Failing config (combined) Same as baseline + speculative: - `--speculative-config {"method":"eagle3","model":"amazon/gpt-oss-120b-p-eagle","n...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug] gpt-oss-120b + P-EAGLE speculative decoding causes openai_harmony parse errors and severe chat latency regression bug ### Your current environment ### 🐛 Describe the bug ## Summary When serving `openai/gpt-oss-120...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: speculative decoding causes openai_harmony parse errors and severe chat latency regression bug ### Your current environment ### 🐛 Describe the bug ## Summary When serving `openai/gpt-oss-120b` on one RTX6000 with our ol...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: (A/B result highlights) Fresh A/B in same cluster/time window: - recipe_2048_512: - baseline: total_tok/s=12830, p99_ttft=5646ms - speculative(2): total_tok/s=3888, p99_ttft=46487ms - thr_1k_512_c12: - baseline: 5373 to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 🐛 Describe the bug ## Summary When serving `openai/gpt-oss-120b` on one RTX6000 with our old baseline (no problems, stable) with speculative decoding (`p-eagle` drafter `amazon/gpt-oss-120b-p-eagle` which is a new appro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug] gpt-oss-120b + P-EAGLE speculative decoding causes openai_harmony parse errors and severe chat latency regression bug ### Your current environment ### 🐛 Describe the bug ## Summary When serving `openai/gpt-oss-120...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

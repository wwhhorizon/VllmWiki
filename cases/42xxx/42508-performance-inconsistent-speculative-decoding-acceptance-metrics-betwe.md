# vllm-project/vllm#42508: [Performance]: Inconsistent speculative decoding acceptance metrics between vLLM and SpecForge on Qwen3-32B baselines

| 字段 | 值 |
| --- | --- |
| Issue | [#42508](https://github.com/vllm-project/vllm/issues/42508) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Inconsistent speculative decoding acceptance metrics between vLLM and SpecForge on Qwen3-32B baselines

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am benchmarking speculative decoding baselines in vLLM and observed inconsistent acceptance metrics compared with SpecForge. I would like to understand whether this difference is expected due to different metric definitions, verification logic, benchmark prompt formatting, or whether it may indicate a configuration mismatch or a potential issue in the vLLM speculative decoding benchmark path. The target model is Qwen3-32B. I tested two speculative decoding baselines: Qwen3-32B with Eagle3-Qwen3-32B-zh, and Qwen3-32B with Qwen3-0.6B as a standalone draft model. In both cases, I set num_speculative_tokens to 3, used max concurrency / batch size 16, greedy decoding with temperature=0 and top_p=1.0, output length 1024, and the same full GSM8K test set with 1319 samples for both vLLM and SpecForge.My intention was to compare chain-style speculative decoding baselines, not tree-style candidate expansion. For the EAGLE3 baseline, I launched vLLM with the following command: VLLM_CACHE_ROOT=/root/.cache/vllm_eagle3_argmax_gpu0 \ SPEC_DECODE_MODE=baseline...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Performance]: Inconsistent speculative decoding acceptance metrics between vLLM and SpecForge on Qwen3-32B baselines performance ### Proposal to improve performance _No response_ ### Report of performance regression _N...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: }' The vLLM benchmark command was: vllm bench serve \ --backend openai \ --base-url http://127.0.0.1:8000 \ --endpoint /v1/completions \ --model Qwen3-32B \ --tokenizer /root/autodl-tmp/Qwen3-32B \ --dataset-name custom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: enchmark prompt formatting, or whether it may indicate a configuration mismatch or a potential issue in the vLLM speculative decoding benchmark path. The target model is Qwen3-32B. I tested two speculative decoding base...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: nt speculative decoding acceptance metrics between vLLM and SpecForge on Qwen3-32B baselines performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc disc...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

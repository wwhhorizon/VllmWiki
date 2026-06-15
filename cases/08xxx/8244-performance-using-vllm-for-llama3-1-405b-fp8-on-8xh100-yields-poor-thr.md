# vllm-project/vllm#8244: [Performance]: Using vLLM for Llama3.1 405b fp8 on 8xH100 yields poor throughput 

| 字段 | 值 |
| --- | --- |
| Issue | [#8244](https://github.com/vllm-project/vllm/issues/8244) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel |
| 症状 | build_error;mismatch;slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Using vLLM for Llama3.1 405b fp8 on 8xH100 yields poor throughput 

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Following the blog post [announcement](https://blog.vllm.ai/2024/07/23/llama31.html), I tried to replicate these numbers, but I got much lower throughput than what is reported. I used the Llama3.1 405b fp8 on an 8xH100 setup. I experimented with different total prompt count [32, 128, 256, 1024] and input vs output token lengths (both with [128, 256, 512, 1024]). The total number of generated tokens per second was at maximum ~700 tokens/sec, which is much lower than what is reported in the blog post above (roughly ~3100 tokens/sec). Also for prompt count of 1024 I get a panic with Cuda illegal memory access, which I would expect should not occur as the system should be able to manage running sequences, even for large queue lengths. ``` Prompt count: 32 Input Tokens: 128 Output Tokens: 512 Processed prompts: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 32/32 [00:48<00:00, 1.53s/it, est. speed input: 28.13 toks/s, output: 335.00 toks/s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` correctness ci_build;frontend_api;quantization cuda;fp8;kernel build_error...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: Using vLLM for Llama3.1 405b fp8 on 8xH100 yields poor throughput performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Following the blog post [announce...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: Using vLLM for Llama3.1 405b fp8 on 8xH100 yields poor throughput performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Following the blog post [announce...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: vLLM for Llama3.1 405b fp8 on 8xH100 yields poor throughput performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Following the blog post [announcement](https://blog.vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: Using vLLM for Llama3.1 405b fp8 on 8xH100 yields poor throughput performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Following the blog post [announce...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

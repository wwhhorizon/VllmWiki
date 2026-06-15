# vllm-project/vllm#26825: [Performance]: QuantFP8 `forward_native()` is on par or slower than `forward_cuda()` on a B200 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#26825](https://github.com/vllm-project/vllm/issues/26825) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: QuantFP8 `forward_native()` is on par or slower than `forward_cuda()` on a B200 GPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When disabling `QuantFP8` CUDA op on B200 architecture (e.g. https://github.com/vllm-project/vllm/pull/25545) and running with `forward_native()`, there are often no observable benefits of running with `forward_cuda()`. My particular scenario is sonnet benchmark on `Qwen/Qwen3-30B-A3B-FP8`. It would be useful to investigate why `forward_native()` brings no speedup in this scenario. Possible related issue: https://github.com/vllm-project/vllm/issues/25094 #### Server ``` vllm serve --model Qwen/Qwen3-30B-A3B-FP8 --max-model-len 2048 --disable-log-requests --tensor-parallel-size 1 --port 7557 ``` #### Queries ``` cd benchmarks vllm bench serve --host localhost --port 7557 --endpoint /v1/completions --model Qwen/Qwen3-30B-A3B-FP8 --num-prompts 100 --save-result --dataset-name sonnet --dataset-path sonnet.txt --sonnet-input-len 256 --sonnet-prefix-len 128 --sonnet-output-len 128 --request-rate 1 vllm bench serve --host localhost --port 7557 --endpoint /v1/completions --model Qwen/Qwen3-30B-A3B-FP8 --num-prompts 100 --save-result --dataset-name sonnet --dataset-path sonnet.txt --sonnet-input-len 512 --sonnet-prefix-len 256 --sonnet-ou...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;samp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: QuantFP8 `forward_native()` is on par or slower than `forward_cuda()` on a B200 GPU bug;stale ### Your current environment ### 🐛 Describe the bug When disabling `QuantFP8` CUDA op on B200 architecture (e....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: formance]: QuantFP8 `forward_native()` is on par or slower than `forward_cuda()` on a B200 GPU bug;stale ### Your current environment ### 🐛 Describe the bug When disabling `QuantFP8` CUDA op on B200 architecture (e.g. h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rd_native()` is on par or slower than `forward_cuda()` on a B200 GPU bug;stale ### Your current environment ### 🐛 Describe the bug When disabling `QuantFP8` CUDA op on B200 architecture (e.g. https://github.com/vllm-pro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: efits of running with `forward_cuda()`. My particular scenario is sonnet benchmark on `Qwen/Qwen3-30B-A3B-FP8`. It would be useful to investigate why `forward_native()` brings no speedup in this scenario. Possible relat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

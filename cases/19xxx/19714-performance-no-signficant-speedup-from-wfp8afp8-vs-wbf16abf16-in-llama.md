# vllm-project/vllm#19714: [Performance]: No signficant speedup from Wfp8Afp8 (vs Wbf16Abf16) in Llama-4 Scout

| 字段 | 值 |
| --- | --- |
| Issue | [#19714](https://github.com/vllm-project/vllm/issues/19714) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: No signficant speedup from Wfp8Afp8 (vs Wbf16Abf16) in Llama-4 Scout

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Dynamic FP8 quantization currently does not lead to significant speedup for Llama-4 Scout model in 8xH200 at smaller batch sizes. Both BF16 and FP8 checkpoints use fused Triton MoE kernel w/ tuned config. The table below reports p50 end-to-end latency in seconds using [benchmark_latency.py ](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_latency.py) script. | BS | input len | output len | meta-llama/Llama-4-Scout-17B-16E-Instruct | RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic | Speedup | | --- | --- | --- | ------------- | ------------- | ------------- | | 4 | 32 | 128 | 1.0608315134886652 | 1.0581926168175415 | 1.0x | | 8 | 32 | 128 | 1.1672972993692383 | 1.1296635085018352 | 1.03x | | 32 | 32 | 128 | 1.5841029789298773 | 1.4512220670003444 | 1.09x | | 8 | 10000 | 100 | 2.044864689465612 | 2.0477603524923325 | 0.099x | ``` python benchmark_latency.py \ --model meta-llama/Llama-4-Scout-17B-16E-Instruct \ --max-model-len 131072 \ --tensor-parallel-size 8 \ --input-len $IL \ --output-len $OL \ --batch-size $BS ``` ``` python benchmark_latency.py \ --model RedHatAI/Llama...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: oes not lead to significant speedup for Llama-4 Scout model in 8xH200 at smaller batch sizes. Both BF16 and FP8 checkpoints use fused Triton MoE kernel w/ tuned config. The table below reports p50 end-to-end latency in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: No signficant speedup from Wfp8Afp8 (vs Wbf16Abf16) in Llama-4 Scout performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Dynamic FP8 quantization curre...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: roposal to improve performance _No response_ ### Report of performance regression Dynamic FP8 quantization currently does not lead to significant speedup for Llama-4 Scout model in 8xH200 at smaller batch sizes. Both BF...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: No signficant speedup from Wfp8Afp8 (vs Wbf16Abf16) in Llama-4 Scout performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Dynamic FP8 quantization curre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

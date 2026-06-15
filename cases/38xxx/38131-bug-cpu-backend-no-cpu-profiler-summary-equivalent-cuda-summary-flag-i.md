# vllm-project/vllm#38131: [Bug]: [CPU Backend] No CPU profiler summary equivalent; CUDA summary flag is silently disabled on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#38131](https://github.com/vllm-project/vllm/issues/38131) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [CPU Backend] No CPU profiler summary equivalent; CUDA summary flag is silently disabled on CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the torch profiler with vLLM on CPU, there is no equivalent to the CUDA profiler summary (```self_cuda_time_total```) and instead, the existing flag ``` torch_profiler_dump_cuda_time_total=True``` is silently overridden to False on CPU, and no alternative CPU summary is written to file. As a result, users explicitly enabling profiler summary output do not get a corresponding CPU summary file and the behavior differs between CPU and GPU without clear documentation or warning. Minimal reproducer ``` python from vllm import LLM, SamplingParams from vllm.config import ProfilerConfig def main(): prof_cfg = ProfilerConfig( profiler="torch", torch_profiler_dir="/tmp/ignored", torch_profiler_dump_cuda_time_total=True, delay_iterations=0, warmup_iterations=0, active_iterations=1, wait_iterations=0, ) print("FRONTEND CONFIG:", prof_cfg, flush=True) llm = LLM( model="meta-llama/Llama-3.1-8B-Instruct", dtype="bfloat16", skip_tokenizer_init=False, trust_remote_code=True, tensor_parallel_size=1, max_model_len=448, max_num_seqs=2, max_num_batched_tokens=512, disable_log_stats=True, profiler_config=prof_cfg, ) sampling_params = Sampli...

## 现有链接修复摘要

#38324 [Bugfix] Preserve torch profiler summary output on CPU | #38366 [BugFix][CPU] Add CPU profiler summary file output | #38466 [Bugfix] Add CPU profiler summary equivalent to CUDA summary

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d no alternative CPU summary is written to file. As a result, users explicitly enabling profiler summary output do not get a corresponding CPU summary file and the behavior differs between CPU and GPU without clear docu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: llm = LLM( model="meta-llama/Llama-3.1-8B-Instruct", dtype="bfloat16", skip_tokenizer_init=False, trust_remote_code=True, tensor_parallel_size=1, max_model_len=448, max_num_seqs=2, max_num_batched_tokens=512, disable_
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mal reproducer ``` python from vllm import LLM, SamplingParams from vllm.config import ProfilerConfig def main(): prof_cfg = ProfilerConfig( profiler="torch", torch_profiler_dir="/tmp/ignored", torch_profiler_dump_cuda_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: [CPU Backend] No CPU profiler summary equivalent; CUDA summary flag is silently disabled on CPU bug;cpu ### Your current environment ### 🐛 Describe the bug When using the torch profiler with vLLM on CPU, there is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: [CPU Backend] No CPU profiler summary equivalent; CUDA summary flag is silently disabled on CPU bug;cpu ### Your current environment ### 🐛 Describe the bug When using the torch profiler with vLLM on CPU, there is...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38324](https://github.com/vllm-project/vllm/pull/38324) | closes_keyword | 0.95 | [Bugfix] Preserve torch profiler summary output on CPU | Fixes #38131. On the CPU backend, `torch_profiler_dump_cuda_time_total=True` was being silently overridden to `False` in `CpuPlatform.check_and_update_config`, which meant CPU t |
| [#38366](https://github.com/vllm-project/vllm/pull/38366) | closes_keyword | 0.95 | [BugFix][CPU] Add CPU profiler summary file output | Fixes #38131. Currently, when using torch profiler on CPU: - torch_profiler_dump_cuda_time_total is disabled internally - No equivalent CPU summary file is written - Only log |
| [#38466](https://github.com/vllm-project/vllm/pull/38466) | closes_keyword | 0.95 | [Bugfix] Add CPU profiler summary equivalent to CUDA summary | Fixes #38131 On CPU backends, `torch_profiler_dump_cuda_time_total` was silently overridden to `False` with no alternative CPU summary, leaving users without any human-readable pr |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#13674: [Bug]: Running ROCm support v1 vLLM Arch triggers ERROR_MEMORY_APERTURE_VIOLATION

| 字段 | 值 |
| --- | --- |
| Issue | [#13674](https://github.com/vllm-project/vllm/issues/13674) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Running ROCm support v1 vLLM Arch triggers ERROR_MEMORY_APERTURE_VIOLATION

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the following benchmarks bash script on MI300X, there are chances in encountering The following error ```bash :0:rocdevice.cpp :3018: 183469315192d us: Callback: Queue 0x7fb378200000 aborting with error : HSA[52/1890] RROR_MEMORY_APERTURE_VIOLATION: The agent attempted to access memory beyond the largest legal address. code: 0x29 ^CTraceback (most recent call last): File "/app/vllmv1test/benchmarks/benchmark_throughput.py", line 554, in main(args) File "/app/vllmv1test/benchmarks/benchmark_throughput.py", line 424, in main elapsed_time = run_vllm(requests, args.n, ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/app/vllmv1test/benchmarks/benchmark_throughput.py", line 198, in run_vllm llm.generate(prompts, File "/app/vllmv1test/vllm/utils.py", line 1057, in inner return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/app/vllmv1test/vllm/entrypoints/llm.py", line 470, in generate outputs = self._run_engine(use_tqdm=use_tqdm) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/app/vllmv1test/vllm/entrypoints/llm.py", line 1377, in _run_engine step_outputs = self.llm_engine.step() ^^^^^^^^^^^^^^^^^^^^^^ File "/app/vllmv1test/vllm/v1/engine/llm_...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Running ROCm support v1 vLLM Arch triggers ERROR_MEMORY_APERTURE_VIOLATION bug;stale ### Your current environment ### 🐛 Describe the bug When running the following benchmarks bash script on MI300X, there are chan...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ): File "/usr/local/lib/python3.12/dist-packages/torch/_inductor/async_compile.py", line 105, in shutdown_compile_worker s ``` The bash script ```bash declare -a in_len=( 128 512 1024 2048 ) declare -a out_len=( 128 256...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: g ROCm support v1 vLLM Arch triggers ERROR_MEMORY_APERTURE_VIOLATION bug;stale ### Your current environment ### 🐛 Describe the bug When running the following benchmarks bash script on MI300X, there are chances in encoun...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: rrent environment ### 🐛 Describe the bug When running the following benchmarks bash script on MI300X, there are chances in encountering The following error ```bash :0:rocdevice.cpp :3018: 183469315192d us: Callback: Que...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: TP="1" PREFIX="VLLM_USE_V1=1 VLLM_USE_TRITON_FLASH_ATTN=0 VLLM_USE_ROCM_FP8_FLASH_ATTN=1 CUDA_VISIBLE_DEVICES=7 HF_HUB_ENABLE_HF_TRANSFER=True HF_TOKEN=" SUFFIX=" >> ptpc_fp8_quantization_llama3170b-instruct-16384-vllmv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

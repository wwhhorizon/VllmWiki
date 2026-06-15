# vllm-project/vllm#20178: [Bug]: Failed profiling vllm (both offline and server) with Nsight Systems

| 字段 | 值 |
| --- | --- |
| Issue | [#20178](https://github.com/vllm-project/vllm/issues/20178) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed profiling vllm (both offline and server) with Nsight Systems

### Issue 正文摘录

### Your current environment `nsys` version info: ``` NVIDIA Nsight Systems version 2023.4.4.54-234433681190v0 ``` ### 🐛 Describe the bug ## **For offline inference:** According to [Official Docs](https://docs.vllm.ai/en/stable/contributing/profiling.html), I use the script below to start profiling: ``` bash SLURM_PARTITION=debug JOB_NAME=drh_profiling NUM_GPUS=1 CPUS_PER_GPU=24 MEM_PER_GPU=242144 NUM_CPUS=$(($NUM_GPUS * $CPUS_PER_GPU)) NUM_MEMS=$(($NUM_GPUS * $MEM_PER_GPU)) MAX_MODEL_LEN=10240 MODEL_PATH=/data/nfs/Qwen3-32B COMMAND="python ../benchmarks/benchmark_latency.py --model ${MODEL_PATH} --num-iters-warmup 5 --num-iters 1 --batch-size 16 --input-len 512 --output-len 8" NSYS_COMMAND="nsys profile -o report.nsys-rep --trace-fork-before-exec=true --cuda-graph-trace=node ${COMMAND}" srun --partition=${SLURM_PARTITION} \ --cpus-per-task=${NUM_CPUS} \ --mem=${NUM_MEMS} \ --gres=gpu:${NUM_GPUS} \ --job-name=${JOB_NAME} \ --nodes=1 \ --ntasks=1 \ -N 1 \ ${NSYS_COMMAND} ``` `../benchmarks/benchmark_latency.py` is the official benchmark script. The profiling fails with output: ``` [1/1] [================69% ] report.nsys-rep Importer error status: Importation failed. Import Failed...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: server) with Nsight Systems bug ### Your current environment `nsys` version info: ``` NVIDIA Nsight Systems version 2023.4.4.54-234433681190v0 ``` ### 🐛 Describe the bug ## **For offline inference:** According to [Offic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: Failed profiling vllm (both offline and server) with Nsight Systems bug ### Your current environment `nsys` version info: ``` NVIDIA Nsight Systems version 2023.4.4.54-234433681190v0 ``` ### 🐛 Describe the bug ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: COMMAND="nsys profile -o report.nsys-rep --trace-fork-before-exec=true --cuda-graph-trace=node ${COMMAND}" srun --partition=${SLURM_PARTITION} \ --cpus-per-task=${NUM_CPUS} \ --mem=${NUM_MEMS} \ --gres=gpu:${NUM_GPUS} \...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ($NUM_GPUS * $CPUS_PER_GPU)) NUM_MEMS=$(($NUM_GPUS * $MEM_PER_GPU)) MAX_MODEL_LEN=10240 MODEL_PATH=/data/nfs/Qwen3-32B COMMAND="python ../benchmarks/benchmark_latency.py --model ${MODEL_PATH} --num-iters-warmup 5 --num-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

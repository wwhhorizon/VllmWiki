# vllm-project/vllm#5792: [Performance]: Long AllReduce wait time on 1 device with tensor parallelism 

| 字段 | 值 |
| --- | --- |
| Issue | [#5792](https://github.com/vllm-project/vllm/issues/5792) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;kernel;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Long AllReduce wait time on 1 device with tensor parallelism 

### Issue 正文摘录

### Proposal to improve performance Propose synchronizing the broadcast of tensor_dict at the beginning of each decoding step or block the process after broadcast. ### Report of performance regression In the decoding stage, after matrix multiplications utilizing tensor parallelism, an all-reduce operation follows, which implicitly synchronizes the processes. However, the asynchronous broadcast of tensor dictionaries (code available [here](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/parallel_state.py#L484-L503)) at the start of each decoding step causes CUDA kernels to launch at quite different times across processes. This leads to the scenario depicted in the following image. ![image (12)](https://github.com/vllm-project/vllm/assets/25590028/6eb4f309-023f-40d1-aace-065fa4bc643d) and ![image (13)](https://github.com/vllm-project/vllm/assets/25590028/061caee8-7d09-41f2-b730-da27b36677ed) @youkaichao ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ``` CUDA_VISIBLE_DEVICES=0,1,2,3 nsys profile -t cuda,nvtx python benchmarks/benchmark_throughput.py --model=meta-llama/Meta-Llama-3-70B-Instruct --quantizatio...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ng step or block the process after broadcast. ### Report of performance regression In the decoding stage, after matrix multiplications utilizing tensor parallelism, an all-reduce operation follows, which implicitly sync...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: s/benchmark_throughput.py --model=meta-llama/Meta-Llama-3-70B-Instruct --quantization=fp8 --dataset=/workspace/sw3/vllm/ShareGPT_V3_unfiltered_cleaned_split.json --output-len=64 --num-prompts=50 --enforce-eager -tp=4 ``...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tilizing tensor parallelism, an all-reduce operation follows, which implicitly synchronizes the processes. However, the asynchronous broadcast of tensor dictionaries (code available [here](https://github.com/vllm-projec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: Long AllReduce wait time on 1 device with tensor parallelism performance;stale ### Proposal to improve performance Propose synchronizing the broadcast of tensor_dict at the beginning of each decoding step...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: g the broadcast of tensor_dict at the beginning of each decoding step or block the process after broadcast. ### Report of performance regression In the decoding stage, after matrix multiplications utilizing tensor paral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

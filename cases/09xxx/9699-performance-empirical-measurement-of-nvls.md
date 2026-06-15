# vllm-project/vllm#9699: [Performance]: Empirical Measurement of NVLS

| 字段 | 值 |
| --- | --- |
| Issue | [#9699](https://github.com/vllm-project/vllm/issues/9699) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Empirical Measurement of NVLS

### Issue 正文摘录

### Proposal to improve performance High-end GPUs like H100 and above have a hardware feature named [SHARP](https://docs.nvidia.com/networking/display/sharpv300). NCCL will automatically enable it when it is available. This issue describes my empirical measurement of the impact of NVLink Sharp. # When will NVLink Sharp be used? Running the test script from https://docs.vllm.ai/en/latest/getting_started/debugging.html#incorrect-hardware-driver , by increasing the number of GPUs, we can check if NVLS is enabled by finding this line in the log: `NCCL INFO NVLS comm 0x765a3b0 headRank 3 nHeads 8 buffSize 4194304 memSize 2097152 nvlsPerRankSize 301989888 nvlsTotalSize 2415919104` Through manual testing, it seems NVLS is only enabled for $n \gt 2$ GPUs, in H100 and above platforms (H100, H200, etc). # Performance Impact of Running Large Models Here I use 8 * H200 to run `meta-llama/Llama-3.1-405B` . The server command is: `vllm serve meta-llama/Llama-3.1-405B -tp 8 --load-format dummy --max-num-seqs 1024 --max_num_batched_tokens 1024 --disable-log-requests` The first difference I observe, is the memory usage and cudagraph capture time: | model=`meta-llama/Llama-3.1-405B` | Default (NVLS...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bove platforms (H100, H200, etc). # Performance Impact of Running Large Models Here I use 8 * H200 to run `meta-llama/Llama-3.1-405B` . The server command is: `vllm serve meta-llama/Llama-3.1-405B -tp 8 --load-format du...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: impact of NVLink Sharp. # When will NVLink Sharp be used? Running the test script from https://docs.vllm.ai/en/latest/getting_started/debugging.html#incorrect-hardware-driver , by increasing the number of GPUs, we can c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: erformance;stale ### Proposal to improve performance High-end GPUs like H100 and above have a hardware feature named [SHARP](https://docs.nvidia.com/networking/display/sharpv300). NCCL will automatically enable it when...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Empirical Measurement of NVLS performance;stale ### Proposal to improve performance High-end GPUs like H100 and above have a hardware feature named [SHARP](https://docs.nvidia.com/networking/display/sharp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lable. This issue describes my empirical measurement of the impact of NVLink Sharp. # When will NVLink Sharp be used? Running the test script from https://docs.vllm.ai/en/latest/getting_started/debugging.html#incorrect-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#25655: [Bug]: Scheduler assigns invalid physical_block_idx, leading to Segmentation Fault in CPU backend on RISC-V

| 字段 | 值 |
| --- | --- |
| Issue | [#25655](https://github.com/vllm-project/vllm/issues/25655) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Scheduler assigns invalid physical_block_idx, leading to Segmentation Fault in CPU backend on RISC-V

### Issue 正文摘录

### Your current environment - vLLM Version: Based on main branch + PR #20292 (which adds initial RISC-V support) - Hardware: Sophgo SG2044 (RISC-V 64-core) - Operating System: EulixOS 3.0 - Compiler: GCC 15.1 - Python: 3.11 - PyTorch: 2.8.0 ### 🐛 Describe the bug 1. Bug Description When running the `vllm bench throughput` benchmark on a RISC-V CPU backend (using code from PR \#20292), the process crashes with a segmentation fault after running successfully for a significant amount of time (processing hundreds of requests). Through an extensive, multi-day GDB debugging session, we have concluded that the bug is not in the low-level C++ attention kernel itself, but in the vLLM scheduler. The scheduler provides an out-of-bounds `physical_block_idx` in the `block_tables` tensor, which causes the C++ kernel to access invalid memory, leading to the crash. 2. Code to Reproduce the Problem The bug can be reliably reproduced by running the standard throughput benchmark with the following command: ```bash vllm bench throughput \ --model Qwen/Qwen1.5-0.5B \ --input-len 128 \ --output-len 128 \ --enforce-eager \ --dtype float16 \ --max_model_len 4096 \ --max_num_batched_tokens 4096 ``` 3. Ob...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ### 🐛 Describe the bug 1. Bug Description When running the `vllm bench throughput` benchmark on a RISC-V CPU backend (using code from PR \#20292), the process crashes with a segmentation fault after running successfully...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Fault in CPU backend on RISC-V bug ### Your current environment - vLLM Version: Based on main branch + PR #20292 (which adds initial RISC-V support) - Hardware: Sophgo SG2044 (RISC-V 64-core) - Operating System: EulixOS...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -0.5B \ --input-len 128 \ --output-len 128 \ --enforce-eager \ --dtype float16 \ --max_model_len 4096 \ --max_num_batched_tokens 4096 ``` 3. Observed Results and Debugging Analysis The program runs for several minutes,...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: `22307`, is abnormally large and clearly an out-of-bounds index for the KV cache blocks. - This confirms that for sequence \#258, the scheduler incorrectly assigned an invalid physical block index. When the C++ kernel `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: enchmark with the following command: ```bash vllm bench throughput \ --model Qwen/Qwen1.5-0.5B \ --input-len 128 \ --output-len 128 \ --enforce-eager \ --dtype float16 \ --max_model_len 4096 \ --max_num_batched_tokens 4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

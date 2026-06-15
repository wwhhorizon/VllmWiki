# vllm-project/vllm#17604: [Bug]: `size_k must divisible by BLOCK_SIZE_K` error when using tensor parallelism with AWQ-quantized MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#17604](https://github.com/vllm-project/vllm/issues/17604) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `size_k must divisible by BLOCK_SIZE_K` error when using tensor parallelism with AWQ-quantized MoE models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to use tensor parallelism with AWQ-quantized MoE models (specifically with Qwen3-30B-A3B-AWQ), I'm encountering issues with tensor parallelism. The behavior varies depending on the tensor parallel size: - TP=1: Works correctly - TP=2: Works correctly - TP=3, 5, 6, 7: Fast fails with `ValueError: Total number of attention heads (32) must be divisible by tensor parallel size` - TP=4, 8: Starts loading but fails during initialization with: ``` RuntimeError: Worker failed with error 'size_k must divisible by BLOCK_SIZE_K', please check the stack trace above for the root cause ``` ### Reproduction Steps 1. Clone the latest vLLM repo 2. Install with `pip install -e .` 3. Run the following command: ```bash python -m vllm.entrypoints.api_server \ --model CognitiveComputations/Qwen3-30B-A3B-AWQ \ --gpu-memory-utilization 0.9 \ --max-model-len 32768 \ --max-num-seqs 64 \ --tensor-parallel-size 4 \ --host 127.0.0.1 \ --port 8080 ``` ### Expected Behavior The model should load successfully with tensor parallelism. ### Actual Behavior For TP=4 and TP=8, the error occurs during model initialization in the fused_moe/fused_moe.py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: n attempting to use tensor parallelism with AWQ-quantized MoE models (specifically with Qwen3-30B-A3B-AWQ), I'm encountering issues with tensor parallelism. The behavior varies depending on the tensor parallel size: - T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: `size_k must divisible by BLOCK_SIZE_K` error when using tensor parallelism with AWQ-quantized MoE models bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to use tensor parallelism with AWQ-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: BLOCK_SIZE_K` error when using tensor parallelism with AWQ-quantized MoE models bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to use tensor parallelism with AWQ-quantized MoE models (spec...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: by BLOCK_SIZE_K` error when using tensor parallelism with AWQ-quantized MoE models bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to use tensor parallelism with AWQ-quantized MoE models (s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: divisible by BLOCK_SIZE_K` error when using tensor parallelism with AWQ-quantized MoE models bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to use tensor parallelism with AWQ-quantized MoE...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

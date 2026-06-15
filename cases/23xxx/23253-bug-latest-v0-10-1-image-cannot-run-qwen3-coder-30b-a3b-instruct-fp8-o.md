# vllm-project/vllm#23253: [Bug]: latest v0.10.1 image cannot run Qwen3-Coder-30B-A3B-Instruct-FP8 on 2xRTX5090

| 字段 | 值 |
| --- | --- |
| Issue | [#23253](https://github.com/vllm-project/vllm/issues/23253) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8;moe;operator |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: latest v0.10.1 image cannot run Qwen3-Coder-30B-A3B-Instruct-FP8 on 2xRTX5090

### Issue 正文摘录

### Your current environment latest docker image v0.10.1. env OS Ubuntu 25.04, 2xRTX5090, Driver Version: 580.65.06, V13.0.48 ### 🐛 Describe the bug Trying to run Qwen3-Coder-30B-A3B-Instruct-FP8 on dual 5090 with the latest 0.10.1 docker image ```sh docker run \ --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --shm-size=32gb --ipc=host \ vllm/vllm-openai:v0.10.1 \ --model Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 \ --enable-expert-parallel \ --gpu-memory-utilization 0.85 \ --max-model-len 65536 \ --tensor_parallel_size 2 \ --max-num-seqs 4 ``` And it crashes with the following error ```text File "/usr/local/lib/python3.12/dist-packages/vllm/_custom_ops.py", line 672, in cutlass_scaled_mm [1;36m(VllmWorker TP1 pid=189)[0;0m ERROR 08-20 03:19:43 [multiproc_executor.py:596] torch.ops._C.cutlass_scaled_mm(out, a, b, scale_a, scale_b, bias) [1;36m(VllmWorker TP1 pid=189)[0;0m ERROR 08-20 03:19:43 [multiproc_executor.py:596] File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1158, in __call__ [1;36m(VllmWorker TP1 pid=189)[0;0m ERROR 08-20 03:19:43 [multiproc_executor.py:596] return self._op(*args, **(kwargs or {})) [1;36m(VllmWorker...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: B-A3B-Instruct-FP8 on 2xRTX5090 bug ### Your current environment latest docker image v0.10.1. env OS Ubuntu 25.04, 2xRTX5090, Driver Version: 580.65.06, V13.0.48 ### 🐛 Describe the bug Trying to run Qwen3-Coder-30B-A3B-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: latest v0.10.1 image cannot run Qwen3-Coder-30B-A3B-Instruct-FP8 on 2xRTX5090 bug ### Your current environment latest docker image v0.10.1. env OS Ubuntu 25.04, 2xRTX5090, Driver Version: 580.65.06, V13.0.48 ###...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: latest v0.10.1 image cannot run Qwen3-Coder-30B-A3B-Instruct-FP8 on 2xRTX5090 bug ### Your current environment latest docker image v0.10.1. env OS Ubuntu 25.04, 2xRTX5090, Driver Version: 580.65.06, V13.0.48 ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ]: latest v0.10.1 image cannot run Qwen3-Coder-30B-A3B-Instruct-FP8 on 2xRTX5090 bug ### Your current environment latest docker image v0.10.1. env OS Ubuntu 25.04, 2xRTX5090, Driver Version: 580.65.06, V13.0.48 ### 🐛 De...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: nai:v0.10.1 \ --model Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 \ --enable-expert-parallel \ --gpu-memory-utilization 0.85 \ --max-model-len 65536 \ --tensor_parallel_size 2 \ --max-num-seqs 4 ``` And it crashes with the fo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

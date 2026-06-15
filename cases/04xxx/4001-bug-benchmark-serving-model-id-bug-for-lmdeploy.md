# vllm-project/vllm#4001: [Bug]: benchmark_serving model_id bug for lmdeploy

| 字段 | 值 |
| --- | --- |
| Issue | [#4001](https://github.com/vllm-project/vllm/issues/4001) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark_serving model_id bug for lmdeploy

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.1.2+cu118 CUDA used to build PyTorch: 11.8 OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 10.2.1 20210130 (Red Hat 10.2.1-11) Libc version: glibc-2.17 Python version: 3.9.16 (main, Aug 15 2023, 19:38:56) [GCC 8.3.1 20190311 (Red Hat 8.3.1-3)] (64-bit runtime) Python platform: Linux-4.18.0-147.mt20200626.413.el8_1.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 470.103.01 ``` ### 🐛 Describe the bug Hi @ywang96 Currently there is a small issue in [benchmarks/backend_request_func](https://github.com/vllm-project/vllm/blob/main/benchmarks/backend_request_func.py) when benchmark [LMDeploy](https://github.com/InternLM/lmdeploy) with [Llama-2-13b-chat-hf](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf). ``` # server python3 -m lmdeploy serve api_server /workdir/Llama-2-13b-chat-hf ``` ``` # client # https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_serving.py python3 benchmarks/benchmark_serving.py --backend lmdeploy --model...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: el_id bug for lmdeploy bug ### Your current environment ```text PyTorch version: 2.1.2+cu118 CUDA used to build PyTorch: 11.8 OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 10.2.1 20210130 (Red Hat 10.2.1-11) Lib...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: benchmark_serving model_id bug for lmdeploy bug ### Your current environment ```text PyTorch version: 2.1.2+cu118 CUDA used to build PyTorch: 11.8 OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 10.2.1 2021...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: benchmark_serving model_id bug for lmdeploy bug ### Your current environment ```text PyTorch version: 2.1.2+cu118 CUDA used to build PyTorch: 11.8 OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 10.2.1 2021...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: y bug ### Your current environment ```text PyTorch version: 2.1.2+cu118 CUDA used to build PyTorch: 11.8 OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 10.2.1 20210130 (Red Hat 10.2.1-11) Libc version: glibc-2.17...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ibe the bug Hi @ywang96 Currently there is a small issue in [benchmarks/backend_request_func](https://github.com/vllm-project/vllm/blob/main/benchmarks/backend_request_func.py) when benchmark [LMDeploy](https://github.c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

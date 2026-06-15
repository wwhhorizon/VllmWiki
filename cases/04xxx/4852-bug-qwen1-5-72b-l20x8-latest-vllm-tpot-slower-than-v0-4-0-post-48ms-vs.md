# vllm-project/vllm#4852: [Bug]: Qwen1.5-72B L20x8 latest vLLM TPOT slower than v0.4.0.post, 48ms vs 39ms, why?

| 字段 | 值 |
| --- | --- |
| Issue | [#4852](https://github.com/vllm-project/vllm/issues/4852) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen1.5-72B L20x8 latest vLLM TPOT slower than v0.4.0.post, 48ms vs 39ms, why?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.14 (main, Mar 21 2024, 16:24:04) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-240.el8.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 GPU 2: NVIDIA L20 GPU 3: NVIDIA L20 GPU 4: NVIDIA L20 GPU 5: NVIDIA L20 GPU 6: NVIDIA L20 GPU 7: NVIDIA L20 Nvidia driver version: 550.54.15 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.0.0 /usr/lib/x86_64...

## 现有链接修复摘要

#4794 [Frontend] Support OpenAI batch file format

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen1.5-72B L20x8 latest vLLM TPOT slower than v0.4.0.post, 48ms vs 39ms, why? bug ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Qwen1.5-72B L20x8 latest vLLM TPOT slower than v0.4.0.post, 48ms vs 39ms, why? bug ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Tsx async abort: Not affected Versions of relevant libraries: [pip3] flashinfer==0.0.4+cu121torch2.3 [pip3] mypy==1.9.0 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4794](https://github.com/vllm-project/vllm/pull/4794) | mentioned | 0.45 | [Frontend] Support OpenAI batch file format | 888.7(+[ 888.7]) other(ms): 47.2 latency(s): 3.20 ``` commit: #4794 bug |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

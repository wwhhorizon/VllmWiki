# vllm-project/vllm#39501: [Bug]: deep_gemm linked with cuda12 in cuda13 build

| 字段 | 值 |
| --- | --- |
| Issue | [#39501](https://github.com/vllm-project/vllm/issues/39501) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deep_gemm linked with cuda12 in cuda13 build

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ============================== Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.6 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13.0.88 [pip3] nvidia-cuda-runtime==13.0.96 [pip3] nvidia-cudnn-cu13==9.15.1.9 [pip3] nvidia-cudnn-frontend==1.18.0 [pip3] nvidia-cufft==12.0.0.61 [pip3] nvidia-cufile==1.15.1.6 [pip3] nvidia-curand==10.4.0.35 [pip3] nvidia-cusolver==12.0.4.66 [pip3] nvidia-cusparse==12.6.3.3 [pip3] nvidia-cusparselt-cu13==0.8.0 [pip3] nvidia-cutlass-dsl==4.4.2 [pip3] nvidia-cutlass-dsl-libs-base==4.4.2 [pip3] nvidia-ml-py==13.595.45 [pip3] nvidia-nccl-cu13==2.28.9 [pip3] nvidia-nvjitlink==13.0.88 [pip3] nvidia-nvshmem-cu13==3.4.5 [pip3] nvidia-nvtx==13.0.85 [pip3] pytorch-triton==3.5.1 [pip3] pyzmq==27.1.0 [pip3] torch==2.10.0+cu130 [pip3] torch-c-dlpack-ext==0.1.5 [pip3] torch-memory-saver==0.0.9 [pip3] torchao==0.15.0+cu130 [pip3] torchaudio==2.10.0+cu130 [pip3] torchcodec==0.8.0+cu130 [pip3] torchvision==0.25.0+cu130 [pip3] transformers==4.57.6 [pip3] triton==3.6.0 ### Before submitting a new issue... - [x] Mak...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: deep_gemm linked with cuda12 in cuda13 build bug ### Your current environment ### 🐛 Describe the bug ============================== Versions of relevant libraries ============================== [pip3] flashinfer-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.6 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13.0.88 [p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: deep_gemm linked with cuda12 in cuda13 build bug ### Your current environment ### 🐛 Describe the bug ============================== Versions of relevant libraries ============================== [pip3] flashinfer-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: deep_gemm linked with cuda12 in cuda13 build bug ### Your current environment ### 🐛 Describe the bug ============================== Versions of relevant libraries ============================== [pip3] flashinfer-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear cuda;triton build_...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

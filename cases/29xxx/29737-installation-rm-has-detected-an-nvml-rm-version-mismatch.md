# vllm-project/vllm#29737: [Installation]: RM has detected an NVML/RM version mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#29737](https://github.com/vllm-project/vllm/issues/29737) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: RM has detected an NVML/RM version mismatch

### Issue 正文摘录

### Your current environment ```text infrastrcture： x86_64 CPU ： 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual CPU: 48 ID： GenuineIntel Name： Intel(R) Xeon(R) Silver 4214R CPU @ 2.40GHz Vulnerability Srbds: Not affected Vulnerability Tsx async abort: Mitigation; TSX disabled ============================== Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-cu12==12.8.93 [pip3] nvidia-cuda-runtime-cu12==12.8.90 [pip3] nvidia-cudnn-cu12==9.10.2.21 [pip3] nvidia-cudnn-frontend==1.16.0 [pip3] nvidia-cufft-cu12==11.3.3.83 [pip3] nvidia-cufile-cu12==1.13.1.3 [pip3] nvidia-curand-cu12==10.3.9.90 [pip3] nvidia-cusolver-cu12==11.7.3.90 [pip3] nvidia-cusparse-cu12==12.5.8.93 [pip3] nvidia-cusparselt-cu12==0.7.1 [pip3] nvidia-cutlass-dsl==4.3.1 [pip3] nvidia-ml-py==13.580.82 [pip3] nvidia-nccl-cu12==2.27.5 [pip3] nvidia-nvjitlink-cu12==12.8.93 [pip3] nvidia-nvshmem-cu12==3.3.20 [pip3] nvidia-nvtx-cu12==12.8.90 [pip3] pyzmq==27.1.0 [pip3] torch==2.9.0+cu128 [pip3] torchaudio==2.9.0+cu128 [pip3] torchvision==0.24.0+c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: RM has detected an NVML/RM version mismatch installation;stale ### Your current environment ```text infrastrcture： x86_64 CPU ： 32-bit, 64-bit Address si
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Installation]: RM has detected an NVML/RM version mismatch installation;stale ### Your current environment ```text infrastrcture： x86_64 CPU ： 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: CHECK=1 TORCHINDUCTOR_COMPILE_THREADS=1 ``` the host machine is running ollama well with info ``` time=2025-11-30T07:24:49.679+08:00 level=INFO source=gpu.go:217 msg="looking for compatible GPUs" time=2025-11-30T07:24:5...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Installation]: RM has detected an NVML/RM version mismatch installation;stale ### Your current environment ```text infrastrcture： x86_64 CPU ： 32-bit, 64-bit Address sizes: 46 bits physical, 48 bit

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

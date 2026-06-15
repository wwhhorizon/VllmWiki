# vllm-project/vllm#25336: [Bug]: metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#25336](https://github.com/vllm-project/vllm/issues/25336) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;triton |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: metrics

### Issue 正文摘录

### Your current environment ============================== Versions of relevant libraries ============================== [pip3] numpy==2.2.5 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12==12.6.80 [pip3] nvidia-cuda-nvrtc-cu12==12.6.77 [pip3] nvidia-cuda-runtime-cu12==12.6.77 [pip3] nvidia-cudnn-cu12==9.5.1.17 [pip3] nvidia-cufft-cu12==11.3.0.4 [pip3] nvidia-cufile-cu12==1.11.1.6 [pip3] nvidia-curand-cu12==10.3.7.77 [pip3] nvidia-cusolver-cu12==11.7.1.2 [pip3] nvidia-cusparse-cu12==12.5.4.2 [pip3] nvidia-cusparselt-cu12==0.6.3 [pip3] nvidia-ml-py==12.560.30 [pip3] nvidia-nccl-cu12==2.26.2 [pip3] nvidia-nvjitlink-cu12==12.6.85 [pip3] nvidia-nvtx-cu12==12.6.77 [pip3] pyzmq==26.2.0 [pip3] torch==2.7.1 [pip3] torchaudio==2.7.1 [pip3] torchvision==0.22.1 [pip3] transformers==4.56.2 [pip3] triton==3.3.1 [conda] blas 1.0 mkl [conda] mkl 2023.1.0 h213fc3f_46344 [conda] mkl-service 2.4.0 py310h5eee18b_2 [conda] mkl_fft 1.3.11 py310h5eee18b_0 [conda] mkl_random 1.2.8 py310h1128e8f_0 [conda] numpy 2.2.6 pypi_0 pypi [conda] numpy-base 2.2.5 py310h06ae042_0 [conda] nvidia-cublas-cu12 12.6.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.6.80 pypi_0 pypi [conda] nvidia-cuda...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: s bug;stale ### Your current environment ============================== Versions of relevant libraries ============================== [pip3] numpy==2.2.5 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: == [pip3] numpy==2.2.5 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12==12.6.80 [pip3] nvidia-cuda-nvrtc-cu12==12.6.77 [pip3] nvidia-cuda-runtime-cu12==12.6.77 [pip3] nvidia-cudnn-cu12==9.5.1.17 [pip3]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: metrics bug;stale ### Your current environment ============================== Versions of relevant libraries ============================== [pip3] numpy==2.2.5 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ntial performance metrics like Time To First Token (TTFT) and end-to-end latency for individual requests. According to previous versions and documentation, this attribute is expected to be a populated Metric object. **E...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.7.1 [pip3] torchvision==0.22.1 [pip3] transformers==4.56.2 [pip3] triton==3.3.1 [conda] blas 1.0 mkl [conda] mkl 2023.1.0 h213fc3f_46344 [conda] mkl-service 2.4.0 py310h5eee18b_2 [c

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

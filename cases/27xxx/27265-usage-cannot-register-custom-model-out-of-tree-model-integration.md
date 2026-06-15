# vllm-project/vllm#27265: [Usage]: Cannot register custom model (Out-of-Tree Model Integration)

| 字段 | 值 |
| --- | --- |
| Issue | [#27265](https://github.com/vllm-project/vllm/issues/27265) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;triton |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Cannot register custom model (Out-of-Tree Model Integration)

### Issue 正文摘录

``` ### Your current environment ============================== Versions of relevant libraries ============================== [pip3] flake8==7.1.1 [pip3] flashinfer==0.1.6+cu124torch2.4 [pip3] flashinfer-python==0.2.5 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.2.1.3 [pip3] nvidia-curand-cu12==10.3.5.147 [pip3] nvidia-cusolver-cu12==11.6.1.9 [pip3] nvidia-cusparse-cu12==12.3.1.170 [pip3] nvidia-cusparselt-cu12==0.6.2 [pip3] nvidia-ml-py==12.560.30 [pip3] nvidia-modelopt==0.31.0 [pip3] nvidia-modelopt-core==0.31.0 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] pynvml==12.0.0 [pip3] pyzmq==26.2.0 [pip3] sentence-transformers==3.3.1 [pip3] torch==2.6.0 [pip3] torch_memory_saver==0.0.6 [pip3] torchao==0.9.0 [pip3] torchaudio==2.6.0 [pip3] torchdata==0.11.0 [pip3] torchprofile==0.0.4 [pip3] torchtext==0.18.0 [pip3] torchvision==0.21.0 [pip3] transformer_engine_torch==2.3.0 [pip3] transformers==4.5...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ) usage ``` ### Your current environment ============================== Versions of relevant libraries ============================== [pip3] flake8==7.1.1 [pip3] flashinfer==0.1.6+cu124torch2.4 [pip3] flashinfer-python=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Cannot register custom model (Out-of-Tree Model Integration) usage ``` ### Your current environment ============================== Versions of relevant libraries ============================== [pip3] flake8==7....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ant libraries ============================== [pip3] flake8==7.1.1 [pip3] flashinfer==0.1.6+cu124torch2.4 [pip3] flashinfer-python==0.2.5 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: hao==0.9.0 [pip3] torchaudio==2.6.0 [pip3] torchdata==0.11.0 [pip3] torchprofile==0.0.4 [pip3] torchtext==0.18.0 [pip3] torchvision==0.21.0 [pip3] transformer_engine_torch==2.3.0 [pip3] transformers==4.51.1 [pip3] trito...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

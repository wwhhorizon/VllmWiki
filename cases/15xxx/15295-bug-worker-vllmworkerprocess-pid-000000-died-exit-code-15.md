# vllm-project/vllm#15295: [Bug]: Worker VllmWorkerProcess pid 000000 died, exit code: -15

| 字段 | 值 |
| --- | --- |
| Issue | [#15295](https://github.com/vllm-project/vllm/issues/15295) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Worker VllmWorkerProcess pid 000000 died, exit code: -15

### Issue 正文摘录

### Your current environment [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.2.1.3 [pip3] nvidia-curand-cu12==10.3.5.147 [pip3] nvidia-cusolver-cu12==11.6.1.9 [pip3] nvidia-cusparse-cu12==12.3.1.170 [pip3] nvidia-cusparselt-cu12==0.6.2 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] pyzmq==26.3.0 [pip3] torch==2.6.0 [pip3] torchaudio==2.6.0 [pip3] torchvision==0.21.0 [pip3] transformers==4.50.0.dev0 [pip3] triton==3.2.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127 pypi_0 pypi [conda] nvidia-cuda-nvrtc-cu12 12.4.127 pypi_0 pypi [conda] nvidia-cuda-runtime-cu12 12.4.127 pypi_0 pypi [conda] nvidia-cudnn-cu12 9.1.0.70 pypi_0 pypi [conda] nvidia-cufft-cu12 11.2.1.3 pypi_0 pypi [conda] nvidia-curand-cu12 10.3.5.147 pypi_0 pypi [conda] nvidia-cusolver-cu12 11.6.1.9 pypi_0 pypi [conda] nvidia-cusparse-cu12 12.3.1.170 pypi_0 pypi [conda] nvidia-cusparselt-cu12...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: usparselt-cu12==0.6.2 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] pyzmq==26.3.0 [pip3] torch==2.6.0 [pip3] torchaudio==2.6.0 [pip3] torchvision==0.21.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ypi ### 🐛 Describe the bug from vllm import LLM llm = LLM( "google/gemma-3-27b-it", tensor_parallel_size=4, dtype="half", trust_remote_code=True, tokenizer_mode="auto", gpu_memory_utilization=0.7, # Lower utilization ma...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2.6.0 [pip3] torchvision==0.21.0 [pip3] transformers==4.50.0.dev0 [pip3] triton==3.2.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: llm = LLM( "google/gemma-3-27b-it", tensor_parallel_size=4, dtype="half", trust_remote_code=True, tokenizer_mode="auto", gpu_memory_utilization=0.7, # Lower utilization max_model_len=2048, # Reduce context length enforc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

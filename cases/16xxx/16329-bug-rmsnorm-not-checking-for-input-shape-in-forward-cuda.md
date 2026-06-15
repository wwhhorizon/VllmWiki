# vllm-project/vllm#16329: [Bug]: RMSNorm not checking for input shape in forward_cuda

| 字段 | 值 |
| --- | --- |
| Issue | [#16329](https://github.com/vllm-project/vllm/issues/16329) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;distributed_parallel;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | activation;cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RMSNorm not checking for input shape in forward_cuda

### Issue 正文摘录

### Your current environment PyTorch version: 2.6.0+cu124 Nvidia driver version: 535.161.08 vLLM Version: 0.8.3 [pip3] flashinfer-python==0.2.5+cu124torch2.6 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.2.1.3 [pip3] nvidia-curand-cu12==10.3.5.147 [pip3] nvidia-cusolver-cu12==11.6.1.9 [pip3] nvidia-cusparse-cu12==12.3.1.170 [pip3] nvidia-cusparselt-cu12==0.6.2 [pip3] nvidia-ml-py==12.570.86 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] pynvml==12.0.0 [pip3] pyzmq==26.4.0 [pip3] torch==2.6.0+cu124 [pip3] torchaudio==2.6.0+cu124 [pip3] torchvision==0.21.0+cu124 [pip3] transformers==4.51.0 [pip3] triton==3.2.0 [conda] flashinfer-python 0.2.5+cu124torch2.6 pypi_0 pypi [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127 pypi_0 pypi [conda] nvidia-cuda-nvrtc-cu12 12.4.127 pypi_0 pypi [conda] nvidia-cuda-runtime-cu12 12.4.127 pypi_0 pypi [conda] nvidia-cudnn-cu1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ut shape in forward_cuda bug;stale ### Your current environment PyTorch version: 2.6.0+cu124 Nvidia driver version: 535.161.08 vLLM Version: 0.8.3 [pip3] flashinfer-python==0.2.5+cu124torch2.6 [pip3] numpy==1.26.4 [pip3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RMSNorm not checking for input shape in forward_cuda bug;stale ### Your current environment PyTorch version: 2.6.0+cu124 Nvidia driver version: 535.161.08 vLLM Version: 0.8.3 [pip3] flashinfer-python==0.2.5+cu124...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2.6.0+cu124 Nvidia driver version: 535.161.08 vLLM Version: 0.8.3 [pip3] flashinfer-python==0.2.5+cu124torch2.6 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: he input shape when using forward_cuda ```python import torch from vllm.model_executor.layers.layernorm import RMSNorm if __name__ == "__main__": norm = RMSNorm(128, eps=1e-5) x = torch.randn(256).cuda() print(norm.forw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: RMSNorm not checking for input shape in forward_cuda bug;stale ### Your current environment PyTorch version: 2.6.0+cu124 Nvidia driver version: 535.161.08 vLLM Version: 0.8.3 [pip3] flashinfer-python==0.2.5+cu124...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

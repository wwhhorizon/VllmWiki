# vllm-project/vllm#15672: [Usage]: torchrun data parallel and tensor parallel at the same time

| 字段 | 值 |
| --- | --- |
| Issue | [#15672](https://github.com/vllm-project/vllm/issues/15672) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: torchrun data parallel and tensor parallel at the same time

### Issue 正文摘录

### Your current environment ``` Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.2.1.3 [pip3] nvidia-curand-cu12==10.3.5.147 [pip3] nvidia-cusolver-cu12==11.6.1.9 [pip3] nvidia-cusparse-cu12==12.3.1.170 [pip3] nvidia-cusparselt-cu12==0.6.2 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] torch==2.6.0 [pip3] torchaudio==2.6.0 [pip3] torchvision==0.21.0 [pip3] triton==3.2.0 Name: vllm Version: 0.8.3.dev77+gb4245a48 [conda] cuda-cudart 12.4.127 h99ab3db_0 [conda] cuda-cudart-dev 12.4.127 h99ab3db_0 [conda] cuda-cudart-dev_linux-64 12.4.127 hd681fbe_0 [conda] cuda-cudart-static 12.4.127 h99ab3db_0 [conda] cuda-cudart-static_linux-64 12.4.127 hd681fbe_0 [conda] cuda-cudart_linux-64 12.4.127 hd681fbe_0 [conda] cuda-cupti 12.4.127 h6a678d5_1 [conda] cuda-cupti-dev 12.4.127 h6a678d5_1 [conda] cuda-libraries 12.4.1 h06a4308_1 [conda] cuda-libraries-dev 12.4.1 h06a4308_1 [conda] cuda-nvrtc 12.4.127 h99ab3d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: parallel at the same time usage;stale ### Your current environment ``` Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: torch==2.6.0 [pip3] torchaudio==2.6.0 [pip3] torchvision==0.21.0 [pip3] triton==3.2.0 Name: vllm Version: 0.8.3.dev77+gb4245a48 [conda] cuda-cudart 12.4.127 h99ab3db_0 [conda] cuda-cudart-dev 12.4.127 h99ab3db_0 [conda]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: oth data-parallel and tensor-parallel. Specifically, I want to split the model into two cards and run 4 processes. So in my understanding, it will be 4 data parallel, and each process use two cards. I should use torchru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sage]: torchrun data parallel and tensor parallel at the same time usage;stale ### Your current environment ``` Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

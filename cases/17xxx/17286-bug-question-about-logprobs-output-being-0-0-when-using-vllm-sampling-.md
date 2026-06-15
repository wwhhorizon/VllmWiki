# vllm-project/vllm#17286: [Bug]:Question about logprobs output being 0.0 when using `vllm` sampling params

| 字段 | 值 |
| --- | --- |
| Issue | [#17286](https://github.com/vllm-project/vllm/issues/17286) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:Question about logprobs output being 0.0 when using `vllm` sampling params

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` ```text [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.2.1.3 [pip3] nvidia-curand-cu12==10.3.5.147 [pip3] nvidia-cusolver-cu12==11.6.1.9 [pip3] nvidia-cusparse-cu12==12.3.1.170 [pip3] nvidia-dali-cuda120==1.35.0 [pip3] nvidia-ml-py==12.560.30 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] nvidia-pyindex==1.0.9 [pip3] onnx==1.15.0rc2 [pip3] optree==0.10.0 [pip3] pynvml==11.4.1 [pip3] pytorch-quantization==2.1.2 [pip3] pytorch-triton==2.2.0+e28a256d7 [pip3] pyzmq==25.1.2 [pip3] torch==2.5.1 [pip3] torch-tensorrt==2.3.0a0 [pip3] torchdata==0.7.1a0 [pip3] torchtext==0.17.0a0 [pip3] torchvision==0.20.1 [pip3] transformers==4.48.0 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.6 ``` ### 🐛 Describe the bug **Title**: Question about logprobs output being 0.0 when using `vllm` sampling params **...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: idia-ml-py==12.560.30 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] nvidia-pyindex==1.0.9 [pip3] onnx==1.15.0rc2 [pip3] optree==0.10.0 [pip3] pynvml==11....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: on about logprobs output being 0.0 when using `vllm` sampling params bug;stale ### Your current environment The output of `python collect_env.py` ```text [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] n...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] pynvml==11.4.1 [pip3] pytorch-quantization==2.1.2 [pip3] pytorch-triton==2.2.0+e28a256d7 [pip3] pyzmq==25.1.2 [pip3] torch==2.5.1 [pip3] torch-tensorrt==2.3.0a0 [pip3] torchdata==0.7.1a0 [pip3] torchtext==0.17.0a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nx==1.15.0rc2 [pip3] optree==0.10.0 [pip3] pynvml==11.4.1 [pip3] pytorch-quantization==2.1.2 [pip3] pytorch-triton==2.2.0+e28a256d7 [pip3] pyzmq==25.1.2 [pip3] torch==2.5.1 [pip3] torch-tensorrt==2.3.0a0 [pip3] torchdat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

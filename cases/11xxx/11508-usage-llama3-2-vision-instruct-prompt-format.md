# vllm-project/vllm#11508: [Usage]: Llama3.2 Vision Instruct prompt format

| 字段 | 值 |
| --- | --- |
| Issue | [#11508](https://github.com/vllm-project/vllm/issues/11508) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Llama3.2 Vision Instruct prompt format

### Issue 正文摘录

### Your current environment Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.2.1.3 [pip3] nvidia-curand-cu12==10.3.5.147 [pip3] nvidia-cusolver-cu12==11.6.1.9 [pip3] nvidia-cusparse-cu12==12.3.1.170 [pip3] nvidia-ml-py==12.560.30 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] pyzmq==26.2.0 [pip3] torch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.46.2 [pip3] triton==3.1.0 ### How would you like to use vllm I want to run inference of a [Llama3.2 Vision Instruct model](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct). In the [Meta's prompt guide](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/vision_prompt_format.md) they said that > Its important to postion the tag appropriately in the prompt. Image will only attend to the subsequent text tokens that means in the prompt, I shoud have format like this {content": [{"type": "image"}, {"type": "text"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ama3.2 Vision Instruct prompt format usage ### Your current environment Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Llama3.2 Vision Instruct prompt format usage ### Your current environment Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.46.2 [pip3] triton==3.1.0 ### How would you like to use vllm I want to run inference of a [Llama3.2 Vision Instruct model](https://huggingface.co/meta-llama/L...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;model_support cuda;triton env_dependency Your curren...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#7797: [Bug]: my vllm phi-3-vision server runs one request correctly then returns an error for the same request stating 2509 image tokens to 0 placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#7797](https://github.com/vllm-project/vllm/issues/7797) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: my vllm phi-3-vision server runs one request correctly then returns an error for the same request stating 2509 image tokens to 0 placeholders

### Issue 正文摘录

### 🐛 Describe the bug I deployed a basic vllm multi-modal server with `phi-3-vision`, that seems to run well at first, i.e my first request is correctly executed, but at the very moment i send a second request i get an internal server error 500, and this output `ERROR:__main__:Error during generation: Attempted to assign 1 x 2509 = 2509 image tokens to 0 placeholders` while sending the same request a second time. ![Capture d’écran 2024-08-23 à 00 50 33](https://github.com/user-attachments/assets/71109a75-d476-4c91-a85d-4eb3978f5db5) ## Your current environment PyTorch version: 2.3.1+cu121 OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 ## Versions of relevant libraries: [pip3] numpy==1.24.4 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvidia-cuda-nvrtc-cu12==12.1.105 [pip3] nvidia-cuda-runtime-cu12==12.1.105 [pip3] nvidia-cudnn-cu12==8.9.2.26 [pip3] nvidia-cufft-cu12==11.0.2.54 [pip3] nvidia-curand-cu12==10.3.2.106 [pip3] nvidia-cusolver-cu12==11.4.5.107 [pip3] nvidia-cusparse-cu12==12.1.0.106 [pip3] nvidia-ml-py==12.555.43 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] nvidia-nvjitlink-cu12==12.5.82 [pip3] nvidia...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 109a75-d476-4c91-a85d-4eb3978f5db5) ## Your current environment PyTorch version: 2.3.1+cu121 OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 ## Versions of relevant libraries: [pip3] n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : [pip3] numpy==1.24.4 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvidia-cuda-nvrtc-cu12==12.1.105 [pip3] nvidia-cuda-runtime-cu12==12.1.105 [pip3] nvidia-cudnn-cu12==8.9.2.26 [pi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.43.2 [pip3] triton==2.3.1 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.3.post1@38c4b7e863570a045308af81...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: my vllm phi-3-vision server runs one request correctly then returns an error for the same request stating 2509 image tokens to 0 placeholders bug ### 🐛 Describe the bug I deployed a basic vllm multi-modal server...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

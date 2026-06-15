# vllm-project/vllm#10290: [Feature]: Chunked prefill for multimodal models

| 字段 | 值 |
| --- | --- |
| Issue | [#10290](https://github.com/vllm-project/vllm/issues/10290) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Chunked prefill for multimodal models

### Issue 正文摘录

### Your current environment [pip3] numpy==1.25.1 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.2.1.3 [pip3] nvidia-curand-cu12==10.3.5.147 [pip3] nvidia-cusolver-cu12==11.6.1.9 [pip3] nvidia-cusparse-cu12==12.3.1.170 [pip3] nvidia-ml-py==12.560.30 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] pyzmq==26.2.0 [pip3] torch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.46.2 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.3.post2.dev280+ge036e527 ### Model Input Dumps [err_execute_model_input_20241113-062507.zip](https://github.com/user-attachments/files/17728816/err_execute_model_input_20241113-062507.zip) ### 🐛 Describe the bug When the multimodal model uses ```chunked prefill``` for inference, if the number of tokens exceeds ```num_max_batched_tokens```, the available prefill slots are not enough for the multimodal placeholders. It will occur an error in ```merge...

## 现有链接修复摘要

#8425 [Hotfix][Core][VLM] Disable chunked prefill by default and prefix caching for multimodal models

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: idia-ml-py==12.560.30 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] pyzmq==26.2.0 [pip3] torch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [pip3] numpy==1.25.1 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Chunked prefill for multimodal models feature request;stale ### Your current environment [pip3] numpy==1.25.1 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Chunked prefill for multimodal models feature request;stale ### Your current environment [pip3] numpy==1.25.1 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.46.2 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.3.post2.dev280+ge036e527 ### Mod...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8425](https://github.com/vllm-project/vllm/pull/8425) | mentioned | 0.45 | [Hotfix][Core][VLM] Disable chunked prefill by default and prefix caching for multimodal models | assign 9 x 576 = 5184 multimodal tokens to 4879 placeholders ``` pr #8425 and #8346 want to solve this problem, and haved been merged. so i use the vllm nightly version. but i fou… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

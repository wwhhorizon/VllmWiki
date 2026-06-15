# vllm-project/vllm#18392: [Performance]: Low GPU Utilization (70%) for ViT+Qwen2 VLM Model.

| 字段 | 值 |
| --- | --- |
| Issue | [#18392](https://github.com/vllm-project/vllm/issues/18392) |
| 状态 | closed |
| 标签 | performance;unstale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Low GPU Utilization (70%) for ViT+Qwen2 VLM Model.

### Issue 正文摘录

### Proposal to improve performance x ### Report of performance regression I am benchmarking a custom model with a VLM structure consisting of ViT + Qwen2. During stress testing, I found that the GPU utilization reaches only 70%. Using the PyTorch profiler, I noticed that each iteration has a 2ms period at the start of Qwen2-forward that doesn't call CUDA. What is this period doing, and can it be optimized? My Qwen2 model is relatively small at 0.5B. ![Image](https://github.com/user-attachments/assets/cba784f5-1932-48a8-b2d2-b5168baee183) My scripts: ```bash vllm serve /custom_model --gpu-memory-utilization 0.8 --port 8523 --max_model_len 4096 --max_num_seqs 256 --limit-mm-per-prompt image=1 --disable-log-requests ``` benchmark scripts with --request-rate=20 trace here: https://drive.google.com/file/d/1pGWAH5j2VXviumqH9LRw7jm182_nAlBK/view?usp=drive_link What are the possible reasons or parameters that could improve performance? Thanks！ ### Misc discussion on performance x ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` INFO 05-20 07:17:33 [__init__.py:248] Automatically detected platform cuda. Collecting environment inform...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: drive.google.com/file/d/1pGWAH5j2VXviumqH9LRw7jm182_nAlBK/view?usp=drive_link What are the possible reasons or parameters that could improve performance? Thanks！ ### Misc discussion on performance x ### Your current env...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Performance]: Low GPU Utilization (70%) for ViT+Qwen2 VLM Model. performance;unstale ### Proposal to improve performance x ### Report of performance regression I am benchmarking a custom model with a VLM structure cons...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: eration has a 2ms period at the start of Qwen2-forward that doesn't call CUDA. What is this period doing, and can it be optimized? My Qwen2 model is relatively small at 0.5B. ![Image](https://github.com/user-attachments...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: nstale ### Proposal to improve performance x ### Report of performance regression I am benchmarking a custom model with a VLM structure consisting of ViT + Qwen2. During stress testing, I found that the GPU utilization...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: dio==2.7.0 [pip3] torchvision==0.22.0 [pip3] transformers==4.51.3 [pip3] triton==3.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.6.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.6.80

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

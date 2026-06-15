# vllm-project/vllm#8564: [Bug]: Issue when benchmarking the dynamically served LoRA adapter 

| 字段 | 值 |
| --- | --- |
| Issue | [#8564](https://github.com/vllm-project/vllm/issues/8564) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue when benchmarking the dynamically served LoRA adapter 

### Issue 正文摘录

### My current environment ````text [pip3] numpy==2.1.1 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvidia-cuda-nvrtc-cu12==12.1.105 [pip3] nvidia-cuda-runtime-cu12==12.1.105 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.0.2.54 [pip3] nvidia-curand-cu12==10.3.2.106 [pip3] nvidia-cusolver-cu12==11.4.5.107 [pip3] nvidia-cusparse-cu12==12.1.0.106 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] nvidia-nvjitlink-cu12==12.6.68 [pip3] nvidia-nvtx-cu12==12.1.105 [pip3] pyzmq==25.1.2 [pip3] torch==2.4.1 [pip3] transformers==4.44.2 [pip3] triton==3.0.0 [conda] numpy 2.1.1 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105 pypi_0 pypi [conda] nvidia-cuda-nvrtc-cu12 12.1.105 pypi_0 pypi [conda] nvidia-cuda-runtime-cu12 12.1.105 pypi_0 pypi [conda] nvidia-cudnn-cu12 9.1.0.70 pypi_0 pypi [conda] nvidia-cufft-cu12 11.0.2.54 pypi_0 pypi [conda] nvidia-curand-cu12 10.3.2.106 pypi_0 pypi [conda] nvidia-cusolver-cu12 11.4.5.107 pypi_0 pypi [conda] nvidia-cusparse-cu12 12.1.0.106 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] nvidia-nvjitlink-cu12 12.6.68 pypi_0 pypi [conda] nvidia-nvtx-c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: arse-cu12==12.1.0.106 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] nvidia-nvjitlink-cu12==12.6.68 [pip3] nvidia-nvtx-cu12==12.1.105 [pip3] pyzmq==25.1.2 [pip3] torch==2.4.1 [pip3] transformers==4.44.2 [pip3] triton==3.0.0 [co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Issue when benchmarking the dynamically served LoRA adapter bug;stale ### My current environment ````text [pip3] numpy==2.1.1 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: xt [pip3] numpy==2.1.1 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvidia-cuda-nvrtc-cu12==12.1.105 [pip3] nvidia-cuda-runtime-cu12==12.1.105 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 3.0.0 pypi_0 pypi``` ```` ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'M working with serving LoRA adapter dynamically with: ````python !export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True !curl -X POST http://...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Issue when benchmarking the dynamically served LoRA adapter bug;stale ### My current environment ````text [pip3] numpy==2.1.1 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

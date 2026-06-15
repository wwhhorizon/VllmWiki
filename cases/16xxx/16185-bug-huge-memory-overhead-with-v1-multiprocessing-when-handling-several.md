# vllm-project/vllm#16185: [Bug]: Huge memory overhead with V1 (multiprocessing) when handling several multimodal inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#16185](https://github.com/vllm-project/vllm/issues/16185) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Huge memory overhead with V1 (multiprocessing) when handling several multimodal inputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This should be reproducible with QWEN VL 2.5 and using `vision_language_multi_image.py` offline inference. When configured to use several images as input (e.g. just multiply `IMAGE_URLS` 8-16 times), the *CPU* memory usage spikes dramatically. With just around 20 or so images, VLLM will try to consume around `20-30GB` of RAM, with 40 it will get into `50-60GB` range. It's interesting that the _number_ of passed elements seem to be a problem, while the _size_ causes less problems (ie. when merging multiple images into one, without scaling, it's possible to send ~60 images via 4 collages and still fit within 30GB). This happens regardless of whether qwen-vl-utils are installed to resize the images. At the same time request preprocessing starts to slow down, and while profiling was not super useful due to multiprocessing it did help as the next step was disabling that. With `VLLM_ENABLE_V1_MULTIPROCESSING=0` the issue completely disappears, processing delays are gone and even with ~100 input files the memory usage is in low GBs. I haven't tried profiling MessageQueue yet, but perhaps someone will also run into this, or maybe already...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: g]: Huge memory overhead with V1 (multiprocessing) when handling several multimodal inputs bug ### Your current environment ### 🐛 Describe the bug This should be reproducible with QWEN VL 2.5 and using `vision_language_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ur current environment ### 🐛 Describe the bug This should be reproducible with QWEN VL 2.5 and using `vision_language_multi_image.py` offline inference. When configured to use several images as input (e.g. just multiply...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ther qwen-vl-utils are installed to resize the images. At the same time request preprocessing starts to slow down, and while profiling was not super useful due to multiprocessing it did help as the next step was disabli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: . At the same time request preprocessing starts to slow down, and while profiling was not super useful due to multiprocessing it did help as the next step was disabling that. With `VLLM_ENABLE_V1_MULTIPROCESSING=0` the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

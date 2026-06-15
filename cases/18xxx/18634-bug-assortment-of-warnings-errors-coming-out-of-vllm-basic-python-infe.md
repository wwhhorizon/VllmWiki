# vllm-project/vllm#18634: [Bug]: assortment of warnings / errors coming out of vllm basic python inference script

| 字段 | 值 |
| --- | --- |
| Issue | [#18634](https://github.com/vllm-project/vllm/issues/18634) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: assortment of warnings / errors coming out of vllm basic python inference script

### Issue 正文摘录

### Your current environment Versions: ``` >>> import torch; torch.__version__ '2.7.0+cu126' >>> import transformers; transformers.__version__ '4.52.2' >>> import vllm; vllm.__version__ '0.9.1.dev59+gb6a6e7a52' ``` ### 🐛 Describe the bug My script is really basic: preparing model input IDs using `tokenizers`, constructing `vllm.LLM` and then invoking `.generate(...)` once But I'm somehow getting a bunch of different nasty errors and warnings. Are they expected? Is it possible to eliminate them? Thanks! ``` huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks... To disable this warning, you can either: - Avoid using `tokenizers` before the fork if possible - Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false) [W523 21:36:39.228028808 TCPStore.cpp:125] [c10d] recvValue failed on SocketImpl(fd=170, addr=[localhost]:60438, remote=[localhost]:50427): failed to recv, got 0 bytes Exception raised from recvBytes at /pytorch/torch/csrc/distributed/c10d/Utils.hpp:678 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string , std::al...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lm basic python inference script bug;stale ### Your current environment Versions: ``` >>> import torch; torch.__version__ '2.7.0+cu126' >>> import transforme
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: gingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks... To disable this warning, you can either: - Avoid using `tokenizers` before t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e7a52' ``` ### 🐛 Describe the bug My script is really basic: preparing model input IDs using `tokenizers`, constructing `vllm.LLM` and then invoking `.generate(...)` once But I'm somehow getting a bunch of different nas...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: f warnings / errors coming out of vllm basic python inference script bug;stale ### Your current environment Versions: ``` >>> import torch; torch.__version__
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false) [W523 21:36:39.228028808 TCPStore.cpp:125] [c10d] recvValue failed on SocketImpl(fd=170, addr=[localhost]:60438, remote=[localhost]:50427): f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

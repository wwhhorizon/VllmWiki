# vllm-project/vllm#15011: [Feature]: Support more video loader

| 字段 | 值 |
| --- | --- |
| Issue | [#15011](https://github.com/vllm-project/vllm/issues/15011) |
| 状态 | closed |
| 标签 | feature request;multi-modality |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support more video loader

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vllm now using `decord` for video loader. There are some problem here: 1. `decord` is unmaintained from 3 years ago. and the newest release 0.6 is from 4 years ago. It may cause some unknown issue with this lib without fix. 2. `decord` only published x86 package to pypi, for some aarch64 machine, such as GH200, users need build it by hand. So it's good to support more video loader for diversity usage. Some investigation maybe useful: 1. huggingface transformers support `decord`, `pyav`, `torchvision` and `opencv`. https://huggingface.co/docs/transformers/chat_template_multimodal#sampling-with-fixed-number-of-frames while only `decord` and `pyav` support `load_from_url` case. `pyav` is the default backend even the performance of `decord` is better. 2. The suggested loader from Qwen2.5 VL are `decord` and `torchvision`. https://github.com/QwenLM/Qwen2.5-VL/blob/f56c4d62f6ed38d725d9da2d1440d19b04c10c66/qwen-vl-utils/src/qwen_vl_utils/vision_process.py#L257-L260 3. sglang is the same with vllm using `decord` cc: @DarkLight1337 @ywang96 @jeejeelee ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issu...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e video loader for diversity usage. Some investigation maybe useful: 1. huggingface transformers support `decord`, `pyav`, `torchvision` and `opencv`. https://huggingface.co/docs/transformers/chat_template_multimodal#sa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: `decord` and `pyav` support `load_from_url` case. `pyav` is the default backend even the performance of `decord` is better. 2. The suggested loader from Qwen2.5 VL are `decord` and `torchvision`. https://github.com/Qwen...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: x86 package to pypi, for some aarch64 machine, such as GH200, users need build it by hand. So it's good to support more video loader for diversity usage. Some investigation maybe useful: 1. huggingface transformers supp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: b without fix. 2. `decord` only published x86 package to pypi, for some aarch64 machine, such as GH200, users need build it by hand. So it's good to support more video loader for diversity usage. Some investigation mayb...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support more video loader feature request;multi-modality ### 🚀 The feature, motivation and pitch vllm now using `decord` for video loader. There are some problem here: 1. `decord` is unmaintained from 3 years...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

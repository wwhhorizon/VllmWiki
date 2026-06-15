# vllm-project/vllm#2275: Awq quantized qwen-72b-chat input long text returns empty string

| 字段 | 值 |
| --- | --- |
| Issue | [#2275](https://github.com/vllm-project/vllm/issues/2275) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Awq quantized qwen-72b-chat input long text returns empty string

### Issue 正文摘录

In the config.json file of qwne-72b-chat, it says that it supports 32768 tokens. I changed max-model-len to 16384 for the awq-quantized model and tried inputting around 10000 tokens but it returned an empty string with the warning message `Input prompt (10854 tokens) is too long and exceeds the capacity of block_manager`. When I loaded the original gptq model quantized by VLLM with max-model-len set to 16384, it returned normally with 10000 tokens input. However, when I changed max-model-len to 32768, it also returned an empty string with the same warning message. Could you please help me figure out what could be causing this issue? My hardware environment includes a single _A800-80G GPU_ and my software environment includes _CUDA 12.1, Python 3.10.13, VLLM 0.2.6, Transformers 4.35.2, and AutoAWQ 0.1.7._ ![Uploading 2023-12-27 09-39-05屏幕截图.png…]()

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Awq quantized qwen-72b-chat input long text returns empty string stale In the config.json file of qwne-72b-chat, it says that it supports 32768 tokens. I changed max-model-len to 16384 for the awq-quantized model and tr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng message `Input prompt (10854 tokens) is too long and exceeds the capacity of block_manager`. When I loaded the original gptq model quantized by VLLM with max-model-len set to 16384, it returned normally with 10000 to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Awq quantized qwen-72b-chat input long text returns empty string stale In the config.json file of qwne-72b-chat, it says that it supports 32768 tokens. I changed max-model-len to 16384 for the awq-quantized model and tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t includes a single _A800-80G GPU_ and my software environment includes _CUDA 12.1, Python 3.10.13, VLLM 0.2.6, Transformers 4.35.2, and AutoAWQ 0.1.7._ ![Uploading 2023-12-27 09-39-05屏幕截图.png…]()
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ge `Input prompt (10854 tokens) is too long and exceeds the capacity of block_manager`. When I loaded the original gptq model quantized by VLLM with max-model-len set to 16384, it returned normally with 10000 tokens inp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
